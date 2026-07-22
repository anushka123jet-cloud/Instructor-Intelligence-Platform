import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from utils.theme import load_css
from utils.components import hero

load_css()
# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Reports",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("📄 Reports")

st.sidebar.success("AI Generated Reports")

st.sidebar.info("""
Generate model reports,
performance summaries,
and export analytics.
""")

# -----------------------------
# Title
# -----------------------------

st.markdown("""
# 📄 Instructor Intelligence Reports

Generate comprehensive reports of instructor performance,
model evaluation and platform statistics.
""")

st.markdown("---")
c1,c2,c3,c4 = st.columns(4)

c1.metric("Model Accuracy","97.22%","+2.8%")
c2.metric("Best Model","Extra Trees")
c3.metric("Features Used","10")
c4.metric("Prediction Classes","3")
st.markdown("## 📊 Model Performance")

report = pd.DataFrame({

    "Model":[
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "AdaBoost",
        "Gradient Boosting",
        "Extra Trees",
        "XGBoost"
    ],

    "Accuracy":[
        88.89,
        86.11,
        94.44,
        86.11,
        97.22,
        97.22,
        88.89
    ]

})

st.dataframe(
    report,
    use_container_width=True
)
fig = px.bar(

    report,

    x="Model",

    y="Accuracy",

    color="Accuracy",

    title="Model Comparison"

)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.markdown("## ⭐ Feature Importance")

feature_df = pd.DataFrame({

"Feature":[

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

],

"Importance":[

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

})

st.dataframe(
    feature_df,
    use_container_width=True
)
st.markdown("## 🤖 AI Report Summary")

st.success("""
### Key Findings

• Extra Trees achieved the highest accuracy (97.22%).

• Completion Rate is the most influential feature.

• High feedback scores strongly improve instructor effectiveness.

• Increased dropout rates negatively affect predictions.

• The model provides reliable classification into
High, Medium and Low instructor effectiveness.
""")
st.markdown("## 📥 Export Report")

csv = report.to_csv(index=False).encode("utf-8")

st.download_button(

label="Download Model Report",

data=csv,

file_name="Instructor_Report.csv",

mime="text/csv",

use_container_width=True

)
st.markdown("---")

st.info(f"""
🗓 Report Generated

Date : {datetime.now().strftime("%d-%m-%Y")}

Time : {datetime.now().strftime("%H:%M:%S")}

Platform : Instructor Intelligence Platform
""")
st.markdown("---")

st.markdown("""
<div style='text-align:center;color:gray;'>

Instructor Intelligence Platform

Machine Learning • Streamlit • Plotly • Scikit-learn

Developed by <b>Anushka Verma</b>

</div>
""", unsafe_allow_html=True)
