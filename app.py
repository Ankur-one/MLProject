import streamlit as st  # type: ignore[reportMissingImports]

from src.pipeline.predict_pipeline import (
    CustomData,
    PredictPipeline
)


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)


# ==========================================
# TITLE
# ==========================================

st.title("🎓 Student Performance Prediction")

st.write(
    "Enter the student's information below "
    "to predict the Mathematics score."
)


# ==========================================
# INPUT FORM
# ==========================================

with st.form("student_prediction_form"):

    st.subheader("Student Information")

    gender = st.selectbox(
        "Gender",
        [
            "male",
            "female"
        ]
    )

    race_ethnicity = st.selectbox(
        "Race/Ethnicity",
        [
            "group A",
            "group B",
            "group C",
            "group D",
            "group E"
        ]
    )

    parental_level_of_education = st.selectbox(
        "Parental Level of Education",
        [
            "some high school",
            "high school",
            "some college",
            "associate's degree",
            "bachelor's degree",
            "master's degree"
        ]
    )

    lunch = st.selectbox(
        "Lunch",
        [
            "standard",
            "free/reduced"
        ]
    )

    test_preparation_course = st.selectbox(
        "Test Preparation Course",
        [
            "none",
            "completed"
        ]
    )

    reading_score = st.number_input(
        "Reading Score",
        min_value=0,
        max_value=100,
        value=70,
        step=1
    )

    writing_score = st.number_input(
        "Writing Score",
        min_value=0,
        max_value=100,
        value=70,
        step=1
    )

    submit = st.form_submit_button(
        "Predict Math Score"
    )


# ==========================================
# PREDICTION
# ==========================================

if submit:

    try:

        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=(
                parental_level_of_education
            ),
            lunch=lunch,
            test_preparation_course=(
                test_preparation_course
            ),
            reading_score=reading_score,
            writing_score=writing_score
        )

        input_df = (
            data.get_data_as_dataframe()
        )

        st.subheader("Input Data")

        st.dataframe(
            input_df,
            use_container_width=True
        )

        pipeline = PredictPipeline()

        prediction = pipeline.predict(
            input_df
        )

        predicted_score = float(
            prediction[0]
        )

        st.success(
            f"🎯 Predicted Math Score: "
            f"{predicted_score:.2f}"
        )

    except Exception as e:

        st.error(
            f"Prediction failed: {e}"
        )