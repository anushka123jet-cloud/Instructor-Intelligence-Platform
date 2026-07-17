import streamlit as st
import os

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(
    page_title="Instructor Intelligence Platform",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# FONTS + DESIGN TOKENS + CUSTOM CSS
# ----------------------------------------------------
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>

:root{
    --bg: #0A0E27;
    --bg-raised: #131A38;
    --bg-raised-2: #1A2247;
    --border: #262F58;
    --text-primary: #F1F3FA;
    --text-secondary: #99A2C9;
    --blue: #4C6FFF;
    --blue-soft: rgba(76,111,255,0.14);
    --teal: #2DD4BF;
    --amber: #F5A623;
    --coral: #F0654A;
}

.stApp{
    background: radial-gradient(ellipse 900px 500px at 15% -10%, rgba(76,111,255,0.16), transparent),
                radial-gradient(ellipse 700px 500px at 100% 10%, rgba(45,212,191,0.10), transparent),
                var(--bg);
}

.block-container{
    padding-top:2.5rem;
    padding-bottom:3rem;
    padding-left:4rem;
    padding-right:4rem;
    max-width:1220px;
}

h1,h2,h3,h4{
    font-family:'Space Grotesk', sans-serif;
    color:var(--text-primary);
}

p, div, span, li, label{
    font-family:'Inter', sans-serif;
    color:var(--text-primary);
}

/* ---------- BADGE ---------- */
.eic-badge{
    display:inline-flex;
    align-items:center;
    gap:8px;
    font-size:12px;
    font-weight:600;
    letter-spacing:0.6px;
    color:var(--teal);
    background:rgba(45,212,191,0.10);
    border:1px solid rgba(45,212,191,0.25);
    padding:6px 14px;
    border-radius:999px;
    margin-bottom:22px;
    text-transform:uppercase;
}

/* ---------- HERO ---------- */
.eic-hero h1{
    font-size:46px;
    font-weight:700;
    line-height:1.12;
    letter-spacing:-1px;
    margin:0 0 18px 0;
}

.eic-hero h1 .accent{
    color:var(--teal);
}

.eic-hero-sub{
    font-size:16px;
    color:var(--text-secondary);
    line-height:1.75;
    max-width:520px;
    margin-bottom:30px;
}

/* ---------- TIER PILLS ---------- */
.eic-pill-row{
    display:flex;
    gap:10px;
    flex-wrap:wrap;
}

.eic-pill{
    display:flex;
    align-items:center;
    gap:8px;
    font-size:13px;
    font-weight:600;
    color:var(--text-primary);
    padding:8px 16px;
    border-radius:999px;
    border:1px solid var(--border);
    background:var(--bg-raised);
}

.eic-dot{
    width:8px;
    height:8px;
    border-radius:50%;
}

/* ---------- HERO IMAGE FRAME ---------- */
.eic-hero-image-wrap{
    position:relative;
    border-radius:20px;
    padding:8px;
    background:linear-gradient(160deg, rgba(76,111,255,0.35), rgba(45,212,191,0.15));
}

.eic-hero-image-inner{
    border-radius:14px;
    overflow:hidden;
    border:1px solid var(--border);
}

/* ---------- CARDS / METRICS ---------- */
.eic-card{
    border:1px solid var(--border);
    border-top:2px solid var(--blue);
    border-radius:12px;
    background:var(--bg-raised);
    padding:22px 24px;
    height:100%;
}

.eic-ledger-row{
    display:flex;
    gap:16px;
    margin-top:40px;
}

.eic-metric-value{
    font-family:'Space Grotesk', sans-serif;
    font-size:26px;
    font-weight:700;
    color:var(--text-primary);
}

.eic-metric-label{
    font-size:13px;
    color:var(--text-secondary);
    margin-top:4px;
}

.eic-caption{
    font-size:13px;
    color:var(--text-secondary);
    margin-top:14px;
}

/* ---------- SECTION HEADINGS ---------- */
.eic-section-heading{
    font-family:'Space Grotesk', sans-serif;
    font-size:26px;
    font-weight:700;
    letter-spacing:-0.5px;
    margin-bottom:6px;
}

.eic-body-text{
    color:var(--text-secondary);
    font-size:16px;
    line-height:1.8;
    max-width:740px;
}

/* ---------- FEATURE CARDS ---------- */
.eic-feature-card{
    border:1px solid var(--border);
    border-radius:14px;
    background:var(--bg-raised);
    padding:26px 24px;
    height:100%;
    transition:border-color 0.2s ease, transform 0.2s ease;
}

.eic-feature-card:hover{
    border-color:var(--blue);
    transform:translateY(-2px);
}

.eic-feature-icon{
    width:38px;
    height:38px;
    border-radius:10px;
    background:var(--blue-soft);
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:18px;
    margin-bottom:16px;
}

.eic-feature-title{
    font-family:'Space Grotesk', sans-serif;
    font-size:17px;
    font-weight:700;
    color:var(--text-primary);
    margin-bottom:12px;
}

.eic-feature-item{
    font-size:14px;
    color:var(--text-secondary);
    margin-bottom:8px;
    padding-left:20px;
    position:relative;
}

.eic-feature-item::before{
    content:"✓";
    position:absolute;
    left:0;
    color:var(--teal);
    font-weight:700;
}

/* ---------- STEPS ---------- */
.eic-step{
    display:flex;
    align-items:flex-start;
    gap:16px;
    padding:16px 0;
    border-bottom:1px solid var(--border);
}

.eic-step:last-child{
    border-bottom:none;
}

.eic-step-index{
    flex-shrink:0;
    width:28px;
    height:28px;
    border-radius:50%;
    background:var(--blue-soft);
    color:var(--blue);
    font-family:'Space Grotesk', sans-serif;
    font-size:13px;
    font-weight:700;
    display:flex;
    align-items:center;
    justify-content:center;
}

.eic-step-text{
    font-size:15px;
    color:var(--text-primary);
    padding-top:4px;
}

/* ---------- DIVIDER ---------- */
.eic-rule{
    border:none;
    border-top:1px solid var(--border);
    margin:38px 0;
}

/* ---------- FOOTER ---------- */
.eic-footer{
    text-align:center;
    padding:24px 0 4px 0;
    margin-top:12px;
    border-top:1px solid var(--border);
    font-size:13px;
    color:var(--text-secondary);
}

.eic-footer span{
    color:var(--teal);
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# HERO SECTION
# ----------------------------------------------------

left, right = st.columns([1.05, 1], gap="large")

with left:
    st.markdown("""
    <div class="eic-hero">
        <div class="eic-badge">🎓 ML Evaluation Platform</div>
        <h1>Instructor effectiveness,<br><span class="accent">scored</span> from real data.</h1>
        <p class="eic-hero-sub">
        A machine learning system that classifies instructors into Low, Medium,
        and High effectiveness tiers using learner engagement, academic
        performance, and feedback data &mdash; giving institutions an
        evidence-based read on teaching quality instead of anecdote.
        </p>
        <div class="eic-pill-row">
            <div class="eic-pill"><span class="eic-dot" style="background:#F0654A;"></span>Low</div>
            <div class="eic-pill"><span class="eic-dot" style="background:#F5A623;"></span>Medium</div>
            <div class="eic-pill"><span class="eic-dot" style="background:#2DD4BF;"></span>High</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with right:
    banner_path = "images/banner.png"
    if os.path.exists(banner_path):
        st.markdown('<div class="eic-hero-image-wrap"><div class="eic-hero-image-inner">', unsafe_allow_html=True)
        st.image(banner_path, use_container_width=True)
        st.markdown('</div></div>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="eic-hero-image-wrap"><div class="eic-hero-image-inner">
        <div style="padding:70px 20px;text-align:center;color:#99A2C9;background:#131A38;">
        🎓<br>Place your banner image at <code>images/banner.png</code>
        </div>
        </div></div>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# METRICS ROW
# ----------------------------------------------------

st.markdown("""
<div class="eic-ledger-row">
    <div class="eic-card">
        <div class="eic-metric-value">94.44%</div>
        <div class="eic-metric-label">Model Accuracy</div>
    </div>
    <div class="eic-card">
        <div class="eic-metric-value">Random Forest</div>
        <div class="eic-metric-label">Best Model</div>
    </div>
    <div class="eic-card">
        <div class="eic-metric-value">10</div>
        <div class="eic-metric-label">Input Features</div>
    </div>
    <div class="eic-card">
        <div class="eic-metric-value">&mdash;</div>
        <div class="eic-metric-label">Cross Validation</div>
    </div>
</div>
<div class="eic-caption">Evaluated on a held-out test set &middot; see project README for full methodology</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="eic-rule">', unsafe_allow_html=True)

# ----------------------------------------------------
# OVERVIEW
# ----------------------------------------------------

st.markdown('<div class="eic-section-heading">Platform Overview</div>', unsafe_allow_html=True)
st.markdown("""
<p class="eic-body-text">
The Instructor Intelligence Platform helps educational institutions evaluate and
monitor instructor performance using machine learning. It predicts instructor
effectiveness from learner engagement, academic performance, and feedback
metrics, and surfaces the features driving each prediction &mdash; so results
are explainable, not a black box.
</p>
""", unsafe_allow_html=True)

st.markdown('<hr class="eic-rule">', unsafe_allow_html=True)

# ----------------------------------------------------
# FEATURES
# ----------------------------------------------------

st.markdown('<div class="eic-section-heading">Key Features</div>', unsafe_allow_html=True)
st.write("")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="eic-feature-card">
        <div class="eic-feature-icon">🎯</div>
        <div class="eic-feature-title">Instructor Prediction</div>
        <div class="eic-feature-item">Predicts instructor effectiveness</div>
        <div class="eic-feature-item">Low / Medium / High classification</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="eic-feature-card">
        <div class="eic-feature-icon">📊</div>
        <div class="eic-feature-title">Analytics</div>
        <div class="eic-feature-item">Feature importance breakdown</div>
        <div class="eic-feature-item">Performance dashboard</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="eic-feature-card">
        <div class="eic-feature-icon">📄</div>
        <div class="eic-feature-title">Reporting</div>
        <div class="eic-feature-item">Batch prediction</div>
        <div class="eic-feature-item">Downloadable reports</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown('<hr class="eic-rule">', unsafe_allow_html=True)

# ----------------------------------------------------
# HOW IT WORKS
# ----------------------------------------------------

st.markdown('<div class="eic-section-heading">How It Works</div>', unsafe_allow_html=True)
st.write("")
 
st.markdown("""
<p class="eic-body-text">
You enter the instructor's engagement, performance, and feedback details.
The model compares them against the patterns it learned during training.
It predicts a Low, Medium, or High effectiveness tier.
The dashboard then shows which features drove that result, along with
recommendations.
</p>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------

st.markdown("""
<div class="eic-footer">
Developed by <span>Anushka Verma</span> &middot; Instructor Intelligence Platform &middot; Machine Learning &middot; Streamlit
</div>
""", unsafe_allow_html=True)