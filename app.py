
import streamlit as st
import pandas as pd
import joblib

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Student Report Card Lab",
    page_icon="🎓",
    layout="wide"
)

# ==========================================
# 2. LOAD MACHINE LEARNING MODEL
# ==========================================

model = joblib.load("student_performance_model.pkl")

# ==========================================
# 3. CUSTOM CSS DESIGN
# ==========================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #10152f, #252052, #162d4a);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 43px;
    font-weight: 900;
    color: white;
}

.subtitle {
    text-align: center;
    color: #c5c9ff;
    font-size: 18px;
}

div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #6146d9, #2878d0);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
}

div.stButton > button {
    background: linear-gradient(90deg, #8b5cf6, #06b6d4);
    color: white;
    border-radius: 15px;
    border: none;
    height: 55px;
    width: 100%;
    font-size: 19px;
    font-weight: bold;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #06b6d4, #8b5cf6);
    color: white;
    border: 1px solid white;
}

.result-card {
    background: linear-gradient(135deg, #372b78, #174c70);
    padding: 30px;
    border-radius: 22px;
    text-align: center;
    border: 1px solid #8175ff;
    margin-top: 20px;
}

.big-score {
    font-size: 65px;
    font-weight: 900;
    color: white;
}

.small-text {
    color: #d4d9ff;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 4. HEADER
# ==========================================

st.markdown(
    '<div class="main-title">🎓 STUDENT REPORT CARD LAB</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">🤖 AI is ready! Let’s predict your academic future!</div>',
    unsafe_allow_html=True
)

st.write("")

st.markdown("""
<div style="text-align:center; font-size:17px;">
🔥 Your marks, your future, and a little bit of AI magic!
</div>
""", unsafe_allow_html=True)

st.divider()


# ==========================================
# 5. SIDEBAR
# ==========================================

st.sidebar.title("🎮 About This App")

st.sidebar.write("""
Welcome to Student Report Card Lab!

This application uses Machine Learning
to estimate a student's average examination score.

✨ Features:

- AI Score Prediction
- Student Performance Analysis
- Fun Result Messages
- Interactive Interface
""")

st.sidebar.info(
    "Built with Python + Streamlit + Machine Learning 🤖"
)


# ==========================================
# 6. STUDENT INPUT SECTION
# ==========================================

st.header("📝 Enter Student Details")

st.caption(
    "Fill in the details below and let AI do its magic!"
)

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "👤 Gender",
        ["male", "female"]
    )

    race = st.selectbox(
        "🌍 Race / Ethnicity",
        [
            "group A",
            "group B",
            "group C",
            "group D",
            "group E"
        ]
    )

    parent_education = st.selectbox(
        "👨‍👩‍👧 Parental Education",
        [
            "some high school",
            "high school",
            "some college",
            "associate's degree",
            "bachelor's degree",
            "master's degree"
        ]
    )

with col2:

    lunch = st.selectbox(
        "🍱 Lunch Type",
        ["standard", "free/reduced"]
    )

    test_preparation = st.selectbox(
        "📚 Test Preparation",
        ["completed", "none"]
    )

st.write("")
st.divider()


# ==========================================
# 7. PREDICTION BUTTON
# ==========================================

st.markdown(
    "<h3 style='text-align:center;'>🚀 Ready for the Big Reveal?</h3>",
    unsafe_allow_html=True
)

if st.button("✨ PREDICT MY SCORE ✨"):

    # BALLOONS EVERY TIME!
    st.balloons()

    # ======================================
    # CREATE STUDENT DATAFRAME
    # ======================================

    new_student = pd.DataFrame({
        "gender": [gender],
        "race/ethnicity": [race],
        "parental level of education": [parent_education],
        "lunch": [lunch],
        "test preparation course": [test_preparation]
    })

    # ======================================
    # MACHINE LEARNING PREDICTION
    # ======================================

    prediction = model.predict(new_student)

    score = float(prediction[0])

    display_score = max(0, min(100, score))

    # ======================================
    # PERFORMANCE ANALYSIS
    # ======================================

    if score >= 90:

        level = "🏆 LEGENDARY GENIUS!"

        message = "Are you secretly Einstein's student? 😂"

        motivation = "Keep shining! The world needs your brilliance! 🌟"

        st.snow()

    elif score >= 80:

        level = "🥇 ACADEMIC SUPERSTAR!"

        message = "Your books are clearly your best friends! 📚"

        motivation = "Amazing work! Keep reaching for the stars!"

        st.snow()

    elif score >= 70:

        level = "🔥 EXCELLENT PERFORMANCE!"

        message = "Someone is taking studies seriously! 😎"

        motivation = "You're doing great. Keep going!"

    elif score >= 60:

        level = "⭐ GOOD PERFORMANCE!"

        message = "Not bad! Your hard work is showing!"

        motivation = "A little more effort can take you higher!"

    elif score >= 50:

        level = "☕ NEEDS SOME EXTRA COFFEE!"

        message = "Maybe reduce Netflix and increase textbooks! 😂"

        motivation = "Don't give up. Every topper starts somewhere!"

    else:

        level = "💪 COMEBACK LOADING..."

        message = "Even Wi-Fi disconnects sometimes. Reconnect and try! 😂"

        motivation = "Your current score doesn't define your future!"

    # ======================================
    # 8. DISPLAY PREDICTION RESULT
    # ======================================

    st.divider()

    st.markdown(
        f"""
        <div class="result-card">
            <h2>🎉 YOUR AI RESULT IS READY!</h2>
            <div class="big-score">{display_score:.2f} / 100</div>
            <h2>{level}</h2>
            <p class="small-text">{message}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ======================================
    # 9. PERFORMANCE METER
    # ======================================

    st.subheader("📊 Performance Meter")

    st.progress(display_score / 100)

    st.write(
        f"Predicted Score: **{display_score:.2f}%**"
    )

    # ======================================
    # 10. MOTIVATIONAL MESSAGE
    # ======================================

    st.success("💡 " + motivation)

    # ======================================
    # 11. STUDENT PROFILE SUMMARY
    # ======================================

    st.subheader("📋 Student Profile Summary")

    result_col1, result_col2 = st.columns(2)

    with result_col1:

        st.write("👤 **Gender:**", gender)

        st.write("🌍 **Group:**", race)

        st.write(
            "🎓 **Parent Education:**",
            parent_education
        )

    with result_col2:

        st.write("🍱 **Lunch:**", lunch)

        st.write(
            "📚 **Test Preparation:**",
            test_preparation
        )

    st.divider()

    st.info(
        "🤖 This prediction is an estimated result generated "
        "by a Machine Learning model. It is not an actual "
        "examination result."
    )

    st.caption(
        "Made with ❤️ using Python, Pandas, Machine Learning & Streamlit"
    )


# ==========================================
# 12. FOOTER
# ==========================================

st.markdown("""
<div style="text-align:center; color:#aeb8e8; padding:20px;">
🎓 STUDENT REPORT CARD LAB
<br>
Powered by Machine Learning 🤖
<br>
Keep learning. Keep growing. Keep winning! 🚀
</div>
""", unsafe_allow_html=True)
