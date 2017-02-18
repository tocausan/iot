'use strict';

const http = require('http');

// service
const service = require('../service/route');
const server = http.createServer(service);
server.listen(8000);

// run log
server.on('listening', function() {
    console.log('Botausan is listening on ' + server.address().port + ' in ' + service.get('env') + ' mode.')
});

// socket.io
const socketio = require('../service/socketio');
//socketio.init(service);