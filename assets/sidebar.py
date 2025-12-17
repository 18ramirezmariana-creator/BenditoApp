import streamlit as st
from PIL import Image

def sidebar_style():

    sidebar_bg = """
    <style>
        /* Target all sidebar titles with class starting with e1dbuyne */
        [class^="st-emotion-cache"][class*="e1dbuyne"] {
            color: #f2470f; same color as bg not to be seen
            font-weight: bold;
            font-size: 20px;
        }
        /* HACER LA IMAGEN CIRCULAR */
        [data-testid="stSidebar"] [data-testid="stImage"] img {
            border-radius: 50%; /* Crea el efecto circular */
            border: 3px solid #ee4b11; /* Un borde azul para resaltar el logo */
            object-fit: cover;
            aspect-ratio: 1 / 1; /* Fuerza que sea un círculo perfecto */
        }
        </style>
    """

    logo = Image.open("assets/logo2Bendito.png")
    st.markdown(sidebar_bg, unsafe_allow_html=True)
    with st.sidebar:
        st.image(logo)