# Streamlit: 
#    Streamlit is a Python framework
#    converts data science and machine learning scripts into interactive web applications.
import streamlit as st
import numpy as np
import pickle
from pathlib import Path

model_path=Path(__file__).parent/"model.pkl"
with open(model_path,"rb") as f:
    model= pickle.load(f)

st.title("Iris Flower Prediction App")
st.markdown("### Developed by Saad Alam")

sepallength= st.slider("Sepal length (cm)",4.3,7.9)
sepalwidth= st.slider("Sepal width (cm)",2.0,4.4)
petallength= st.slider("Petal length (cm)",1.0,6.9)
petalwidth= st.slider("Petal width (cm)",0.1,2.5)

if st.button("Prediction"):
    input_data=np.array([[sepallength, sepalwidth,petallength,petalwidth]])
    prediction= model.predict(input_data)
    species= ["Setosa", "Versicolor","Virginica"]
    st.success(f"Predict Species: {species[prediction[0]]}")



