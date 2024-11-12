import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snb
import time
from PIL import Image

st.set_page_config(page_title="WAVELAB", layout="wide")
st.markdown("""
    <style>
        .animated-title {
            text-align: left;
            color: #DBE2EF;
            font-size: 40px;
            font-weight: bold;
            background-color:#3F72AF;
            transition: all 0.3s ease; /* Smooth transition for color and other properties */
        }

        .animated-title:hover {
            animation: fadeInOut 4s ease-in-out infinite;
        }

        @keyframes fadeInOut {
            0% { opacity: 0; transform: translateY(-20px); }
            50% { opacity: 1; transform: translateY(0); }
            100% { opacity: 0; transform: translateY(20px); }
        }
    </style>
    <h1 class="animated-title"> WAVELAB</h1>
""", unsafe_allow_html=True)

# Icons for different math tools (placeholders for the tool icons)
#col1, col2, col3= st.columns(3)
#col1.image("https://via.placeholder.com/64.png?text=Graphing", caption="Graphing", use_container_width=True)
#col2.image("https://via.placeholder.com/64.png?text=Scientific", caption="Scientific", use_container_width=True)
#col3.image("https://via.placeholder.com/64.png?text=Four+Function", caption="Four Function", use_container_width=True)
st.markdown(
    """
    <style>
    .button-container {
        display: flex;
        flex-direction:row;text-align: center;
        justify-content: space-between; 
        
        align-items:baseline;
    }
    .custom-button {
        text-align: center;
        border-radius: 15px;
        padding: 20px;
        color: white;
        font-size: 40px;
        text-decoration: none;
        width: 600px;
    }
    .probability { background-color: #DCCCEC; }
    .physics { background-color: #FFCBE1; }
    .linear-algebra { background-color: #D6E5BD;}
    </style>
    """,
    unsafe_allow_html=True
)
# Create a layout for the buttons  color: #DBE2EF 
st.markdown('<div class="button-container">', unsafe_allow_html=True)

st.markdown('<div class="custom-button probability" href="#">Probability </div>', unsafe_allow_html=True)
st.markdown('<div class="custom-button physics" href="#">Physics</div>', unsafe_allow_html=True)
st.markdown('<div class="custom-button linear-algebra" href="#">Statistics </div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)