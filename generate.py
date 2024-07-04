from openai import OpenAI
import streamlit as st

from PIL import Image
import requests
from io import BytesIO


client= OpenAI()

st.title("Generate Image")

input = st.text_input("Enter your prompt")

if input:
    # image generation
    res= client.images.generate(
        model="dall-e-3",
        prompt="a white horse running on white blue beach",
        size="612*612",
        quality="standard", 
        n=1
    )

    imageURL= res[0].url

    if imageURL:
        res = requests.get(imageURL)
        img = Image(BytesIO( res.content))
        st.image(img, caption="Image Generated")



