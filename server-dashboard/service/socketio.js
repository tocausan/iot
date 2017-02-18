'use strict';

// handle message
function handleOnConnection(client, nlp) {

    const io = require('socket.io').listen(client);

    // connection listener
    let userCount = 0;
    let users = [];
    let userId = null;
    let requestData = null;

    function userData() {
        return {
            userId: userId,
            userCount: userCount,
            users: users
        };
    }

    io.on('connect', function(socket) {
        // user identification
        userId = socket.id;
        users.push(userId);
        userCount += 1;

        // users data
        console.log(userData());
        socket.emit('userData', userData())
        socket.broadcast.emit('userData', userData())

        // request listener
        socket.on('request', function(req) {
            requestData = {
                userId: userId,
                request: req
            };
            //console.log(requestData);
            io.to(userId).emit('requestData', requestData);

            // ask nlp
            handleOnRequest(requestData, nlp);
        });

        // disconnect listener
        socket.on('disconnect', function() {
            // remove user
            users.splice(users.indexOf(userId), 1);
            userCount -= 1;

            // users data
            console.log(userData());
            socket.broadcast.emit('userData', userData())

        });
    });
};

function handleOnRequest(req, nlp) {
    if (req.request) {
        nlp.ask(req.request, (err, res) => {
            if (err) {
                console.log(err);
                return;
            };

            try {
                if (!res) {
                    throw new Error('Could not extract intent.');
                };

                const intent = require('./intents/' + res.intent[0] + 'Intent');
                console.log('request to botausan')

                intent.process(res, function(error, response) {
                    if (error) {
                        console.log(error);
                        return;
                    };

                    console.log(response);
                    io.to(userId).emit('result', response);
                    return;
                })
            } catch (err) {
                console.log(err);
                console.log('Sorry, I don\'t know what you are talking about.');
                return;
            };
        });
    };
};

module.exports.init = function socketio(client, nlp) {
    handleOnConnection(client, nlp);
}