import streamlit as st


def load_css():

    st.markdown("""
    <style>

    .stApp{
        background:#08111f;
    }

    section[data-testid="stSidebar"]{
        background:#0b1727;
    }

    .main-title{
        font-size:52px;
        font-weight:700;
        color:white;
    }

    .sub-title{
        color:#94a3b8;
        font-size:18px;
    }

    .metric-card{
        background:#111c2e;
        border-radius:18px;
        padding:25px;
        text-align:center;
        border:1px solid #22314b;
    }

    .metric-title{
        color:#94a3b8;
        font-size:14px;
    }

    .metric-value{
        color:white;
        font-size:36px;
        font-weight:700;
    }

    .resource-card{
        background:#13293d;
        border-radius:12px;
        padding:16px;
        margin-bottom:12px;
    }

    .alert-card{
        background:#3d310b;
        border-radius:12px;
        padding:16px;
        margin-bottom:12px;
    }

    .section-card{
        background:#111c2e;
        padding:20px;
        border-radius:18px;
        border:1px solid #22314b;
    }

    </style>
    """,
    unsafe_allow_html=True)