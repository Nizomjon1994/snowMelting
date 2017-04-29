import gc
from flask import Blueprint
from flask import Flask, render_template, jsonify, request, url_for, Response
from flask import flash
from functools import wraps
from flask import redirect
from flask import session
from blue.models import *
from .forms import *
from blue import engine, desc

mod = Blueprint('site', __name__, template_folder='templates')


@mod.route('/home')
def home():
    return "<h1>You are on the home</h1>"


@mod.route('/', methods=['GET', 'POST'])
def login():
    error = ''
    rows_count = 0
    global username, password
    if request.method == "POST":
        attempted_username = request.form['username']
        attempted_password = request.form['password']
        connection = engine.connect()
        x = connection.execute("SELECT * FROM user WHERE username = ? ", attempted_username)
        for row in x:
            username = row['username']
            password = row['password']
            rows_count += 1
        if rows_count != 0 and str(attempted_username) == str(username) and str(attempted_password) == str(
                password):
            session['logged_in'] = True
            session['username'] = request.form['username']
            flash("You are now logged in")
            return redirect(url_for("realTime"))
        else:
            error = "Invalid credentials. Try Again."
        return render_template("test_login.html", error=error)
    heating_history_list = HeatingHistory.query.order_by(desc(HeatingHistory.heating_end_time)).limit(5).all()
    return render_template("real_time_demo.html", heating_history=heating_history_list)


@mod.route('/register/', methods=["GET", "POST"])
def register_page():
    rows_count = 0
    try:
        form = RegistrationForm(request.form)
        if request.method == "POST":
            username = form.username.data
            email = form.email.data
            password = ((str(form.password.data)))
            connection = engine.connect()
            x = connection.execute("SELECT * FROM user WHERE username = ?",
                                   ((username)))
            for row in x:
                rows_count += 1
            if rows_count > 0:
                error = ("That username is already taken, please choose another")
                return render_template('register.html', form=form, error=error)
            else:
                user = User(username, email, password)
                db.session.add(user)
                db.session.commit()
                flash("Thanks for registering!")
                gc.collect()
                session['logged_in'] = True
                session['username'] = username
                return redirect(url_for('login'))

        return render_template("register.html", form=form)

    except Exception as e:
        return (str(e))


@mod.route('/real_time/', methods=['POST', 'GET'])
def realTime():
    global r
    if request.method == "POST":
        json_dict = request.get_json()
        a = json_dict['temp']
        b = json_dict['hum']
        c = json_dict['date']
        weather = Weather(a, b, c)
        db.session.add(weather)
        db.session.commit()
        data = {
            'temp': a,
            'hum': b,
            'time': c
        }
        return jsonify(data), 201
    elif request.method == "GET":
        heating_history_list = HeatingHistory.query.all()
        return render_template('real_time_demo.html', heating_history=heating_history_list)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login_page'))

    return wrap


@mod.route("/logout/")
@login_required
def logout():
    session.clear()
    flash("You have been logged out!")
    gc.collect()
    return redirect(url_for('login'))


@mod.route('/graph/')
def graph():
    weather_list = get_records_based_on_time('2017-02-20', '2017-02-30')

    time_adjusted_temperatures = []
    time_adjusted_humidities = []

    for record in weather_list:
        time_adjusted_temperatures.append(record.temp)
        time_adjusted_humidities.append(record.hum)

    list_count = len(weather_list)
    return render_template("graph.html", weather_list=weather_list, list_count=list_count)


def get_records_based_on_time(from_time, to_time):
    weather_list = []
    connection = engine.connect()

    results = connection.execute("SELECT * FROM weather WHERE date BETWEEN ? AND ?",
                                 (from_time.format('YYYY-MM-DD HH:mm:ss'), to_time.format('YYYY-MM-DD HH:mm:ss')))
    for row in results:
        weather_list.append(WeatherModel(float(row['temp']), float(row['hum']), str(row['weather_date'])))
    connection.close()
    return weather_list


@mod.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', error=e)
