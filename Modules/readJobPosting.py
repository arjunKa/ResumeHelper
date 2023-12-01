from re import findall
import re

def preprocess_posting_text(text):
    if text is None:
        return []
    words = re.findall(r'\b(?:\w+\.?\w*|\w+)\b', text)
    lowercase_words = [word.lower() for word in words]
    
    return lowercase_words