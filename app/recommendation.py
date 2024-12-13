from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.models import Video

def get_content_based_recommendations(user_posts, all_videos):
  
    video_descriptions = [video['description'] for video in all_videos]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(video_descriptions)

    user_video_descriptions = [video['description'] for video in user_posts]
    user_tfidf_matrix = vectorizer.transform(user_video_descriptions)
    
    similarities = cosine_similarity(user_tfidf_matrix, tfidf_matrix)
    
    recommendations = []
    for idx in similarities.argsort()[0][-10:]:
        recommendations.append(all_videos[idx])
    
    return recommendations

def get_category_based_recommendations(category_id, all_videos):
 
    recommendations = [video for video in all_videos if category_id in video['category']]
    return recommendations

def get_mood_based_recommendations(mood, all_videos):
    recommendations = []
    
    for video in all_videos:
        
        description = video.get('description', '')
        
        if mood.lower() in description.lower():
            recommendations.append(video)
    
    return recommendations

