from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer #TfidVectorizer to convert the text into feature vectors(numbers)
import pickle
import logging

# Enable logging for debugging purposes
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


app = Flask(__name__)

# Load the trained model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorize = pickle.load(open('vect.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news_text = request.form['news_text']
        # Vectorize the news text
        news_vector = vectorize.transform([news_text])
        # Make prediction using the loaded model
        prediction = model.predict(news_vector)[0]
        # Determine the class label
        if prediction == 1:
            result = 'True'  # True with 95% precision
        else:
            result = 'Fake'  # Fake with 93% 
        return render_template('index.html', prediction=result, news_text=news_text)

if __name__ == '__main__':
    app.run(debug=True)
