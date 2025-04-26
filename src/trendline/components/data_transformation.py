import os
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from src.trendline.utils.common import get_target_worksheet_df
from src.trendline.logging import logger

from src.trendline.entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.preprocessor = None
        self.schema = None

    def load_data(self) -> pd.DataFrame:
        try:
            raw_data = get_target_worksheet_df(
                file_path=str(self.config.data_path),
                sheet_name='3.4.2 (incl CCL)',
                skip_rows=6,
                read_rows=83
            )

            expected_columns = [
                'Year', 'Quarter',
                'Electricity: Very Small (Pence per kWh)',
                'Electricity: Small (Pence per kWh)',
                'Electricity: Small/Medium (Pence per kWh)',
                'Electricity: Medium (Pence per kWh)',
                'Electricity: Large (Pence per kWh)',
                'Electricity: Very Large (Pence per kWh)',
                'Electricity: Extra Large (Pence per kWh)',
                'Electricity: Average (Pence per kWh)',
                'Gas: Very Small (Pence per kWh)',
                'Gas: Small (Pence per kWh)',
                'Gas: Medium (Pence per kWh)',
                'Gas: Large (Pence per kWh)',
                'Gas: Very Large (Pence per kWh)',
                'Gas: Average (Pence per kWh)'
            ]

            if len(raw_data.columns) == len(expected_columns):
                raw_data.columns = expected_columns
            else:
                logger.warning(f"Column count mismatch. Expected {len(expected_columns)}, got {len(raw_data.columns)}. Using available columns.")

            valid_quarters = ['1st', '2nd', '3rd', '4th']
            raw_data = raw_data[
                raw_data['Year'].apply(lambda x: str(x).replace('.', '', 1).isdigit()) &
                raw_data['Quarter'].isin(valid_quarters)
            ]

            raw_data['Year'] = pd.to_numeric(raw_data['Year'], errors='coerce')

            logger.info(f"Loaded and cleaned data from {self.config.data_path} with shape {raw_data.shape}")
            return raw_data
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise e

    def handle_missing_values(self, data: pd.DataFrame) -> pd.DataFrame:
        initial_shape = data.shape
        cleaned_data = data.dropna()
        logger.info(f"Dropped missing values. Shape changed from {initial_shape} to {cleaned_data.shape}")
        return cleaned_data

    def drop_irrelevant_columns(self, data: pd.DataFrame) -> pd.DataFrame:
        columns_to_drop = [
            'Gas: Very Small (Pence per kWh)',
            'Gas: Small (Pence per kWh)',
            'Gas: Medium (Pence per kWh)',
            'Gas: Large (Pence per kWh)',
            'Gas: Very Large (Pence per kWh)',
            'Gas: Average (Pence per kWh)'
        ]
        columns_to_drop = [col for col in columns_to_drop if col in data.columns]
        filtered_data = data.drop(columns=columns_to_drop)
        logger.info(f"Dropped columns: {columns_to_drop}. New shape: {filtered_data.shape}")
        return filtered_data

    def engineer_features(self, data: pd.DataFrame) -> pd.DataFrame:
        engineered_data = data.copy()
        
        quarter_mapping = {'1st': 1, '2nd': 2, '3rd': 3, '4th': 4}
        engineered_data['Quarter'] = engineered_data['Quarter'].map(quarter_mapping)
        
        price_columns = [
            'Electricity: Very Small (Pence per kWh)',
            'Electricity: Small (Pence per kWh)',
            'Electricity: Small/Medium (Pence per kWh)',
            'Electricity: Medium (Pence per kWh)',
            'Electricity: Large (Pence per kWh)',
            'Electricity: Very Large (Pence per kWh)',
            'Electricity: Extra Large (Pence per kWh)'
        ]
        price_columns = [col for col in price_columns if col in engineered_data.columns]
        engineered_data['Avg_Electricity_Price'] = engineered_data[price_columns].mean(axis=1)
        
        engineered_data['Year'] = engineered_data['Year'].astype(str)
        
        logger.info("Feature engineering completed: Quarter converted, Avg_Electricity_Price added, Year as string")
        return engineered_data

    def save_transformed_data(self, data: pd.DataFrame):
        os.makedirs(self.config.root_dir, exist_ok=True)
        
        save_path = self.config.root_dir / "temple_data_transformed.xlsx"
        
        try:
            with pd.ExcelWriter(save_path, engine='openpyxl') as writer:
                data.to_excel(writer, index=False, sheet_name='3.4.2 (incl CCL)')
            logger.info(f"Transformed data saved to {save_path}")
        except Exception as e:
            logger.error(f"Error saving transformed data: {e}")
            raise e

    def transform_data(self) -> pd.DataFrame:
        data = self.load_data()
        data = self.handle_missing_values(data)
        data = self.drop_irrelevant_columns(data)
        data = self.engineer_features(data)
        self.save_transformed_data(data)
        
        logger.info(f"Data transformation completed. Final shape: {data.shape}")
        return data

    def train_test_splitting(self):
        data = pd.read_excel(self.config.root_dir / "temple_data_transformed.xlsx", sheet_name='3.4.2 (incl CCL)')
        
        train, test = train_test_split(data, test_size=0.25, random_state=42)

        train_path = self.config.root_dir / "train.csv"
        test_path = self.config.root_dir / "test.csv"

        train.to_csv(train_path, index=False)
        test.to_csv(test_path, index=False)

        logger.info("Split data into training and test sets")
        logger.info(f"Train shape: {train.shape}, Test shape: {test.shape}")

        return train, test

