import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Dashboard - FactGuard AI",
    page_icon="📊",
    layout="wide"
)

st.markdown("# 📊 Analytics Dashboard")
st.markdown("---")

if not st.session_state.get('analysis_history'):
    st.info("📭 No analyses yet. Go to the Home page and analyze your first document!")
else:
    # Statistics
    total_docs = len(st.session_state.analysis_history)
    total_claims = sum(len(analysis['claims']) for analysis in st.session_state.analysis_history)
    verified_count = sum(sum(1 for c in analysis['claims'] if c.get('status') == 'Verified') for analysis in st.session_state.analysis_history)
    inaccurate_count = sum(sum(1 for c in analysis['claims'] if c.get('status') == 'Inaccurate') for analysis in st.session_state.analysis_history)
    false_count = sum(sum(1 for c in analysis['claims'] if c.get('status') == 'False') for analysis in st.session_state.analysis_history)
    
    # Metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("📄 Documents", total_docs)
    with col2:
        st.metric("📝 Total Claims", total_claims)
    with col3:
        st.metric("✅ Verified", verified_count)
    with col4:
        st.metric("⚠️ Inaccurate", inaccurate_count)
    with col5:
        st.metric("❌ False", false_count)
    
    # Charts
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Claim Status Distribution")
        chart_data = pd.DataFrame({
            'Status': ['Verified', 'Inaccurate', 'False'],
            'Count': [verified_count, inaccurate_count, false_count]
        })
        st.bar_chart(chart_data.set_index('Status'))
    
    with col2:
        st.markdown("### Recent Activity")
        recent = st.session_state.analysis_history[-5:]
        for analysis in reversed(recent):
            st.markdown(f"""
            <div style="background: #f0f0f0; padding: 0.75rem; border-radius: 8px; margin-bottom: 0.5rem;">
                <strong>{analysis['filename']}</strong><br>
                <small>{analysis['timestamp']} | {len(analysis['claims'])} claims</small>
            </div>
            """, unsafe_allow_html=True)
    
    # History table
    st.markdown("---")
    st.markdown("### 📜 Full History")
    
    history_data = []
    for analysis in st.session_state.analysis_history:
        history_data.append({
            "Document": analysis['filename'],
            "Timestamp": analysis['timestamp'],
            "Total Claims": len(analysis['claims']),
            "Verified": sum(1 for c in analysis['claims'] if c.get('status') == 'Verified'),
            "Inaccurate": sum(1 for c in analysis['claims'] if c.get('status') == 'Inaccurate'),
            "False": sum(1 for c in analysis['claims'] if c.get('status') == 'False')
        })
    
    df = pd.DataFrame(history_data)
    st.dataframe(df, use_container_width=True)
