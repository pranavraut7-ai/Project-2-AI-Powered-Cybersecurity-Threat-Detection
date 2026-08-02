"""
==========================================================
Detection Pipeline
----------------------------------------------------------
Project : AI-Powered Cybersecurity Threat Detection System

Description:
    Executes the complete threat detection workflow.
==========================================================
"""

import pandas as pd

from src.detection.predictor import ThreatPredictor
from src.detection.severity import ThreatSeverity
from src.detection.alert_generator import AlertGenerator
from src.utils.logger import get_logger

logger = get_logger(__name__)


class DetectionPipeline:

    def __init__(self):

        self.predictor = ThreatPredictor()
        self.severity = ThreatSeverity()
        self.alert_generator = AlertGenerator()

    def run(
        self,
        dataframe: pd.DataFrame,
    ):

        logger.info("=" * 60)
        logger.info("Starting Detection Pipeline")
        logger.info("=" * 60)

        predictions = self.predictor.predict(
            dataframe
        )

        severity = self.severity.classify(
            predictions
        )

        alerts = self.alert_generator.generate(
            predictions,
            severity,
        )

        logger.info("=" * 60)
        logger.info("Detection Pipeline Completed Successfully")
        logger.info("=" * 60)

        return (
            predictions,
            severity,
            alerts,
        )