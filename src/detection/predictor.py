"""
==========================================================
Prediction Engine
----------------------------------------------------------
Project : AI-Powered Cybersecurity Threat Detection System

Description:
    Loads the trained model and predicts whether
    incoming network traffic is benign or malicious.
==========================================================
"""

from pathlib import Path

import joblib
import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


class ThreatPredictor:

    def __init__(
        self,
        model_directory: str = "models",
    ):

        self.model_directory = Path(model_directory)

        logger.info("=" * 60)
        logger.info("Loading Prediction Engine")
        logger.info("=" * 60)

        self.model = joblib.load(
            self.model_directory / "best_model.pkl"
        )

        self.scaler = joblib.load(
            self.model_directory / "scaler.pkl"
        )

        self.label_encoder = joblib.load(
            self.model_directory / "label_encoder.pkl"
        )

        logger.info("Prediction engine loaded successfully.")

    def predict(
        self,
        dataframe: pd.DataFrame,
    ):

        logger.info("=" * 60)
        logger.info("Starting Prediction")
        logger.info("=" * 60)

        scaled_features = self.scaler.transform(
            dataframe
        )

        encoded_predictions = self.model.predict(
            scaled_features
        )

        predictions = self.label_encoder.inverse_transform(
            encoded_predictions
        )

        logger.info(
            "Prediction completed successfully."
        )

        return predictions