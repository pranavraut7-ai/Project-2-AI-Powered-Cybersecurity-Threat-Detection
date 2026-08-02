"""
==========================================================
Training Application
----------------------------------------------------------
Project : AI-Powered Cybersecurity Threat Detection System

Description:
    Executes the complete training workflow.
==========================================================
"""

from src.preprocessing.pipeline import PreprocessingPipeline
from src.training.pipeline import TrainingPipeline
from src.utils.logger import get_logger

logger = get_logger(__name__)


def main():

    logger.info("=" * 70)
    logger.info("MODEL TRAINING STARTED")
    logger.info("=" * 70)

    preprocessing = PreprocessingPipeline()

    (
        X_train,
        X_test,
        y_train,
        y_test,
    ) = preprocessing.run()

    training = TrainingPipeline()

    (
        comparison,
        best_model_name,
        best_model,
    ) = training.run(
        X_train,
        X_test,
        y_train,
        y_test,
    )

    logger.info("=" * 70)
    logger.info("TRAINING COMPLETED")
    logger.info("Best Model : %s", best_model_name)
    logger.info("=" * 70)


if __name__ == "__main__":
    main()