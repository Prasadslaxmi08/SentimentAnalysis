import streamlit as st 
import joblib 

#load the joblib model 
model_nb = joblib.load("SentimentAnalysis")

st.title("SentimentAnalysis")
ip = st.text_input('Enter your review :')

op = model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])
