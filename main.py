import os
import streamlit as st
import requests
import urllib.parse

st.title('✍️ Rephraser')

@st.cache
def Rephrase(input):
  phrase = urllib.parse.quote(input)
  x = requests.get(f'https://rephraser.johnpaulbin.repl.co/rephrase/{phrase}').text
  st.success("Rephrased")
  return x


prompt = st.text_area("Enter Your Prompt", "Type Here ...")

if(st.button('Rephrase')):
  st.write(f"**{Rephrase(prompt)}**")

os.system("streamlit run main.py --server.enableCORS false")
