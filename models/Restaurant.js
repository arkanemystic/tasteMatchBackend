const mongoose = require('mongoose');

const restaurantSchema = new mongoose.Schema({
    name: { type: String, required: true },
    address: { type: String, required: true },
    cuisine: { type: String, required: true },
    rating: { type: Number, required: true },
    // Add any other fields you need
});

module.exports = mongoose.model('Restaurant', restaurantSchema);
