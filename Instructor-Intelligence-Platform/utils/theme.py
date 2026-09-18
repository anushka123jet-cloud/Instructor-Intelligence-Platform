import streamlit as st
from pathlib import Path


def load_css():
    # Project root directory
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Absolute path to CSS file
    css_path = BASE_DIR / "assets" / "css" / "style.css"

    # Load CSS
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
