import pandas as pd
import glob

paths = "D:/Desktop/Test/Test_dagster_dbt/sorce/"
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
soruce.to_csv("D:/Desktop/Test/Test_dagster_dbt/data/raw_data.csv", index=False)
print("======Data Successfully Inserted======")
