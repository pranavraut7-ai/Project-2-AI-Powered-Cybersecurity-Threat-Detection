"""
==========================================================
Feature Engineering Module
----------------------------------------------------------
Project : AI-Powered Cybersecurity Threat Detection System
Description:
    Converts cleaned data into ML-ready datasets by
    encoding labels, scaling features, splitting data,
    and saving preprocessing artifacts.
==========================================================
"""

from pathlib import Path

import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from src.utils.logger import get_logger

logger = get_logger(__name__)


class FeatureEngineer:

    def __init__(
        self,
        model_path: str = "models"
    ):

        self.model_path = Path(model_path)
        self.model_path.mkdir(
            parents=True,
            exist_ok=True
        )

    def separate_features_and_target(
        self,
        dataframe: pd.DataFrame
    ):

        if "Label" not in dataframe.columns:
            raise ValueError(
                "Target column 'Label' not found."
            )

        X = dataframe.drop(
            columns=["Label"]
        )

        y = dataframe["Label"]

        logger.info(
            "Features and target separated."
        )

        return X, y

    def encode_target(self, y):

        encoder = LabelEncoder()

        y_encoded = encoder.fit_transform(y)

        joblib.dump(
            encoder,
            self.model_path / "label_encoder.pkl"
        )

        logger.info(
            "Label encoder saved."
        )

        return y_encoded

    def scale_features(self, X):

        scaler = StandardScaler()

        X_scaled = scaler.fit_transform(X)

        joblib.dump(
            scaler,
            self.model_path / "scaler.pkl"
        )

        logger.info(
            "Feature scaler saved."
        )

        return X_scaled

    def split_dataset(
        self,
        X,
        y
    ):

        return train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
            stratify=y
        )

    def process(
        self,
        dataframe: pd.DataFrame
    ):

        logger.info("=" * 60)
        logger.info("Starting Feature Engineering")
        logger.info("=" * 60)

        X, y = self.separate_features_and_target(
            dataframe
        )

        y = self.encode_target(y)

        X = self.scale_features(X)

        (
            X_train,
            X_test,
            y_train,
            y_test
        ) = self.split_dataset(
            X,
            y
        )

        logger.info(
            "Training samples : %d",
            len(X_train)
        )

        logger.info(
            "Testing samples : %d",
            len(X_test)
        )

        logger.info("=" * 60)

        return (
            X_train,
            X_test,
            y_train,
            y_test
        )