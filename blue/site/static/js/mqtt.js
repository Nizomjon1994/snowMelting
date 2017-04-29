/**
 * Created by nizom on 1/29/17.
 */
var temp = 0.0;
var temperature = 0.0
var temperature1 = 0.0
var humidity = 0.0
var humidity1 = 0.0
var date = 0.0
var date1 = 0.0
const CURRENT_DATA_TOPIC = 'udblab/sensor/+/current_data/'
const FIXED_TIME_HUM_DATA_TOPIC = 'udblab/sensor/+/hum/fixed_time_data/'
const FIXED_TIME_TEMP_DATA_TOPIC = 'udblab/sensor/+/tem/fixed_time_data/'
const SENSOR_HEATING_DATA_TOPIC = 'udblab/sensor/heating/'
const CURRENT_DATA_SUFFIX = '/current_data/'
const FIXED_TIME_DATA_SUFFIX = '/fixed_time_data/'
const DURATION_OF_HEATING_DATA_TOPIC = 'udblab/sensor/+/duration_of_heating/'
const DURATION_OF_HEATING_DATA_SUFFIX = '/duration_of_heating/'
const SENSORS_ID = [1111, 1112, 1113]
var client
var connected_broker = ''
function init_broker(broker_url, port, isMain, isHive, isSSL) {
    client = new Paho.MQTT.Client(broker_url, Number(port), '');
    client.onConnectionLost = onConnectionLost;
    client.onMessageArrived = onMessageArrived;

    var connect_options = {
        timeout: 3,
        onSuccess: function () {
            console.log('Connected to ' + broker_url);
            client.subscribe(CURRENT_DATA_TOPIC, {qos: 0})
            client.subscribe(SENSOR_HEATING_DATA_TOPIC, {qos: 1})
            client.subscribe(FIXED_TIME_HUM_DATA_TOPIC, {qos: 1})
            client.subscribe(FIXED_TIME_TEMP_DATA_TOPIC, {qos: 2})
            client.subscribe(DURATION_OF_HEATING_DATA_TOPIC, {qos: 2})
        },
        onFailure: function (message) {
            if (isMain && isHive) {
                init_broker("m12.cloudmqtt.com", 33226, false, false, true)
            } else if (!isMain && !isHive) {
                init_broker("broker.hivemq.com", 8000, true, true, false)
            }
        },
        useSSL: !!isSSL,
        userName: isMain ? "udblab" : 'hlqbtvzv',
        password: isMain ? "12345" : 'rGA8NiRaD2KX',
    };

    client.connect(connect_options);
    function onConnectionLost(responseObject) {
        if (responseObject.errorCode !== 0) {
            console.log("Connection Lost:" + responseObject.errorMessage);
            init_broker("159.203.160.131", 8080, true, true)
        }
    }

    function onMessageArrived(message) {
        var str = message.destinationName;
        var sensor_id = message.destinationName.slice(14, 18);
        if (str.endsWith(CURRENT_DATA_SUFFIX)) {
            if (sensor_id == String(SENSORS_ID[1])) {
                var json = message.payloadString
                var obj = JSON.parse(json);
                window.temperature = obj["temp"]
                window.humidity = obj["hum"]
                $("#temperature").text(obj["temp"]);
                $("#humidity").text(obj["hum"]);
                $("#date").text(obj["date"]);
                console.log(sensor_id)
                console.log("Parsed json " + json)

            } else if (sensor_id == String(SENSORS_ID[0])) {
                var json = message.payloadString
                var obj = JSON.parse(json);
                window.temperature1 = obj["temp"]
                window.humidity1 = obj["hum"]
                $("#temperature1").text(obj["temp"]);
                $("#humidity1").text(obj["hum"]);
                $("#date1").text(obj["date"]);
                console.log(sensor_id)
                console.log("Parsed json " + json)
            }

        } else if (str.endsWith(FIXED_TIME_DATA_SUFFIX)) {
            console.log(message.destinationName)
            var json = message.payloadString
            console.log(json)
            $.ajax({
                url: '/api/v1/weather/',
                data: json,
                dataType: "json",
                type: 'POST',
                contentType: 'application/json;charset=UTF-8',
                success: function (response) {
                    console.log(response);
                },
                error: function (error) {
                    console.log(error);
                }
            });
        } else if (str.endsWith(DURATION_OF_HEATING_DATA_SUFFIX)) {
            console.log(message.destinationName)
            var json = message.payloadString
            console.log(json)
            $.ajax({
                url: '/api/v1/heating_history/',
                data: json,
                dataType: "json",
                type: 'POST',
                contentType: 'application/json;charset=UTF-8',
                success: function (response) {
                    console.log(response);
                },
                error: function (error) {
                    console.log(error);
                }
            });
        }

    }
}
init_broker("159.203.160.131", 8080, true, true, false)

var g1, g2, g3, g4;
document.addEventListener("DOMContentLoaded", function (event) {
    g1 = new JustGage({
        id: "g1",
        value: temperature,
        min: 0,
        max: 100,
        humanFriendly: true,
        startAnimationTime: 500,
        refreshAnimationTime: 500,
        title: "Temperature",
        label: "current temperature"
    });
    g2 = new JustGage({
        id: "g2",
        value: humidity,
        min: 0,
        max: 100,
        humanFriendly: true,
        startAnimationTime: 500,
        refreshAnimationTime: 500,
        title: "Humidity",
        label: "current humidity"
    });
    g3 = new JustGage({
        id: "g3",
        value: temperature1,
        min: 0,
        max: 100,
        humanFriendly: true,
        startAnimationTime: 500,
        refreshAnimationTime: 500,
        title: "Temperature",
        label: "current temperature"
    });
    g4 = new JustGage({
        id: "g4",
        value: humidity1,
        min: 0,
        max: 100,
        humanFriendly: true,
        startAnimationTime: 500,
        refreshAnimationTime: 500,
        title: "Humidity",
        label: "current humidity"
    });

    setInterval(function () {
        g1.refresh(temperature, 100);
        g2.refresh(humidity, 100);
        // g3.refresh(temperature1, 100);
        // g4.refresh(humidity1, 100);
    }, 1000);
});


//Do this when button is clicked.
$("#toggleBtn").click(function () {
    var message = new Paho.MQTT.Message("test");
    message.destinationName = SENSOR_HEATING_DATA_TOPIC;
    client.send(message);
    console.log('publishing new value:' + "asda");
    setTimeout(function () {
        $("#toggleBtn").click();
    }, 10000)
});