module.exports= (app)=>{
    const books= require('../controllers/book.controller.js');

    //Create a new Book
    app.post('/books',books.create);

    //Get all Books
    app.get('/books',books.getAll);

    //Get a single Book with bookId
    app.get('/books/:bookId',books.getById);

    //Update a Book with bookId
    app.put('/books/:bookId',books.update);

    //Delete a Book with bookId
    app.delete('/books/:bookId',books.delete);
}