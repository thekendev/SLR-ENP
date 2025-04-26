from src.trendline.logging import logger
from src.trendline.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.trendline.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>>> Stage: {STAGE_NAME} has started <<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>> Stage: {STAGE_NAME} has been completed <<<<<<<<<<<<<\n\nx=====================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
        #pipeline order 
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> Stage: {STAGE_NAME} has started <<<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> Stage: {STAGE_NAME} has been completed <<<<<<<<<<<<<\n\nx=====================x")
    except Exception as e:
        logger.exception(e)
        raise e
