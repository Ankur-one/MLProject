import os
import sys

import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.utils import load_object


class PredictPipeline:

    def __init__(self):

        self.model_path = os.path.join(
            "artifacts",
            "model.pkl"
        )

        self.preprocessor_path = os.path.join(
            "artifacts",
            "preprocessor.pkl"
        )

    def predict(self, features):

        try:

            logging.info(
                "Loading preprocessor and model"
            )

            preprocessor = load_object(
                self.preprocessor_path
            )

            model = load_object(
                self.model_path
            )

            logging.info(
                "Preprocessor and model loaded successfully"
            )

            # Transform input data
            data_scaled = preprocessor.transform(
                features
            )

            # Prediction
            prediction = model.predict(
                data_scaled
            )

            return prediction

        except Exception as e:

            logging.error(
                "Exception occurred during prediction"
            )

            raise CustomException(
                e,
                sys
            )


class CustomData:

    def __init__(
        self,
        gender,
        race_ethnicity,
        parental_level_of_education,
        lunch,
        test_preparation_course,
        reading_score,
        writing_score
    ):

        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = (
            parental_level_of_education
        )
        self.lunch = lunch
        self.test_preparation_course = (
            test_preparation_course
        )
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_dataframe(self):

        try:

            custom_data_input_dict = {

                "gender": [
                    self.gender
                ],

                "race_ethnicity": [
                    self.race_ethnicity
                ],

                "parental_level_of_education": [
                    self.parental_level_of_education
                ],

                "lunch": [
                    self.lunch
                ],

                "test_preparation_course": [
                    self.test_preparation_course
                ],

                "reading_score": [
                    self.reading_score
                ],

                "writing_score": [
                    self.writing_score
                ]
            }

            return pd.DataFrame(
                custom_data_input_dict
            )

        except Exception as e:

            logging.error(
                "Exception occurred while creating "
                "prediction dataframe"
            )

            raise CustomException(
                e,
                sys
            )