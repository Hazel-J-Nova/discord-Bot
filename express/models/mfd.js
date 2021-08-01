//jshint esversion:9

const mongoose = require('mongoose');
const Schema = mongoose.Schema;


const MfdSchema = new Schema({
    name: string,
    votes: Number,
    plan: string,
    url: string,
    author: string,
});

module.exports = mongoose.model("Mfd", MfdSchema);