from re import findall
import re
#import demoji

from gensim.parsing.preprocessing import remove_stopwords
from unidecode import unidecode

from num2words import num2words
from nltk.stem import WordNetLemmatizer


def lemmatizer(text):
    lemm_txt = [lemmatizer.lemmatize(word) for word in text]
    return lemm_txt


def convert_numbers(text):
    # Find all numbers in the text
    numbers = findall(r"\d+", text)

    # Replace each number with its full form
    for number in numbers:
        full_form = num2words(int(number))
        text = text.replace(number, full_form)

    return text


# library that contains punctuation
import string

string.punctuation


# defining the function to remove punctuation
def remove_punctuation(text):
    new_punctuation = ''.join(char for char in string.punctuation if char not in ['+', '#', '.'])
    punctuationfree = "".join([i for i in text if i not in new_punctuation])
    return punctuationfree


# storing the puntuation free text


def preprocess_text(text):
    if text is None:
        return []
    words = re.findall(r'\b(?:\w+\.?\w*|\w+\+?\w*)\b', text)
    text = remove_punctuation(text)
    #text = demoji.replace(text, "")
    text = unidecode(text)
    text = convert_numbers(text)
    text = text.strip()
    text = text.lower()
    text = remove_stopwords(text)
    lemmatizer = WordNetLemmatizer()
    text = lemmatizer.lemmatize(text)
    #print(text)
    return words

def preprocess_posting_text(text):
    if text is None:
        return []
    words = re.findall(r'\b(?:\w+\.?\w*|\w+)\b', text)
    lowercase_words = [word.lower() for word in words]
    
    return lowercase_words