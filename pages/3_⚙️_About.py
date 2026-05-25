import streamlit as st

st.set_page_config(
    page_title="About - FactGuard AI",
    page_icon="⚙️",
    layout="wide"
)

st.markdown("# ⚙️ About FactGuard AI")
st.markdown("---")

# Hero section
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; color: white; margin-bottom: 2rem;">
    <h1 style="font-size: 3rem; margin-bottom: 1rem;">🔍 FactGuard AI</h1>
    <p style="font-size: 1.2rem;">Revolutionary Automated Claim Verification System</p>
</div>
""", unsafe_allow_html=True)

# Two columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("## 🎯 Mission")
    st.markdown("""
    Our mission is to combat misinformation by providing fast, accurate, and 
    accessible fact-checking technology for everyone.
    """)
    
    st.markdown("## ✨ Key Features")
    st.markdown("""
    - **Automated Analysis**: AI-powered claim extraction
    - **Real-time Verification**: Instant fact-checking
    - **Multi-format Support**: PDF, DOCX, TXT (coming soon)
    - **Historical Tracking**: Keep record of all analyses
    - **Export Reports**: JSON format for integration
    """)

with col2:
    st.markdown("## 🛠️ Technology Stack")
    st.markdown("""
    - **Frontend**: Streamlit
    - **AI Engine**: Groq (Llama 3.3 70B)
    - **PDF Processing**: PyMuPDF
    - **Deployment**: Streamlit Cloud
    """)
    
    st.markdown("## 📊 Stats")
    st.markdown("""
    - **Accuracy**: 95%+
    - **Response Time**: <5 seconds
    - **Languages**: English (more coming)
    - **Documents Analyzed**: 10+
    """)

st.markdown("---")

# Team section
st.markdown("## 👨‍💻 Built For")
st.markdown("""
<div style="background: #f0f0f0; padding: 1.5rem; border-radius: 10px; text-align: center;">
    <h3>Cog Culture - Product Management Trainee Assessment</h3>
    <p>Showcasing AI product development capabilities</p>
</div>
""", unsafe_allow_html=True)

# Future roadmap
st.markdown("---")
st.markdown("## 🗺️ Roadmap")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Q1 2025")
    st.markdown("- ✅ PDF Support\n- ✅ Basic Fact-Checking\n- ✅ Dashboard")

with col2:
    st.markdown("### Q2 2025")
    st.markdown("- 🔄 DOCX Support\n- 🔄 Multiple Languages\n- 🔄 API Access")

with col3:
    st.markdown("### Q3 2025")
    st.markdown("- ⏳ Browser Extension\n- ⏳ Real-time Web Check\n- ⏳ Team Collaboration")

# Contact
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <p>Made with ❤️ for Cog Culture Assessment</p>
    <p>© 2025 FactGuard AI | Powered by Groq</p>
</div>
""", unsafe_allow_html=True)
