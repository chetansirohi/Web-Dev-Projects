const http=require("http");

const host = 'localhost';

const port=8000;

const books=JSON.stringify([
    {title:"The Alchemist",author:"Paulo Coelho",year:1988},
    {title:"The Prophet",author:"Khalil Gibran",year:1923 }
]);

const authors=JSON.stringify([
    {name:"Paulo Coelho",countryOfBirth:"Brazil",yearOfBirth:1947},
    {name:"Khalil Gibran",countryOfBirth:"Lebanon",yearOfBirth:1883}
]);

const requestListener = function(req,res) {
    res.setHeader("Content-Type","application/json");
    switch(req.url){
        case "/books":
            res.writeHead(200);
            res.end(books);
            break
        case "/authors":
            res.writeHead(200);
            res.end(authors);
            break
        default :
        res.writeHead(404);
        res.end(JSON.stringify({error:"Resources not found"}));
    }
};

const server= http.createServer(requestListener);
server.listen(port,host,()=>{
    console.log(`Server is running on http://${host}:${port}`);
});

