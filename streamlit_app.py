import streamlit as st

from workflow.orchestrator import DisasterWorkflow

from ui.styles import load_css
from ui.sidebar import render_sidebar
from ui.dashboard import render_dashboard
from ui.sample_data import SAMPLE_INCIDENTS


st.set_page_config(
    page_title="Disaster Relief Logistics Router",
    page_icon="🛡️",
    layout="wide"
)

load_css()

workflow = DisasterWorkflow()

render_sidebar()

st.markdown("""
<div class="hero-header">
    <div>
        <div class="hero-title">
            Disaster Relief Logistics Router
        </div>
        <div class="hero-subtitle">
            AI-Powered Emergency Coordination System
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="glass-card">
""", unsafe_allow_html=True)

st.subheader("New Incident Report")

selected_incident = st.radio(
    "Load Sample Incident",
    list(SAMPLE_INCIDENTS.keys()),
    horizontal=True
)

report = st.text_area(
    "Incident Description",
    value=SAMPLE_INCIDENTS[selected_incident],
    height=140
)

analyze = st.button(
    "Analyze Incident",
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)

if analyze:

    with st.spinner("Analyzing incident..."):

        try:

            incident = workflow.run(
                report=report
            )

            st.session_state["incident"] = incident

        except Exception as e:

            st.error(f"Workflow Error: {e}")

if "incident" in st.session_state:

    render_dashboard(
        st.session_state["incident"]
    )