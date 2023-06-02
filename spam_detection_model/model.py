import numpy as np 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle

def models_response(message = ""):
    model =  pickle.load(open("spam_detection_model/clfPipeline.pkl", "rb"))
    return True if model.predict([message]) == np.array([1]) else False