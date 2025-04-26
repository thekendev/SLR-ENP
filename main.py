from src.trendline.logging import logger
from src.trendline.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>>> Stage: {STAGE_NAME} has started <<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>> Stage: {STAGE_NAME} has been completed <<<<<<<<<<<<<\n\nx=====================x")
except Exception as e:
    logger.exception(e)
    raise e

