from app.data_fetcher import fetch_viewed_posts, fetch_liked_posts, fetch_inspired_posts, fetch_rated_posts
from app.models import User

def fetch_user_data(username):
    """
    Fetch user interaction data using the provided username.
    This includes liked, viewed, inspired, rated posts.
    """
    viewed_posts = fetch_viewed_posts()
    liked_posts = fetch_liked_posts()
    inspired_posts = fetch_inspired_posts()
    rated_posts = fetch_rated_posts()

    interactions = {
        'viewed': viewed_posts,
        'liked': liked_posts,
        'inspired': inspired_posts,
        'rated': rated_posts,
    }
    
    return User(username=username, interactions=interactions)
