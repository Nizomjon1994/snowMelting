/**
 * Created by Nizomjon on 18/02/2017.
 */
var request = new XMLHttpRequest();
request.open('GET',"http://apis.skplanetx.com/weather/current/hourly?lon=127.9259&lat=36.9910&version=1&appKey=4ce0462a-3884-30ab-ab13-93efb1bc171f")
request.onload = function () {
    var data = JSON.parse(request.responseText)
    console.log(data)
}