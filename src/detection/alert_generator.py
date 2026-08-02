"""
==========================================================
Alert Generator
----------------------------------------------------------
Project : AI-Powered Cybersecurity Threat Detection System

Description:
    Generates security alerts based on
    predicted threats and severity levels.
==========================================================
"""

from datetime import datetime
from pathlib import Path

import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


class AlertGenerator:

    def __init__(
        self,
        output_directory: str = "outputs/predictions",
    ):

        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def generate(
        self,
        predictions,
        severity,
    ):

        logger.info("=" * 60)
        logger.info("Generating Security Alerts")
        logger.info("=" * 60)

        alerts = []

        for attack, level in zip(
            predictions,
            severity,
        ):

            alerts.append(
                {
                    "Timestamp": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                    "Prediction": attack,
                    "Severity": level,
                }
            )

        alert_dataframe = pd.DataFrame(
            alerts
        )

        output_file = (
            self.output_directory
            / "security_alerts.csv"
        )

        alert_dataframe.to_csv(
            output_file,
            index=False,
        )

        logger.info(
            "Security alerts generated successfully."
        )

        logger.info(
            "Location : %s",
            output_file,
        )

        return alert_dataframe