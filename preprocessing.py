import re
import string

import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download Required things
#
# nltk.download('stopwords')
# nltk.download('punkt')


stop_words = stopwords.words('english')


def remove_punctuation(text):
    """
    Function to remove Punctuation
    :param text:
    :return returns text without punctuation:
    """
    text = "".join([char for char in text if char not in string.punctuation])
    return text


def remove_stop_words(word_list):
    """
    Function to remove Stop Words
    :param word_list:
    :return returns list after removing stop words:
    """
    word_list = [word for word in word_list if word not in stop_words]
    return word_list


def stem_word(word_list):
    """
    Function to perform Stemming
    :param word_list:
    :return returns a list after performing stemming in each word:
    """
    porter = PorterStemmer()
    stemmed_words = [porter.stem(word) for word in word_list]
    return stemmed_words


def text_preprocessing(text):
    text = remove_punctuation(text)
    text_tokens = word_tokenize(text)
    text_tokens = [word for word in text_tokens if len(word) > 0]
    filtered_words = remove_stop_words(text_tokens)
    stemmed_words = stem_word(filtered_words)
    return stemmed_words


def preprocessing(data):
    lines = sent_tokenize(data)
    ready_data = []
    ready_data = [text_preprocessing(line.lower()) for line in lines]
    return ready_data

