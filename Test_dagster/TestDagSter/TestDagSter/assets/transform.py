import pandas as pd
from dagster import asset, get_dagster_logger, Output, MetadataValue,Config

# class MyMetadataConfig(Config):
#     description: str = Field(description="transform")
    

@asset
def transform(extract):
    """TEST"""
    df_raw = extract
    #print(df_raw.info())
    df_raw["Daily_Min_Temp"].fillna("0",inplace=True)
    #print(df_raw.info())
    #df_raw.to_csv("D:/Desktop/Test/Test_dagster_02/Data/transform_data.csv", index=False)
    return Output(  # The return value is updated to wrap it in `Output` class
        value=df_raw,   # The original df is passed in with the `value` parameter
        metadata={
            "num_records": len(df_raw), # Metadata can be any key-value pair
            "preview": MetadataValue.md(df_raw.head().to_markdown()),
            "Description001": MetadataValue.text("Description"),
            # The `MetadataValue` class has useful static methods to build Metadata
        }
    )
