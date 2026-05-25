# FactGuard AI 🔍

An AI-powered **Fact-Checking Web App** that automatically verifies claims in PDF documents using Groq's Llama 3.3 70B model.

## 🚀 Live Demo
https://factguard-ai-2etssbphxqcr2ppfxjitnd.streamlit.app/

## ✨ Features
- 📄 Upload any PDF document
- 🤖 AI extracts all verifiable claims (stats, dates, figures)
- 🌐 Cross-references claims against Llama 3.3's knowledge base
- 🚨 Flags claims as **Verified** ✅, **Inaccurate** ⚠️, or **False** ❌
- 📊 Summary dashboard with claim breakdown
- 📜 History tracking of all analyses
- 📥 Export reports as JSON

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **AI Engine:** Groq (Llama 3.3 70B)
- **PDF Parsing:** PyMuPDF (fitz)
- **Deployment:** Streamlit Cloud
- **Language:** Python

## 📦 Installation (Local)

```bash
git clone https://github.com/Yash8439/factguard-ai
cd factguard-ai
pip install -r requirements.txt
streamlit run app.py
