# AI Resume Analyzer

An AI-powered Streamlit application that analyzes resumes using Google's Gemini API to provide insights, scoring, and feedback. This project is structured in a modular way to separate concerns and improve maintainability.

## 🚀 Features

- **Resume Upload**: Upload your resume in PDF format.
- **AI-Powered Analysis**: Get an in-depth analysis of your resume, including a score and detailed feedback.
- **ATS Friendliness Check**: See how well your resume might perform with Applicant Tracking Systems.
- **Professional Tips**: Receive actionable tips to improve your resume.

## 📂 Project Structure

The project is organized into a modular structure:

- `app.py`: The main entry point for the Streamlit application.
- `requirements.txt`: A list of all the Python packages required to run the project.
- `.env`: Configuration file to store your Gemini API key.
- `static/`: Contains all static files.
  - `base.css`: Global CSS styles, variables, and animations.
  - `assets/`: For images and other static assets.
- `components/`: Contains all the UI components of the application. Each component is a self-contained module with its own Python and CSS file.
  - `about/`: The "About" section.
  - `analyzer/`: The core resume analysis UI.
  - `home/`: The main home/upload section.
  - `layout/`: The Navbar and Footer.
  - `pro_tips/`: The "Pro Tips" section.
- `utils/`: Contains helper functions and backend logic.
  - `ai_analysis.py`: Handles the interaction with the Gemini API.
  - `pdf_extractor.py`: Extracts text from uploaded PDF files.
  - `helpers.py`: Utility functions used across the app.

## ⚙️ Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone <your-repo-url>
    cd ai-resume-analyzer
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API Key:**

    - Create a file named `.env` in the root directory.
    - Add your Google Gemini API key to it like this:
      ```
      GEMINI_API_KEY="YOUR_API_KEY"
      ```

5.  **Run the application:**
    ```bash
    streamlit run app.py
    ```
