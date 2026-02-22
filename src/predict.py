import pickle
import pandas as pd

def load_model(path):
    with open(path, 'rb') as f:
        model = pickle.load(f)
    return model

def predict(model, input_data):
    prediction = model.predict(input_data)
    return prediction

