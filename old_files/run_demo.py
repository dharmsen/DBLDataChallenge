# Standard dependencies
#import pickle
import numpy as np
import pandas as pd

# Preprocessing
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

# Machine Learning
import xgboost as xgb
from xgboost import XGBClassifier
from keras.models import load_model

from DBL1_repo.demo.plotter import Plotter


class SentimentDemo:
    '''
    Sentiment analysis
    '''

    def __init__(self):
        self.sentence = ''
        self.stopwords = set(stopwords.words('english'))
        self.stemmer = SnowballStemmer("english")
        self.vectorizer = TfidfVectorizer()
        self.nn_model = load_model('nn_sentiment_model.h5')
        self.xgb_model = pickle.load(open('xgboost_1.dat', 'rb'))
        self.mapping = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}

    def tokenize(self, sentence):
        '''
        Splits up words and makes a list of all words in the tweet
        '''
        tokenized_sentence = word_tokenize(sentence)
        return tokenized_sentence

    def remove_stopwords(self, sentence):
        '''Removes stopwords like 'a', 'the', 'and', etc.'''
        filtered_sentence = []
        for w in sentence:
            if w not in self.stopwords and len(w) > 1 and w[:2] != '//' and w != 'https':
                filtered_sentence.append(w)
        return filtered_sentence

    def stem(self, sentence):
        '''
        Stems certain words to their root form.
        For example, words like 'computer', 'computation'
        all get trunacated to 'comput'
        '''
        return [self.stemmer.stem(word) for word in sentence]

    def join_to_string(self, sentence):
        '''
        Joins the tokenized words to one string.
        '''
        return ' '.join(sentence)

    def vectorize(self, sentence):
        '''
        Vectorizes a preprocessed sentence into a TF-IDF format
        Returns a sparse matrix
        '''
        _ = self.vectorizer.fit_transform(np.load('vector.npy'))
        return self.vectorizer.transform(sentence)

    def predict(self, X):
        '''
        Makes predictions and maps the integer predictions to strings
        '''
        mapping = self.mapping
        nn_prediction = mapping[np.argmax(self.nn_model.predict(X))]
        xgb_prediction = mapping[int(self.xgb_model.predict(xgb.DMatrix(X)))]
        return nn_prediction, xgb_prediction

    def preprocess(self):
        '''
        Preprocess a selected number of rows and
        connects them back to strings
        '''
        # Perform preprocessing
        tweet = self.sentence
        tokenized = self.tokenize(tweet)
        cleaned = self.remove_stopwords(tokenized)
        stemmed = self.stem(cleaned)
        return self.join_to_string(stemmed)

    def demo(self):
        '''
        Asks for input and returns to
        sentiment predictions as strings
        '''
        print('Please input your tweet\n')
        self.sentence = input()
        print(f'\nRetreiving predictions...')
        # Preprocess, Vectorize and get predictions
        processed = self.preprocess()
        vectorized = self.vectorize(processed)
        predictions = self.predict(vectorized)
        print(
            f'\nPrediction 1 (Neural Network): {predictions[0]}\n\nPrediction 2 (Gradient Boosting): {predictions[1]}')
        # Return predictions as a tuple
        return predictions

if __name__ == '__main__':
    # Initialize demo
    Demo = SentimentDemo()
    # Perform demo
    Demo.demo()
