import streamlit as st
from utils.helpers import load_css

def show_footer():
    load_css("components/layout/footer.css")
    st.markdown("""
        <div class='footer-container'>
            <p>© 2025 AI Resume Analyzer • Powered by Google Gemini AI</p>
        </div>
    """, unsafe_allow_html=True)
