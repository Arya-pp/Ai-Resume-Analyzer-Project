import streamlit as st
from utils.helpers import load_css

def show_pro_tips():
    load_css("components/pro_tips/pro_tips_box.css")
    st.markdown("""
        <div class="summary-box">
            <h3 style='display:flex;align-items:center;gap:0.5rem;margin-top:0;'>
                <span>⚡</span>
                <span class='text-gradient'>Pro Tips</span>
            </h3>
            <div style='margin-top:1rem;display:flex;flex-direction:column;gap:0.6rem;'>
                <div class='text-muted'>💡 Ensure your resume is in PDF format</div>
                <div class='text-muted'>💡 Include relevant skills & experience</div>
                <div class='text-muted'>💡 Keep formatting consistent</div>
                <div class='text-muted'>💡 Highlight measurable achievements</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
