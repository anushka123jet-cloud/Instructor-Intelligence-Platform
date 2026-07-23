import streamlit as st

def hero(title, subtitle, emoji="🚀"):
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg,#2563EB,#7C3AED,#06B6D4);
            padding:45px;
            border-radius:25px;
            color:white;
            text-align:center;
            box-shadow:0 12px 35px rgba(0,0,0,0.35);
            margin-bottom:30px;
        ">
            <h1 style="
                font-size:52px;
                margin-bottom:10px;
                font-weight:800;
            ">
                {emoji} {title}
            </h1>

            <p style="
                font-size:20px;
                opacity:0.95;
            ">
                {subtitle}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
