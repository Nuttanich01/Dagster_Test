import pandas as pd
import glob
from dagster import asset, Output, MetadataValue

@asset()
def all_file():
    """รวมไฟล์ทั้งหมด"""
    paths = "D:/Desktop/Test/Test_dbt_dag_postgres/sorce/"
    all_files = glob.glob(paths + "*.csv")
    #print(all_files)
    df = pd.DataFrame(columns=["First_Name","Last_Name","Age","Sex"])
    for file in all_files:
        #print(file)
        raw = pd.read_csv(file,sep='[|]',engine='python')
        to_df =  pd.DataFrame(raw)
        to_df = to_df.rename(columns={"First Name":"First_Name","Last Name":"Last_Name"})
        df = pd.concat([df,to_df], axis=0)
        
    soruce = df.fillna(value="Null")
    soruce.to_csv("D:/Desktop/Test/Test_dbt_dag_postgres/data/raw_data.csv", index=False)
    return Output(  # The return value is updated to wrap it in `Output` class
        value=soruce,   # The original df is passed in with the `value` parameter
        metadata={
            "num_records": len(soruce), # Metadata can be any key-value pair
            "preview": MetadataValue.md(soruce.head().to_markdown()),
        }
    )
