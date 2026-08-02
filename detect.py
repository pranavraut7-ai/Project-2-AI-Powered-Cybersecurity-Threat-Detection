"""
==========================================================
Threat Detection Application
----------------------------------------------------------
Project : AI-Powered Cybersecurity Threat Detection System

Description:
    Loads the trained model and performs
    threat detection on processed network data.
==========================================================
"""

from pathlib import Path

import pandas as pd

from src.detection.pipeline import DetectionPipeline
from src.utils.logger import get_logger

logger = get_logger(__name__)


def main():

    logger.info("=" * 70)
    logger.info("THREAT DETECTION STARTED")
    logger.info("=" * 70)

    dataset_path = Path(
        "data/processed/X_test.csv"
    )

    if not dataset_path.exists():

        logger.error(
            "Processed dataset not found."
        )

        logger.error(
            "Run train.py first."
        )

        return

    dataframe = pd.read_csv(
        dataset_path
    ).head(10)

    detection = DetectionPipeline()

    (
        predictions,
        severity,
        alerts,
    ) = detection.run(
        dataframe
    )

    logger.info("=" * 70)
    logger.info("Prediction Results")
    logger.info("=" * 70)

    for attack, level in zip(
        predictions,
        severity,
    ):

        logger.info(
            "%-30s  %s",
            attack,
            level,
        )

    logger.info("=" * 70)
    logger.info("THREAT DETECTION COMPLETED")
    logger.info("=" * 70)


if __name__ == "__main__":
    main()