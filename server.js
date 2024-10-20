const express = require('express');
const mongoose = require('mongoose');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(express.json());

// MongoDB connection
mongoose.connect('mongodb://127.0.0.1:27017/restaurantDB', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch(err => console.error('MongoDB connection error:', err));

// Dummy restaurant data (you can replace this with actual data from MongoDB)
const restaurantData = [
    {
        restaurant_id: 1,
        name: "Pizza Place",
        cuisines: ["Italian"],
        location: "123 Main St",
        rating: 4.5,
        dietary_options: ["vegetarian", "gluten-free"]
    },
    {
        restaurant_id: 2,
        name: "Sushi Bar",
        cuisines: ["Japanese"],
        location: "456 Elm St",
        rating: 4.7,
        dietary_options: ["vegetarian", "vegan"]
    },
    // Add more restaurant objects as needed
];

// Endpoint to get recommendations from Python service
app.post('/api/recommendations', async (req, res) => {
    const userPreferences = req.body;  // user data comes from client

    try {
        // Call the Python API to get recommendations
        const response = await axios.post('http://localhost:5001/recommend', {
            user: userPreferences,  // Pass user data to Python API
            restaurants: restaurantData  // Pass restaurant data (this can come from MongoDB)
        });

        // Send back the recommendations from Python API
        res.json(response.data);
    } catch (error) {
        console.error('Error fetching recommendations:', error);
        res.status(500).json({ error: 'Error generating recommendations' });
    }
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
