import streamlit as st
from utils.helpers import load_css
from utils.pdf_extractor import extract_text_from_pdf
from utils.ai_analysis import analyze_with_gemini
from components.pro_tips.pro_tips_box import show_pro_tips

def show_analyzer(api_key):
    load_css("components/analyzer/analyzer_ui.css")

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown("""
            <div class="upload-box">
                <div style='font-size:3.5rem;margin-bottom:1rem;'>📄</div>
                <div style='color:rgba(230,233,239,0.9);font-size:1.2rem;font-weight:500;margin-bottom:0.8rem;'>
                    Drop your resume here
                </div>
                <div style='color:rgba(230,233,239,0.6);font-size:0.9rem;margin-bottom:1.5rem;'>
                    PDF format • Max 200MB
                </div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader("Drag and drop file here or click Browse", type=["pdf"], label_visibility="collapsed")
        
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
            <div style='margin-top:2rem;'>
                <h3 style='display:flex;align-items:center;gap:0.5rem;'>
                    <span>📋</span>
                    <span class='text-gradient'>Job Description</span>
                </h3>
            </div>
        """, unsafe_allow_html=True)

        job_description = st.text_area(
            "Job Description",
            height=150,
            placeholder="Paste the job description here...",
            label_visibility="collapsed"
        )

    with col2:
        show_pro_tips()

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown('<div id="analyze"></div>', unsafe_allow_html=True)
    colA, colB, colC = st.columns([1, 2, 1])
    with colB:
        analyze_clicked = st.button("🔍 Analyze Resume", disabled=not uploaded_file or not api_key)

    if analyze_clicked and uploaded_file:
        with st.spinner("Analyzing resume... Please wait ⏳"):
            resume_text = extract_text_from_pdf(uploaded_file)
            if resume_text:
                analysis = analyze_with_gemini(resume_text, job_description)
                
                if "error" in analysis:
                    st.error(analysis["error"])
                    return

                st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
                st.markdown("<h2 class='analysis-header'>📊 Analysis Results</h2>", unsafe_allow_html=True)

                # --- Score Display ---
                st.markdown(f"""
                    <div class="score-container">
                        <div class="score-circle match">
                            <div class="score-icon">🎯</div>
                            <div class="score-value">{analysis.get('match_percentage', 0)}%</div>
                            <div class="score-label">Match %</div>
                        </div>
                        <div class="score-circle ats">
                            <div class="score-icon">🤖</div>
                            <div class="score-value">{analysis.get('ats_score', 0)}%</div>
                            <div class="score-label">ATS Score</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

                # --- Results Cards ---
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.markdown("<div class='result-card success-card'><h3>💪 Strengths</h3>", unsafe_allow_html=True)
                    for s in analysis.get("strengths", []):
                        st.markdown(f"<div>• {s}</div>", unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)

                with c2:
                    st.markdown("<div class='result-card info-card'><h3>🎯 Hard Skills</h3>", unsafe_allow_html=True)
                    for s in analysis.get("hard_skills", []):
                        st.markdown(f"<div>• {s}</div>", unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)

                with c3:
                    st.markdown("<div class='result-card warning-card'><h3>🤝 Soft Skills</h3>", unsafe_allow_html=True)
                    for s in analysis.get("soft_skills", []):
                        st.markdown(f"<div>• {s}</div>", unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)

                st.markdown(f"""
                <div class="result-card verbs-card">
                    <h3 style='display:flex;align-items:center;gap:0.5rem;margin-top:0;'>
                        <span>✨</span>
                        <span>Action Verbs to Use</span>
                    </h3>
                    {", ".join(analysis.get("action_verbs", [])) or "No verbs detected."}
                </div>
                """, unsafe_allow_html=True)

                st.subheader("📝 Suggestions for Improvement")
                st.markdown(f"<div class='result-card'>{analysis.get('suggestions', '')}</div>", unsafe_allow_html=True)

                st.subheader("📋 Summary")
                st.markdown(f"<div class='result-card'>{analysis.get('match_summary', '')}</div>", unsafe_allow_html=True)

                if analysis.get("missing_skills"):
                    st.markdown("**🚫 Missing Skills:** " + ", ".join(analysis["missing_skills"]))
