"""
==========================================================
Preprocessing Pipeline
----------------------------------------------------------
Project : AI-Powered Cybersecurity Threat Detection System

Description:
    Executes the complete preprocessing workflow
    and saves processed datasets.
==========================================================
"""

from pathlib import Path

import pandas as pd

from src.preprocessing.loader import DatasetLoader
from src.preprocessing.cleaner import DataCleaner
from src.preprocessing.feature_engineering import FeatureEngineer
from src.utils.logger import get_logger

logger = get_logger(__name__)


class PreprocessingPipeline:

    def __init__(self):

        self.loader = DatasetLoader()
        self.cleaner = DataCleaner()
        self.engineer = FeatureEngineer()

        self.output_directory = Path(
            "data/processed"
        )

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def run(self):

        logger.info("=" * 60)
        logger.info("Starting Complete Preprocessing Pipeline")
        logger.info("=" * 60)

        dataframe = self.loader.load()

        dataframe = self.cleaner.clean(
            dataframe
        )

        (
            X_train,
            X_test,
            y_train,
            y_test,
        ) = self.engineer.process(
            dataframe
        )

        pd.DataFrame(
            X_train
        ).to_csv(
            self.output_directory /
            "X_train.csv",
            index=False,
        )

        pd.DataFrame(
            X_test
        ).to_csv(
            self.output_directory /
            "X_test.csv",
            index=False,
        )

        pd.DataFrame(
            y_train
        ).to_csv(
            self.output_directory /
            "y_train.csv",
            index=False,
        )

        pd.DataFrame(
            y_test
        ).to_csv(
            self.output_directory /
            "y_test.csv",
            index=False,
        )

        logger.info(
            "Processed datasets saved successfully."
        )

        logger.info("=" * 60)
        logger.info("Preprocessing Pipeline Completed")
        logger.info("=" * 60)

        return (
            X_train,
            X_test,
            y_train,
            y_test,
        )