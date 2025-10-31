import streamlit as st
from utils.helpers import load_css

def show_about():
    load_css("components/about/about_section.css")
    st.markdown('<div id="about"></div>', unsafe_allow_html=True)
    st.markdown("<div class='divider' style='margin: 4rem 0 2rem 0;'></div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class='about-header'>
            <h2>About AI Resume Analyzer</h2>
        </div>
    """, unsafe_allow_html=True)
    
    col_row1_1, col_row1_2 = st.columns(2, gap="large")
    
    with col_row1_1:
        st.markdown("""
            <div class='result-card' style='height: 240px; padding: 2rem;'>
                <h3 style='display:flex;align-items:center;gap:0.5rem;margin-top:0;margin-bottom:1rem;font-size:1.2rem;'>
                    <span>🤖</span>
                    <span class='text-gradient'>AI-Powered Analysis</span>
                </h3>
                <p>
                    This application leverages <strong>Google's Gemini 1.5 Flash</strong>, a cutting-edge AI model, 
                    to provide comprehensive resume analysis. Our system evaluates your resume across multiple 
                    dimensions including hard skills, soft skills, action verbs, and ATS compatibility.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col_row1_2:
        st.markdown("""
            <div class='result-card' style='height: 240px; padding: 2rem;'>
                <h3 style='display:flex;align-items:center;gap:0.5rem;margin-top:0;margin-bottom:1rem;font-size:1.2rem;'>
                    <span>🎯</span>
                    <span class='text-gradient'>Key Features</span>
                </h3>
                <ul>
                    <li><strong>ATS Score:</strong> Resume compatibility evaluation</li>
                    <li><strong>Match %:</strong> Job description alignment</li>
                    <li><strong>Skills Detection:</strong> Auto-identify hard & soft skills</li>
                    <li><strong>Action Verbs:</strong> Powerful verb suggestions</li>
                    <li><strong>Instant Feedback:</strong> Real-time improvements</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    col_row2_1, col_row2_2 = st.columns(2, gap="large")
    
    with col_row2_1:
        st.markdown("""
            <div class='result-card' style='margin-top: 1.5rem; height: 280px; padding: 2rem;'>
                <h3 style='display:flex;align-items:center;gap:0.5rem;margin-top:0;margin-bottom:1rem;font-size:1.2rem;'>
                    <span>🚀</span>
                    <span class='text-gradient'>How It Works</span>
                </h3>
                <ol>
                    <li><strong>Upload:</strong> Drag and drop your resume in PDF format</li>
                    <li><strong>Job Description:</strong> Paste job description for targeted analysis</li>
                    <li><strong>Analyze:</strong> AI processes your resume using advanced NLP</li>
                    <li><strong>Review:</strong> Get detailed insights with scores and recommendations</li>
                    <li><strong>Improve:</strong> Apply suggestions to optimize your resume</li>
                </ol>
            </div>
        """, unsafe_allow_html=True)
    
    with col_row2_2:
        st.markdown("""
            <div class='result-card' style='margin-top: 1.5rem; height: 280px; padding: 2rem;'>
                <h3 style='display:flex;align-items:center;gap:0.5rem;margin-top:0;margin-bottom:1rem;font-size:1.2rem;'>
                    <span>💡</span>
                    <span class='text-gradient'>Technology Stack</span>
                </h3>
                <div>
                    <p><strong>Frontend:</strong> Streamlit with custom CSS for modern UI</p>
                    <p><strong>AI Model:</strong> Google Gemini 1.5 Flash API</p>
                    <p><strong>PDF Processing:</strong> PyPDF2 for text extraction</p>
                    <p><strong>Design:</strong> Glassmorphism with advanced animations</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class='built-with'>
            <p>Built with ❤️ using Python, modern web technologies, and AI innovation.</p>
        </div>
    """, unsafe_allow_html=True)
