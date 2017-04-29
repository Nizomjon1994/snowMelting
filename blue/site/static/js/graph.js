/**
 * Created by nizom on 2/1/17.
 */
var start_time;
var finish_time;

$(document).ready(function () {
    $("#submit_date").click(function () {

        // draw_chart()

        var start_time = $('#start_time').val()
        var finish_time = $('#finish_time').val()
        var dic = []
        dic.push({
            "start_time": start_time,
            "finish_time": finish_time
        })
        $.ajax({
            url: "/graph.html",
            data: JSON.stringify(dic),
            dataType: "json",
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            success: function (response) {
                console.log(JSON.stringify(response.json_list));
            },
            error: function (error) {
                console.log($('form').serialize());
            }
        });

    });
})

function draw_chart(jsonList) {
   google.charts.load('current', {packages: ['corechart', 'line']});
google.charts.setOnLoadCallback(drawBackgroundColor(jsonList));

function drawBackgroundColor(jsonList) {
      var data = new google.visualization.DataTable();
      data.addColumn('number', 'X');
      data.addColumn('number', 'Dogs');


      data.addRows([
        [0, 0],   [1, 10],  [2, 23],  [3, 17]
      ]);

      var options = {
        hAxis: {
          title: 'Time'
        },
        vAxis: {
          title: 'Popularity'
        },
        backgroundColor: '#f1f8e9'
      };

      var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }
}