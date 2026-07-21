import os
import joblib
import pandas as pd
import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Early Academic Support System",
    page_icon="🎓",
    layout="wide"
)
st.markdown("""
<style>

[data-testid="stMetric"]{
    background-color:#0D47A1;
    border-radius:12px;
    padding:20px;
    border:2px solid #1976D2;
    box-shadow:0px 4px 10px rgba(0,0,0,0.3);
}

[data-testid="stMetricLabel"]{
    color:white !important;
    font-size:18px;
    font-weight:bold;
}

[data-testid="stMetricValue"]{
    color:white !important;
    font-size:40px !important;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.main{
    background-color:#F5F9FF;
}

h1{
    color:#1565C0;
    text-align:center;
}

h3{
    color:#0D47A1;
}

.stButton>button{
    width:100%;
    height:55px;
    background:#1976D2;
    color:white;
    font-size:18px;
    border-radius:10px;
    border:none;
}

.stMetric{
    border-radius:10px;
    padding:10px;
    background:#E3F2FD;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# LOAD MODEL
# =====================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "student_risk_model.pkl"
)

model = joblib.load(MODEL_PATH)

# =====================================
# HEADER
# =====================================

st.title("🎓 Early Academic Support System")

st.markdown(
"""
### AI-Based Student Academic Risk Prediction

This application predicts whether a student may require
additional academic support based on academic information.
"""
)

st.markdown("---")

st.subheader("📋 Student Information")



# =====================================
# INPUT FORM
# =====================================

col1, col2 = st.columns(2)

with col1:

    school_display = st.selectbox(
        "🏫 School",
        [
            "Gabriel Pereira (GP)",
            "Mousinho da Silveira (MS)"
        ],
        key="school"
    )

    gender_display = st.selectbox(
        "👤 Gender",
        [
            "Female",
            "Male"
        ],
        key="gender"
    )

    age = st.number_input(
        "🎂 Age",
        min_value=15,
        max_value=22,
        value=17,
        key="age"
    )

    Medu = st.slider(
        "👩 Mother's Education",
        0,
        4,
        2,
        key="Medu"
    )

    Fedu = st.slider(
        "👨 Father's Education",
        0,
        4,
        2,
        key="Fedu"
    )

    schoolsup_display = st.selectbox(
        "🏫 School Support",
        [
            "Yes",
            "No"
        ],
        key="schoolsup"
    )

    higher_display = st.selectbox(
        "🎓 Plans for Higher Education",
        [
            "Yes",
            "No"
        ],
        key="higher"
    )

with col2:

    address_display = st.selectbox(
        "📍 Address",
        [
            "Urban",
            "Rural"
        ],
        key="address"
    )

    studytime = st.slider(
        "📚 Study Time",
        1,
        4,
        2,
        key="studytime"
    )

    failures = st.slider(
        "❌ Previous Failures",
        0,
        3,
        0,
        key="failures"
    )

    famsup_display = st.selectbox(
        "👨‍👩‍👧 Family Support",
        [
            "Yes",
            "No"
        ],
        key="famsup"
    )

    absences = st.number_input(
        "📅 Absences",
        min_value=0,
        max_value=100,
        value=5,
        key="absences"
    )

    G1 = st.slider(
        "📝 First Grade (G1)",
        0,
        20,
        10,
        key="G1"
    )

    G2 = st.slider(
        "📝 Second Grade (G2)",
        0,
        20,
        10,
        key="G2"
    )


    # =====================================
# PREDICT BUTTON
# =====================================

if st.button("🔍 Predict Academic Risk", key="predict_btn"):

    # Convert display values to model values

    school = "GP" if "Gabriel" in school_display else "MS"

    sex = "F" if gender_display == "Female" else "M"

    address = "U" if address_display == "Urban" else "R"

    schoolsup = schoolsup_display.lower()

    famsup = famsup_display.lower()

    higher = higher_display.lower()

    # Create dataframe

    input_data = pd.DataFrame({

        "school": [school],
        "sex": [sex],
        "age": [age],
        "address": [address],

        "Medu": [Medu],
        "Fedu": [Fedu],

        "studytime": [studytime],
        "failures": [failures],

        "schoolsup": [schoolsup],
        "famsup": [famsup],
        "higher": [higher],

        "absences": [absences],

        "G1": [G1],
        "G2": [G2]

    })

    # Prediction

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

#if st.button("🔍 Predict Academic Risk", key="predict_academic_risk"):

    school = "GP" if "Gabriel" in school_display else "MS"
    sex = "F" if gender_display == "Female" else "M"
    address = "U" if address_display == "Urban" else "R"

    schoolsup = schoolsup_display.lower()
    famsup = famsup_display.lower()
    higher = higher_display.lower()

    input_data = pd.DataFrame({
        "school":[school],
        "sex":[sex],
        "age":[age],
        "address":[address],
        "Medu":[Medu],
        "Fedu":[Fedu],
        "studytime":[studytime],
        "failures":[failures],
        "schoolsup":[schoolsup],
        "famsup":[famsup],
        "higher":[higher],
        "absences":[absences],
        "G1":[G1],
        "G2":[G2]
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]


    st.markdown(f"""
    <div style="
    background-color:#0B3D91;
    padding:20px;
    border-radius:12px;
    text-align:center;
    margin-bottom:20px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.3);
    ">
    <h3 style="color:white;margin:0;">Risk Probability</h3>
    <h1 style="color:white;margin-top:10px;">{probability:.1%}</h1>
    </div>
    """, unsafe_allow_html=True)


    st.progress(float(probability))


    if prediction == 1:

        st.error("⚠️ Student may need academic support.")

        st.info("""
### 📌 Recommended Actions

✅ Meet with the student

✅ Review attendance

✅ Provide additional academic support

✅ Monitor academic performance

✅ Involve teachers and parents if necessary
""")

    else:

        st.success("✅ Student is currently not identified as high risk.")
        st.balloons()


# ==============================
# FOOTER
# ==============================

st.markdown("---")

st.info(
    "ℹ️ This system is a decision-support tool. Final decisions should always involve teachers or counselors."
)

st.caption(
    "🎓 Developed by Mizba | Early Academic Support System | Machine Learning Project"
)