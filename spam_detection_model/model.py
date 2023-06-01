import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

def models_response(message = ""):
    message = np.array(message.split())
    message.reshape(1,-1)
    model1 = pickle.load(open("spam_detection_model/multinomialnb.pkl", "rb"))
    model2 = pickle.load(open("spam_detection_model/support-vector-machine.pkl", "rb"))
    model3 = pickle.load(open("spam_detection_model/randomforestclassifier.pkl", "rb"))
    return [model1.predict(message), model1.predict(message), model1.predict(message)]