from extract import fetch_comments
from transform import analyze_sentiment
from load import save_to_csv

# sample : JVKE - Golden Hour
video_id = "Pw-0pbY9JeU"

print("🔍 Fetching comments...")
df = fetch_comments(video_id, max_results=200)

print("🧹 Analyzing sentiment...")
df = analyze_sentiment(df)

print("💾 Saving to CSV...")
save_to_csv(df, filename="golden_hour_comments.csv")

print("✅ Done. Ready for dashboard!")
