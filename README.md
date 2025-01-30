# 🍽️ Taste Match

## About
Taste Match is a Tinder-inspired restaurant discovery app that helps food lovers find their perfect dining match. By combining smart recommendation algorithms with an intuitive swipe interface, users can easily discover restaurants that match their tastes and dietary preferences.

## ✨ Features

### Core Features
- 📱 Tinder-style swipe interface for restaurant discovery
- 🎯 Personalized recommendations based on user preferences
- 📍 Location-based restaurant suggestions
- 🥗 Dietary preference filtering (vegetarian, vegan, gluten-free, etc.)
- 👍 Preference learning algorithm that improves with usage

### User Experience
- Quick and easy onboarding process
- Stunning food photography
- Detailed restaurant information at a glance
- Seamless bookmark and history tracking
- Share favorites with friends

## 🛠️ Technical Stack

### Frontend
- React Native
- Redux for state management
- Expo for development
- React Navigation

### Backend
- Node.js
- Express.js
- MongoDB
- AWS S3 for image storage

### APIs
- Google Places API for restaurant data
- Mapbox for location services
- Stripe for payment processing

## 📱 Installation

### Prerequisites
```bash
node >= 14.0.0
npm >= 6.14.0
expo-cli
```

### Setup Steps
1. Clone the repository:
```bash
git clone https://github.com/yourusername/taste-match.git
cd taste-match
```

2. Install dependencies:
```bash
# Install frontend dependencies
cd client
npm install

# Install backend dependencies
cd ../server
npm install
```

3. Configure environment variables:
```bash
# In client/.env
GOOGLE_PLACES_API_KEY=your_api_key
MAPBOX_TOKEN=your_token

# In server/.env
MONGODB_URI=your_mongodb_uri
AWS_ACCESS_KEY=your_aws_key
AWS_SECRET_KEY=your_aws_secret
```

4. Start the development servers:
```bash
# Start backend server
cd server
npm run dev

# Start frontend
cd client
expo start
```

## 🔧 Configuration

### Restaurant Matching Algorithm
The recommendation engine can be fine-tuned in `src/utils/matching.js`:
```javascript
const PREFERENCE_WEIGHTS = {
  cuisine: 0.4,
  price: 0.2,
  distance: 0.2,
  rating: 0.2
};
```

### Dietary Preferences
Add or modify dietary filters in `src/constants/dietary.js`:
```javascript
export const DIETARY_OPTIONS = [
  'vegetarian',
  'vegan',
  'gluten-free',
  'halal',
  'kosher'
];
```

## 📱 Usage

1. **Initial Setup**
   - Create an account
   - Set dietary preferences
   - Enable location services

2. **Discovery**
   - Swipe right to like a restaurant
   - Swipe left to pass
   - Tap for more details

3. **Matches**
   - View matched restaurants in profile
   - Book tables directly through the app
   - Share with friends

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Project is incomplete
