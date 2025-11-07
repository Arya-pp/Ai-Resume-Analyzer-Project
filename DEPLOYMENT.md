# 🚀 Deployment Guide for AI Resume Analyzer

## Quick Deploy Options

### 1️⃣ Streamlit Community Cloud (Recommended - FREE)

**Easiest and fastest deployment method!**

#### Steps:

1. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
2. Sign in with your GitHub account
3. Click "New app"
4. Select:
   - Repository: `Arya-pp/Ai-Resume-Analyzer-Project`
   - Branch: `main`
   - Main file path: `ai_resume_analyzer/app.py`
5. Click "Advanced settings"
6. Add Secret:
   ```
   GEMINI_API_KEY = "your_actual_api_key_here"
   ```
7. Click "Deploy"!

Your app will be live at: `https://your-app-name.streamlit.app`

**Benefits:**

- ✅ Completely FREE
- ✅ Auto-deploys on every git push
- ✅ Built-in HTTPS
- ✅ Easy secrets management
- ✅ No server configuration needed

---

### 2️⃣ Render (FREE Tier Available)

#### Steps:

1. Go to [render.com](https://render.com) and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repo
4. Configure:
   - **Name:** ai-resume-analyzer
   - **Build Command:** `pip install -r ai_resume_analyzer/requirements.txt`
   - **Start Command:** `streamlit run ai_resume_analyzer/app.py --server.port $PORT --server.address 0.0.0.0`
5. Add Environment Variable:
   - Key: `GEMINI_API_KEY`
   - Value: Your API key
6. Click "Create Web Service"

---

### 3️⃣ Heroku

#### Prerequisites:

- Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli

#### Steps:

```bash
# Login to Heroku
heroku login

# Create new app
heroku create your-app-name

# Set environment variable
heroku config:set GEMINI_API_KEY="your_api_key_here"

# Deploy
git push heroku main
```

Your app will be live at: `https://your-app-name.herokuapp.com`

---

## 📝 Pre-Deployment Checklist

Before deploying, make sure:

- [x] All code is pushed to GitHub
- [x] `requirements.txt` is up to date
- [x] `.env` file is in `.gitignore` (don't commit API keys!)
- [x] API key is ready to add as environment variable
- [x] All components are working locally

---

## 🔐 Security Notes

**NEVER commit your API key to GitHub!**

Always use environment variables:

- Streamlit Cloud: Use "Secrets" in app settings
- Render/Heroku: Use environment variable settings
- Keep `.env` in `.gitignore`

---

## 🐛 Troubleshooting

### App won't start:

- Check logs in your deployment platform
- Verify `GEMINI_API_KEY` is set correctly
- Ensure `requirements.txt` has all dependencies

### Import errors:

- Add missing packages to `requirements.txt`
- Redeploy

### Slow performance:

- Gemini API response time is ~10-15 seconds (normal)
- Consider caching results for frequently analyzed resumes

---

## 📊 Post-Deployment

After deployment, test:

1. Upload a sample resume
2. Verify AI analysis works
3. Check all UI components display correctly
4. Test on mobile devices

---

**Need help?** Check the deployment platform's documentation or create an issue on GitHub.
