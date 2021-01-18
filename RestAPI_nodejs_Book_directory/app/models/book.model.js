const mongoose= require('mongoose');

const BookSchema = mongoose.Schema({
    title:{
        type:String,
        required:true
    },
    author:String
}, {
    timestamps:true
});

module.exports = mongoose.model('Book',BookSchema);