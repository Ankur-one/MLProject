from src.pipeline.predict_pipeline import (
    CustomData,
    PredictPipeline
)


data = CustomData(
    gender="female",
    race_ethnicity="group B",
    parental_level_of_education="bachelor's degree",
    lunch="standard",
    test_preparation_course="none",
    reading_score=72,
    writing_score=74
)


input_data = data.get_data_as_dataframe()

print("\nInput Data:")
print(input_data)


pipeline = PredictPipeline()

prediction = pipeline.predict(
    input_data
)

print("\nPredicted Math Score:")
print(prediction[0])