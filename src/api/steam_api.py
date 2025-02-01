import requests
import pandas as pd
import os

# Load API key from environment variable
STEAM_API_KEY = os.getenv("STEAM_API_KEY")  # Set this in your .env file or system

# Base URL for Steam reviews
STEAM_REVIEW_URL = "https://store.steampowered.com/appreviews/{app_id}"

def fetch_reviews(app_id, num_reviews=100):
    """
    Fetches user reviews from Steam for a given app ID.
    
    :param app_id: The Steam app ID of the game.
    :param num_reviews: Number of reviews to fetch.
    :return: A pandas DataFrame containing the reviews.
    """
    params = {
        "json": 1,
        "num_per_page": num_reviews,
        "purchase_type": "all"
    }

    response = requests.get(STEAM_REVIEW_URL.format(app_id=app_id), params=params)

    if response.status_code != 200:
        print(f"Error fetching reviews: {response.status_code}")
        return None

    data = response.json()
    
    if "reviews" not in data:
        print("No reviews found.")
        return None

    reviews = data["reviews"]
    df = pd.DataFrame([{
        "recommendation": review["recommendationid"],
        "review_text": review["review"],
        "timestamp_created": review["timestamp_created"],
        "voted_up": review["voted_up"],
        "votes_up": review["votes_up"],
        "votes_funny": review["votes_funny"],
    } for review in reviews])

    return df

# Test with a sample game (e.g., Portal 2, app_id=620)
if __name__ == "__main__":
    game_id = 620  # Change this to any game's Steam App ID
    reviews_df = fetch_reviews(game_id)
    if reviews_df is not None:
        print(reviews_df.head())  # Print the first few reviews
