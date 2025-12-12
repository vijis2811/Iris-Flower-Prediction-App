This project is a simple Streamlit web application that trains a Machine Learning model using the built-in Iris dataset and allows users to make real-time predictions through an interactive UI.

It is designed for beginners who want to learn:

how to build a simple ML model

how to integrate it into a Streamlit web app

how to take user input and view predictions live

Features

Loads and explores the Iris dataset

Trains a Random Forest Classifier

Interactive UI for entering flower measurements

Real-time prediction of Iris species

Option to view the dataset inside the app

Project Structure
project/
│── app.py           
│── README.md       

Machine Learning Model

The app uses:

Dataset: Iris (from scikit-learn)

Algorithm: RandomForestClassifier

Task: Multi-class classification
(Predicting Setosa, Versicolor, or Virginica)

The model is trained inside the app so no saved model file is required.
