/*
    Created on : 01 Jan, 2016, 5:00:04 PM
    Author     : Anshuman
*/

var app = angular.module('outlet', []);

app.controller('app_ctrl', ['$scope','$http','$anchorScroll','$interval',
    function ($scope,$http,$anchorScroll,$interval) {
        $scope.heading = "outlets";

        $scope.submit_to_drive = function (outlet) {
            $http({
                    method: 'POST',
                    url: base_url + '',
                    data: "about=" + $scope.heading + "city=" + "cluster=" + outlet.cluster + "name=" + outlet.name + "lat=" + outlet.lat + "lon=" + outlet.lon,

                }).then(function successCallback(response) {
                    var ret = response.data.data
                    $scope.heading = ret.heading;
                    $scope.cont = ret.data;
                    console.log(ret.data)
                }, function errorCallback(response) {
                });


        }
    


    }]);



