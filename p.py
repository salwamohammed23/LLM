import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
import requests
from PIL import Image
import io

API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
HEADERS = {"Authorization": f"Bearer {'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'}"}

# Replace the empty strings with your actual OpenAI API key
open_ai_key = "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"
chat = ChatOpenAI(openai_api_key=open_ai_key)

st.header("project_2")
Keyword_Selection = st.text_input("keyword:")

if st.button("Generate"):
    # Step 1: Generate Blog Content
    messages_1 = [
        SystemMessage(content="You are an assistant blogger. Create the blog post content. Choose a language for the blog post content that matches the language of the Keyword Selection."),
        HumanMessage(content=Keyword_Selection),
    ]

    generated_blog_content = chat.invoke(messages_1)
    generated_blog = generated_blog_content.content

    # Step 2: Generate Image Descriptions
    messages_2 = [
        SystemMessage(content="You are a blogger assistant who extracts short, suitable, single-image descriptions using the English language."),
        HumanMessage(content=generated_blog),
    ]

    image_descriptions_content = chat.invoke(messages_2)
    key_image = image_descriptions_content.content

    # Step 3: Send Image Descriptions to the Computer Vision Model
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": key_image})
    image_bytes = response.content
    image = Image.open(io.BytesIO(image_bytes))

    # Display Generated Blog Content and Inferred Image Side by Side
    col1, col2 = st.columns(2)
    col1.image(image, caption="Inferred Image", use_column_width=True)
    col2.write(generated_blog)
    
