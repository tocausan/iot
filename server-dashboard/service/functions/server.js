'use strict';

const cmd = require('node-cmd');

module.exports = {
    // OS X notification 
    notification: (title, description) => {
        cmd.run("osascript -e 'display notification \"" + description + "\" with title \"" + title + "\"'");
    },
    // shutdown
    shutdown: () => {
        cmd.run("sudo shutdown -h now");
    },
    // reboot
    reboot: () => {
        cmd.run("sudo shutdown -r now");
    },
};