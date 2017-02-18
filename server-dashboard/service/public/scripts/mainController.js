'use strict';

angular.module('mainController', [])
    .controller('mainController', ($scope) => {

        // http get
        const httpget = (url) => {
            new Promise(
                (resolve, reject) => {
                    const req = new XMLHttpRequest();
                    // get page
                    req.open('GET', url);
                    // onload status
                    req.onload = () => {
                        if (req.status == 200) {
                            resolve(req.response);
                        } else {
                            reject(req.statusText);
                        };
                    };
                    // error handler
                    req.onerror = () => {
                        reject(Error('Network error'));
                    };
                    // send request 
                    req.send();
                }
            );
        }

        // restart the sevrer
        $scope.shutdownServer = () => {
            return httpget('server/shutdown');
        }

        // shutdown the server
        $scope.rebootServer = () => {
            return httpget('server/reboot');
        }
    })