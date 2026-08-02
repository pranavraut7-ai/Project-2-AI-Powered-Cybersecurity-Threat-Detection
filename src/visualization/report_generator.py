"""
==========================================================
Report Generator
----------------------------------------------------------
Project : AI-Powered Cybersecurity Threat Detection System

Description:
    Generates project, model, and detection reports.
==========================================================
"""

from pathlib import Path
from datetime import datetime

import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


class ReportGenerator:

    def __init__(
        self,
        report_directory: str = "outputs/reports",
    ):

        self.report_directory = Path(report_directory)

        self.report_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    # ======================================================
    # Internal Helper
    # ======================================================

    def _write_report(
        self,
        filename: str,
        content: str,
    ):

        report_path = self.report_directory / filename

        with open(
            report_path,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(content)

        logger.info(
            "Generated report -> %s",
            report_path,
        )

    # ======================================================
    # Project Summary
    # ======================================================

    def generate_project_summary(self):

        content = f"""
==================================================
AI-Powered Cybersecurity Threat Detection System
==================================================

Generated:
{datetime.now()}

Modules
-------
✔ Data Loading
✔ Data Cleaning
✔ Feature Engineering
✔ Model Training
✔ Model Evaluation
✔ Threat Prediction
✔ Severity Assessment
✔ Alert Generation
✔ Visualization

Dataset
-------
CICIDS2017

Status
------
Project pipeline executed successfully.
"""

        self._write_report(
            "project_summary.txt",
            content,
        )

    # ======================================================
    # Model Summary
    # ======================================================

    def generate_model_summary(
        self,
        comparison_csv="outputs/reports/model_comparison.csv",
    ):

        comparison_csv = Path(comparison_csv)

        if not comparison_csv.exists():

            logger.warning(
                "Model comparison CSV not found."
            )

            return

        dataframe = pd.read_csv(comparison_csv)

        best_model = dataframe.sort_values(
            "F1 Score",
            ascending=False,
        ).iloc[0]

        content = f"""
==================================================
Model Performance Summary
==================================================

Generated:
{datetime.now()}

Best Model
----------

{best_model['Model']}

Accuracy
--------

{best_model['Accuracy']:.4f}

Precision
---------

{best_model['Precision']:.4f}

Recall
------

{best_model['Recall']:.4f}

Weighted F1 Score
-----------------

{best_model['F1 Score']:.4f}
"""

        self._write_report(
            "model_summary.txt",
            content,
        )

    # ======================================================
    # Detection Summary
    # ======================================================

    def generate_detection_summary(
        self,
        alerts_csv="outputs/predictions/prediction_log.csv",
    ):

        alerts_csv = Path(alerts_csv)

        if not alerts_csv.exists():

            logger.warning(
                "Prediction log not found."
            )

            return

        alerts = pd.read_csv(alerts_csv)

        total_alerts = len(alerts)

        threat_counts = (
            alerts["prediction"]
            .value_counts()
        )

        severity_counts = (
            alerts["severity"]
            .value_counts()
        )

        content = f"""
==================================================
Detection Summary
==================================================

Generated:
{datetime.now()}

Total Alerts
------------

{total_alerts}

Threat Distribution
-------------------

{threat_counts.to_string()}

Severity Distribution
---------------------

{severity_counts.to_string()}

Average Risk Score
------------------

{alerts['risk_score'].mean():.2f}
"""

        self._write_report(
            "detection_summary.txt",
            content,
        )

    # ======================================================
    # Generate All Reports
    # ======================================================

    def generate_all_reports(self):

        logger.info(
            "Generating project reports..."
        )

        self.generate_project_summary()

        self.generate_model_summary()

        self.generate_detection_summary()

        logger.info(
            "All reports generated successfully."
        )