import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

# -----------------------------------
# Load Dataset
# -----------------------------------

df = pd.read_csv(
    "instructor_effectiveness_dataset_2000_rows - instructor_effectiveness_dataset_2000_rows.csv"
)

# -----------------------------------
# Sidebar
# -----------------------------------

st.sidebar.title("📈 Analytics")

st.sidebar.success("Dataset Analysis")

st.sidebar.info("""
Explore instructor performance
using interactive visualizations.
""")

# -----------------------------------
# Title
# -----------------------------------

st.title("📈 Instructor Analytics")

st.caption("Explore • Visualize • Understand")

st.markdown("---")

st.subheader("📋 Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing Values", int(df.isnull().sum().sum()))
col4.metric("Duplicate Rows", int(df.duplicated().sum()))

st.markdown("---")

st.subheader("📄 Dataset Preview")

st.dataframe(df.head(10), use_container_width=True)

st.markdown("---")

st.markdown("---")
st.subheader("📊 Statistical Summary")

st.dataframe(
    df.describe(),
    use_container_width=True
)

st.markdown("---")
st.subheader("📈 Completion Rate Distribution")

fig_completion = px.histogram(
    df,
    x="completion_rate",
    nbins=20,
    color_discrete_sequence=["#3B82F6"],
    title="Completion Rate Distribution"
)

st.plotly_chart(
    fig_completion,
    use_container_width=True
)

st.markdown("---")
st.subheader("📝 Quiz Score Distribution")

fig_quiz = px.histogram(
    df,
    x="avg_quiz_score",
    nbins=20,
    color_discrete_sequence=["#10B981"],
    title="Quiz Score Distribution"
)

st.plotly_chart(
    fig_quiz,
    use_container_width=True
)

st.markdown("---")
st.subheader("📉 Dropout Rate Distribution")

fig_dropout = px.histogram(
    df,
    x="dropout_rate",
    nbins=20,
    color_discrete_sequence=["#EF4444"],
    title="Dropout Rate Distribution"
)

st.plotly_chart(
    fig_dropout,
    use_container_width=True
)

st.markdown("---")
st.subheader("🔥 Feature Correlation Heatmap")

corr = df.corr(numeric_only=True)

fig_heat = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    aspect="auto"
)

st.plotly_chart(
    fig_heat,
    use_container_width=True
)

st.markdown("---")
st.subheader("📦 Feature Distribution")

left, right = st.columns(2)

with left:

    fig_box = px.box(
        df,
        y="completion_rate",
        title="Completion Rate"
    )

    st.plotly_chart(fig_box, use_container_width=True)

with right:

    fig_box2 = px.box(
        df,
        y="avg_quiz_score",
        title="Quiz Score"
    )

    st.plotly_chart(fig_box2, use_container_width=True)

st.markdown("---")
st.subheader("🛠 Missing Value Analysis")

missing = df.isnull().sum()

missing = missing[missing > 0]

if len(missing) == 0:
    st.success("✅ No Missing Values Found")
else:
    st.dataframe(missing)