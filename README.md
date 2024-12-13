# Video Recommendation System

This project is a **Video Recommendation System** built using **FastAPI**. It provides personalized video recommendations based on the user's preferences such as mood, category, and content. The system allows fetching recommendations based on different parameters and is designed for easy integration with frontend applications.

## Features

- **Content-Based Recommendations**: Recommends videos based on the user's previous posts.
- **Category-Based Recommendations**: Provides video recommendations based on a specified category.
- **Mood-Based Recommendations**: Suggests videos according to the user's mood.
- **Multiple Endpoints**: Three endpoints for fetching recommended videos based on different filters.

## Installation

Follow these steps to set up the project locally.

### Prerequisites

Make sure you have the following installed:

- Python 3.7 or above
- pip (Python package manager)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/NishitPatel25/video-recommendation-system.git
   cd video-recommendation-system

### API Endpoints

The following endpoints are available for fetching recommended videos based on different parameters:

#### 1. **Get Recommended Videos by Mood and Category**

- **URL**: `/feed`
- **Method**: `GET`
- **Parameters**:
  - `username` (required): The username for fetching recommendations.
  - `category_id` (optional): The category of videos (e.g., "action", "comedy").
  - `mood` (optional): The user's mood (e.g., "happy", "sad").
  
- **Example Request**:
http://localhost:8000/feed?username=johndoe&category_id=action&mood=happy


- **Response**:
Returns a list of recommended videos based on mood, category, and content preferences.

---

#### 2. **Get Recommended Videos by Category**

- **URL**: `/feed/category`
- **Method**: `GET`
- **Parameters**:
- `username` (required): The username for fetching recommendations.
- `category_id` (required): The category of videos (e.g., "action", "comedy").

- **Example Request**:
http://localhost:8000/feed/category?username=johndoe&category_id=action


- **Response**:
Returns a list of recommended videos based on the specified category and user posts.

---

#### 3. **Get Recommended Videos by Username**

- **URL**: `/feed/username`
- **Method**: `GET`
- **Parameters**:
- `username` (required): The username for fetching recommendations based on the user’s posts.

- **Example Request**:
http://localhost:8000/feed/username?username=johndoe
