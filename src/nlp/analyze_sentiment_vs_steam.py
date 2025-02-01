import pandas as pd

# Load the processed data
df = pd.read_csv("data/processed_reviews_with_ratings.csv")

# Count matching and mismatching sentiment vs. Steam ratings
df["match"] = df["sentiment"] == df["steam_rating"]

# Calculate percentages
total_reviews = len(df)
matching_reviews = df["match"].sum()
mismatching_reviews = total_reviews - matching_reviews

match_percentage = (matching_reviews / total_reviews) * 100
mismatch_percentage = (mismatching_reviews / total_reviews) * 100

# Print results
print(f"✅ Total Reviews: {total_reviews}")
print(f"✅ Matches: {matching_reviews} ({match_percentage:.2f}%)")
print(f"❌ Mismatches: {mismatching_reviews} ({mismatch_percentage:.2f}%)")

# Save mismatch data for review
mismatch_df = df[df["match"] == False]
mismatch_df.to_csv("data/mismatched_reviews.csv", index=False)

print("🔍 Mismatched reviews saved to data/mismatched_reviews.csv")
