"""
==========================================================
Visualization Engine
----------------------------------------------------------
Project : AI-Powered Cybersecurity Threat Detection System

Description:
    Generates visualizations for:

    • Model Comparison
    • Confusion Matrix
    • Feature Importance
    • Threat Distribution
    • Severity Distribution
    • Risk Score Distribution
    • Alert Timeline
==========================================================
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay

from src.utils.logger import get_logger

logger = get_logger(__name__)


class VisualizationEngine:
    """
    Generates and saves project visualizations.
    """

    def __init__(
        self,
        output_directory: str = "outputs/visualizations",
    ):

        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    # ======================================================
    # Internal Helper
    # ======================================================

    def _save_figure(self, filename: str):

        plt.tight_layout()

        output_path = self.output_directory / filename

        plt.savefig(
            output_path,
            dpi=300,
            bbox_inches="tight",
        )

        plt.close()

        logger.info(
            "Saved visualization -> %s",
            output_path,
        )

    # ======================================================
    # Model Comparison
    # ======================================================

    def plot_model_comparison(
        self,
        comparison_df: pd.DataFrame,
    ):

        plt.figure(figsize=(9, 5))

        plt.bar(
            comparison_df["Model"],
            comparison_df["F1 Score"],
        )

        plt.title("Model Comparison (Weighted F1 Score)")
        plt.xlabel("Model")
        plt.ylabel("Weighted F1 Score")

        plt.xticks(rotation=20)

        self._save_figure(
            "model_comparison.png"
        )

    # ======================================================
    # Confusion Matrix
    # ======================================================

    def plot_confusion_matrix(
        self,
        model,
        X_test,
        y_test,
    ):

        ConfusionMatrixDisplay.from_estimator(
            model,
            X_test,
            y_test,
            cmap="Blues",
            xticks_rotation=90,
        )

        plt.gcf().set_size_inches(8, 8)

        self._save_figure(
            "confusion_matrix.png"
        )

    # ======================================================
    # Feature Importance
    # ======================================================

    def plot_feature_importance(
        self,
        model,
        feature_names,
        top_n: int = 20,
    ):

        if not hasattr(model, "feature_importances_"):

            logger.warning(
                "Selected model does not support feature importance."
            )

            return

        importance = pd.DataFrame(
            {
                "Feature": feature_names,
                "Importance": model.feature_importances_,
            }
        )

        importance = importance.sort_values(
            by="Importance",
            ascending=False,
        ).head(top_n)

        importance.to_csv(
            self.output_directory /
            "feature_importance.csv",
            index=False,
        )

        plt.figure(figsize=(10, 7))

        plt.barh(
            importance["Feature"],
            importance["Importance"],
        )

        plt.gca().invert_yaxis()

        plt.title("Top Feature Importance")

        self._save_figure(
            "feature_importance.png"
        )

    # ======================================================
    # Threat Distribution
    # ======================================================

    def plot_threat_distribution(
        self,
        alerts_df: pd.DataFrame,
    ):

        counts = alerts_df["prediction"].value_counts()

        plt.figure(figsize=(9, 5))

        plt.bar(
            counts.index,
            counts.values,
        )

        plt.title("Threat Distribution")
        plt.xlabel("Threat Type")
        plt.ylabel("Alert Count")

        plt.xticks(rotation=30)

        self._save_figure(
            "threat_distribution.png"
        )

    # ======================================================
    # Severity Distribution
    # ======================================================

    def plot_severity_distribution(
        self,
        alerts_df: pd.DataFrame,
    ):

        severity_order = [
            "Low",
            "Medium",
            "High",
            "Critical",
        ]

        counts = (
            alerts_df["severity"]
            .value_counts()
            .reindex(
                severity_order,
                fill_value=0,
            )
        )

        plt.figure(figsize=(7, 5))

        plt.bar(
            counts.index,
            counts.values,
        )

        plt.title("Severity Distribution")
        plt.xlabel("Severity")
        plt.ylabel("Number of Alerts")

        self._save_figure(
            "severity_distribution.png"
        )

    # ======================================================
    # Risk Score Distribution
    # ======================================================

    def plot_risk_score_distribution(
        self,
        alerts_df: pd.DataFrame,
    ):

        plt.figure(figsize=(8, 5))

        plt.hist(
            alerts_df["risk_score"],
            bins=10,
        )

        plt.title("Risk Score Distribution")
        plt.xlabel("Risk Score")
        plt.ylabel("Frequency")

        self._save_figure(
            "risk_score_distribution.png"
        )

    # ======================================================
    # Alert Timeline
    # ======================================================

    def plot_alert_timeline(
        self,
        alerts_df: pd.DataFrame,
    ):

        dataframe = alerts_df.copy()

        dataframe["timestamp"] = pd.to_datetime(
            dataframe["timestamp"]
        )

        timeline = (
            dataframe
            .groupby(
                dataframe["timestamp"].dt.floor("min")
            )
            .size()
        )

        plt.figure(figsize=(12, 5))

        plt.plot(
            timeline.index,
            timeline.values,
            marker="o",
        )

        plt.title("Alert Timeline")
        plt.xlabel("Time")
        plt.ylabel("Number of Alerts")

        plt.xticks(rotation=30)

        self._save_figure(
            "alert_timeline.png"
        )

    # ======================================================
    # Generate Every Alert Visualization
    # ======================================================

    def generate_alert_dashboard(
        self,
        alerts_csv: str = "outputs/predictions/prediction_log.csv",
    ):

        alerts_csv = Path(alerts_csv)

        if not alerts_csv.exists():

            logger.warning(
                "Prediction log not found: %s",
                alerts_csv,
            )

            return

        alerts_df = pd.read_csv(alerts_csv)

        logger.info(
            "Generating security visualizations..."
        )

        self.plot_threat_distribution(alerts_df)

        self.plot_severity_distribution(alerts_df)

        self.plot_risk_score_distribution(alerts_df)

        self.plot_alert_timeline(alerts_df)

        logger.info(
            "All security visualizations generated successfully."
        )