import streamlit as st
import os
from pathlib import Path

def load_css(path):
    try:
        # Get the directory where the script is running from
        base_dir = Path(__file__).parent.parent
        css_path = base_dir / path
        
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"⚠️ CSS file not found at {path}.")

def activate_drag_and_drop_style():
    st.markdown("""
    <script>
        const fileUploader = parent.document.querySelector('[data-testid="stFileUploader"]');
        if (fileUploader) {
            ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
                fileUploader.addEventListener(eventName, preventDefaults, false);
            });
            
            function preventDefaults(e) {
                e.preventDefault();
                e.stopPropagation();
            }
            
            ['dragenter', 'dragover'].forEach(eventName => {
                fileUploader.addEventListener(eventName, () => {
                    const uploadBox = parent.document.querySelector('.upload-box');
                    if (uploadBox) uploadBox.classList.add('drag-active');
                }, false);
            });
            
            ['dragleave', 'drop'].forEach(eventName => {
                fileUploader.addEventListener(eventName, () => {
                    const uploadBox = parent.document.querySelector('.upload-box');
                    if (uploadBox) uploadBox.classList.remove('drag-active');
                }, false);
            });
        }
    </script>
    """, unsafe_allow_html=True)
