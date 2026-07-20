import streamlit as st

# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# =====================================
# Custom CSS
# =====================================

st.markdown("""
<style>

.main{
    background-color:#0E1117;
}

.hero{
    background:linear-gradient(90deg,#2563EB,#7C3AED);
    padding:40px;
    border-radius:20px;
    color:white;
    text-align:center;
}

.card{
    background:#1E293B;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 8px 18px rgba(0,0,0,0.3);
}

.tech{
    background:#111827;
    padding:15px;
    border-radius:12px;
    text-align:center;
    border:1px solid #374151;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# Hero Section
# =====================================

st.markdown("""
<div class="hero">

<h1>🎓 Instructor Intelligence Platform</h1>

<h3>
AI-Powered Instructor Effectiveness Prediction System
</h3>

<p style="font-size:18px;">
A complete Machine Learning platform that predicts instructor effectiveness,
provides analytics dashboards, batch prediction,
interactive reports and educational insights.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("")

# =====================================
# Project Overview
# =====================================

st.markdown("## 🚀 Project Overview")

st.write("""
The Instructor Intelligence Platform is an end-to-end Machine Learning application
designed to evaluate instructor effectiveness using educational performance data.

The platform combines machine learning, interactive dashboards and data visualization
to assist educational institutions in making data-driven decisions.
""")

st.markdown("---")

# =====================================
# Features
# =====================================

st.markdown("## ✨ Platform Features")

c1,c2,c3=st.columns(3)

with c1:
    st.success("""
🎯 Instructor Prediction

Predict instructor effectiveness using trained ML models.
""")

with c2:
    st.info("""
📊 Interactive Dashboard

Visualize analytics and feature importance.
""")

with c3:
    st.warning("""
📂 Batch Prediction

Predict hundreds of instructors from a CSV file.
""")

c4,c5,c6=st.columns(3)

with c4:
    st.success("""
📈 Analytics

Educational performance insights.
""")

with c5:
    st.info("""
📄 Report Generation

Export prediction reports.
""")

with c6:
    st.warning("""
🤖 AI Insights

Automatically generated recommendations.
""")

st.markdown("---")

# =====================================
# Technology Stack
# =====================================

st.markdown("## 💻 Technology Stack")

t1,t2,t3,t4=st.columns(4)

with t1:
    st.markdown("""
<div class="tech">
<h3>🐍 Python</h3>
</div>
""",unsafe_allow_html=True)

with t2:
    st.markdown("""
<div class="tech">
<h3>⚡ Streamlit</h3>
</div>
""",unsafe_allow_html=True)

with t3:
    st.markdown("""
<div class="tech">
<h3>📊 Plotly</h3>
</div>
""",unsafe_allow_html=True)

with t4:
    st.markdown("""
<div class="tech">
<h3>🤖 Scikit-learn</h3>
</div>
""",unsafe_allow_html=True)

st.markdown("")

t5,t6,t7,t8=st.columns(4)

with t5:
    st.markdown("""
<div class="tech">
<h3>🐼 Pandas</h3>
</div>
""",unsafe_allow_html=True)

with t6:
    st.markdown("""
<div class="tech">
<h3>🔢 NumPy</h3>
</div>
""",unsafe_allow_html=True)

with t7:
    st.markdown("""
<div class="tech">
<h3>📈 Matplotlib</h3>
</div>
""",unsafe_allow_html=True)

with t8:
    st.markdown("""
<div class="tech">
<h3>🎨 Seaborn</h3>
</div>
""",unsafe_allow_html=True)

st.markdown("---")

# =====================================
# Workflow
# =====================================

st.markdown("## 🔄 Project Workflow")

st.code("""

Dataset
    │
    ▼
Data Preprocessing
    │
    ▼
Feature Engineering
    │
    ▼
Model Training
    │
    ▼
Extra Trees Classifier
    │
    ▼
Prediction
    │
    ▼
Analytics Dashboard
    │
    ▼
Reports

""")

st.markdown("---")

# =====================================
# Model Performance
# =====================================

st.markdown("## 🏆 Model Performance")

st.metric("Best Model","Extra Trees Classifier")

st.metric("Accuracy","97.22%")

st.metric("Cross Validation","94.12%")

st.markdown("---")

# =====================================
# Future Scope
# =====================================

st.markdown("## 🚀 Future Enhancements")

st.write("""
✅ Real-time instructor monitoring

✅ Deep Learning models

✅ Cloud Deployment

✅ Student Feedback Analysis

✅ Automated Email Reports

✅ Mobile Dashboard

✅ Explainable AI (SHAP)

✅ Institution-wise Analytics
""")

st.markdown("---")

# =====================================
# Developer
# =====================================

st.markdown("## 👩‍💻 Developer")

st.info("""
**Anushka Verma**

MCA Student

Harcourt Butler Technical University (HBTU), Kanpur

Machine Learning | Data Science | AI Enthusiast
""")

st.markdown("---")

st.markdown("""
<div style='text-align:center;color:gray;'>

Instructor Intelligence Platform © 2026

Developed using ❤️ Python, Streamlit and Machine Learning

</div>
""", unsafe_allow_html=True)
