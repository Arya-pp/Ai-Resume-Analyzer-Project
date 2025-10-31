import streamlit as st
from utils.helpers import load_css

def show_home():
    load_css("components/home/home_section.css")
    st.markdown('<div id="home"></div>', unsafe_allow_html=True)
    st.title("AI Resume Analyzer")
    st.markdown("""
        <div style='text-align:center;padding:0.5rem 1rem 2.5rem 1rem;'>
            <p style='font-size:1.2rem;color:rgba(230,233,239,0.8);margin-bottom:1rem;'>
                🚀 Transform your resume review process with AI-powered insights
            </p>
            <div class='divider' style='width:200px;margin:0 auto;'></div>
        </div>
    """, unsafe_allow_html=True)
