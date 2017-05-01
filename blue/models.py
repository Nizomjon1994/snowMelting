from blue import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }


class Humidity(db.Model):
    __tablename__ = 'sensor_humidity'
    id = db.Column(db.Integer, primary_key=True)
    hum = db.Column(db.Float)
    time_stamp = db.Column(db.String(50))
    sensor_id = db.Column(db.Integer)

    def __init__(self, hum, time_stamp, sensor_id):
        self.hum = hum
        self.time_stamp = time_stamp
        self.sensor_id = sensor_id

    @property
    def serialize(self):
        return {
            'id': self.id,
            'hum': self.hum,
            'time_stamp': self.time_stamp,
            'sensor_id': self.sensor_id
        }


class HeatingHistory(db.Model):
    __tablename__ = 'heating_history'
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.String(10))
    heating_start_time = db.Column(db.String(50))
    heating_end_time = db.Column(db.String(50))
    calculated_heating_time = db.Column(db.String(50))

    def __init__(self, sensor_id, heating_start_time, heating_end_time, calculated_heating_time):
        self.sensor_id = sensor_id
        self.heating_start_time = heating_start_time
        self.heating_end_time = heating_end_time
        self.calculated_heating_time = calculated_heating_time

    def get_heating_start_time(self):
        return self.heating_start_time

    def get_heating_end_time(self):
        return self.heating_end_time

    def get_calculated_heating_time(self):
        return self.calculated_heating_time

    def set_calculated_heating_time_to_human_readable(self, time):
        self.calculated_heating_time = time

    @property
    def serialize(self):
        return {
            'sensor_id': self.sensor_id,
            'heating_start_time': self.heating_start_time,
            'heating_end_time': self.heating_end_time,
            'calculated_heating_time': self.calculated_heating_time
        }


class Temperature(db.Model):
    __tablename__ = 'sensor_temperature'
    id = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.Float)
    time_stamp = db.Column(db.String(50))
    sensor_id = db.Column(db.Integer)

    def __init__(self, temp, time_stamp, sensor_id):
        self.temp = temp
        self.time_stamp = time_stamp
        self.sensor_id = sensor_id

    @property
    def serialize(self):
        return {
            'id': self.id,
            'temp': self.temp,
            'time_stamp': self.time_stamp,
            'sensor_id': self.sensor_id
        }


class Weather(db.Model):
    __tablename__ = 'weather'
    id = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.String(20))
    hum = db.Column(db.String(50))
    date = db.Column(db.String(50))

    def __init__(self, temp, hum, date):
        self.temp = temp
        self.hum = hum
        self.date = date

    @property
    def serialize(self):
        return {
            'id': self.id,
            'temp': self.temp,
            'hum': self.hum,
            'date': self.date
        }


class WeatherModel(object):
    def __init__(self, temp=None, hum=None, date=None):
        self.temp = temp
        self.hum = hum
        self.date = date

    @property
    def x(self):
        print("getter of x called")
        return self.temp

    @property
    def x(self):
        print("getter of x called")
        return self.date

    @property
    def x(self):
        print("getter of x called")
        return self.hum

    @property
    def serialize(self):
        return {
            'temp': self.temp,
            'hum': self.hum,
            'date': self.date
        }


class Sensor:
    __tablename__ = 'sensor'
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.String(20))
    latitude = db.Column(db.String(50))
    longitude = db.Column(db.String(50))
    created_time = db.Column(db.String(50))

    def __init__(self, sensor_id, latitude, longitude, created_time):
        self.sensor_id = sensor_id
        self.latitude = latitude
        self.longitude = longitude
        self.created_time = created_time

    @property
    def serialize(self):
        return {
            'sensor_id': self.sensor_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'created_time': self.created_time
        }
