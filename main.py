from src.cancerClassification import logger
from src.cancerClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cancerClassification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cancerClassification.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from src.cancerClassification.pipeline.stage_04_model_evaluation import EvaluationPipeline
import os


os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Sohail1173/End-to-End-with-mlflow-dvc.mlflow "
os.environ["MLFLOW_TRACKING_USERNAME"]="Sohail1173"
os.environ["MLFLOW_TRACKING_PASSWORD"]="456ac5abdd3e02452a4de39d5f900553bf0c93e8"

STAGE_NAME="Data  Ingestion Stage"

try:
        logger.info(f">>>>>>>>>>>>>>stage{STAGE_NAME} started <<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>> stage{STAGE_NAME} completed <<<<<<\n\n============x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME="Prepare base model"



try:
        logger.info(f">>>>>>>>>>>>>>stage{STAGE_NAME} started <<<<<<")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>> stage{STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME="Model Trainer"


try:
        logger.info(f">>>>>>>>>>>>>>stage{STAGE_NAME} started <<<<<<")
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>> stage{STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME="Model Evaluation"


try:
        logger.info(f">>>>>>>>>>>>>>stage{STAGE_NAME} started <<<<<<")
        obj=EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>> stage{STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e