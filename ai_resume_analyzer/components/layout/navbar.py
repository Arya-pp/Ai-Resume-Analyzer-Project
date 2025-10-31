import streamlit as st
from utils.helpers import load_css

def show_navbar():
    load_css("components/layout/navbar.css")
    st.markdown("""
        <div class="top-nav">
            <a href="#home" onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return false;">Home</a>
            <a href="#analyze" onclick="document.querySelector('.stButton button')?.scrollIntoView({behavior: 'smooth'}); return false;">Analyze</a>
            <a href="#about" onclick="window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'}); return false;">About</a>
        </div>
    """, unsafe_allow_html=True)
