import pandas as pd
from dagster import asset

@asset
def load(transform):
    real_df = transform
    #print(real_df.info())
    real_df.to_csv("D:/Desktop/Test/Dagster/Test_dagster/Data/real_data.csv", index=False)