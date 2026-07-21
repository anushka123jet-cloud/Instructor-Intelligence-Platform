import streamlit as st
import pandas as pd
import plotly.express as px
from utils.theme import load_css

load_css()
from utils.components import hero

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)
st.markdown("""
<style>

/* Main background */
.main{
    background-color:#0E1117;
}

/* KPI Card */
.metric-card{
    background:linear-gradient(135deg,#2563EB,#4F46E5);
    padding:20px;
    border-radius:18px;
    color:white;
    text-align:center;
    box-shadow:0px 8px 20px rgba(0,0,0,0.3);
}

/* Section Heading */
.section{
    font-size:30px;
    font-weight:700;
    color:#3B82F6;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)
# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("📊 Dashboard")

st.sidebar.success("Instructor Analytics")

st.sidebar.info("""
This dashboard presents
interactive analytics,
model performance,
and platform insights.
""")

# -----------------------------
# Title
# -----------------------------

st.markdown("""
<div class="hero">

<div class="hero-badge">
🚀 AI Powered • Real-Time Analytics • Machine Learning
</div>

<h1 class="hero-title">
📊 Instructor Analytics Dashboard
</h1>

<p class="hero-subtitle">
Transform educational data into actionable insights with intelligent
analytics, interactive visualizations, and machine learning predictions.
</p>

</div>
""", unsafe_allow_html=True)

c1,c2,c3,c4=st.columns(4)

cards=[
("🎯 Accuracy","97.22%"),
("🤖 Best Model","Extra Trees"),
("📚 Features","10"),
("📈 CV Score","94.12%")
]

for col,(title,value) in zip([c1,c2,c3,c4],cards):

    with col:

        st.markdown(f"""
        <div class="metric-card">

        <h3>{title}</h3>

        <h1>{value}</h1>

        </div>
        """,unsafe_allow_html=True)
st.markdown("---")
# =====================================
# Feature Importance
# =====================================

features = [
    "Completion Rate",
    "Score Improvement",
    "Quiz Score",
    "Dropout Rate",
    "Watch Time",
    "Assignment Submission",
    "Forum Activity",
    "Feedback Score",
    "Feedback Response",
    "Number of Batches"
]

importance = [
    0.17,
    0.15,
    0.13,
    0.09,
    0.08,
    0.11,
    0.07,
    0.10,
    0.06,
    0.04
]

fig = px.bar(
    x=importance,
    y=features,
    orientation="h",
    title="📈 Feature Importance"
)

# =====================================
# Model Comparison
# =====================================

models = [
    "Logistic Regression",
    "Decision Tree",
    "Random Forest",
    "AdaBoost",
    "Gradient Boosting",
    "Extra Trees",
    "XGBoost"
]

accuracy = [
    88.89,
    86.11,
    94.44,
    86.11,
    97.22,
    97.22,
    88.89
]

fig2 = px.bar(
    x=models,
    y=accuracy,
    color=accuracy,
    title="🏆 Model Comparison"
)

# =====================================
# Pie Chart
# =====================================

labels = ["High", "Medium", "Low"]

values = [40,35,25]

fig3 = px.pie(
    names=labels,
    values=values,
    title="🎯 Instructor Categories"
)

# =====================================
# Display Charts
# =====================================

left, right = st.columns(2)

with left:
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.plotly_chart(fig3, use_container_width=True)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("## 📈 Dataset Statistics")

a,b,c=st.columns(3)

a.info("""
### 👨‍🏫 High

40%
""")

b.warning("""
### 📘 Medium

35%
""")

c.error("""
### 📕 Low

25%
""")
st.markdown("---")

st.subheader("📈 Platform Insights")

st.markdown("## 🤖 AI Insights")

st.success("""
✔ Extra Trees is the best-performing model with **97.22% accuracy**.
""")

st.info("""
📈 Completion Rate is the strongest predictor of instructor effectiveness.
""")

st.warning("""
⚠ Higher dropout rates generally reduce instructor effectiveness.
""")

st.success("""
⭐ Instructors with strong feedback scores consistently achieve better predictions.
""")
st.markdown("---")

st.markdown("""
<div style='text-align:center;color:gray;'>

Instructor Intelligence Platform

Machine Learning • Streamlit • Plotly • Scikit-learn

Developed by <b>Anushka Verma</b>

</div>
""", unsafe_allow_html=True)
