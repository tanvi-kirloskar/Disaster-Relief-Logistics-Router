from streamlit_option_menu import option_menu
import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.image(
            "https://cdn-icons-png.flaticon.com/512/854/854878.png",
            width=80
        )

        selected = option_menu(
            menu_title=None,

            options=[
                "Dashboard",
                "Incidents",
                "Resources",
                "Teams",
                "Notifications",
                "Analytics",
                "Reports",
                "Settings"
            ],

            icons=[
                "house",
                "exclamation-triangle",
                "box",
                "people",
                "bell",
                "graph-up",
                "file-earmark",
                "gear"
            ],

            default_index=0
        )

        st.markdown("---")

        st.success("""
Active Incident

ID: INC-2026-001

Severity: CRITICAL

Pune, Maharashtra
""")

    return selected