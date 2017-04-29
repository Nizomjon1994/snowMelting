/**
 * Created by nizom on 1/15/17.
 */
var  app = angular.module("app",[])

app.filter('nameFormat',function () {
    return function (x) {
        var  i,  c , txt="";
        for( i =0 ;i<x.length;i++){
            c= x[i]
            if (i%2==0){
                c = c.toUpperCase();
            }
            txt +=c;
        }
        return txt;
    }
})

app.controller("myCtrl",function ($scope,$timeout) {
    $scope.myHeader = "Hello World"
    $timeout(function () {
        $scope.myHeader = "How are you today"
    },2000)
})

app.controller("AppCtrl",function ($scope) {
    $scope.firstName = "John";
    $scope.lastName = "Doe";
    $scope.price = 20
    $scope.fullName = function() {
        return $scope.firstName + " " + $scope.lastName;
    };

    $scope.names = [
        {name:'Jani',country:'Norway'},
        {name:'Hege',country:'Sweden'},
        {name:'Kai',country:'Denmark'}
    ];
    $scope.nameList = ['Jani', 'Carl', 'Margareth', 'Hege', 'Joe', 'Gustav', 'Birgit', 'Mary', 'Kai'];
})