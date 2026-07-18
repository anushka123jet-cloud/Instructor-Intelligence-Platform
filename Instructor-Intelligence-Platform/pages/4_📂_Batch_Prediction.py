import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="Batch Prediction",
    page_icon="📂",
    layout="wide"
)

# =====================================
# Load Model
# =====================================

model = joblib.load("models/instructor_effectiveness_model.pkl")
scaler = joblib.load("models/minmax_scaler.pkl")

# =====================================
# Sidebar
# =====================================

st.sidebar.title("📂 Batch Prediction")

st.sidebar.success("Bulk Instructor Prediction")

st.sidebar.info("""
Upload a CSV file containing instructor data.

The model will predict the effectiveness of every instructor automatically.
""")

# =====================================
# Title
# =====================================

st.title("📂 Batch Prediction")

st.write(
    "Predict instructor effectiveness for multiple instructors using a CSV file."
)

st.markdown("---")
uploaded_file = st.file_uploader(
    "📤 Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("✅ File uploaded successfully!")

    st.subheader("📄 Dataset Preview")

    st.dataframe(
        df.head(),
        use_container_width=True
    )
    required_columns = [

        "completion_rate",
        "avg_score_improvement",
        "avg_quiz_score",
        "dropout_rate",
        "avg_watch_time",
        "assignment_submission_rate",
        "forum_activity_rate",
        "avg_feedback_score",
        "feedback_response_rate",
        "num_batches"

    ]

    missing = [
        col
        for col in required_columns
        if col not in df.columns
    ]

    if len(missing) > 0:

        st.error("❌ Missing Columns")

        st.write(missing)

        st.stop()

    st.success("✅ Dataset Validation Passed")
# =====================================
# Scale Features
# =====================================

    scaled_columns = [

    "completion_rate",
    "avg_score_improvement",
    "avg_quiz_score",
    "dropout_rate",
    "avg_watch_time",
    "assignment_submission_rate",
    "forum_activity_rate",
    "avg_feedback_score",
    "feedback_response_rate"

]

    scaled_df = df.copy()

    scaled_df[scaled_columns] = scaler.transform(
       scaled_df[scaled_columns]
)
    # =====================================
    # Predict
    # =====================================

    if st.button("🚀 Predict All Instructors", use_container_width=True):

        predictions = model.predict(scaled_df)

        result_df = df.copy()

        result_df["Predicted Effectiveness"] = predictions

        st.success("✅ Prediction Completed Successfully!")

        st.subheader("📋 Prediction Results")

        st.dataframe(
            result_df,
            use_container_width=True
        )

        st.markdown("---")

        st.subheader("📊 Prediction Summary")

        summary = (
            result_df["Predicted Effectiveness"]
            .value_counts()
            .reset_index()
        )

        summary.columns = [
            "Category",
            "Count"
        ]

        st.dataframe(
            summary,
            use_container_width=True
        )

        

        fig = px.pie(
            summary,
            names="Category",
            values="Count",
            title="Prediction Distribution",
            hole=0.45
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        csv = result_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Prediction Results",
            data=csv,
            file_name="Instructor_Predictions.csv",
            mime="text/csv",
            use_container_width=True
        )

        

