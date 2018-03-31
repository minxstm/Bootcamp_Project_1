import pandas as pd
la_df=pd.read_csv("LA_Crime_Data_from_2010_to_Present.csv")
#print(la_df.head())
la_vc = la_df["Crime Code Description"].value_counts()
#print(la_vc)
pd.DataFrame(la_vc).to_csv("crime_types_la_1.csv")
