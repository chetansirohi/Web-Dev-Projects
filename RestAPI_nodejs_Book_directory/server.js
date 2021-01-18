const express= require('express');
const bodyParser= require('body-parser');


//create express app
const app = express();

//parse requests of content type - application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({extended:true}))

//parse requests of content -type -application/json
app.use(bodyParser.json())

//configure the database
const dbConfig= require('../RestAPI_nodejs_Book_directory/config/development.config');
const mongoose= require('mongoose');

mongoose.Promise=global.Promise;

//connecting to the database
mongoose.connect(dbConfig.url,{
    useNewUrlParser:true
}).then(()=> {
    console.log("Succesfully connected to the myapp database");
}).catch(err => {
    console.log('Could not connect to the database. Exiting now...',err);
    process.exit();
});

//define a simple route 
app.get('/',(req,res)=>{
    res.json({"message":"Welcome to the ExpressMongoApp created by Chetan Sirohi"});
});

//listen for requests
app.listen(3000,()=>{
    console.log("Server is listening on port 3000");
});

//Require Books routes
require('../RestAPI_nodejs_Book_directory/app/routes/book.routes')(app);//this app in bracket is the const app
