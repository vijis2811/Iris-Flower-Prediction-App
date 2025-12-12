import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
st.title("Iris Flower Prediction App")
st.write("This simple app trains a Random Forest model on the Iris dataset and predicts the flower type based on your inputs.")
iris = load_iris()
X = iris.data
y = iris.target
if st.checkbox("Show Iris Dataset"):
    df = pd.DataFrame(X, columns=iris.feature_names)
    df["target"] = y
    st.dataframe(df)
model = RandomForestClassifier()
model.fit(X, y)
st.success("Model trained successfully!")
st.header("Enter Flower Measurements")
sepal_length = st.number_input("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.number_input("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.number_input("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.number_input("Petal Width (cm)", 0.1, 2.5, 1.3)
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
if st.button("Predict"):
    prediction = model.predict(input_data)
    species = iris.target_names[prediction][0]
    st.subheader("Predicted Flower Species:")
    st.success(species)

    st.balloons()