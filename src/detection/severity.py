"""
==========================================================
Threat Severity Engine
----------------------------------------------------------
Project : AI-Powered Cybersecurity Threat Detection System

Description:
    Assigns a severity level to every predicted attack.
==========================================================
"""

from src.utils.logger import get_logger

logger = get_logger(__name__)


class ThreatSeverity:

    def __init__(self):

        self.severity_map = {

            "BENIGN": "Low",

            "PortScan": "Medium",

            "Bot": "High",

            "FTP-Patator": "High",
            "SSH-Patator": "High",

            "DoS Hulk": "Critical",
            "DoS GoldenEye": "Critical",
            "DoS slowloris": "Critical",
            "DoS Slowhttptest": "Critical",

            "DDoS": "Critical",

            "Heartbleed": "Critical",

            "Web Attack – Brute Force": "High",
            "Web Attack – Sql Injection": "Critical",
            "Web Attack – XSS": "High",

            "Infiltration": "Critical",
        }

    def classify(
        self,
        predictions,
    ):

        logger.info("=" * 60)
        logger.info("Assigning Threat Severity")
        logger.info("=" * 60)

        severity = []

        for attack in predictions:

            severity.append(
                self.severity_map.get(
                    attack,
                    "Unknown",
                )
            )

        logger.info(
            "Threat severity assigned successfully."
        )

        return severity