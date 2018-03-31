

```python
import os
import csv
import pandas as pd
```


```python
file_one=('Crimes_-_2001_to_present.csv')
```


```python
# Read our Data file with the pandas library
# datafile too large to upload and contains unncessary data; use drop & filter to remove unncessary data. 
file_one_df = pd.read_csv(file_one, encoding = "ISO-8859-1")
```


```python
# Show just the header 
file_one_df
```


```python
#removing coloumn names
#https://stackoverflow.com/questions/13411544/delete-column-from-pandas-dataframe-using-python-del

update_1 = file_one_df.drop('FBI Code',1)
#update_1.head()
update_2 = update_1.drop('Ward',1)
#update_2.head()
update_3 = update_2.drop('Beat' ,1)
update_4 = update_3.drop("IUCR",1)
update_5 = update_4.drop("Block",1)
update_5 = update_4.drop("Block",1)
update_6 = update_5.drop("Updated On", 1)
#update_6.head()
update_7 = update_6.drop("District",1)
update_8 = update_7.drop("ID",1)
update_9 = update_8.drop("Community Area",1)
update_10 = update_9.drop("Domestic",1)
#update_11 = update_10.drop("Date",1)
update_11 = update_10.drop("X Coordinate",1)
update_12 = update_11.drop("Arrest",1)
update_13 = update_12.drop("Location" ,1)
update_14 = update_13.drop("Latitude",1)
update_15 = update_14.drop("Longitude",1)
update_16 = update_15.drop("Y Coordinate",1)
update_17 = update_16.drop("Location Description",1)


update_17.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Case Number</th>
      <th>Date</th>
      <th>Primary Type</th>
      <th>Description</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HY189866</td>
      <td>03/18/2015 07:44:00 PM</td>
      <td>BATTERY</td>
      <td>AGGRAVATED: HANDGUN</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>1</th>
      <td>HY190059</td>
      <td>03/18/2015 11:00:00 PM</td>
      <td>OTHER OFFENSE</td>
      <td>PAROLE VIOLATION</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>2</th>
      <td>HY190052</td>
      <td>03/18/2015 10:45:00 PM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>3</th>
      <td>HY190054</td>
      <td>03/18/2015 10:30:00 PM</td>
      <td>BATTERY</td>
      <td>SIMPLE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>4</th>
      <td>HY189976</td>
      <td>03/18/2015 09:00:00 PM</td>
      <td>ROBBERY</td>
      <td>ARMED: HANDGUN</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</div>




```python
update_17['Primary Type'].count()
```




    6561084




```python
#filtering years
#https://stackoverflow.com/questions/11869910/pandas-filter-rows-of-dataframe-with-operator-chaining
df_filtered = update_17[update_17['Year'] >= 2015]
df_filtered.count()
```




    Case Number     845293
    Date            845293
    Primary Type    845293
    Description     845293
    Year            845293
    dtype: int64




```python
#convert to csv
#https://stackoverflow.com/questions/16923281/pandas-writing-dataframe-to-csv-file
#df_filtered.to_csv('Chicago_Crime_15-Present.csv')
```


```python
df_chicago = df_filtered[df_filtered.Year != 2018]
```


```python
df_chicago
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Case Number</th>
      <th>Date</th>
      <th>Primary Type</th>
      <th>Description</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HY189866</td>
      <td>03/18/2015 07:44:00 PM</td>
      <td>BATTERY</td>
      <td>AGGRAVATED: HANDGUN</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>1</th>
      <td>HY190059</td>
      <td>03/18/2015 11:00:00 PM</td>
      <td>OTHER OFFENSE</td>
      <td>PAROLE VIOLATION</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>2</th>
      <td>HY190052</td>
      <td>03/18/2015 10:45:00 PM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>3</th>
      <td>HY190054</td>
      <td>03/18/2015 10:30:00 PM</td>
      <td>BATTERY</td>
      <td>SIMPLE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>4</th>
      <td>HY189976</td>
      <td>03/18/2015 09:00:00 PM</td>
      <td>ROBBERY</td>
      <td>ARMED: HANDGUN</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>5</th>
      <td>HY190032</td>
      <td>03/18/2015 10:00:00 PM</td>
      <td>BATTERY</td>
      <td>SIMPLE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>6</th>
      <td>HY190047</td>
      <td>03/18/2015 11:00:00 PM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>7</th>
      <td>HY189988</td>
      <td>03/18/2015 09:35:00 PM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>8</th>
      <td>HY190020</td>
      <td>03/18/2015 10:09:00 PM</td>
      <td>NARCOTICS</td>
      <td>POSS: CANNABIS 30GMS OR LESS</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>9</th>
      <td>HY189964</td>
      <td>03/18/2015 09:25:00 PM</td>
      <td>BATTERY</td>
      <td>SIMPLE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>10</th>
      <td>HY189984</td>
      <td>03/18/2015 09:30:00 PM</td>
      <td>CRIMINAL DAMAGE</td>
      <td>TO VEHICLE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>11</th>
      <td>HY189719</td>
      <td>03/15/2015 04:10:00 PM</td>
      <td>OTHER OFFENSE</td>
      <td>HARASSMENT BY TELEPHONE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>12</th>
      <td>HY189966</td>
      <td>03/18/2015 09:14:00 PM</td>
      <td>WEAPONS VIOLATION</td>
      <td>UNLAWFUL POSS OF HANDGUN</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>13</th>
      <td>HY190056</td>
      <td>03/18/2015 10:50:00 PM</td>
      <td>BATTERY</td>
      <td>SIMPLE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>14</th>
      <td>HY190019</td>
      <td>03/18/2015 10:31:00 PM</td>
      <td>THEFT</td>
      <td>RETAIL THEFT</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>15</th>
      <td>HY189725</td>
      <td>03/18/2015 12:55:00 PM</td>
      <td>BURGLARY</td>
      <td>FORCIBLE ENTRY</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>16</th>
      <td>HY190071</td>
      <td>03/18/2015 08:00:00 PM</td>
      <td>MOTOR VEHICLE THEFT</td>
      <td>AUTOMOBILE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>17</th>
      <td>HY190036</td>
      <td>03/18/2015 09:00:00 PM</td>
      <td>THEFT</td>
      <td>FROM BUILDING</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>18</th>
      <td>HY190063</td>
      <td>03/18/2015 10:56:00 PM</td>
      <td>PUBLIC PEACE VIOLATION</td>
      <td>RECKLESS CONDUCT</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>19</th>
      <td>HY190068</td>
      <td>03/18/2015 10:45:00 PM</td>
      <td>THEFT</td>
      <td>FROM BUILDING</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>20</th>
      <td>HY190031</td>
      <td>03/18/2015 10:00:00 PM</td>
      <td>THEFT</td>
      <td>RETAIL THEFT</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>22</th>
      <td>HY190072</td>
      <td>03/18/2015 11:55:00 PM</td>
      <td>ROBBERY</td>
      <td>STRONGARM - NO WEAPON</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>23</th>
      <td>HY190073</td>
      <td>03/18/2015 11:40:00 PM</td>
      <td>BATTERY</td>
      <td>AGGRAVATED: OTHER DANG WEAPON</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>24</th>
      <td>HY189969</td>
      <td>03/18/2015 09:44:00 PM</td>
      <td>WEAPONS VIOLATION</td>
      <td>UNLAWFUL USE HANDGUN</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>25</th>
      <td>HY190060</td>
      <td>03/18/2015 11:30:00 PM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>26</th>
      <td>HY190035</td>
      <td>03/18/2015 10:45:00 PM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>27</th>
      <td>HY190027</td>
      <td>03/18/2015 10:33:00 PM</td>
      <td>ASSAULT</td>
      <td>SIMPLE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>28</th>
      <td>HY190096</td>
      <td>03/19/2015 01:20:00 AM</td>
      <td>BATTERY</td>
      <td>SIMPLE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>29</th>
      <td>HY190003</td>
      <td>03/18/2015 09:59:00 PM</td>
      <td>BATTERY</td>
      <td>AGGRAVATED: HANDGUN</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>30</th>
      <td>HY190101</td>
      <td>03/19/2015 01:28:00 AM</td>
      <td>CRIMINAL TRESPASS</td>
      <td>TO STATE SUP LAND</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>6560455</th>
      <td>HY185287</td>
      <td>03/13/2015 06:00:00 PM</td>
      <td>ASSAULT</td>
      <td>SIMPLE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>6560456</th>
      <td>HY185342</td>
      <td>03/14/2015 09:00:00 PM</td>
      <td>CRIMINAL DAMAGE</td>
      <td>TO VEHICLE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>6560461</th>
      <td>HY132069</td>
      <td>01/28/2015 03:12:39 PM</td>
      <td>NARCOTICS</td>
      <td>POSS: CANNABIS 30GMS OR LESS</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>6560462</th>
      <td>HY148040</td>
      <td>02/11/2015 12:26:17 PM</td>
      <td>NARCOTICS</td>
      <td>POSS: COCAINE</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>6560581</th>
      <td>JB145188</td>
      <td>12/16/2017 06:00:00 PM</td>
      <td>ASSAULT</td>
      <td>SIMPLE</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6560601</th>
      <td>JB145816</td>
      <td>01/01/2015 12:00:00 AM</td>
      <td>DECEPTIVE PRACTICE</td>
      <td>FINANCIAL IDENTITY THEFT OVER $ 300</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>6561016</th>
      <td>JB145174</td>
      <td>11/21/2017 10:00:00 AM</td>
      <td>OTHER OFFENSE</td>
      <td>OTHER VEHICLE OFFENSE</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561017</th>
      <td>JB145166</td>
      <td>12/15/2017 09:00:00 AM</td>
      <td>DECEPTIVE PRACTICE</td>
      <td>FINANCIAL IDENTITY THEFT $300 AND UNDER</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561019</th>
      <td>JB145251</td>
      <td>08/30/2017 03:36:00 AM</td>
      <td>DECEPTIVE PRACTICE</td>
      <td>FRAUD OR CONFIDENCE GAME</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561022</th>
      <td>JB145191</td>
      <td>11/10/2017 09:00:00 AM</td>
      <td>DECEPTIVE PRACTICE</td>
      <td>CREDIT CARD FRAUD</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561023</th>
      <td>JB145264</td>
      <td>12/19/2017 10:00:00 AM</td>
      <td>DECEPTIVE PRACTICE</td>
      <td>FINANCIAL IDENTITY THEFT OVER $ 300</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561024</th>
      <td>JB145245</td>
      <td>11/28/2017 04:00:00 PM</td>
      <td>BATTERY</td>
      <td>AGGRAVATED DOMESTIC BATTERY: HANDS/FIST/FEET S...</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561025</th>
      <td>JB145159</td>
      <td>03/01/2017 11:00:00 AM</td>
      <td>DECEPTIVE PRACTICE</td>
      <td>FINANCIAL IDENTITY THEFT OVER $ 300</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561037</th>
      <td>JB145336</td>
      <td>10/14/2017 01:00:00 AM</td>
      <td>CRIMINAL DAMAGE</td>
      <td>TO PROPERTY</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561040</th>
      <td>JB145314</td>
      <td>01/31/2017 03:00:00 PM</td>
      <td>DECEPTIVE PRACTICE</td>
      <td>FORGERY</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561043</th>
      <td>JB145491</td>
      <td>12/12/2017 09:00:00 AM</td>
      <td>THEFT</td>
      <td>FROM BUILDING</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561046</th>
      <td>JB145570</td>
      <td>06/12/2016 09:00:00 AM</td>
      <td>DECEPTIVE PRACTICE</td>
      <td>FINANCIAL IDENTITY THEFT OVER $ 300</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>6561047</th>
      <td>JB145557</td>
      <td>11/06/2017 10:00:00 AM</td>
      <td>CRIM SEXUAL ASSAULT</td>
      <td>NON-AGGRAVATED</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561051</th>
      <td>JB145595</td>
      <td>12/29/2017 09:00:00 AM</td>
      <td>DECEPTIVE PRACTICE</td>
      <td>FORGERY</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561052</th>
      <td>JB145513</td>
      <td>11/30/2017 12:00:00 AM</td>
      <td>DECEPTIVE PRACTICE</td>
      <td>FINANCIAL IDENTITY THEFT OVER $ 300</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561053</th>
      <td>JB145530</td>
      <td>12/20/2017 12:00:00 PM</td>
      <td>DECEPTIVE PRACTICE</td>
      <td>FINANCIAL IDENTITY THEFT OVER $ 300</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561054</th>
      <td>JB145353</td>
      <td>10/01/2017 12:00:00 PM</td>
      <td>OTHER OFFENSE</td>
      <td>HARASSMENT BY TELEPHONE</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561058</th>
      <td>JB145765</td>
      <td>12/23/2017 09:00:00 AM</td>
      <td>THEFT</td>
      <td>OVER $500</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561059</th>
      <td>JB145586</td>
      <td>08/18/2017 05:00:00 PM</td>
      <td>OTHER OFFENSE</td>
      <td>OTHER VEHICLE OFFENSE</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561067</th>
      <td>JB145857</td>
      <td>12/21/2017 06:00:00 PM</td>
      <td>DECEPTIVE PRACTICE</td>
      <td>FINANCIAL IDENTITY THEFT OVER $ 300</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561069</th>
      <td>JB145878</td>
      <td>09/20/2017 09:00:00 AM</td>
      <td>DECEPTIVE PRACTICE</td>
      <td>ATTEMPT - FINANCIAL IDENTITY THEFT</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561073</th>
      <td>JB146060</td>
      <td>08/09/2017 12:01:00 AM</td>
      <td>SEX OFFENSE</td>
      <td>AGG CRIMINAL SEXUAL ABUSE</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561074</th>
      <td>JB145848</td>
      <td>01/14/2017 03:00:00 AM</td>
      <td>ROBBERY</td>
      <td>ARMED: HANDGUN</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561075</th>
      <td>JB145234</td>
      <td>12/15/2017 09:00:00 AM</td>
      <td>DECEPTIVE PRACTICE</td>
      <td>CREDIT CARD FRAUD</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>6561076</th>
      <td>JB146244</td>
      <td>12/23/2017 12:00:00 PM</td>
      <td>DECEPTIVE PRACTICE</td>
      <td>FINANCIAL IDENTITY THEFT OVER $ 300</td>
      <td>2017</td>
    </tr>
  </tbody>
