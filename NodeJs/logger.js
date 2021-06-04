const EventEmitter = require('events');//if the variable is in camel case we say it is a class


var url= 'https://mylogger.io/log';

//In order to incorporate all the functions of Event Emitter,we use a class

class Logger extends EventEmitter{ //using extends gives us all capabilities of EventEmitter
    log(message){//when function is inside a class we refer it as method
    console.log(message);
    this.emit('messageLogged', {id:1,url:"https:/"});//as we used extends we replace emitter->this
    }
}

module.exports=Logger;


// module.exports = log; //exporting an object
// we can export a function or a single object
// module.exports.log = log; , it is a function

//when we execute a node program we are invoking a custom wrapper function which wraps oour program

// (function (exports,require,module,__filename,__dirname){our program body goes here} <-this function is called during runtime