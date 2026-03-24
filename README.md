# YouTube Summarizer 🎥

A simple Flask web app that uses **Google Gemini AI** to summarize YouTube videos instantly.

## What You Get 📊

**Input:** YouTube Video Link  
**Output:** AI-generated summary of the video

## Features ✨

- ✅ Enter any YouTube URL
- ✅ Get instant AI summary
- ✅ Add custom instructions (optional)
- ✅ Works in your browser

## How It Works 🔧

1. User enters YouTube link in the web form
2. Flask backend sends it to Gemini AI
3. Gemini analyzes the video
4. Summary appears in a new tab

## Setup (Easy Steps) 🚀

### 1. Get API Key
- Go to [Google Cloud Console](https://console.cloud.google.com/)
- APIs & Services → Credentials
- Click "Create Credentials" → "API Key"
- Copy your key

### 2. Enable API
- Search for "Generative Language API"
- Click "Enable"

### 3. Install & Run

```bash
# Navigate to project
cd youtube-summarizer

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Upgrade library (important!)
pip install --upgrade google-generativeai

# Update API key in app.py
# Replace: API_KEY = "REPLACE THIS WITH YOUR API KEY"

# Run the app
python app.py
```

### 4. Open in Browser
```
http://localhost:8080
```

## Files Included 📁

| File | Purpose |
|------|---------|
| `app.py` | Backend Flask application |
| `index.html` | Web form (in templates folder) |
| `requirements.txt` | Python packages needed |

## Commands to Remember 💻

```bash
cd youtube-summarizer                    # Go to project folder
python -m venv venv                      # Create virtual environment
source venv/bin/activate                 # Activate it
pip install -r requirements.txt          # Install packages
pip install --upgrade google-generativeai # Update Gemini library
python app.py                            # Run the app
```

## Test Example 🧪

**URL:** `https://youtu.be/xVVHZ_CJllg?si=47jDMT1abliM7EmX`  
**Model:** Gemini 2.5 Flash  
**Prompt:** (leave empty or add custom text)

**Result:** You'll get a detailed summary of the video!

## Models Available 🤖

- **gemini-2.5-flash** (Recommended - fastest & best)
- **gemini-2.0-flash** (Also good)

## If You Get Errors 🐛

| Error | Fix |
|-------|-----|
| "API not enabled" | Go to Google Cloud, enable Generative Language API |
| "Port 8080 in use" | Run: `fuser -k 8080/tcp` |
| "Invalid API key" | Check your API key in app.py |
| "Model not found" | Make sure you're using `gemini-2.5-flash` |

## Deploy to Cloud ☁️

```bash
gcloud run deploy youtube-summarizer \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

Get your live URL and share it with anyone!

## Tech Stack 🛠️

- **Flask** - Web framework
- **Google Gemini AI** - Summarization AI
- **HTML/CSS** - Frontend
- **Python** - Backend

## File Contents Quick Reference 📄

### app.py
- Handles web requests
- Connects to Gemini API
- Returns summaries

### index.html
- Simple form with 3 fields:
  1. YouTube link input
  2. Model selector (Gemini 2.5 Flash)
  3. Additional prompt (optional)
- Green "Summarize" button

### requirements.txt
```
Flask==2.3.3
requests==2.31.0
debugpy
google-generativeai==0.8.6
```

## Quick Start Video 📹

1. Open `index.html` (form loads)
2. Paste YouTube URL
3. Click "Summarize"
4. See AI summary in new tab!

## Troubleshooting Checklist ✅

- [ ] API key added in `app.py`
- [ ] Generative Language API enabled
- [ ] `requirements.txt` installed
- [ ] Virtual environment activated
- [ ] Using port 8080
- [ ] Flask running without errors

## Need Help? 💬

Common issues and solutions are in the error table above.

## License 📜

Free to use and modify.

---

**That's it! Start summarizing videos! 🚀**
