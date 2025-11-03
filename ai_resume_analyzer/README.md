# 🎯 AI Resume Analyzer

An **AI-powered resume analysis tool** built using **Streamlit** and **Google Gemini API**.  
This application helps users evaluate and enhance their resumes with intelligent insights, skill detection, and ATS (Applicant Tracking System) compatibility checks — all presented through a modern, responsive interface.

---

## � About the Project

The **AI Resume Analyzer** automates the resume review process by leveraging Google Gemini's advanced natural language capabilities.  
It reads and analyzes your uploaded resume (PDF format) to provide:

- � **Match Percentage:** Measures how closely your resume aligns with a job description
- 🤖 **ATS Score:** Evaluates your resume's readiness for Applicant Tracking Systems
- � **Strengths & Skills:** Detects key hard and soft skills
- ✨ **Action Verbs:** Suggests impactful verbs to strengthen your phrasing
- 💡 **Suggestions:** Offers professional improvement tips and formatting recommendations

The app is lightweight, fast, and visually appealing — designed to make AI-driven resume enhancement accessible to everyone.

---

## 🛠️ Tech Stack

- **Framework:** Streamlit (Python)
- **AI Model:** Google Gemini 2.5 Flash API
- **Libraries:** PyPDF2, python-dotenv
- **Styling:** Custom CSS with modern animations
- **Architecture:** Modular components for easy scalability

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Arya-pp/Ai-Resume-Analyzer-Project.git
cd Ai-Resume-Analyzer-Project/ai_resume_analyzer
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # For Windows
source venv/bin/activate   # For macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your Gemini API Key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY="your_api_key_here"
```

💡 Get your API key from: [Google AI Studio](https://makersuite.google.com/app/apikey)

### 5. Run the Application

```bash
streamlit run app.py
```

Then open your browser and go to 👉 **http://localhost:8501**

---

## 🧩 Key Highlights

✅ **Drag-and-drop resume upload**  
✅ **AI-powered resume scoring and insights**  
✅ **Smart recommendations for improvement**  
✅ **Smooth animations and elegant design**  
✅ **Built for accuracy, speed, and ease of use**

---

## 📝 Usage

1. **Launch the application**
2. **Upload your resume** in PDF format using drag-and-drop
3. **Wait for AI analysis** (typically 10-15 seconds)
4. **Review your comprehensive report** including:
   - Overall resume score
   - ATS compatibility rating
   - Detailed strengths and weaknesses
   - Professional improvement suggestiosns
   - Action verbs and skill recommendations

---

⭐ **If you find this project helpful, please consider giving it a star!**
