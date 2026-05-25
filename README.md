# FactGuard AI 🔍

An AI-powered **Fact-Checking Web App** that automatically verifies claims in PDF documents using Google Gemini.

## 🚀 Live Demo
[Click here to try the app](https://your-app.streamlit.app) ← update after deploy

## ✨ Features
- 📄 Upload any PDF document
- 🤖 AI extracts all verifiable claims (stats, dates, figures)
- 🌐 Cross-references claims against Gemini's knowledge
- 🚨 Flags claims as **Verified**, **Inaccurate**, or **False**
- 📊 Summary dashboard with claim breakdown

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **AI Engine:** Google Gemini 1.5 Flash
- **PDF Parsing:** PyMuPDF (fitz)
- **Deployment:** Streamlit Cloud

## 📦 Installation (Local)

```bash
git clone https://github.com/yourusername/factguard-ai
cd factguard-ai
pip install -r requirements.txt
streamlit run app.py
```

## 🔑 Setup
1. Get a free Gemini API key from [aistudio.google.com](https://aistudio.google.com)
2. Paste it in the app's API key field
3. Upload a PDF and click **Analyze**

## 📋 How It Works
1. **Extract** — PyMuPDF parses the PDF and extracts all text
2. **Analyze** — Gemini AI identifies specific, verifiable claims
3. **Verify** — Each claim is checked against known facts
4. **Report** — Results flagged as Verified ✅, Inaccurate ⚠️, or False 🚨

## 🎯 Built For
Cog Culture — Product Management Trainee Assessment
