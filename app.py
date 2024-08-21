import streamlit as st
import google.generativeai as genai

st.title("Welcome To Alyx ")
genai.configure(api_key="AIzaSyCCHm6DPGyYjZT4JmQj5hA3Ew8scBfwoHc")
text = st.text_input("Enter Your Question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])



if st.button("click me"):
    response = chat.send_message(text)
    st.write(response.text)
