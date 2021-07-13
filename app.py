import streamlit as st
import joblib
st.title('Sentiment Analysis Deployment')
test_model = joblib.load('sentimet analysis')
ip = st.text_input('Enter the text')
op =  test_model.predict([ip])
if st.button('Predict'):
    st.title(op[0])
    
