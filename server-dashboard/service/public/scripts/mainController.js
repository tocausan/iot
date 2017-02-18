'use strict';

angular.module('mainController', [])
    .controller('mainController', ($scope) => {

        // restart the sevrer
        $scope.shutdownServer = () => {
            document.location.href = "server/shutdown";
            document.location.href = "/";
        }

        // shutdown the server
        $scope.rebootServer = () => {
            document.location.href = "server/reboot";
            document.location.href = "/";
        }
    })