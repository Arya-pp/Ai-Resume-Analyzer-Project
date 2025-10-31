# 🎯 AI Resume Analyzer

A full-stack AI-powered Streamlit application that analyzes resumes using Google's Gemini API to provide comprehensive insights, scoring, and professional feedback. This project features a modular architecture designed for scalability and maintainability.

---

## 🚀 Features

✨ **Smart Resume Upload** - Upload resumes in PDF format with drag-and-drop support  
🤖 **AI-Powered Analysis** - Leverage Google Gemini AI for in-depth resume evaluation  
📊 **Comprehensive Scoring** - Get detailed scores across multiple resume criteria  
🎯 **ATS Optimization** - Check and improve your resume's ATS (Applicant Tracking System) compatibility  
💡 **Professional Tips** - Receive actionable recommendations to enhance your resume  
🎨 **Modern UI/UX** - Clean, responsive interface with smooth animations  
📦 **Modular Architecture** - Well-structured codebase for easy maintenance and scaling

---

## �️ Tech Stack

**Frontend:**
- Streamlit (Python web framework)
- Custom CSS3 (with animations and responsive design)
- Component-based architecture

**Backend:**
- Python 3.x
- Google Generative AI (Gemini API)
- PyPDF2 (PDF text extraction)
- python-dotenv (environment management)

**Architecture:**
- Modular component structure
- Utility-based helper functions
- Scoped CSS styling per component

---

---

## 📂 Project Structure

```
ai_resume_analyzer/
├── app.py                      # Main application entry point
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (API keys)
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
│
├── components/                 # UI Components (modular)
│   ├── __init__.py
│   ├── about/                  # About section component
│   │   ├── about_section.py
│   │   └── about_section.css
│   ├── analyzer/               # Core analysis UI component
│   │   ├── analyzer_ui.py
│   │   └── analyzer_ui.css
│   ├── home/                   # Home/upload section
│   │   ├── home_section.py
│   │   └── home_section.css
│   ├── layout/                 # Layout components (Navbar, Footer)
│   │   ├── navbar.py
│   │   ├── navbar.css
│   │   ├── footer.py
│   │   └── footer.css
│   └── pro_tips/               # Pro tips component
│       ├── pro_tips_box.py
│       └── pro_tips_box.css
│
├── utils/                      # Utility functions & backend logic
│   ├── __init__.py
│   ├── ai_analysis.py          # Gemini API integration
│   ├── pdf_extractor.py        # PDF text extraction
│   └── helpers.py              # Helper functions
│
└── static/                     # Static assets
    ├── base.css                # Global styles & animations
    └── assets/                 # Images and other assets
```

---

---

## ⚙️ Setup and Installation

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Arya-pp/Ai-Resume-Analyzer-Project.git
   cd Ai-Resume-Analyzer-Project/ai_resume_analyzer
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY="your_api_key_here"
   ```

5. **Run the application:**
   ```bash
   streamlit run app.py
   ```

6. **Open in browser:**
   
   The app will automatically open at `http://localhost:8501`

---

## 🎨 Features Showcase

- **Circular Score Display**: Visual representation of resume scores
- **Interactive File Upload**: Drag-and-drop PDF upload with real-time feedback
- **Detailed Analysis**: Category-wise breakdown of resume strengths and weaknesses
- **Responsive Design**: Works seamlessly on desktop and mobile devices

---

## 📝 Usage

1. Launch the application
2. Upload your resume in PDF format
3. Wait for the AI analysis (typically 10-15 seconds)
4. Review your comprehensive resume report including:
   - Overall score
   - ATS compatibility rating
   - Detailed feedback and suggestions
   - Professional tips for improvement

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Arya**
- GitHub: [@Arya-pp](https://github.com/Arya-pp)

---

## 🙏 Acknowledgments

- Google Gemini AI for providing the powerful AI analysis capabilities
- Streamlit for the amazing web framework
- All contributors and users of this project

---

⭐ **If you find this project helpful, please consider giving it a star!**
