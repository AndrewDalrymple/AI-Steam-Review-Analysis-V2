import re
import os
import pandas as pd
import spacy
import nltk
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# Load NLP model & NLTK resources
nltk.download("stopwords")
nltk.download("vader_lexicon")
nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))
sia = SentimentIntensityAnalyzer()  # VADER Sentiment Analyzer

def clean_text(text):
    """Cleans and preprocesses text for analysis."""
    if not isinstance(text, str):
        return ""
    
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Keep letters only
    text = text.lower()
    doc = nlp(text)
    words = [token.lemma_ for token in doc if token.text not in stop_words]
    
    return " ".join(words)

def get_sentiment(text):
    """Classifies sentiment using VADER."""
    if not isinstance(text, str) or text.strip() == "":
        return "Neutral"

    sentiment_score = sia.polarity_scores(text)["compound"]

    if sentiment_score >= 0.05:
        return "Positive"
    elif sentiment_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def preprocess_reviews(df):
    """Processes reviews: cleaning, sentiment classification, and Steam rating comparison."""
    df["cleaned_review"] = df["review_text"].astype(str).apply(clean_text)
    df["sentiment"] = df["cleaned_review"].apply(get_sentiment)
    df["steam_rating"] = df["voted_up"].apply(lambda x: "Positive" if x else "Negative")
    return df

if __name__ == "__main__":
    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)

    reviews_path = "data/sample_reviews.json"
    if not os.path.exists(reviews_path):
        print(f"❌ ERROR: Missing {reviews_path}. Fetch Steam reviews first!")
        exit(1)

    # Load and process reviews
    reviews_df = pd.read_json(reviews_path)
    cleaned_df = preprocess_reviews(reviews_df)

    # Save sentiment analysis results
    output_path = "data/processed_reviews_with_ratings.csv"
    cleaned_df.to_csv(output_path, index=False)
    print(f"✅ Sentiment analysis completed! Results saved to {output_path}")

    # Extract useful words (NOT phrases) from positive and negative reviews
    print("🔹 Extracting meaningful words for sentiment analysis...")

    def extract_common_words(sentiment):
        text = " ".join(cleaned_df[cleaned_df["sentiment"] == sentiment]["cleaned_review"].astype(str))
        words = [word.lower() for word in text.split() if word.lower() not in stop_words]
        return Counter(words).most_common(10)  # Get top 10 most common words

    top_positive_words = extract_common_words("Positive")
    top_negative_words = extract_common_words("Negative")

    print("🔹 Top 10 Positive Words:", top_positive_words)
    print("🔹 Top 10 Negative Words:", top_negative_words)

    # Generate word clouds
    for sentiment, words in [("Positive", top_positive_words), ("Negative", top_negative_words)]:
        if words:
            wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(dict(words))
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.title(f"Most Common {sentiment} Words in Steam Reviews")
            plt.show()
        else:
            print(f"⚠️ No meaningful words found for {sentiment} sentiment. Try fetching more reviews.")
