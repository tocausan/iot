'use strict';

const cmd = require('node-cmd');

module.exports = {
    // OS X notification 
    notification: (title, description) => {
        cmd.run("osascript -e 'display notification \"" + description + "\" with title \"" + title + "\"'");
    },
    // shutdown
    shutdown: () => {
        cmd.run("sudo shutdown now");
    },
    // reboot
    shutdown: () => {
        cmd.run("sudo reboot");
    },
};