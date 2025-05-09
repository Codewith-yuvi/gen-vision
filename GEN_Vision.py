from dotenv import load_dotenv
load_dotenv()
#loading all the envirement variables

import streamlit as st 
import os 
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-2.0-flash-exp")
def get_gemini_response(input,image):
    if input !=" ":
        response=model.generate_content([input,image])
    else:
         response=model.generate_content(input,image)
    return response.text
st.set_page_config(page_title="vision image demo")

st.header("GEN Vision")
st.subheader("See the batter future with GEN-vision")
input= st.text_input("Input prompt: ",key="input")

uploaded_file = st.file_uploader("choose an image . . . . ", type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="uploaded image. ",use_column_width=True)

submit= st.button("Submit")

if submit:

    response=get_gemini_response(input,image)
    st.header("The Response is ")
    st.write(response)
