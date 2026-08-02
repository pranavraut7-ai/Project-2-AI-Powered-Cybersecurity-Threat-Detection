"""
==========================================================
Dataset Loader Module
----------------------------------------------------------
Project : AI-Powered Cybersecurity Threat Detection System
Author  : Pranav
Description:
    Loads, validates, and merges CICIDS2017 dataset files.
==========================================================
"""

from pathlib import Path

import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


class DatasetLoader:
    """
    Loads and validates all CICIDS2017 dataset files.
    """

    def __init__(
        self,
        raw_data_path: str = "data/raw",
        processed_data_path: str = "data/processed",
    ) -> None:
        self.raw_data_path = Path(raw_data_path)
        self.processed_data_path = Path(processed_data_path)

    def validate_directory(self) -> None:
        """
        Validate that the raw dataset directory exists.
        """

        logger.info("Validating dataset directory...")

        if not self.raw_data_path.exists():
            logger.error("Raw dataset directory does not exist.")
            raise FileNotFoundError(
                f"Directory not found: {self.raw_data_path}"
            )

        logger.info("Dataset directory found.")

    def get_csv_files(self) -> list[Path]:
        """
        Retrieve all CSV files from the dataset directory.
        """

        csv_files = sorted(self.raw_data_path.glob("*.csv"))

        if not csv_files:
            logger.error("No CSV files found.")
            raise FileNotFoundError(
                "No CSV files were found inside data/raw."
            )

        logger.info("Discovered %d dataset file(s).", len(csv_files))

        return csv_files

    def load_single_file(self, file_path: Path) -> pd.DataFrame:
        """
        Load one CSV dataset.
        """

        logger.info("Loading %s", file_path.name)

        dataframe = pd.read_csv(file_path)

        logger.info(
            "%s loaded successfully | Shape: %s",
            file_path.name,
            dataframe.shape,
        )

        return dataframe

    def merge_datasets(self) -> pd.DataFrame:
        """
        Merge all CSV files into one DataFrame.
        """

        self.validate_directory()

        csv_files = self.get_csv_files()

        dataframe_list = []

        for csv_file in csv_files:
            dataframe = self.load_single_file(csv_file)
            dataframe_list.append(dataframe)

        logger.info("Merging all datasets...")

        merged_dataframe = pd.concat(
            dataframe_list,
            ignore_index=True,
        )

        logger.info(
            "Merged dataset shape: %s",
            merged_dataframe.shape,
        )

        return merged_dataframe

    def save_processed_dataset(
        self,
        dataframe: pd.DataFrame,
        filename: str = "merged_cicids2017.csv",
    ) -> Path:
        """
        Save merged dataset.
        """

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
            "Merged dataset saved successfully."
        )

        logger.info(
            "Location: %s",
            output_path,
        )

        return output_path

    def load(self) -> pd.DataFrame:
        """
        Execute complete dataset loading pipeline.
        """

        logger.info("=" * 60)
        logger.info("Starting Dataset Loading Pipeline")
        logger.info("=" * 60)

        merged_dataframe = self.merge_datasets()

        self.save_processed_dataset(
            merged_dataframe
        )

        logger.info(
            "Dataset loading completed successfully."
        )

        logger.info(
            "Rows    : %d",
            merged_dataframe.shape[0],
        )

        logger.info(
            "Columns : %d",
            merged_dataframe.shape[1],
        )

        logger.info("=" * 60)

        return merged_dataframe