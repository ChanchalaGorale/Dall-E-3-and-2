from openai import OpenAI

import streamlit as st

from PIL import Image
from io import BytesIO
import requests

client = openAI()

st.title("Try Image on Image")


main_image = st.file_uploader("Choose Main Image", type=["png", "jpg", "jpeg"])
mask_image = st.file_uploader("Choose Mask Image", type=["png", "jpg", "jpeg"])

prompt =  st.text_input("How you wanna add the mask image on main image and where ...")

if main_image:
    st.image(main_image, caption="Main Image.", use_column_width=True)


if mask_image:
    st.image(mask_image, caption="Mask Image.", use_column_width=True)


def image_processing(image):
    img = Image.open(image)
    img= img.resize((256, 256))
    byte_stream = BytesIO()
    image.save(byte_stream, format='PNG')
    byte_array = byte_stream.getvalue()

    return byte_array



if main_image and mask_image and prompt:

    try:
        res= client.images.edit(
            model="dall-e-2",
            image= image_processing(main_image ),
            mask= image_processing(mask_image),
            prompt=prompt,
            n=1,
            size="612*612"
        )

        image_url=res[0].url

        if image_url:
            res =  requests.get(image_url)

            img = Image(BytesIO(res.content))

            st.image(img, "Image edited")
    except:
        print("Error Occured!")