</table>
<p>798734 rows × 5 columns</p>
</div>




```python
df_chicago.count()
df_chicago.to_csv('Chicago_Crime_2015-2017.csv')
```


```python
df_chicago['Primary Type'].describe()
```




    count     798734
    unique        33
    top        THEFT
    freq      183050
    Name: Primary Type, dtype: object




```python
df_chicago['Primary Type'].value_counts()
```




    THEFT                                183050
    BATTERY                              148389
    CRIMINAL DAMAGE                       88713
    ASSAULT                               55053
    DECEPTIVE PRACTICE                    52524
    OTHER OFFENSE                         51902
    NARCOTICS                             48668
    BURGLARY                              40445
    ROBBERY                               33475
    MOTOR VEHICLE THEFT                   32793
    CRIMINAL TRESPASS                     19521
    WEAPONS VIOLATION                     11494
    OFFENSE INVOLVING CHILDREN             6809
    PUBLIC PEACE VIOLATION                 5525
    CRIM SEXUAL ASSAULT                    4473
    INTERFERENCE WITH PUBLIC OFFICER       3328
    SEX OFFENSE                            2912
    PROSTITUTION                           2856
    HOMICIDE                               1950
    ARSON                                  1414
    LIQUOR LAW VIOLATION                    710
    GAMBLING                                690
    KIDNAPPING                              583
    STALKING                                510
    INTIMIDATION                            408
    OBSCENITY                               185
    CONCEALED CARRY LICENSE VIOLATION       139
    NON-CRIMINAL                            101
    PUBLIC INDECENCY                         34
    HUMAN TRAFFICKING                        32
    NON - CRIMINAL                           25
    OTHER NARCOTIC VIOLATION                 20
    NON-CRIMINAL (SUBJECT SPECIFIED)          3
    Name: Primary Type, dtype: int64




