/**
 * Created by nizom on 2/10/17.
 */
$("#toggle-event_1").change(function () {
    if ($(this).prop('checked')) {
        const SENSOR_HEATING_DATA_TOPIC = 'udblab/sensor/1112/heating/'
        $("p").toggle();
        var message = new Paho.MQTT.Message("on");
        message.destinationName = SENSOR_HEATING_DATA_TOPIC;
        client.send(message);
        console.log('publishing new value:' + "asda");

    } else {
        const SENSOR_HEATING_DATA_TOPIC = 'udblab/sensor/1112/heating/'
        $("p").toggle();
        var message = new Paho.MQTT.Message("off");
        message.destinationName = SENSOR_HEATING_DATA_TOPIC;
        client.send(message);
        console.log('publishing new value:' + "asda");

    }

});
// $("#toggle-event_2").change(function () {
//     if ($(this).prop('checked')) {
//         const SENSOR_HEATING_DATA_TOPIC = 'udblab/sensor/1111/heating/'
//         $("p").toggle();
//         var message = new Paho.MQTT.Message("Heyyy");
//         message.destinationName = SENSOR_HEATING_DATA_TOPIC;
//         client.send(message);
//         console.log('publishing new value:' + "asda");
//         setTimeout(function () {
//             $('#toggle-event_2').bootstrapToggle('on')
//             $("p").toggle()
//         }, 5000)
//     } else {
//         $("p").toggle()
//     }
//
// });
//
