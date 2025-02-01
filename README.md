#### **🚀 AI-Powered Steam Review Analysis Tool**
📌 **Analyze and summarize Steam game reviews using AI & NLP.**  
🔍 **Automates sentiment analysis, key theme extraction, and question generation.**

---

### **📌 Features**
✅ **Fetch & Process Steam Reviews** – Uses Steam API to collect user feedback  
✅ **Sentiment Analysis** – Classifies reviews as Positive, Negative, or Neutral  
✅ **AI-Generated Review Summaries** – Uses GPT to extract key positives & negatives  
✅ **Common Player Requests** – Identifies trending feature requests  
✅ **Word Cloud Visualization** – Displays top positive & negative keywords  
✅ **Markdown & JSON Summaries** – Saves AI insights in structured formats  

---

### **📌 Installation Guide**

#### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-username/AI-Steam-Review-Analysis-V2.git
cd AI-Steam-Review-Analysis-V2
```

#### **Step 2: Set Up Python Environment**  
Ensure you have Python 3.9+ installed. You can use Anaconda or venv.  
```bash
conda create --name steam_ai python=3.9
conda activate steam_ai
pip install -r requirements.txt
```

#### **Step 3: Set Up API Keys**  
Create a `.env` file in the root folder and add:
```
OPENAI_API_KEY=your-openai-key
STEAM_API_KEY=your-steam-key
```

---

### **📌 Usage Instructions**

#### **Fetch Game Reviews:**  
```bash
python src/api/steam_api.py --game_id 620
```

#### **Run Sentiment Analysis & Word Cloud:**  
```bash
python src/nlp/sentiment_analysis.py
```

#### **Generate AI Summaries:**  
```bash
python src/llm/generate_summaries.py
```

---

### **📌 Example AI-Generated Summary**
```md
**Key Positives:**
- Players praise the co-op mode, puzzle design, and voice acting.
- The game’s story and atmosphere are immersive and memorable.

**Key Negatives:**
- Some players feel the game is too short.
- Certain puzzles outside the test chambers are seen as tedious.

**Common Player Requests:**
- Players want additional DLC and extended modding support.
```

---

### **📌 Future Enhancements**
🔹 **Train a Custom Sentiment Model** – Move beyond VADER for better accuracy  
🔹 **Track Review Trends Over Time** – Analyze sentiment shifts after game updates  
🔹 **Web Dashboard** – Expand CLI to an interactive web app  

---

### **📌 Contributing & License**
📝 **MIT License** – Free for personal and educational use.  
📩 **Want to contribute?** Open an issue or fork the repo!  

---

🚀 **Ready to get started? Clone the repo and analyze your favorite games!**


