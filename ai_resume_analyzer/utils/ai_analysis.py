import streamlit as st
import json
import google.generativeai as genai

def analyze_with_gemini(text, job_description=None):
    """Analyze resume using Gemini AI."""
    try:
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        prompt = f"""
        You are a professional resume analysis expert.

        Analyze the following resume text and return ONLY valid JSON (no markdown, no code fences).
        Include this structure:

        {{
          "strengths": ["3-5 key strengths"],
          "hard_skills": ["5-8 hard skills"],
          "soft_skills": ["5-8 soft skills"],
          "action_verbs": ["10 action verbs"],
          "weaknesses": ["2-3 improvement areas"],
          "suggestions": "1 short improvement paragraph",
          "match_summary": "2-3 line summary",
          "match_percentage": 0,
          "missing_skills": ["skills missing for job"],
          "ats_score": 0
        }}

        Resume:
        {text}
        """

        if job_description:
            prompt += f"""

            Job Description:
            {job_description}

            Update match_percentage, missing_skills, and ats_score (0–100).
            """

        response = model.generate_content(prompt)
        response_text = (response.text or "").strip()
        cleaned = (
            response_text.replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(cleaned)
    except Exception as e:
        st.error(f"Error during Gemini analysis: {e}")
        return {"error": str(e)}
