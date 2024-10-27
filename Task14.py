import os
from nltk.corpus import wordnet
from difflib import get_close_matches

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return synonyms

def process_text_file(file_path, target_word):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        # Check if the target word is present in the text
        if target_word in text:
            print(f"Document: {os.path.basename(file_path)}")
            print(f"Words with the same meaning as '{target_word}':")
            synonyms = get_synonyms(target_word)
            synonyms_in_text = set(text.split()).intersection(synonyms)
            if synonyms_in_text:
                print(synonyms_in_text)
            else:
                print("No words with the same meaning found.")
            print("=" * 50)

def analyze_text_files_in_directory(directory, target_word):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            process_text_file(file_path, target_word)

# Directory containing text files
directory_path = "path_to_directory_containing_text_files"

# Target word to search for synonyms
target_word = "your_target_word"

# Analyze text files in the directory
analyze_text_files_in_directory(directory_path, target_word)
