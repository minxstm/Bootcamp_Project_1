import pandas as pd
la_df=pd.read_csv("LA_Crime_Data_from_2010_to_Present.csv")
def recent(datestring):
    return datestring[-2:] in ["15","16","17"]

la_df["Recent Year"] = la_df["Date Occurred"].map(recent)
la_df_recent = la_df.loc[la_df["Recent Year"]==True]
la_df_condense = la_df_recent[["DR Number","Date Occurred","Time Occurred","Crime Code",
                               "Crime Code Description","Location "]]
la_df_condense.to_csv("LA_Crime_2015-2017.csv")