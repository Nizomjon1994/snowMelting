/**
 * Created by nizom on 2/9/17.
 */
$(document).ready(function () {

    $('#login').click(function () {
        var username = $('#username').val()
        var password = $('#password').val()
        var dic = []
        dic.push({
            "username": username,
            "password": password
        })
        $.ajax({
            url: '/api/v1/login/',
            data: JSON.stringify(dic),
            dataType: "json",
            type: "POST",
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
