import streamlit as st


def render_dashboard(incident):

    st.markdown("---")

    st.subheader("🚨 Incident Analysis")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Severity",
            incident.severity
        )

    with col2:
        st.metric(
            "Security",
            incident.security_status
        )

    with col3:
        st.metric(
            "Resources",
            len(
                incident.recommended_resources
            )
        )

    with col4:
        st.metric(
            "Alerts",
            len(
                incident.notifications
            )
        )

    st.markdown("---")

    left, right = st.columns(2)

    with left:

        st.subheader("Severity")

        st.error(
            f"Severity: {incident.severity}"
        )

        st.subheader(
            "Security Status"
        )

        st.write(
            incident.security_status
        )

        st.subheader(
            "Human Review"
        )

        st.write(
            incident.review_status
        )

    with right:

        st.subheader(
            "Recommended Resources"
        )

        for resource in (
            incident.recommended_resources
        ):
            st.success(resource)

        st.subheader(
            "Notifications"
        )

        for alert in (
            incident.notifications
        ):
            st.warning(alert)