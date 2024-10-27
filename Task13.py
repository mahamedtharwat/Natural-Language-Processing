import os
from textblob import TextBlob
from difflib import get_close_matches

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

def process_text_file(file_path, target_word):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        blob = TextBlob(text)
        # Check if the target word is present in the text
        if target_word in blob.words:
            sentiment = analyze_sentiment(text)
            print(f"Document: {os.path.basename(file_path)}, Sentiment: {sentiment}")
        else:
            # Find the closest word in the text
            closest_word = get_close_matches(target_word, blob.words)
            if closest_word:
                print(f"Word '{target_word}' not found in {os.path.basename(file_path)}. Closest match: {closest_word[0]}")
            else:
                print(f"Word '{target_word}' not found in {os.path.basename(file_path)}.")

def analyze_text_files_in_directory(directory, target_word):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            process_text_file(file_path, target_word)

# Directory containing text files
directory_path = "Cover_letter.pdf"

# Target word to search for
target_word = "your_target_word"

# Analyze text files in the directory
analyze_text_files_in_directory(Cover_letter.pdf, target_word)
