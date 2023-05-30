import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

def models_response(message = ""):
    model1 = pickle.load(open("multinomialnb", "rb"))
    model2 = pickle.load(open("support-vector-machine", "rb"))
    model3 = pickle.load(open("randomforestclassifier", "rb"))
    return [model1.predict(message), model1.predict(message), model1.predict(message)]