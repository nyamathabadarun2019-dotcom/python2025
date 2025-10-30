 # social_media_analytics_simple.py

import pandas as pd
import matplotlib.pyplot as plt

# ---------------- Step 1: Create mock data ----------------
twitter_data = {
    "post": [
        "Launching our new product!",
        "AI is changing everything!",
        "Follow us for more updates!"
    ],
    "likes": [120, 340, 210],
    "retweets": [45, 90, 70],
    "replies": [12, 20, 10],
    "date": pd.date_range("2025-10-01", periods=3)
}

youtube_data = {
    "video": [
        "Intro to Python",
        "AI Explained Simply",
        "Data Science Tips"
    ],
    "views": [1500, 2300, 1800],
    "likes": [300, 500, 420],
    "comments": [25, 50, 35],
    "date": pd.date_range("2025-09-01", periods=3)
}

twitter_df = pd.DataFrame(twitter_data)
youtube_df = pd.DataFrame(youtube_data)

# ---------------- Step 2: Analyze data ----------------
def analyze_data(df, platform_name):
    print(f"\n===== {platform_name} Stats =====")
    print(df.describe())

    # Find top post/video
    top_post = df.loc[df['likes'].idxmax()]
    print(f"\n🔥 Top {platform_name} post/video:")
    print(top_post)

    # Average likes
    avg_likes = df['likes'].mean()
    print(f"⭐ Average likes on {platform_name}: {avg_likes:.2f}")

# ---------------- Step 3: Visualize data ----------------
def plot_data(df, x, y, title, color):
    plt.figure(figsize=(6,4))
    plt.bar(df[x], df[y], color=color)
    plt.title(title)
    plt.xticks(rotation=20, ha='right')
    plt.ylabel(y)
    plt.tight_layout()
    plt.show()

# ---------------- Step 4: Run everything ----------------
if __name__ == "__main__":
    print("🚀 Social Media Analytics Tool\n")

    analyze_data(twitter_df, "Twitter")
    analyze_data(youtube_df, "YouTube")

    # Visualizations
    plot_data(twitter_df, "post", "likes", "Twitter Likes per Post", "skyblue")
    plot_data(youtube_df, "video", "likes", "YouTube Likes per Video", "orange")

    print("\n✅ Done! Insights and charts displayed.")
