import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snb
import utils as ut

st.set_page_config(page_title="Beautiful Free Math", layout="wide")

# Create a container with custom styling
st.markdown(
    """
    <style>
    .title-container {
        background-color: #2E73A6;
        padding: 50px 0;
        text-align: center;
        color: white;
    }
    .title-container h1 {
        font-size: 50px;
        font-weight: bold;
        margin: 0;
    }
    .title-container p {
        font-size: 20px;
        margin-top: 10px;
    }
    .logo {
        display: block;
        margin: 20px auto;
        width: 150px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display logo and title
st.markdown("""
<div class="title-container">
    <img src="Logo.jpeg" class="logo">
    <h1>Beautiful Free Math</h1>
    <p>A Personalised and Customizable Toolkit exclusively for IIIT Vadodara Students</p>
</div>
""", unsafe_allow_html=True)

# Additional app content
st.button("Open Graphing Calculator")
st.markdown("### Explore all of our math tools!")