import streamlit as st
import json
from datetime import datetime

st.set_page_config(
    page_title="History - FactGuard AI",
    page_icon="📜",
    layout="wide"
)

st.markdown("# 📜 Analysis History")
st.markdown("---")

if not st.session_state.get('analysis_history'):
    st.info("📭 No analysis history yet. Start by analyzing your first document!")
else:
    # Filter
    st.markdown("### 🔍 Filter History")
    col1, col2 = st.columns(2)
    with col1:
        search = st.text_input("Search by filename", placeholder="Enter filename...")
    with col2:
        sort_by = st.selectbox("Sort by", ["Newest First", "Oldest First", "Most Claims"])
    
    # Get history
    history = st.session_state.analysis_history.copy()
    
    # Apply search
    if search:
        history = [h for h in history if search.lower() in h['filename'].lower()]
    
    # Apply sorting
    if sort_by == "Newest First":
        history.reverse()
    elif sort_by == "Most Claims":
        history.sort(key=lambda x: len(x['claims']), reverse=True)
    
    # Display history items
    for idx, analysis in enumerate(history):
        with st.expander(f"📄 {analysis['filename']} - {analysis['timestamp']}"):
            col1, col2, col3, col4 = st.columns(4)
            total = len(analysis['claims'])
            verified = sum(1 for c in analysis['claims'] if c.get('status') == 'Verified')
            inaccurate = sum(1 for c in analysis['claims'] if c.get('status') == 'Inaccurate')
            false = sum(1 for c in analysis['claims'] if c.get('status') == 'False')
            
            with col1:
                st.metric("Total Claims", total)
            with col2:
                st.metric("Verified", verified)
            with col3:
                st.metric("Inaccurate", inaccurate)
            with col4:
                st.metric("False", false)
            
            st.markdown("#### Claim Details")
            for claim in analysis['claims']:
                status = claim.get('status', '')
                if status == 'Verified':
                    icon = "✅"
                elif status == 'Inaccurate':
                    icon = "⚠️"
                else:
                    icon = "❌"
                
                st.markdown(f"""
                <div style="background: #f9f9f9; padding: 0.75rem; border-radius: 8px; margin-bottom: 0.5rem;">
                    <strong>{icon} {status}</strong><br>
                    "{claim.get('claim', 'N/A')}"<br>
                    <small style="color: #666;">→ {claim.get('explanation', 'No explanation')}</small>
                </div>
                """, unsafe_allow_html=True)
            
            # Delete button
            if st.button(f"🗑️ Delete", key=f"delete_{idx}"):
                st.session_state.analysis_history.pop(idx)
                st.rerun()
