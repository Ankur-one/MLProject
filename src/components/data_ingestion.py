import os
import sys
import pandas as pd

from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


@dataclass
class DataIngestionConfig:

    train_data_path: str = os.path.join(
        "artifacts",
        "train.csv"
    )

    test_data_path: str = os.path.join(
        "artifacts",
        "test.csv"
    )

    raw_data_path: str = os.path.join(
        "artifacts",
        "data.csv"
    )


class DataIngestion:

    def __init__(self):

        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        logging.info(
            "Entered the data ingestion method or component"
        )

        try:

            # Read dataset
            df = pd.read_csv(
                os.path.join(
                    "notebook",
                    "data",
                    "stud.csv"
                )
            )

            logging.info(
                "Read the dataset as dataframe"
            )

            # Create artifacts directory
            os.makedirs(
                os.path.dirname(
                    self.ingestion_config.train_data_path
                ),
                exist_ok=True
            )

            # Save raw data
            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )

            logging.info(
                "Raw data saved successfully"
            )

            # Train test split
            logging.info(
                "Train test split initiated"
            )

            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            # Save train data
            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )

            # Save test data
            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )

            logging.info(
                "Ingestion of the data is completed"
            )

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:

            logging.error(
                "Exception occurred during data ingestion"
            )

            raise CustomException(
                e,
                sys
            )


if __name__ == "__main__":

    try:

        # ============================
        # DATA INGESTION
        # ============================

        obj = DataIngestion()

        train_data, test_data = (
            obj.initiate_data_ingestion()
        )

        logging.info(
            "Data ingestion completed successfully"
        )

        # ============================
        # DATA TRANSFORMATION
        # ============================

        data_transformation = DataTransformation()

        train_arr, test_arr, _ = (
            data_transformation.initiate_data_transformation(
                train_data,
                test_data
            )
        )

        logging.info(
            "Data transformation completed successfully"
        )

        # ============================
        # MODEL TRAINING
        # ============================

        model_trainer = ModelTrainer()

        score = (
            model_trainer.initiate_model_trainer(
                train_arr,
                test_arr
            )
        )

        print(
            f"Model Training Result: {score}"
        )

        logging.info(
            "Model training completed successfully"
        )

    except Exception as e:

        logging.error(
            "Pipeline execution failed"
        )

        raise CustomException(
            e,
            sys
        )