from pathlib import Path
import streamlit as st


def load_css():

    BASE_DIR = Path(__file__).resolve().parent.parent

    CSS_PATH = BASE_DIR / "assets" / "css" / "style.css"

    with open(CSS_PATH, "r", encoding="utf-8") as f:
        css = f.read()

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )
