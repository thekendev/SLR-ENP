#update components
import os
import pandas as pd
from src.trendline.logging import logger
import openpyxl
from src.trendline.entity import DataValidationConfig

from src.trendline.utils.common import get_target_worksheet_df




class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        self.df = get_target_worksheet_df(file_path=self.config.unzip_data_dir)

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            data = self.df
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                else:
                    validation_status = True

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")
            return validation_status

        except Exception as e:
            raise e