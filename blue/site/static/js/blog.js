/**
 * Created by nizom on 1/21/17.
 */
var app = angular.module("blog",[])

app.controller('blogCtrl', function ($scope,$http) {
    $scope.name = "Tesdst";
    // $scope.getBlog = function () {
    //     $http.get('/blog-single-post')
    //         .success(function (data, status) {
    //             $scope.pin = data
    //         })
    //
    // }
})