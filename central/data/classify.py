import joblib
import numpy as np

class Classify:
    def __init__(self):
        pass
    def predicState(self, X):

        # Load the saved SVM model from the file
        loaded_svm_model = joblib.load('svm_model.pkl')
        state = loaded_svm_model.predict(X)
        return state
