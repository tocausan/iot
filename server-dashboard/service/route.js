'use strict';

const express = require('express');
const service = express();
const serverFunctions = require('./functions/server');

// routes
// public path
service.use(express.static(__dirname + '/public'));
// index
service.get('/', (req, res, next) => {
    return res.sendFile(__dirname + '/views/index.html');
})

// server path
const server = express.Router();
service.use('/server', server);
// shutdown
server.route('/shutdown')
    .get((req, res, next) => {
        serverFunctions.shutdown();
    })
    // reboot
server.route('/reboot')
    .get((req, res, next) => {
        serverFunctions.reboot();
    })


// get location
service.get('/api/:location', (req, res, next) => {
    return res.json({ result: req.params.location });
});

module.exports = service;