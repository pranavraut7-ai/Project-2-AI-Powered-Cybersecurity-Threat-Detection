"""
==========================================================
Logging Utility
----------------------------------------------------------
Project : AI-Powered Cybersecurity Threat Detection System
Description:
    Provides a centralized logger for all project modules.
==========================================================
"""

import logging
import sys


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a configured logger instance.

    Parameters
    ----------
    name : str
        Name of the module requesting the logger.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(levelname)s] %(message)s"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    logger.propagate = False

    return logger