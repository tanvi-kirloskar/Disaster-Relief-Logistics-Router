import streamlit as st


def metric_card(title,value):

    st.markdown(
        f"""
        <div class="metric-card">

            <div class="metric-title">
                {title}
            </div>

            <div class="metric-value">
                {value}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def resource_card(resource):

    st.markdown(
        f"""
        <div class="resource-card">
            {resource}
        </div>
        """,
        unsafe_allow_html=True
    )


def alert_card(alert):

    st.markdown(
        f"""
        <div class="alert-card">
            {alert}
        </div>
        """,
        unsafe_allow_html=True
    )