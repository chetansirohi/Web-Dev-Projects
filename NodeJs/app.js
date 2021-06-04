// const log= require('./logger');

// log('message'); //this is an exported objext
 // for an exported function we can use logger.log('message')

// const path=require('path'); //node looks for builtin node modules else it looks for it in relative path

// var pathObj=path.parse(__filename);
// console.log(pathObj);

// const os= require('os'); //os module
// var totalMem= os.totalmem()
// var freeMem= os.freemem()

// console.log(totalMem);
// console.log(freeMem);

//Tempalte String, prevents concatination
// console.log(`Total Memory : ${totalMem}`);
// const fs= require('fs');//synchronous method
// const files =fs.readdirSync('./');
// console.log(files);

//Asynchronous calls
// const fs=require('fs');

// fs.readdir('./',function(err,files){
//     if (err) console.log('Error',err);
//     else console.log('Result',files);
// });

///EVENTS

// const EventEmitter = require('events');//if the variable is in camel case we say it is a class
// const emitter = new EventEmitter();

// //Register a Listener,to be called before emit
// emitter.on('messageLogged',function(arg){ //args of emitter
//     console.log('Listener Called',arg);
// });

// //Listerne with arrow function 
// emitter.on('messageLogged',(arg) =>{ //args of emitter
//     console.log('Listener Called',arg);
// });

// //We have Raised an event here,but there is no listener
// //if we want to send some data about an event we use event arguments
// emitter.emit('messageLogged', {id:1,url:"https:/"}); //signalling something

// const EventEmitter=  require('events') ;

// const Logger =require('./logger');
// const logger =new Logger();

// logger.on('messageLogged',(arg) =>{ //args of emitter
//     console.log('Listener Called',arg);
// });

// logger.log('message');

// const http =require('http');
// const server = http.createServer((req,res)=>{
//     if (req.url==='/'){
//         res.write('Hello World');
//         res.end();
//     }
//     if (req.url==='/api/courses'){
//         res.write(JSON.stringify([1,2,3,4,5]))
//         res.end();
//     }

// }); //event emitter

// server.on('connection',(socker)=>{//This only responds when we call the server
//     console.log('New Connection')
// });

// server.listen(3000);
// console.log('Listening OnPort 3000...');
