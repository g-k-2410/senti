import requests
import pandas as pd
from config import YOUTUBE_API_KEY

def fetch_comments(video_id, max_results=200):
    comments = []
    url = "https://www.googleapis.com/youtube/v3/commentThreads"
    params = {
        "part": "snippet",
        "videoId": video_id,
        "maxResults": 100,
        "textFormat": "plainText",
        "key": YOUTUBE_API_KEY
    }

    print("Fetching comments from YouTube...")
    total_fetched = 0

    while total_fetched < max_results:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch comments: {response.text}")
        
        data = response.json()
        items = data.get("items", [])
        
        for item in items:
            comment = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "author": comment["authorDisplayName"],
                "text": comment["textDisplay"],
                "likeCount": comment["likeCount"],
                "publishedAt": comment["publishedAt"]
            })
            total_fetched += 1
            if total_fetched >= max_results:
                break

        # Check if there are more pages
        if "nextPageToken" in data and total_fetched < max_results:
            params["pageToken"] = data["nextPageToken"]
        else:
            break

    print(f"✅ {len(comments)} comments fetched.")
    return pd.DataFrame(comments)
