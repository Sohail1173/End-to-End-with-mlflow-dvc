from src.cancerClassification import logger
from src.cancerClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cancerClassification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cancerClassification.pipeline.stage_03_model_trainer import ModelTrainingPipeline

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