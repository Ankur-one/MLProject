import os
import sys
import pickle

from src.exception import CustomException
from src.logger import logging

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)


def save_object(file_path, obj):

    try:

        logging.info(
            f"Entered save_object method with file path: {file_path}"
        )

        file_dir = os.path.dirname(file_path)

        if file_dir:
            os.makedirs(
                file_dir,
                exist_ok=True
            )

        with open(
            file_path,
            "wb"
        ) as file_obj:

            pickle.dump(
                obj,
                file_obj
            )

        logging.info(
            f"Object saved successfully at: {file_path}"
        )

    except Exception as e:

        logging.error(
            "Exception occurred while saving object"
        )

        raise CustomException(
            e,
            sys
        )


def load_object(file_path):

    try:

        logging.info(
            f"Loading object from: {file_path}"
        )

        with open(
            file_path,
            "rb"
        ) as file_obj:

            obj = pickle.load(
                file_obj
            )

        logging.info(
            "Object loaded successfully"
        )

        return obj

    except Exception as e:

        logging.error(
            "Exception occurred while loading object"
        )

        raise CustomException(
            e,
            sys
        )


def evaluate_models(
    X_train,
    y_train,
    X_test,
    y_test,
    models,
    param
):

    try:

        report = {}

        for model_name, model in models.items():

            logging.info(
                f"Training model: {model_name}"
            )

            # Get hyperparameters for current model
            model_params = param.get(
                model_name,
                {}
            )

            # Apply parameters if available
            if model_params:

                from sklearn.model_selection import GridSearchCV

                gs = GridSearchCV(
                    estimator=model,
                    param_grid=model_params,
                    cv=3,
                    n_jobs=-1,
                    scoring="r2"
                )

                gs.fit(
                    X_train,
                    y_train
                )

                model = gs.best_estimator_

                logging.info(
                    f"Best parameters for {model_name}: "
                    f"{gs.best_params_}"
                )

            else:

                model.fit(
                    X_train,
                    y_train
                )

            # Predictions
            y_train_pred = model.predict(
                X_train
            )

            y_test_pred = model.predict(
                X_test
            )

            # R2 score
            train_model_score = r2_score(
                y_train,
                y_train_pred
            )

            test_model_score = r2_score(
                y_test,
                y_test_pred
            )

            # MAE
            test_mae = mean_absolute_error(
                y_test,
                y_test_pred
            )

            # RMSE
            test_rmse = mean_squared_error(
                y_test,
                y_test_pred
            ) ** 0.5

            logging.info(
                f"{model_name} | "
                f"Train R2: {train_model_score:.4f} | "
                f"Test R2: {test_model_score:.4f}"
            )

            print(
                f"\n{'=' * 50}"
            )

            print(
                f"Model: {model_name}"
            )

            print(
                f"Train R2 Score : {train_model_score:.4f}"
            )

            print(
                f"Test R2 Score  : {test_model_score:.4f}"
            )

            print(
                f"Test MAE       : {test_mae:.4f}"
            )

            print(
                f"Test RMSE      : {test_rmse:.4f}"
            )

            print(
                f"{'=' * 50}"
            )

            report[
                model_name
            ] = test_model_score

        return report

    except Exception as e:

        logging.error(
            "Exception occurred during model evaluation"
        )

        raise CustomException(
            e,
            sys
        )