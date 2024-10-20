from flask import Flask, request, jsonify

app = Flask(__name__)

class Restaurant:
    def __init__(self, restaurant_id, name, cuisines, location, rating, dietary_options):
        self.restaurant_id = restaurant_id
        self.name = name
        self.cuisines = cuisines #array
        self.location = location
        self.rating = rating
        self.dietary_options = dietary_options #array

class User:
    def __init__(self, user_id, food_preferences, dietary_preferences):
        self.user_id = user_id
        self.food_preferences = food_preferences #cuisines
        self.dietary_preferences = dietary_preferences #ex: vegan, vegetarian
        self.disliked_cuisines = set()

def calculate_similarity(user, restaurant):
    preferences_set = set(user.food_preferences) - user.disliked_cuisines
    cuisines_set = set(restaurant.cuisines)
    intersection_cuisines = preferences_set.intersection(cuisines_set)

    dietary_preferences_set = set(user.dietary_preferences)
    dietary_options_set = set(restaurant.dietary_options)
    intersection_dietary = dietary_preferences_set.intersection(dietary_options_set)

    similarity_score = (len(intersection_cuisines) + len(intersection_dietary)) / \
                       (len(user.food_preferences) + len(user.dietary_preferences)) if \
                       (user.food_preferences or user.dietary_preferences) else 0

    return similarity_score

def recommend_restaurants(user, restaurants):
    recommendations = []
    for restaurant in restaurants:
        similarity = calculate_similarity(user, restaurant)
        recommendations.append((restaurant, similarity))
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    # Get the JSON data from the request
    data = request.json
    user_data = data['user']
    restaurant_data = data['restaurants']

    # Create User and Restaurant objects
    user = User(user_id=user_data['user_id'], food_preferences=user_data['food_preferences'], dietary_preferences=user_data['dietary_preferences'])
    restaurants = [Restaurant(**rest) for rest in restaurant_data]

    # Get the recommendations
    recommendations = recommend_restaurants(user, restaurants)

    # Convert the Restaurant object to a dictionary for JSON response
    recommendations_json = [{
        'restaurant_id': rec[0].restaurant_id,
        'name': rec[0].name,
        'cuisines': rec[0].cuisines,
        'location': rec[0].location,
        'rating': rec[0].rating,
        'dietary_options': rec[0].dietary_options,
        'similarity_score': rec[1]
    } for rec in recommendations]

    return jsonify(recommendations_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
