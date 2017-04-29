from flask import Blueprint, request, Response, json,jsonify
from blue import engine
from blue.models import *

mod = Blueprint('api', __name__)



@mod.route('/login/', methods=['GET', 'POST'])
def login_api():
    global username, password
    rows_count = 0
    error = ''
    try:

        if request.method == "POST":
            json_dict = request.get_json()
            attempted_username = json_dict['username']
            attempted_password = json_dict['password']

            connection = engine.connect()

            x = connection.execute("SELECT * FROM user WHERE username = ? ", attempted_username)
            for row in x:
                username = row['username']
                password = row['password']
                rows_count += 1

            if rows_count != 0 and str(attempted_username) == str(username) and str(attempted_password) == str(
                    password):
                data = {
                    'username': username,
                    'status': 'success'
                }
                return Response(json.dumps(data), 200, mimetype='application/json')
            else:
                error = "Invalid credentials. Try Again."
                data = {
                    'status': 'error',
                    'error': error
                }
            return Response(json.dumps(data), 401, mimetype='application/json')
    except Exception as e:
        # flash(e)
        return e


@mod.route("/register/", methods=['GET', 'POST'])
def register_api():
    rows_count = 0
    if request.method == 'POST':
        json_dict = request.get_json()
        username = json_dict['username']
        email = json_dict['email']
        password = json_dict['password']
        connection = engine.connect()

        x = connection.execute("SELECT * FROM user WHERE username = ?",
                               ((username)))
        for row in x:
            rows_count += 1
        if rows_count > 0:
            data = {
                'status': 'error',
                'error': 'That username is already taken, please choose another'
            }
            return Response(json.dumps(data), 401, mimetype='application/json')

        else:
            user = User(username, email, password)
            db.session.add(user)
            db.session.commit()

            return Response(json.dumps(user.serialize), 201, mimetype='application/json')


@mod.route('/sensor_list/', methods=['GET', 'POST'])
def collect_sensors():
    if request.method == "POST":
        json_dict = request.get_json()
        sensor_id = json_dict['sensor_id']
        created_time = json_dict['created_time']
        sensor = Sensor(sensor_id, '', '', created_time)
        db.session.add(sensor)
        db.session.commit()
    elif request.method == "GET":
        return jsonify(sensors=[i.serialize for i in Sensor.query.all()])


@mod.route('/heating_history/', methods=['GET', 'POST'])
def collect_heating_history():
    if request.method == "POST":
        json_dict = request.get_json()
        sensor_id = json_dict['sensor_id']
        heating_on_time = json_dict['heating_on_time']
        heating_off_time = json_dict['heating_off_time']
        calculated_heating_time = json_dict['calculated_heating_time']
        heating_history = HeatingHistory(sensor_id, heating_on_time, heating_off_time, calculated_heating_time)
        db.session.add(heating_history)
        db.session.commit()
    elif request.method == "GET":
        return jsonify(haeting_history=[i.serialize for i in HeatingHistory.query.all()])


@mod.route('/weather/', methods=['GET', 'POST'])
def collect_weather_data():
    if request.method == "POST":
        json_dict = request.get_json()
        type = json_dict['type']
        if type == 'humidity':
            hum = json_dict['hum']
            date = json_dict['date']
            sensor_id = json_dict['sensor_id']
            humidity = Humidity(hum, date, sensor_id)
            db.session.add(humidity)
            db.session.commit()
            data = {
                'sensor_id': sensor_id,
                'hum': hum,
                'time': date
            }
            return jsonify(data), 201
        elif type == 'temperature':
            temp = json_dict['temp']
            sensor_id = json_dict['sensor_id']
            date = json_dict['date']
            temperature = Temperature(temp, date, sensor_id)
            db.session.add(temperature)
            db.session.commit()
            data = {
                'sensor_id': sensor_id,
                'temp': temp,
                'time': date
            }
            return jsonify(data), 201
    else:
        result = (Humidity.query.all())

        return jsonify(json_list=[i.serialize for i in result])
