import streamlit as st
import pandas as pd
import joblib
from utils.theme import load_css
from utils.components import hero

load_css()

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Instructor Prediction",
    page_icon="🎯",
    layout="wide"
)

# ==========================================
# Load Model & Scaler
# ==========================================

model = joblib.load("models/instructor_effectiveness_model.pkl")
scaler = joblib.load("models/minmax_scaler.pkl")

# ==========================================
# Sidebar
# ==========================================

st.sidebar.title("🎯 Prediction Module")

st.sidebar.markdown("---")

st.sidebar.success("Machine Learning Prediction")

st.sidebar.info("""
This module predicts instructor effectiveness
based on learning analytics and engagement metrics.
""")

st.sidebar.markdown("---")

st.sidebar.write("### Model Information")

st.sidebar.write("✔ Best Model : Extra Trees")

st.sidebar.write("✔ Accuracy : 97.22%")

st.sidebar.write("✔ Cross Validation : 94.12%")

st.sidebar.write("✔ Features : 10")

# ==========================================
# Custom CSS
# ==========================================

st.markdown("""
<style>

.big-title{
font-size:42px;
font-weight:800;
color:#4F8BF9;
}

.sub{
font-size:18px;
color:gray;
}

.card{

padding:20px;

border-radius:15px;

background:#111827;

border:1px solid #374151;

}

</style>
""",unsafe_allow_html=True)

# ==========================================
# Heading
# ==========================================

hero(
    "Instructor Effectiveness Prediction",
    "Predict instructor effectiveness using Machine Learning and Artificial Intelligence.",
    "🎯"
)

# ==========================================
# Two Columns
# ==========================================

left,right=st.columns([1.3,1])

# ==========================================
# LEFT SIDE
# ==========================================

with left:

    st.subheader("📋 Instructor Details")

    completion_rate = st.slider(
        "Completion Rate",
        0.0,
        1.0,
        0.80
    )

    avg_score_improvement = st.slider(
        "Average Score Improvement",
        0.0,
        50.0,
        25.0
    )

    avg_quiz_score = st.slider(
        "Average Quiz Score",
        0.0,
        100.0,
        80.0
    )

    dropout_rate = st.slider(
        "Dropout Rate",
        0.0,
        1.0,
        0.10
    )

    avg_watch_time = st.slider(
        "Average Watch Time",
        0.0,
        1.0,
        0.80
    )

    assignment_submission_rate = st.slider(
        "Assignment Submission Rate",
        0.0,
        1.0,
        0.90
    )

    forum_activity_rate = st.slider(
        "Forum Activity Rate",
        0.0,
        1.0,
        0.30
    )

    avg_feedback_score = st.slider(
        "Average Feedback Score",
        1.0,
        5.0,
        4.5
    )

    feedback_response_rate = st.slider(
        "Feedback Response Rate",
        0.0,
        1.0,
        0.90
    )

    num_batches = st.number_input(
        "Number of Batches",
        1,
        100,
        10
    )

    predict = st.button(
        "🚀 Predict Instructor Effectiveness",
        use_container_width=True
    )
    # ==========================================
# RIGHT SIDE
# ==========================================

with right:

    st.subheader("📊 Prediction Result")

    st.info("Enter the instructor details and click **Predict** to view the result.")

# ==========================================
# Prediction
# ==========================================

if predict:

    # Create DataFrame
    input_data = pd.DataFrame([{

        "completion_rate": completion_rate,

        "avg_score_improvement": avg_score_improvement,

        "avg_quiz_score": avg_quiz_score,

        "dropout_rate": dropout_rate,

        "avg_watch_time": avg_watch_time,

        "assignment_submission_rate": assignment_submission_rate,

        "forum_activity_rate": forum_activity_rate,

        "avg_feedback_score": avg_feedback_score,

        "feedback_response_rate": feedback_response_rate,

        "num_batches": num_batches

    }])

    # Scale only first 9 features

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

    input_scaled = input_data.copy()

    input_scaled[scaled_columns] = scaler.transform(
        input_scaled[scaled_columns]
    )

    # Prediction

    prediction = model.predict(input_scaled)[0]

    # Prediction Probability

    try:

        probabilities = model.predict_proba(input_scaled)[0]

        confidence = max(probabilities) * 100

    except:

        confidence = None
    # ==========================================
    # Display Result
    # ==========================================

    st.markdown("---")

    col1, col2 = st.columns([1,1])

    with col1:

        st.subheader("🎯 Prediction")

        if prediction == "High":

            st.success("🟢 HIGH Instructor Effectiveness")

        elif prediction == "Medium":

            st.warning("🟡 MEDIUM Instructor Effectiveness")

        else:

            st.error("🔴 LOW Instructor Effectiveness")

        if confidence is not None:

            st.write(f"### Confidence : {confidence:.2f}%")

            st.progress(confidence/100)

    with col2:

        st.subheader("💡 AI Recommendation")

        if prediction == "High":

            st.success("""

✅ Excellent instructor performance.

• Maintain current teaching strategy.

• Encourage mentoring.

• Continue engaging students.

""")

        elif prediction == "Medium":

            st.warning("""

Improve the following:

• Increase learner engagement.

• Improve assignment submissions.

• Increase feedback response rate.

""")

        else:

            st.error("""

Immediate attention required.

• Reduce dropout rate.

• Improve quiz performance.

• Increase course completion.

• Improve learner interaction.

""")
    st.markdown("---")

    st.subheader("📋 Instructor Summary")

    c1, c2 = st.columns(2)

    with c1:

        st.metric("Completion Rate",
                  f"{completion_rate*100:.0f}%")

        st.metric("Quiz Score",
                  avg_quiz_score)

        st.metric("Feedback Score",
                  avg_feedback_score)

        st.metric("Watch Time",
                  f"{avg_watch_time*100:.0f}%")

        st.metric("Forum Activity",
                  f"{forum_activity_rate*100:.0f}%")

    with c2:

        st.metric("Dropout Rate",
                  f"{dropout_rate*100:.0f}%")

        st.metric("Assignment Submission",
                  f"{assignment_submission_rate*100:.0f}%")

        st.metric("Feedback Response",
                  f"{feedback_response_rate*100:.0f}%")

        st.metric("Score Improvement",
                  avg_score_improvement)

        st.metric("Number of Batches",
                  num_batches)
