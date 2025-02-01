import json
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API Key
load_dotenv()
STEAM_AI_OPENAI_KEY = os.getenv("STEAM_AI_OPENAI_KEY")
client = OpenAI(api_key=STEAM_AI_OPENAI_KEY)

# Function to save AI summary in Markdown format for GitHub
def save_summary_as_markdown(summary_text, file_path="data/ai_summary.md"):
    """
    Saves the AI-generated summary as a Markdown file for GitHub.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure directory exists
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("# 🎮 AI-Generated Steam Review Summary\n\n")
        f.write(summary_text)
    
    print(f"✅ AI summary saved in Markdown format: {file_path}")

# Function to save AI summary as a JSON file
def save_summary_as_json(summary_dict, file_path="data/ai_summary.json"):
    """
    Saves the AI-generated summary as a JSON file for structured storage.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure directory exists
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(summary_dict, f, indent=4)

    print(f"✅ AI summary saved in JSON format: {file_path}")

# Load processed review data
with open("data/processed_reviews_with_ratings.csv", "r", encoding="utf-8") as f:
    reviews_text = f.read()

# Trim reviews to avoid exceeding token limits
MAX_REVIEW_LENGTH = 5000  # Adjust as needed based on OpenAI limits
if len(reviews_text) > MAX_REVIEW_LENGTH:
    reviews_text = reviews_text[:MAX_REVIEW_LENGTH] + "...\n[Truncated due to token limits]"
    print("⚠️ Warning: Review text truncated to fit within OpenAI token limits.")


# Define LLM prompt for structured summarization
messages = [
    {"role": "system", "content": (
        "Analyze the following Steam reviews and generate a structured summary using only real player feedback. "
        "DO NOT include generic game descriptions, marketing language, or irrelevant details.\n\n"
        "**Key Positives:**\n"
        "- Summarize the most frequently praised aspects (gameplay, mechanics, story, visuals, sound, performance).\n"
        "- Only include feedback that appears in multiple reviews—avoid one-off opinions.\n"
        "- Do not make subjective statements—stick to what players explicitly say.\n\n"
        
        "**Key Negatives:**\n"
        "- Identify the most common player complaints (bugs, balance issues, UI problems, pacing concerns).\n"
        "- Separate technical issues from design concerns.\n"
        "- Ensure all complaints are based on recurring patterns—ignore isolated comments.\n\n"
        
        "**Common Player Requests:**\n"
        "- List frequent suggestions for improvements (DLC, features, balance changes).\n"
        "- Include requests mentioned by multiple players—ignore niche suggestions.\n"
        "- Only summarize specific requests, not general opinions.\n\n"
        
        "**Sentiment-Based Analysis:**\n"
        "- Extract the five most common positive and negative keywords (actual feedback, no generic words).\n"
        "- Provide an estimated sentiment breakdown: % positive, % negative, % mixed.\n"
        "- Only include meaningful sentiment trends—do not assume a rating.\n\n"
        
        "**Use clear bullet points for clarity. Keep responses concise, factual, and strictly based on provided reviews.**"
    )},
    {"role": "user", "content": reviews_text}
]

# Generate AI response
response = client.chat.completions.create(
    model="gpt-4",  # Adjust based on available models
    messages=messages,
    max_tokens=500
)

# Extract AI summary text
ai_summary = response.choices[0].message.content.strip()

# Print AI summary
print("\n✅ AI-Generated Review Summary:\n")
print(ai_summary)

# Save AI summary in Markdown format for GitHub
save_summary_as_markdown(ai_summary)

# Convert AI summary to dictionary format & save as JSON
summary_dict = {
    "summary_text": ai_summary
}
save_summary_as_json(summary_dict)

