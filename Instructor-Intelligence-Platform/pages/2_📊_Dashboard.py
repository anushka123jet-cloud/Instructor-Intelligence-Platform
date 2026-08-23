

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load CSS
load_css()


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("📊 Dashboard")

st.sidebar.success("Instructor Analytics")

st.sidebar.info("""
This dashboard presents
interactive analytics,
model performance,
and platform insights.
""")


# ==========================================
# HERO SECTION
# ==========================================

hero(
    "Instructor Analytics Dashboard",
    "Transform educational data into actionable insights with intelligent analytics, interactive visualizations, and machine learning predictions.",
    "📊"
)


# ==========================================
# METRIC CARDS
# ==========================================

c1, c2, c3, c4 = st.columns(4)

cards = [
    ("🎯 Accuracy", "97.22%"),
    ("🤖 Best Model", "Extra Trees"),
    ("📚 Features", "10"),
    ("📈 CV Score", "94.12%")
]

for col, (title, value) in zip([c1, c2, c3, c4], cards):

    with col:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">{title}</div>
                <div class="metric-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


st.markdown("---")


# ==========================================
# FEATURE IMPORTANCE
# ==========================================

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


# ==========================================
# MODEL COMPARISON
# ==========================================

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


# ==========================================
# INSTRUCTOR CATEGORIES
# ==========================================

labels = [
    "High",
    "Medium",
    "Low"
]

values = [
    40,
    35,
    25
]

fig3 = px.pie(
    names=labels,
    values=values,
    title="🎯 Instructor Categories"
)


# ==========================================
# DISPLAY CHARTS
# ==========================================

left, right = st.columns(2)

with left:

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    st.plotly_chart(
        fig3,
        use_container_width=True
    )


st.plotly_chart(
    fig2,
    use_container_width=True
)


# ==========================================
# DATASET STATISTICS
# ==========================================

st.markdown("## 📈 Dataset Statistics")

a, b, c = st.columns(3)

with a:

    st.info("""
    ### 👨‍🏫 High

    40%
    """)

with b:

    st.warning("""
    ### 📘 Medium

    35%
    """)

with c:

    st.error("""
    ### 📕 Low

    25%
    """)


st.markdown("---")


# ==========================================
# PLATFORM INSIGHTS
# ==========================================

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


# ==========================================
# FOOTER
# ==========================================

st.markdown(
    """
    <div style="
        text-align:center;
        color:gray;
        padding:20px;
    ">

        <b>Instructor Intelligence Platform</b><br>

        Machine Learning • Streamlit • Plotly • Scikit-learn<br><br>

        Developed by <b>Anushka Verma</b>

    </div>
    """,
    unsafe_allow_html=True
)
