"""
==========================================================
Training Pipeline
----------------------------------------------------------
Project : AI-Powered Cybersecurity Threat Detection System

Description:
    Executes the complete machine learning workflow:
        • Model Training
        • Model Evaluation
        • Best Model Selection
==========================================================
"""

from src.models.trainer import ModelTrainer
from src.models.evaluator import ModelEvaluator
from src.utils.logger import get_logger

logger = get_logger(__name__)


class TrainingPipeline:

    def __init__(self):

        self.trainer = ModelTrainer()
        self.evaluator = ModelEvaluator()

    def run(
        self,
        X_train,
        X_test,
        y_train,
        y_test,
    ):

        logger.info("=" * 60)
        logger.info("Starting Training Pipeline")
        logger.info("=" * 60)

        trained_models = self.trainer.train(
            X_train,
            y_train,
        )

        (
            comparison,
            best_model_name,
            best_model,
        ) = self.evaluator.evaluate(
            trained_models,
            X_test,
            y_test,
        )

        logger.info("=" * 60)
        logger.info("Training Pipeline Completed Successfully")
        logger.info("Best Model : %s", best_model_name)
        logger.info("=" * 60)

        return (
            comparison,
            best_model_name,
            best_model,
        )