from src.cancerClassification import logger
from src.cancerClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data  Ingestion Stage"

try:
        logger.info(f">>>>>>>>>>>>>>stage{STAGE_NAME} started <<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>> stage{STAGE_NAME} completed <<<<<<\n\n============x")
except Exception as e:
        logger.exception(e)
        raise e