import nltk

# Download NLTK resources for Arabic (if not already downloaded)
nltk.download('stopwords')

# Get the list of Arabic stopwords
arabic_stopwords = nltk.corpus.stopwords.words('arabic')

# Print the list of Arabic stopwords
print("List of Arabic stopwords:")
print(arabic_stopwords)