```python
file_two=('Categories.csv')
file_two_df = pd.read_csv(file_two, encoding = "ISO-8859-1")
```


```python
file_two_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Primary Type</th>
      <th>Category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>THEFT</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BATTERY</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>2</th>
      <td>CRIMINAL DAMAGE</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ASSAULT</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>4</th>
      <td>DECEPTIVE PRACTICE</td>
      <td>White-Collar</td>
    </tr>
  </tbody>
</table>
</div>




```python
merged = pd.merge(df_chicago, file_two_df, on="Primary Type",how="outer")
merged
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Case Number</th>
      <th>Date</th>
      <th>Primary Type</th>
      <th>Description</th>
      <th>Year</th>
      <th>Category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HY189866</td>
      <td>03/18/2015 07:44:00 PM</td>
      <td>BATTERY</td>
      <td>AGGRAVATED: HANDGUN</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>1</th>
      <td>HY190052</td>
      <td>03/18/2015 10:45:00 PM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>2</th>
      <td>HY190054</td>
      <td>03/18/2015 10:30:00 PM</td>
      <td>BATTERY</td>
      <td>SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>3</th>
      <td>HY190032</td>
      <td>03/18/2015 10:00:00 PM</td>
      <td>BATTERY</td>
      <td>SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>4</th>
      <td>HY190047</td>
      <td>03/18/2015 11:00:00 PM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>5</th>
      <td>HY189988</td>
      <td>03/18/2015 09:35:00 PM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>6</th>
      <td>HY189964</td>
      <td>03/18/2015 09:25:00 PM</td>
      <td>BATTERY</td>
      <td>SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>7</th>
      <td>HY190056</td>
      <td>03/18/2015 10:50:00 PM</td>
      <td>BATTERY</td>
      <td>SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>8</th>
      <td>HY190073</td>
      <td>03/18/2015 11:40:00 PM</td>
      <td>BATTERY</td>
      <td>AGGRAVATED: OTHER DANG WEAPON</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>9</th>
      <td>HY190060</td>
      <td>03/18/2015 11:30:00 PM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>10</th>
      <td>HY190035</td>
      <td>03/18/2015 10:45:00 PM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>11</th>
      <td>HY190096</td>
      <td>03/19/2015 01:20:00 AM</td>
      <td>BATTERY</td>
      <td>SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>12</th>
      <td>HY190003</td>
      <td>03/18/2015 09:59:00 PM</td>
      <td>BATTERY</td>
      <td>AGGRAVATED: HANDGUN</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>13</th>
      <td>HY190094</td>
      <td>03/19/2015 12:50:00 AM</td>
      <td>BATTERY</td>
      <td>AGGRAVATED:KNIFE/CUTTING INSTR</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>14</th>
      <td>HY190100</td>
      <td>03/19/2015 02:00:00 AM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>15</th>
      <td>HY190102</td>
      <td>03/19/2015 01:00:00 AM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>16</th>
      <td>HY190082</td>
      <td>03/19/2015 12:15:00 AM</td>
      <td>BATTERY</td>
      <td>SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>17</th>
      <td>HY189345</td>
      <td>03/18/2015 12:20:00 PM</td>
      <td>BATTERY</td>
      <td>AGG PRO.EMP: OTHER DANG WEAPON</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>18</th>
      <td>HY190125</td>
      <td>03/19/2015 02:30:00 AM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>19</th>
      <td>HY190043</td>
      <td>03/18/2015 11:00:00 PM</td>
      <td>BATTERY</td>
      <td>AGGRAVATED: HANDGUN</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>20</th>
      <td>HY190116</td>
      <td>03/18/2015 03:00:00 PM</td>
      <td>BATTERY</td>
      <td>AGGRAVATED: OTHER DANG WEAPON</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>21</th>
      <td>HY190133</td>
      <td>03/19/2015 03:00:00 AM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>22</th>
      <td>HY190136</td>
      <td>03/19/2015 03:51:00 AM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>23</th>
      <td>HY190111</td>
      <td>03/19/2015 02:05:00 AM</td>
      <td>BATTERY</td>
      <td>SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>24</th>
      <td>HY190119</td>
      <td>03/19/2015 02:31:00 AM</td>
      <td>BATTERY</td>
      <td>AGGRAVATED: OTHER DANG WEAPON</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>25</th>
      <td>HY190076</td>
      <td>03/19/2015 12:01:00 AM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>26</th>
      <td>HY190147</td>
      <td>03/19/2015 04:38:00 AM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>27</th>
      <td>HY190106</td>
      <td>03/19/2015 12:30:00 AM</td>
      <td>BATTERY</td>
      <td>AGGRAVATED: OTHER DANG WEAPON</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>28</th>
      <td>HY190067</td>
      <td>03/18/2015 11:20:00 PM</td>
      <td>BATTERY</td>
      <td>AGGRAVATED: HANDGUN</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>29</th>
      <td>HY189272</td>
      <td>03/18/2015 12:20:00 PM</td>
      <td>BATTERY</td>
      <td>DOMESTIC BATTERY SIMPLE</td>
      <td>2015</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>798704</th>
      <td>HZ271882</td>
      <td>05/20/2016 08:06:00 AM</td>
      <td>NON-CRIMINAL</td>
      <td>FOID - REVOCATION</td>
      <td>2016</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798705</th>
      <td>HY321435</td>
      <td>06/29/2015 10:23:00 PM</td>
      <td>NON-CRIMINAL</td>
      <td>CONCEALED CARRY LICENSE REVOCATION</td>
      <td>2015</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798706</th>
      <td>HZ122461</td>
      <td>11/20/2015 03:00:00 PM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2015</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798707</th>
      <td>HZ177884</td>
      <td>03/07/2016 10:00:00 AM</td>
      <td>NON-CRIMINAL</td>
      <td>FOID - REVOCATION</td>
      <td>2016</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798708</th>
      <td>HZ187848</td>
      <td>03/15/2016 09:30:00 AM</td>
      <td>NON-CRIMINAL</td>
      <td>FOID - REVOCATION</td>
      <td>2016</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798709</th>
      <td>HZ206450</td>
      <td>01/13/2016 12:00:00 PM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2016</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798710</th>
      <td>HZ215497</td>
      <td>03/31/2016 06:00:00 PM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2016</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798711</th>
      <td>HY127540</td>
      <td>01/24/2015 08:55:00 PM</td>
      <td>NON-CRIMINAL</td>
      <td>GUN OFFENDER NOTIFICATION-NO CONTACT</td>
      <td>2015</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798712</th>
      <td>HY152596</td>
      <td>02/15/2015 03:29:00 PM</td>
      <td>NON-CRIMINAL</td>
      <td>FOUND PASSPORT</td>
      <td>2015</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798713</th>
      <td>HZ252499</td>
      <td>05/01/2016 10:00:00 PM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2016</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798714</th>
      <td>HZ328710</td>
      <td>12/25/2015 09:00:00 AM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2015</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798715</th>
      <td>HZ340883</td>
      <td>06/25/2016 09:00:00 AM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2016</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798716</th>
      <td>HZ464033</td>
      <td>09/03/2016 03:00:00 PM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2016</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798717</th>
      <td>HZ495381</td>
      <td>10/28/2016 12:00:00 PM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2016</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798718</th>
      <td>JA114693</td>
      <td>11/21/2016 12:00:00 PM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2016</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798719</th>
      <td>JA110558</td>
      <td>01/09/2017 09:00:00 AM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2017</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798720</th>
      <td>JA136849</td>
      <td>01/27/2017 02:00:00 PM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2017</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798721</th>
      <td>JA295080</td>
      <td>05/01/2017 07:00:00 AM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2017</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798722</th>
      <td>JA296395</td>
      <td>05/05/2017 12:00:00 PM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2017</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798723</th>
      <td>JA410716</td>
      <td>08/29/2017 12:00:00 PM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2017</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798724</th>
      <td>JA493393</td>
      <td>10/24/2017 10:00:00 AM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2017</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798725</th>
      <td>JA496918</td>
      <td>11/03/2017 08:45:00 AM</td>
      <td>NON-CRIMINAL</td>
      <td>CONCEALED CARRY LICENSE REVOCATION</td>
      <td>2017</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798726</th>
      <td>JA506113</td>
      <td>11/10/2017 09:33:00 AM</td>
      <td>NON-CRIMINAL</td>
      <td>FOID - REVOCATION</td>
      <td>2017</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798727</th>
      <td>JA558229</td>
      <td>11/17/2017 12:00:00 PM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2017</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798728</th>
      <td>JB112261</td>
      <td>11/24/2017 09:00:00 AM</td>
      <td>NON-CRIMINAL</td>
      <td>NOTIFICATION OF STALKING - NO CONTACT ORDER</td>
      <td>2017</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798729</th>
      <td>JB121599</td>
      <td>12/10/2017 04:00:00 PM</td>
      <td>NON-CRIMINAL</td>
      <td>LOST PASSPORT</td>
      <td>2017</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798730</th>
      <td>HY505345</td>
      <td>11/17/2015 07:30:00 PM</td>
      <td>NON-CRIMINAL</td>
      <td>FOID - REVOCATION</td>
      <td>2015</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798731</th>
      <td>HZ107512</td>
      <td>01/07/2016 05:36:00 PM</td>
      <td>NON-CRIMINAL (SUBJECT SPECIFIED)</td>
      <td>NOTIFICATION OF CIVIL NO CONTACT ORDER</td>
      <td>2016</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798732</th>
      <td>JA189460</td>
      <td>03/16/2017 06:12:00 PM</td>
      <td>NON-CRIMINAL (SUBJECT SPECIFIED)</td>
      <td>NOTIFICATION OF CIVIL NO CONTACT ORDER</td>
      <td>2017</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>798733</th>
      <td>JA143710</td>
      <td>02/06/2017 01:20:00 PM</td>
      <td>NON-CRIMINAL (SUBJECT SPECIFIED)</td>
      <td>NOTIFICATION OF CIVIL NO CONTACT ORDER</td>
      <td>2017</td>
      <td>Other</td>
    </tr>
  </tbody>
</table>
<p>798734 rows × 6 columns</p>
</div>




```python
merged.to_csv('Chicago_Crime_2015-2017_UPDATE.csv')
```
