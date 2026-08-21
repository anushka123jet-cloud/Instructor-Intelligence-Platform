import streamlit as st


def hero(title, subtitle, emoji="🚀"):
    html = f"""
<div class="hero">
<div class="hero-badge">{emoji} AI Powered • Real-Time Analytics • Machine Learning</div>
<div class="hero-content">
<h1 class="hero-title">{emoji} {title}</h1>
<p class="hero-subtitle">{subtitle}</p>
</div>
</div>
"""

    st.markdown(html, unsafe_allow_html=True)
