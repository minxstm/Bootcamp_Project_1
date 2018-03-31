import pandas as pd
chicago_df=pd.read_csv("Chicago_Crime_2015-2017.csv")
#print(chicago_df.head())
chicago_vc = chicago_df["Primary Type"].value_counts()
pd.DataFrame(chicago_vc).to_csv("crime_types_chicago_1.csv")
