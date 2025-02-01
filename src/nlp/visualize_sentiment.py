import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load processed review data
df = pd.read_csv("data/processed_reviews_with_ratings.csv")

# Ensure 'sentiment' and 'steam_rating' columns exist
if "sentiment" not in df.columns or "steam_rating" not in df.columns:
    print("❌ Error: Sentiment analysis results not found.")
    exit()

# Create the 'figures' directory if it doesn't exist
os.makedirs("figures", exist_ok=True)

# 📊 **1. Sentiment Distribution Pie Chart**
plt.figure(figsize=(6, 6))
df["sentiment"].value_counts().plot.pie(autopct="%1.1f%%", colors=["green", "red", "gray"])
plt.title("Sentiment Distribution")
plt.ylabel("")  # Hide y-axis label
plt.savefig("figures/sentiment_distribution.png")
plt.show()

# 📊 **2. Steam Rating vs. AI Sentiment (Bar Chart)**
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="sentiment", hue="steam_rating", palette="coolwarm")
plt.title("Steam Rating vs. AI Sentiment")
plt.xlabel("VADER Sentiment")
plt.ylabel("Count of Reviews")
plt.savefig("figures/sentiment_vs_steam_rating.png")
plt.show()

# 📊 **3. Mismatched Reviews Histogram**
df["match"] = df["sentiment"] == df["steam_rating"]
mismatch_counts = df["match"].value_counts()

plt.figure(figsize=(6, 4))
mismatch_counts.plot(kind="bar", color=["green", "red"])
plt.xticks(ticks=[0, 1], labels=["Mismatch", "Match"], rotation=0)
plt.title("How Often AI Sentiment Matches Steam Ratings")
plt.ylabel("Number of Reviews")
plt.savefig("figures/match_vs_mismatch.png")
plt.show()

print("✅ Visualizations saved in the 'figures' folder!")
