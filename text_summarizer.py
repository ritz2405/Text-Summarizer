import streamlit as st
import torch
import re

from transformers import pipeline

summarizer = pipeline('summarization', model='facebook/bart-large-cnn')

st.write("""
# Text Summarizer
""")

text_input = st.text_area("Text to summarize")

if text_input:
    text_input = str(text_input)

st.write("## Summarized Text")
output_text = str(summarizer(text_input, max_length=1000, min_length=10, do_sample=False))
output_text = re.sub(r'[^\w\s]', '', output_text)
output_text = output_text.split(' ', 1)[1]
output_text = str(output_text)
st.write("".join(output_text))