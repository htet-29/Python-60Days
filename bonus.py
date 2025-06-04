import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
   camera_image = st.camera_input("Camera")


with st.expander("Upload Image"):
    file_image = st.file_uploader("Upload Image")


if camera_image:
    img = Image.open(camera_image)
    gray_convert_img = img.convert("L")
    st.image(gray_convert_img)


if file_image:
    f_img = Image.open(file_image)
    f_gray_img = f_img.convert("L")
    st.image(f_gray_img)