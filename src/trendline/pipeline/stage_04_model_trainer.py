from src.trendline.config.configuration import ConfigurationManager
from src.trendline.components.model_trainer import ModelTrainer
from src.trendline.logging import logger
from pathlib import Path




STAGE_NAME = "Model Trainer Stage"


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config = model_trainer_config)  # ✅ correct variable name
        model_trainer.train()  # ✅ call the train method
        
        
        #pipeline order 
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> Stage: {STAGE_NAME} has started <<<<<<<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> Stage: {STAGE_NAME} has been completed <<<<<<<<<<<<<\n\nx=====================x")
    except Exception as e:
        logger.exception(e)
        raise e
    
            