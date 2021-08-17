""" Reads in the sales data and loads into a pandas dataframe """
import collections
import glob
import json
from json import encoder
import re
import os
import logging
import pandas as pd


JSON_PATH = "markdown_predictions"


class LoadSalesData:
    
    def __init__(self, sales_data: pd.DataFrame):
        self.sales_data = sales_data
    
    @staticmethod
    def extract_season(file_path: str, file_name: str):
        """ Regex the file name to extract the season """
        # Define the regex expression
        regex_expr = re.compile(rf"{file_path}\/(?P<season>\w+) W.+")
        m = regex_expr.search(file_name)
            
        if m:
            return m.group('season')
        else:
            logging.critical(f"Season cannot be extracted from {file_name}.")
            return None
    
    @staticmethod
    def read_in_files(file_path: str, pre_post_toggle: str):
        all_sales_data = []
        for seasonal_file in glob.glob(f'{file_path}/*{pre_post_toggle}*'):
            logging.info(f"Reading file: {seasonal_file}")
            season = LoadSalesData.extract_season(file_path=file_path, file_name=seasonal_file)
            
            if not season:
                # If season unable to be extracted skip
                continue
            
            with open(os.path.join(JSON_PATH, f'{pre_post_toggle.lower()}_columns_to_extract.json')) as f:
                feature_cols = json.load(f)
            
            # Parse csv into dataframe
            pre_season_data = pd.read_csv(seasonal_file, index_col=None, encoding='utf-8', usecols=list(feature_cols.keys()))
            pre_season_data.rename(columns=feature_cols, inplace=True)
            
            # Add season as a column to the dataframe
            pre_season_data['season'] = season
            
            # Add suffix
            pre_season_data = pre_season_data.add_suffix(suffix=f"_{pre_post_toggle}")
            
            all_sales_data.append(pre_season_data)
        return pd.concat(all_sales_data, axis=0, ignore_index=True)

    @classmethod
    def load_in_files(cls, file_path: str):
        """ Load in Files """
        # pre_sales_data = LoadSalesData.read_in_files(file_path=file_path, pre_post_toggle="PRE")
        post_sales_data = LoadSalesData.read_in_files(file_path=file_path, pre_post_toggle="POST")
        
        # sales_data = pd.merge(pre_sales_data, post_sales_data, left_on=["Reference_PRE", "season_PRE"], right_on=["Reference_POST", "season_POST"],  how="inner")
        # sales_data.drop(columns=["season_POST"], inplace=True)
        # return cls(sales_data)


if __name__ == "__main__":
    loaded_data = LoadSalesData.load_in_files("raw_data")
