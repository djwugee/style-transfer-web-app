import streamlit as st
from data import *
from input import image_input, webcam_input

st.title("Neural Style Transfer")
st.sidebar.title('Navigation')

method = st.sidebar.radio('Go To ->', options=['Webcam', 'Image', 'Video']) # Add 'Video' option

st.sidebar.header('Options')
style_model_name = st.sidebar.selectbox("Choose the style model: ", style_models_name)

if method == 'Image':
    image_input(style_model_name)
elif method == 'Webcam':
    webcam_input(style_model_name)
else: # Video input functionality
    st.header("Video Input")
    video_file = st.sidebar.file_uploader("Choose a Video File", type=["mp4", "webm"])
    if video_file is not None:
        st.video(video_file)
    else:
        st.warning("Upload a Video File")
