"""
==========================================================
Data Cleaner Module
----------------------------------------------------------
Project : AI-Powered Cybersecurity Threat Detection System
Description:
    Cleans the merged CICIDS2017 dataset by removing
    duplicates, handling missing values, replacing
    invalid values, and standardizing column names.
==========================================================
"""

from pathlib import Path

import numpy as np
import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


class DataCleaner:
    """
    Cleans and validates the merged dataset.
    """

    def __init__(
        self,
        processed_data_path: str = "data/processed",
    ) -> None:

        self.processed_data_path = Path(processed_data_path)

    def standardize_columns(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Remove leading/trailing spaces from column names.
        """

        dataframe.columns = dataframe.columns.str.strip()

        logger.info("Column names standardized.")

        return dataframe

    def remove_duplicates(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        before = len(dataframe)

        dataframe = dataframe.drop_duplicates()

        removed = before - len(dataframe)

        logger.info(
            "Duplicate rows removed: %d",
            removed,
        )

        return dataframe

    def replace_infinite_values(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        dataframe = dataframe.replace(
            [np.inf, -np.inf],
            np.nan,
        )

        logger.info(
            "Infinite values replaced with NaN."
        )

        return dataframe

    def handle_missing_values(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        before = len(dataframe)

        dataframe = dataframe.dropna()

        removed = before - len(dataframe)

        logger.info(
            "Rows removed due to missing values: %d",
            removed,
        )

        return dataframe

    def reset_dataframe(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        dataframe = dataframe.reset_index(drop=True)

        logger.info("Index reset.")

        return dataframe

    def save_dataset(
        self,
        dataframe: pd.DataFrame,
        filename: str = "cleaned_cicids2017.csv",
    ) -> Path:

        self.processed_data_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path = self.processed_data_path / filename

        dataframe.to_csv(
            output_path,
            index=False,
        )

        logger.info(
            "Cleaned dataset saved to %s",
            output_path,
        )

        return output_path

    def clean(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        logger.info("=" * 60)
        logger.info("Starting Data Cleaning")
        logger.info("=" * 60)

        dataframe = self.standardize_columns(
            dataframe
        )

        dataframe = self.remove_duplicates(
            dataframe
        )

        dataframe = self.replace_infinite_values(
            dataframe
        )

        dataframe = self.handle_missing_values(
            dataframe
        )

        dataframe = self.reset_dataframe(
            dataframe
        )

        self.save_dataset(
            dataframe
        )

        logger.info(
            "Cleaning completed successfully."
        )

        logger.info(
            "Final dataset shape: %s",
            dataframe.shape,
        )

        logger.info("=" * 60)

        return dataframe