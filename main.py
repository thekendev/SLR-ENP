from src.trendline.logging import logger
from src.trendline.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.trendline.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.trendline.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.trendline.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.trendline.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

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



STAGE_NAME = "Data Transformation Stage"
        #pipeline order 
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> Stage: {STAGE_NAME} has started <<<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> Stage: {STAGE_NAME} has been completed <<<<<<<<<<<<<\n\nx=====================x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    
    
# Model Trainer
    STAGE_NAME = "Model Trainer Stage"
    try:
        logger.info(f">>>>>>>>>>> Stage: {STAGE_NAME} has started <<<<<<<<<<<")
        data_ingestion = ModelTrainerTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>>>>>> Stage: {STAGE_NAME} has been completed <<<<<<<<<<<<<\n\nx=====================x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    
    
    #model evaluation
STAGE_NAME = "Model evaluation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = ModelEvaluationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e