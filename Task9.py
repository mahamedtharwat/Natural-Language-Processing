import PyPDF2
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from nltk.stem import PorterStemmer

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def extract_text_from_pdf(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        first_page_text = pdf_reader.getPage(0).extractText()
        return first_page_text

def tokenize_and_tag(text):
    sentences = sent_tokenize(text)
    tagged_sentences = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        tagged_words = pos_tag(words)
        tagged_sentences.append(tagged_words)
    return tagged_sentences

def stem_tagged_sentences(tagged_sentences):
    stemmer = PorterStemmer()
    stemmed_sentences = []
    for tagged_sentence in tagged_sentences:
        stemmed_sentence = []
        for word, tag in tagged_sentence:
            stemmed_word = stemmer.stem(word)
            stemmed_sentence.append((stemmed_word, tag))
        stemmed_sentences.append(stemmed_sentence)
    return stemmed_sentences

pdf_file_path = "path_to_your_pdf_file.pdf"
text = extract_text_from_pdf(pdf_file_path)
tagged_sentences = tokenize_and_tag(text)
stemmed_sentences = stem_tagged_sentences(tagged_sentences)

for sentence in stemmed_sentences:
    print(sentence)
