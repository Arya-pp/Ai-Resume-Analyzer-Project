import streamlit as st
import io
from PyPDF2 import PdfReader

def extract_text_from_pdf(file):
    """Extract text from uploaded PDF file."""
    try:
        pdf_bytes = io.BytesIO(file.getvalue())
        reader = PdfReader(pdf_bytes)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
        return text.strip()
    except Exception as e:
        st.error(f"Error extracting text: {e}")
        return None
