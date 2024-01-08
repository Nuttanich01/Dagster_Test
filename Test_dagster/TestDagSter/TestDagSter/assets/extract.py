import pandas as pd
from dagster import asset

@asset()
def extract():
    raw_1 = pd.read_csv('D:/Desktop/Test/Dagster/Test_dagster/source/R_CIS_D_MAX_TEMP.csv', skiprows=3)
    raw_2 = pd.read_csv('D:/Desktop/Test/Dagster/Test_dagster/source/R_CIS_D_MIN_TEMP.csv', skiprows=3)
    df_raw_1 = pd.DataFrame(raw_1)
    df_raw_2 = pd.DataFrame(raw_2)
    #print(df_raw_1.count(),df_raw_2.count())
    df = pd.concat([df_raw_1,df_raw_2], axis=0)
    #print(df.info())
    #print(df)
    #df.to_csv("D:/Desktop/Test/Test_dagster_02/Data/raw_data.csv", index=False)
    return df
