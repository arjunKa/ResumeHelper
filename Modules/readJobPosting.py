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
    numbers = re.findall(r"\d+", text)

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
    punctuationfree = "".join([i for i in text if i not in string.punctuation])
    return punctuationfree


# storing the puntuation free text


def preprocess_text(text):
    if text is None:
        return []
    text = remove_punctuation(text)
    # text = demoji.replace(text, "")
    text = unidecode(text)
    text = convert_numbers(text)
    text = text.strip()
    text = text.lower()
    text = remove_stopwords(text)
    lemmatizer = WordNetLemmatizer()
    text = lemmatizer.lemmatize(text)
    return text
