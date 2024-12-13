from fastapi import FastAPI, Query
from typing import List, Optional
from app.recommendation import get_content_based_recommendations, get_category_based_recommendations, get_mood_based_recommendations
from app.data_fetching import get_user_posts, fetch_all_videos
from app.models import Video

app = FastAPI()

@app.get("/feed")
async def get_recommended_videos(
    username: str,
    category_id: Optional[str] = Query(None),
    mood: Optional[str] = Query(None)
):
    all_videos = fetch_all_videos()
    user_posts = get_user_posts(username)
    recommendations = []

    if mood:
        recommendations.extend(get_mood_based_recommendations(mood, all_videos))

    if category_id:
        recommendations.extend(get_category_based_recommendations(category_id, all_videos))

    recommendations.extend(get_content_based_recommendations(user_posts, all_videos))

    return {"recommended_videos": recommendations[:10]}

@app.get("/feed/category")
async def get_recommended_videos_by_category(
    username: str,
    category_id: str
):
    all_videos = fetch_all_videos()
    user_posts = get_user_posts(username)
    recommendations = get_category_based_recommendations(category_id, all_videos)
    recommendations.extend(get_content_based_recommendations(user_posts, all_videos))
    return {"recommended_videos": recommendations[:10]}

@app.get("/feed/username")
async def get_recommended_videos_by_username(
    username: str
):
    all_videos = fetch_all_videos()
    user_posts = get_user_posts(username)
    recommendations = get_content_based_recommendations(user_posts, all_videos)
    return {"recommended_videos": recommendations[:10]}
