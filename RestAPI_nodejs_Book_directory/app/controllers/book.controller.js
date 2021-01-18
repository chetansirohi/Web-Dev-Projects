const Book= require('../models/book.model.js');

// Create and Save a new Book
exports.create = (req, res) => {
    // Validate request because in model we required the title
    if(!req.body.title) {
        return res.status(400).send({
            message: "Please enter book title."
        });
    }

    // Create a book
    const book = new Book({
        title: req.body.title,
        author: req.body.author || 'IT Jugadu'
    });

    // Save Book
    book.save()
        .then(oBook => {
            res.send(oBook);
        }).catch(err => {
        res.status(500).send({
            message: err.message || "Some error occurred while creating the Book."
        });
    });
};

// Get all and return all books.
exports.getAll = (req, res) => {
    Book.find()
        .then(oBook => {
            res.send(oBook);
        }).catch(err => {
        res.status(500).send({
            message: err.message || "Some error occurred while retrieving the book."
        });
    });
};

// Get a single book with a bookId
exports.getById = (req, res) => {
    Book.findById(req.params.bookId)
        .then(oBook => {
            if(oBook) {
                res.send(oBook);
            }
            return res.status(404).send({
                message: "Book not exist with id " + req.params.bookId
            });
        }).catch(err => {
        if(err.kind === 'ObjectId') {
            return res.status(404).send({
                message: "Book not exist with id " + req.params.bookId
            });
        }
        return res.status(500).send({
            message: "Some error occurred while retrieving the book with bookId " + req.params.bookId
        });
    });
};

// Update a book by the bookId
exports.update = (req, res) => {
    // Validate Request because title is required
    if(!req.body.title) {
        return res.status(400).send({
            message: "Please enter book title."
        });
    }

    // Find book and update it
    Book.findByIdAndUpdate(req.params.bookId, {
        title: req.body.title,
        author: req.body.author || "IT jugadu"
    }, {new: true})
        .then(oBook => {
            if(oBook) {
                res.send(oBook);
            }
            return res.status(404).send({
                message: "Book does not exist with bookId " + req.params.bookId
            });

        }).catch(err => {
        if(err.kind === 'ObjectId') {
            return res.status(404).send({
                message: "Book does not exist with bookId " + req.params.bookId
            });
        }
        return res.status(500).send({
            message: "Some error occurred while updating the book with bookId" + req.params.bookId
        });
    });
};

// Delete the Book with the bookId
exports.delete = (req, res) => {
    Book.findByIdAndRemove(req.params.bookId)
        .then(oBook => {
            if(oBook) {
                res.send({message: "Book has been deleted successfully!"});
            }
            return res.status(404).send({
                message: "Book not exist with bookId" + req.params.bookId
            });
        }).catch(err => {
        if(err.kind === 'ObjectId' || err.name === 'NotFound') {
            return res.status(404).send({
                message: "Book not exist with bookId" + req.params.bookId
            });
        }
        return res.status(500).send({
            message: "Some error occurred while deleting the book with bookId" + req.params.bookId
        });
    });
};