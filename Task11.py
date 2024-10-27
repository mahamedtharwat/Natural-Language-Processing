import os
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

def process_text_file(cover_letter.pdf):
    with open(cover_letter.pdf, 'r', encoding='utf-8') as file:
        text = file.read()
        sentiment = analyze_sentiment(text)
        return sentiment

def analyze_text_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            sentiment = process_text_file(file_path)
            print(f"Document: {filename}, Sentiment: {sentiment}")

# Directory containing text files
directory_path = "cover_letter.pdf"

# Analyze text files in the directory
analyze_text_files_in_directory(cover_letter.pdf)
