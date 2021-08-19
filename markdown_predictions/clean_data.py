""" This script cleans the dataframe """
import pandas as pd

from parse_data import LoadSalesData

class PreProcessor:
    
    def __init__(self, df: pd.Dataframe):
        self.df = df
    
    def remove_pct_sign(self):
        """ Removes the pct sign from any column values """
        pass

    def remove_euro_sign(self):
        """ Removes the euro sign from any column values """
        pass
    
    def make_columns_numeric(self):
        """ Try to make columns numeric, else leave as original type """
        pass


if __name__ == "__main__":
    # Load in the data locally into a single dataframe
    loaded_data = LoadSalesData.load_in_files("raw_data")
    # Initiate pre-processing class instance
    pre_processor = PreProcessor(df=loaded_data.sales_data)
