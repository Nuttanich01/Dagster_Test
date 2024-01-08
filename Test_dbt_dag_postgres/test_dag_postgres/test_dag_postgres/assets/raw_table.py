import psycopg2
from dagster import asset, Output, MetadataValue
import pandas as pd


@asset(key_prefix=["public"])
def raw_table(all_file):
    """Insert to Database [test_dbt_dagster].[public].[raw_table]"""
    conn = psycopg2.connect(database = "test_dbt_dagster", 
                            user = "postgres", 
                            host= 'localhost',
                            password = "docker",
                            port = 5432)

    cursor = conn.cursor()
    sql_insert = "INSERT INTO raw_table (First_name,Last_name,Age,Sex) VALUES (%s, %s, %s, %s)"
    df_source_list = all_file.values.tolist()
    cursor.executemany(sql_insert,df_source_list)
    conn.commit()
    cursor.close()
    conn.close()
    return Output(  # The return value is updated to wrap it in `Output` class
        value=all_file,   # The original df is passed in with the `value` parameter
        metadata={
            "num_records": len(all_file), # Metadata can be any key-value pair
            "preview": MetadataValue.md(all_file.head().to_markdown()),
        }
        )
