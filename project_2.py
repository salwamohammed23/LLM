import streamlit as st
import requests
from PIL import Image
import io
from transformers import pipeline
import matplotlib.pyplot as plt





# Split the page into two tabs
tab1, tab2= st.tabs(["Image Generate App", "Text Generation App"])

# Image Inference Section
with tab1:
    st.header("Image Inference")
    image_url = st.text_input("Enter your keyword:")
    if st.button("Generate Image"):
        # API Query
        response = requests.post(API_URL, headers=HEADERS, json={"inputs": image_url})
        image_bytes = response.content

        # Display Image
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption="Inferred Image", use_column_width=True)

# Text Generation Section
with tab2:
    st.header("Text Generation")
    keyword = st.text_input("Enter keyword:")
    if st.button("Generate Text"):
        # Text Generation Pipeline
        generator = pipeline('text-generation', model='gpt2')
        generated_text = generator(keyword, max_length=100, num_return_sequences=1)[0]['generated_text']
        st.write(generated_text)


