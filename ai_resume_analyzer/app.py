import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

from utils.helpers import load_css, activate_drag_and_drop_style
from components.layout.navbar import show_navbar
from components.home.home_section import show_home
from components.analyzer.analyzer_ui import show_analyzer
from components.about.about_section import show_about
from components.layout.footer import show_footer

# ==============================
# 🔑 Load Environment Variables & Page Config
# ==============================
def setup_app():
    # Load .env file from the current directory
    from pathlib import Path
    env_path = Path(__file__).parent / '.env'
    
    # Debug: Check if .env file exists
    if not env_path.exists():
        st.error(f"⚠️ .env file not found at: {env_path}")
    
    load_dotenv(dotenv_path=env_path)
    api_key = os.getenv("GEMINI_API_KEY")
    
    # Debug: Print if key is loaded (for testing only)
    # st.write(f"Debug: API Key loaded: {api_key is not None}")

    st.set_page_config(
        page_title="AI Resume Analyzer",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    load_css("static/base.css")
    
    if not api_key:
        st.error("⚠️ Please add your GEMINI_API_KEY in the .env file.")
    else:
        genai.configure(api_key=api_key)
    
    return api_key

# ==============================
# 🌟 Main App UI
# ==============================
def main():
    api_key = setup_app()
    
    show_navbar()
    activate_drag_and_drop_style()
    
    st.markdown("<style>.block-container{padding-top:2rem !important;}</style>", unsafe_allow_html=True)

    show_home()
    show_analyzer(api_key)
    show_about()
    show_footer()

if __name__ == "__main__":
    main()
