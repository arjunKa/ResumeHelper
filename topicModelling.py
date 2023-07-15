from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel
from readJobPosting import *


def preprocess_text2(text):
    if text is None:
      return []
    text = remove_punctuation(text)
    text = demoji.replace(text, '')
    text = unidecode(text)
    text = convert_numbers(text)
    text= text.strip()
    text = text.lower()
    text = remove_stopwords(text)
    lemmatizer = WordNetLemmatizer()
    text = lemmatizer.lemmatize(text)
    tokens = text.split()
    return tokens

def return_topics(reviews):
    # Preprocess the reviews
    review_tokens = [preprocess_text2((reviews))]

    # Create a dictionary from the tokens
    dictionary = Dictionary(review_tokens)

    # Create a bag-of-words corpus from the dictionary
    corpus = [dictionary.doc2bow(tokens) for tokens in review_tokens]

    # Train the LDA model on the corpus
    num_topics = 10
    lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, passes=10)

    # Print the topics
    text = ''
    for i, topic in lda_model.show_topics(num_topics=num_topics, num_words=14, formatted=False):
        text += ('Topic {}: {}\n'.format(i+1, [word for word, _ in topic]))
        
    return text