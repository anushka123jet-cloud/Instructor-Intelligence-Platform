import streamlit as st


def hero(title, subtitle, emoji="🚀"):
    st.markdown(
        f"""
        <div class="hero">

            <div class="hero-badge">
                {emoji} AI Powered • Real-Time Analytics • Machine Learning
            </div>

            <h1 class="hero-title">
                {emoji} {title}
            </h1>

            <p class="hero-subtitle">
                {subtitle}
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )
