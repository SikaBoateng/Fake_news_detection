# Fake_news_detection_project
Fake News Detection Project
Description
This project aims at detecting fake news using the naïve Bayes classifier. This repository contains the necessary code and resources to build, train, and evaluate this fake news detection model.

Table of Contents
•	Installation
•	Usage
•	Dataset
•	Model
•	Evaluation
•	Contributions

Installation
•	Download and extract the Aqu8app folder 
•	Right-click on the folder and choose "Open with terminal"
•	Type in the command "python app.py" to start the application
•	Press Ctrl on the keyboard and click on the URL "http://127.0.0.1:5000" to launch the app.

Usage
1.	Prepare your dataset 
2.	Preprocess the data (cleaning, tokenization, etc.) 
3.	Train the fake news detection model using the prepared data (
4.	Evaluate the model's performance using the evaluation metrics
5.	Fine-tune the model, or experiment with different architectures to improve performance.
   
Dataset
The dataset used for this project is the ISOT Fake News Dataset. This dataset contains 2 sub-datasets: true.csv and fake.csv. You can use publicly available datasets or create your own. The dataset was cleaned using preprocessing functions from SCIKIT learn. Make sure the dataset is split into training, validation, and test sets. 
Model
We use a machine learning model based on text classification for fake news detection. The classifier used was the Multinomial Naïve Bayes classifier. You can experiment with other classifiers and parameters to achieve the best results.

Evaluation
We use metrics such as accuracy, precision, recall, F1-score, and macro average to evaluate the model's performance. 




