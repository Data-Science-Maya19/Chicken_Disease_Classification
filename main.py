from CNN_Classifier import logger
from CNN_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"----- Stage {STAGE_NAME} started ------")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"----- Stage {STAGE_NAME} completed ------\n\nx")
except Exception as e:
    logger.exception(e)
    raise e
