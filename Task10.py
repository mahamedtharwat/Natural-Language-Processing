import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')

def determine_stems(sentence):
    stemmer = PorterStemmer()
    tokens = word_tokenize(sentence)
    stems = [stemmer.stem(token) for token in tokens]
    return stems

# Input sentence
input_sentence = "The quick brown foxes are jumping over the lazy dogs."

# Determine stems in the input sentence
stems = determine_stems(input_sentence)

print("Original sentence:", input_sentence)
print("Stems in the sentence:", stems)
