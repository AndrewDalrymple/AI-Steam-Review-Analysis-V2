# AI-Powered Steam Review Analysis Tool (V2)
# Repository Initialization Script

# This script helps set up the project directory structure for the AI-Steam-Review-Analysis-V2 project.
# Run this script in your desired project folder.

import os

# Define the directory structure
project_structure = {
    "data": ["sample_reviews.json", "processed_reviews.json", "prompt_eval_results.json", "stopwords.txt"],
    "notebooks": ["sentiment_analysis.ipynb", "theme_extraction.ipynb", "prompt_testing.ipynb", "model_evaluation.ipynb"],
    "src/api": ["steam_api.py"],
    "src/nlp": ["sentiment_analysis.py", "keyword_extraction.py", "theme_classification.py"],
    "src/llm": ["prompt_generation.py", "prompt_evaluation.py", "fine_tuning.py"],
    "src/cli": ["cli_main.py", "cli_helpers.py"],
    "tests": ["test_sentiment.py", "test_llm.py", "test_api.py", "test_cli.py"],
    "docs": ["README.md", "INSTALL.md", "USAGE.md", "EVALUATION.md", "API_REFERENCE.md"],
}

# Create directories and placeholder files
for folder, files in project_structure.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder, file)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                if file.endswith(".md"):
                    f.write(f"# {file.replace('.md', '').replace('_', ' ').title()}\n")
                elif file.endswith(".py"):
                    f.write("# Placeholder for {}\n".format(file))

# Create essential files
essential_files = [".gitignore", "requirements.txt", "setup.py", "main.py"]
for file in essential_files:
    if not os.path.exists(file):
        with open(file, "w") as f:
            f.write(f"# {file} - Auto-generated\n")

print("Project structure created successfully.")
