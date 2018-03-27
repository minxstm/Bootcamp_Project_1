

```python
import pandas as pd
import numpy as np
```


```python
la_df = pd.read_csv("LA_Crime_2015-2017.csv")
la_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>DR Number</th>
      <th>Date Occurred</th>
      <th>Time Occurred</th>
      <th>Crime Code</th>
      <th>Crime Code Description</th>
      <th>Location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>200396</td>
      <td>809</td>
      <td>01/16/2015</td>
      <td>2130</td>
      <td>510</td>
      <td>VEHICLE - STOLEN</td>
      <td>(34.1814, -118.4263)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>200435</td>
      <td>150108522</td>
      <td>03/11/2015</td>
      <td>1600</td>
      <td>442</td>
      <td>SHOPLIFTING - PETTY THEFT ($950 &amp; UNDER)</td>
      <td>(34.0481, -118.2507)</td>
    </tr>
    <tr>
      <th>2</th>
      <td>201015</td>
      <td>150109432</td>
      <td>03/23/2015</td>
      <td>1800</td>
      <td>310</td>
      <td>BURGLARY</td>
      <td>(34.0388, -118.2574)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>201036</td>
      <td>150109804</td>
      <td>03/29/2015</td>
      <td>800</td>
      <td>510</td>
      <td>VEHICLE - STOLEN</td>
      <td>(34.0628, -118.2395)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>201376</td>
      <td>150114304</td>
      <td>06/08/2015</td>
      <td>1015</td>
      <td>850</td>
      <td>INDECENT EXPOSURE</td>
      <td>(34.0488, -118.2483)</td>
    </tr>
    <tr>
      <th>5</th>
      <td>201500</td>
      <td>150115324</td>
      <td>06/23/2015</td>
      <td>2230</td>
      <td>510</td>
      <td>VEHICLE - STOLEN</td>
      <td>(34.051, -118.2445)</td>
    </tr>
    <tr>
      <th>6</th>
      <td>201520</td>
      <td>150116252</td>
      <td>07/06/2015</td>
      <td>545</td>
      <td>946</td>
      <td>OTHER MISCELLANEOUS CRIME</td>
      <td>(34.0525, -118.2409)</td>
    </tr>
    <tr>
      <th>7</th>
      <td>202385</td>
      <td>150116299</td>
      <td>07/08/2015</td>
      <td>2355</td>
      <td>888</td>
      <td>TRESPASSING</td>
      <td>(34.0467, -118.252)</td>
    </tr>
    <tr>
      <th>8</th>
      <td>202642</td>
      <td>150116489</td>
      <td>07/10/2015</td>
      <td>2100</td>
      <td>510</td>
      <td>VEHICLE - STOLEN</td>
      <td>(34.0386, -118.2638)</td>
    </tr>
    <tr>
      <th>9</th>
      <td>204858</td>
      <td>150116490</td>
      <td>07/10/2015</td>
      <td>2100</td>
      <td>510</td>
      <td>VEHICLE - STOLEN</td>
      <td>(34.0462, -118.2585)</td>
    </tr>
    <tr>
      <th>10</th>
      <td>205020</td>
      <td>150116494</td>
      <td>07/11/2015</td>
      <td>1200</td>
      <td>510</td>
      <td>VEHICLE - STOLEN</td>
      <td>(34.0519, -118.2531)</td>
    </tr>
    <tr>
      <th>11</th>
      <td>205081</td>
      <td>150116696</td>
      <td>07/13/2015</td>
      <td>1400</td>
      <td>510</td>
      <td>VEHICLE - STOLEN</td>
      <td>(34.0454, -118.2657)</td>
    </tr>
    <tr>
      <th>12</th>
      <td>205459</td>
      <td>150116830</td>
      <td>07/15/2015</td>
      <td>1600</td>
      <td>350</td>
      <td>THEFT, PERSON</td>
      <td>(34.048, -118.2577)</td>
    </tr>
    <tr>
      <th>13</th>
      <td>408298</td>
      <td>150117314</td>
      <td>07/23/2015</td>
      <td>715</td>
      <td>330</td>
      <td>BURGLARY FROM VEHICLE</td>
      <td>(34.0688, -118.2333)</td>
    </tr>
    <tr>
      <th>14</th>
      <td>490068</td>
      <td>150117319</td>
      <td>07/17/2015</td>
      <td>1510</td>
      <td>649</td>
      <td>DOCUMENT FORGERY / STOLEN FELONY</td>
      <td>(34.0604, -118.2393)</td>
    </tr>
    <tr>
      <th>15</th>
      <td>570205</td>
      <td>150118406</td>
      <td>08/07/2015</td>
      <td>2000</td>
      <td>330</td>
      <td>BURGLARY FROM VEHICLE</td>
      <td>(34.0439, -118.2479)</td>
    </tr>
    <tr>
      <th>16</th>
      <td>570517</td>
      <td>150118407</td>
      <td>08/06/2015</td>
      <td>2000</td>
      <td>330</td>
      <td>BURGLARY FROM VEHICLE</td>
      <td>(34.0589, -118.2527)</td>
    </tr>
    <tr>
      <th>17</th>
      <td>571296</td>
      <td>150118562</td>
      <td>08/10/2015</td>
      <td>1810</td>
      <td>440</td>
      <td>THEFT PLAIN - PETTY ($950 &amp; UNDER)</td>
      <td>(34.0481, -118.2507)</td>
    </tr>
    <tr>
      <th>18</th>
      <td>571568</td>
      <td>150119001</td>
      <td>08/16/2015</td>
      <td>1530</td>
      <td>310</td>
      <td>BURGLARY</td>
      <td>(34.0396, -118.2558)</td>
    </tr>
    <tr>
      <th>19</th>
      <td>653303</td>
      <td>150128751</td>
      <td>12/30/2015</td>
      <td>1600</td>
      <td>510</td>
      <td>VEHICLE - STOLEN</td>
      <td>(34.0628, -118.2433)</td>
    </tr>
    <tr>
      <th>20</th>
      <td>657884</td>
      <td>171013348</td>
      <td>07/20/2017</td>
      <td>2000</td>
      <td>330</td>
      <td>BURGLARY FROM VEHICLE</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>734905</td>
      <td>171013326</td>
      <td>07/21/2017</td>
      <td>1000</td>
      <td>330</td>
      <td>BURGLARY FROM VEHICLE</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>979485</td>
      <td>150115675</td>
      <td>06/28/2015</td>
      <td>1730</td>
      <td>510</td>
      <td>VEHICLE - STOLEN</td>
      <td>(34.0387, -118.2611)</td>
    </tr>
    <tr>
      <th>23</th>
      <td>979544</td>
      <td>150307045</td>
      <td>02/19/2015</td>
      <td>1500</td>
      <td>510</td>
      <td>VEHICLE - STOLEN</td>
      <td>(34.0247, -118.3089)</td>
    </tr>
    <tr>
      <th>24</th>
      <td>979683</td>
      <td>150411088</td>
      <td>06/17/2015</td>
      <td>400</td>
      <td>510</td>
      <td>VEHICLE - STOLEN</td>
      <td>(34.0646, -118.197)</td>
    </tr>
    <tr>
      <th>25</th>
      <td>979727</td>
      <td>150125362</td>
      <td>11/13/2015</td>
      <td>1300</td>
      <td>510</td>
      <td>VEHICLE - STOLEN</td>
      <td>(34.051, -118.248)</td>
    </tr>
    <tr>
      <th>26</th>
      <td>979788</td>
      <td>150125678</td>
      <td>11/15/2015</td>
      <td>200</td>
      <td>351</td>
      <td>PURSE SNATCHING</td>
      <td>(34.048, -118.2577)</td>
    </tr>
    <tr>
      <th>27</th>
      <td>979894</td>
      <td>150113111</td>
      <td>05/19/2015</td>
      <td>1830</td>
      <td>510</td>
      <td>VEHICLE - STOLEN</td>
      <td>(34.0444, -118.2628)</td>
    </tr>
    <tr>
      <th>28</th>
      <td>979913</td>
      <td>150104713</td>
      <td>01/13/2015</td>
      <td>110</td>
      <td>350</td>
      <td>THEFT, PERSON</td>
      <td>(34.0478, -118.2502)</td>
    </tr>
    <tr>
      <th>29</th>
      <td>979971</td>
      <td>150506835</td>
      <td>03/04/2015</td>
      <td>2200</td>
      <td>510</td>
      <td>VEHICLE - STOLEN</td>
      <td>(33.7433, -118.2945)</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>666865</th>
      <td>1704623</td>
      <td>182006723</td>
      <td>12/06/2017</td>
      <td>1300</td>
      <td>860</td>
      <td>BATTERY WITH SEXUAL CONTACT</td>
      <td>(34.0598, -118.2987)</td>
    </tr>
    <tr>
      <th>666866</th>
      <td>1704641</td>
      <td>182007539</td>
      <td>02/01/2015</td>
      <td>1</td>
      <td>956</td>
      <td>LETTERS, LEWD  -  TELEPHONE CALLS, LEWD</td>
      <td>(34.0652, -118.2857)</td>
    </tr>
    <tr>
      <th>666867</th>
      <td>1704665</td>
      <td>182007664</td>
      <td>12/14/2017</td>
      <td>1512</td>
      <td>649</td>
      <td>DOCUMENT FORGERY / STOLEN FELONY</td>
      <td>(34.0618, -118.3004)</td>
    </tr>
    <tr>
      <th>666868</th>
      <td>1704673</td>
      <td>182007733</td>
      <td>10/26/2017</td>
      <td>1200</td>
      <td>121</td>
      <td>RAPE, FORCIBLE</td>
      <td>(34.0598, -118.2979)</td>
    </tr>
    <tr>
      <th>666869</th>
      <td>1704729</td>
      <td>182007651</td>
      <td>11/17/2016</td>
      <td>1000</td>
      <td>510</td>
      <td>VEHICLE - STOLEN</td>
      <td>(34.0672, -118.2966)</td>
    </tr>
    <tr>
      <th>666870</th>
      <td>1704739</td>
      <td>182007678</td>
      <td>10/01/2017</td>
      <td>900</td>
      <td>354</td>
      <td>THEFT OF IDENTITY</td>
      <td>(34.0652, -118.2878)</td>
    </tr>
    <tr>
      <th>666871</th>
      <td>1704740</td>
      <td>182007679</td>
      <td>02/27/2017</td>
      <td>2100</td>
      <td>354</td>
      <td>THEFT OF IDENTITY</td>
      <td>(34.0473, -118.2924)</td>
    </tr>
    <tr>
      <th>666872</th>
      <td>1704759</td>
      <td>182007725</td>
      <td>01/01/2015</td>
      <td>1</td>
      <td>354</td>
      <td>THEFT OF IDENTITY</td>
      <td>(34.0672, -118.2941)</td>
    </tr>
    <tr>
      <th>666873</th>
      <td>1704772</td>
      <td>182007843</td>
      <td>10/07/2016</td>
      <td>1200</td>
      <td>354</td>
      <td>THEFT OF IDENTITY</td>
      <td>(34.0799, -118.3057)</td>
    </tr>
    <tr>
      <th>666874</th>
      <td>1704806</td>
      <td>182007920</td>
      <td>07/07/2017</td>
      <td>800</td>
      <td>812</td>
      <td>CRM AGNST CHLD (13 OR UNDER) (14-15 &amp; SUSP 10 ...</td>
      <td>(34.0508, -118.2907)</td>
    </tr>
    <tr>
      <th>666875</th>
      <td>1704826</td>
      <td>182008016</td>
      <td>06/16/2017</td>
      <td>100</td>
      <td>627</td>
      <td>CHILD ABUSE (PHYSICAL) - SIMPLE ASSAULT</td>
      <td>(34.0581, -118.3066)</td>
    </tr>
    <tr>
      <th>666876</th>
      <td>1704865</td>
      <td>182107145</td>
      <td>12/23/2017</td>
      <td>2130</td>
      <td>121</td>
      <td>RAPE, FORCIBLE</td>
      <td>(34.2176, -118.6017)</td>
    </tr>
    <tr>
      <th>666877</th>
      <td>1704868</td>
      <td>182107226</td>
      <td>02/23/2017</td>
      <td>1200</td>
      <td>956</td>
      <td>LETTERS, LEWD  -  TELEPHONE CALLS, LEWD</td>
      <td>(34.1825, -118.6529)</td>
    </tr>
    <tr>
      <th>666878</th>
      <td>1704875</td>
      <td>182106544</td>
      <td>01/01/2016</td>
      <td>800</td>
      <td>341</td>
      <td>THEFT-GRAND ($950.01 &amp; OVER)EXCPT,GUNS,FOWL,LI...</td>
      <td>(34.1644, -118.6046)</td>
    </tr>
    <tr>
      <th>666879</th>
      <td>1704880</td>
      <td>182106744</td>
      <td>01/01/2015</td>
      <td>1200</td>
      <td>627</td>
      <td>CHILD ABUSE (PHYSICAL) - SIMPLE ASSAULT</td>
      <td>(34.201, -118.6044)</td>
    </tr>
    <tr>
      <th>666880</th>
      <td>1704885</td>
      <td>182106915</td>
      <td>02/28/2017</td>
      <td>2100</td>
      <td>330</td>
      <td>BURGLARY FROM VEHICLE</td>
      <td>(34.2195, -118.6147)</td>
    </tr>
    <tr>
      <th>666881</th>
      <td>1704905</td>
      <td>182107186</td>
      <td>04/10/2016</td>
      <td>1200</td>
      <td>354</td>
      <td>THEFT OF IDENTITY</td>
      <td>(34.1592, -118.6108)</td>
    </tr>
    <tr>
      <th>666882</th>
      <td>1704938</td>
      <td>182107320</td>
      <td>08/07/2017</td>
      <td>2200</td>
      <td>236</td>
      <td>INTIMATE PARTNER - AGGRAVATED ASSAULT</td>
      <td>(34.1912, -118.5941)</td>
    </tr>
    <tr>
      <th>666883</th>
      <td>1704959</td>
      <td>182107358</td>
      <td>12/13/2017</td>
      <td>1200</td>
      <td>420</td>
      <td>THEFT FROM MOTOR VEHICLE - PETTY ($950 &amp; UNDER)</td>
      <td>(34.1912, -118.5941)</td>
    </tr>
    <tr>
      <th>666884</th>
      <td>1704973</td>
      <td>182107381</td>
      <td>07/01/2017</td>
      <td>1650</td>
      <td>812</td>
      <td>CRM AGNST CHLD (13 OR UNDER) (14-15 &amp; SUSP 10 ...</td>
      <td>(34.2053, -118.6517)</td>
    </tr>
    <tr>
      <th>666885</th>
      <td>1704980</td>
      <td>182107399</td>
      <td>12/20/2017</td>
      <td>1015</td>
      <td>354</td>
      <td>THEFT OF IDENTITY</td>
      <td>(34.1773, -118.5974)</td>
    </tr>
    <tr>
      <th>666886</th>
      <td>1704993</td>
      <td>182107416</td>
      <td>12/01/2017</td>
      <td>1</td>
      <td>812</td>
      <td>CRM AGNST CHLD (13 OR UNDER) (14-15 &amp; SUSP 10 ...</td>
      <td>(34.2065, -118.5991)</td>
    </tr>
    <tr>
      <th>666887</th>
      <td>1705001</td>
      <td>182107245</td>
      <td>11/15/2017</td>
      <td>1200</td>
      <td>354</td>
      <td>THEFT OF IDENTITY</td>
      <td>(34.2259, -118.6126)</td>
    </tr>
    <tr>
      <th>666888</th>
      <td>1705005</td>
      <td>182107310</td>
      <td>10/01/2017</td>
      <td>1200</td>
      <td>354</td>
      <td>THEFT OF IDENTITY</td>
      <td>(34.1807, -118.6535)</td>
    </tr>
    <tr>
      <th>666889</th>
      <td>1705023</td>
      <td>182107458</td>
      <td>08/05/2017</td>
      <td>1015</td>
      <td>354</td>
      <td>THEFT OF IDENTITY</td>
      <td>(34.212, -118.5754)</td>
    </tr>
    <tr>
      <th>666890</th>
      <td>1705035</td>
      <td>182107476</td>
      <td>07/19/2017</td>
      <td>1</td>
      <td>901</td>
      <td>VIOLATION OF RESTRAINING ORDER</td>
      <td>(34.1754, -118.5974)</td>
    </tr>
    <tr>
      <th>666891</th>
      <td>1705051</td>
      <td>182107512</td>
      <td>01/01/2017</td>
      <td>1</td>
      <td>649</td>
      <td>DOCUMENT FORGERY / STOLEN FELONY</td>
      <td>(34.2047, -118.5994)</td>
    </tr>
    <tr>
      <th>666892</th>
      <td>1705052</td>
      <td>182107513</td>
      <td>11/27/2017</td>
      <td>1205</td>
      <td>649</td>
      <td>DOCUMENT FORGERY / STOLEN FELONY</td>
      <td>(34.1828, -118.6102)</td>
    </tr>
    <tr>
      <th>666893</th>
      <td>1705059</td>
      <td>182107534</td>
      <td>10/01/2016</td>
      <td>800</td>
      <td>341</td>
      <td>THEFT-GRAND ($950.01 &amp; OVER)EXCPT,GUNS,FOWL,LI...</td>
      <td>(34.2222, -118.5937)</td>
    </tr>
    <tr>
      <th>666894</th>
      <td>1705071</td>
      <td>182107551</td>
      <td>11/12/2017</td>
      <td>1200</td>
      <td>624</td>
      <td>BATTERY - SIMPLE ASSAULT</td>
      <td>(34.1733, -118.599)</td>
    </tr>
  </tbody>
</table>
<p>666895 rows × 7 columns</p>
</div>




```python
la_df_laconic = la_df[["DR Number","Date Occurred", "Crime Code Description"]]
la_df_laconic
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DR Number</th>
      <th>Date Occurred</th>
      <th>Crime Code Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>809</td>
      <td>01/16/2015</td>
      <td>VEHICLE - STOLEN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>150108522</td>
      <td>03/11/2015</td>
      <td>SHOPLIFTING - PETTY THEFT ($950 &amp; UNDER)</td>
    </tr>
    <tr>
      <th>2</th>
      <td>150109432</td>
      <td>03/23/2015</td>
      <td>BURGLARY</td>
    </tr>
    <tr>
      <th>3</th>
      <td>150109804</td>
      <td>03/29/2015</td>
      <td>VEHICLE - STOLEN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>150114304</td>
      <td>06/08/2015</td>
      <td>INDECENT EXPOSURE</td>
    </tr>
    <tr>
      <th>5</th>
      <td>150115324</td>
      <td>06/23/2015</td>
      <td>VEHICLE - STOLEN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>150116252</td>
      <td>07/06/2015</td>
      <td>OTHER MISCELLANEOUS CRIME</td>
    </tr>
    <tr>
      <th>7</th>
      <td>150116299</td>
      <td>07/08/2015</td>
      <td>TRESPASSING</td>
    </tr>
    <tr>
      <th>8</th>
      <td>150116489</td>
      <td>07/10/2015</td>
      <td>VEHICLE - STOLEN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>150116490</td>
      <td>07/10/2015</td>
      <td>VEHICLE - STOLEN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>150116494</td>
      <td>07/11/2015</td>
      <td>VEHICLE - STOLEN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>150116696</td>
      <td>07/13/2015</td>
      <td>VEHICLE - STOLEN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>150116830</td>
      <td>07/15/2015</td>
      <td>THEFT, PERSON</td>
    </tr>
    <tr>
      <th>13</th>
      <td>150117314</td>
      <td>07/23/2015</td>
      <td>BURGLARY FROM VEHICLE</td>
    </tr>
    <tr>
      <th>14</th>
      <td>150117319</td>
      <td>07/17/2015</td>
      <td>DOCUMENT FORGERY / STOLEN FELONY</td>
    </tr>
    <tr>
      <th>15</th>
      <td>150118406</td>
      <td>08/07/2015</td>
      <td>BURGLARY FROM VEHICLE</td>
    </tr>
    <tr>
      <th>16</th>
      <td>150118407</td>
      <td>08/06/2015</td>
      <td>BURGLARY FROM VEHICLE</td>
    </tr>
    <tr>
      <th>17</th>
      <td>150118562</td>
      <td>08/10/2015</td>
      <td>THEFT PLAIN - PETTY ($950 &amp; UNDER)</td>
    </tr>
    <tr>
      <th>18</th>
      <td>150119001</td>
      <td>08/16/2015</td>
      <td>BURGLARY</td>
    </tr>
    <tr>
      <th>19</th>
      <td>150128751</td>
      <td>12/30/2015</td>
      <td>VEHICLE - STOLEN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>171013348</td>
      <td>07/20/2017</td>
      <td>BURGLARY FROM VEHICLE</td>
    </tr>
    <tr>
      <th>21</th>
      <td>171013326</td>
      <td>07/21/2017</td>
      <td>BURGLARY FROM VEHICLE</td>
    </tr>
    <tr>
      <th>22</th>
      <td>150115675</td>
      <td>06/28/2015</td>
      <td>VEHICLE - STOLEN</td>
    </tr>
    <tr>
      <th>23</th>
      <td>150307045</td>
      <td>02/19/2015</td>
      <td>VEHICLE - STOLEN</td>
    </tr>
    <tr>
      <th>24</th>
      <td>150411088</td>
      <td>06/17/2015</td>
      <td>VEHICLE - STOLEN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>150125362</td>
      <td>11/13/2015</td>
      <td>VEHICLE - STOLEN</td>
    </tr>
    <tr>
      <th>26</th>
      <td>150125678</td>
      <td>11/15/2015</td>
      <td>PURSE SNATCHING</td>
    </tr>
    <tr>
      <th>27</th>
      <td>150113111</td>
      <td>05/19/2015</td>
      <td>VEHICLE - STOLEN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>150104713</td>
      <td>01/13/2015</td>
      <td>THEFT, PERSON</td>
    </tr>
    <tr>
      <th>29</th>
      <td>150506835</td>
      <td>03/04/2015</td>
      <td>VEHICLE - STOLEN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>666865</th>
      <td>182006723</td>
      <td>12/06/2017</td>
      <td>BATTERY WITH SEXUAL CONTACT</td>
    </tr>
    <tr>
      <th>666866</th>
      <td>182007539</td>
      <td>02/01/2015</td>
      <td>LETTERS, LEWD  -  TELEPHONE CALLS, LEWD</td>
    </tr>
    <tr>
      <th>666867</th>
      <td>182007664</td>
      <td>12/14/2017</td>
      <td>DOCUMENT FORGERY / STOLEN FELONY</td>
    </tr>
    <tr>
      <th>666868</th>
      <td>182007733</td>
      <td>10/26/2017</td>
      <td>RAPE, FORCIBLE</td>
    </tr>
    <tr>
      <th>666869</th>
      <td>182007651</td>
      <td>11/17/2016</td>
      <td>VEHICLE - STOLEN</td>
    </tr>
    <tr>
      <th>666870</th>
      <td>182007678</td>
      <td>10/01/2017</td>
      <td>THEFT OF IDENTITY</td>
    </tr>
    <tr>
      <th>666871</th>
      <td>182007679</td>
      <td>02/27/2017</td>
      <td>THEFT OF IDENTITY</td>
    </tr>
    <tr>
      <th>666872</th>
      <td>182007725</td>
      <td>01/01/2015</td>
      <td>THEFT OF IDENTITY</td>
    </tr>
    <tr>
      <th>666873</th>
      <td>182007843</td>
      <td>10/07/2016</td>
      <td>THEFT OF IDENTITY</td>
    </tr>
    <tr>
      <th>666874</th>
      <td>182007920</td>
      <td>07/07/2017</td>
      <td>CRM AGNST CHLD (13 OR UNDER) (14-15 &amp; SUSP 10 ...</td>
    </tr>
    <tr>
      <th>666875</th>
      <td>182008016</td>
      <td>06/16/2017</td>
      <td>CHILD ABUSE (PHYSICAL) - SIMPLE ASSAULT</td>
    </tr>
    <tr>
      <th>666876</th>
      <td>182107145</td>
      <td>12/23/2017</td>
      <td>RAPE, FORCIBLE</td>
    </tr>
    <tr>
      <th>666877</th>
      <td>182107226</td>
      <td>02/23/2017</td>
      <td>LETTERS, LEWD  -  TELEPHONE CALLS, LEWD</td>
    </tr>
    <tr>
      <th>666878</th>
      <td>182106544</td>
      <td>01/01/2016</td>
      <td>THEFT-GRAND ($950.01 &amp; OVER)EXCPT,GUNS,FOWL,LI...</td>
    </tr>
    <tr>
      <th>666879</th>
      <td>182106744</td>
      <td>01/01/2015</td>
      <td>CHILD ABUSE (PHYSICAL) - SIMPLE ASSAULT</td>
    </tr>
    <tr>
      <th>666880</th>
      <td>182106915</td>
      <td>02/28/2017</td>
      <td>BURGLARY FROM VEHICLE</td>
    </tr>
    <tr>
      <th>666881</th>
      <td>182107186</td>
      <td>04/10/2016</td>
      <td>THEFT OF IDENTITY</td>
    </tr>
    <tr>
      <th>666882</th>
      <td>182107320</td>
      <td>08/07/2017</td>
      <td>INTIMATE PARTNER - AGGRAVATED ASSAULT</td>
    </tr>
    <tr>
      <th>666883</th>
      <td>182107358</td>
      <td>12/13/2017</td>
      <td>THEFT FROM MOTOR VEHICLE - PETTY ($950 &amp; UNDER)</td>
    </tr>
    <tr>
      <th>666884</th>
      <td>182107381</td>
      <td>07/01/2017</td>
      <td>CRM AGNST CHLD (13 OR UNDER) (14-15 &amp; SUSP 10 ...</td>
    </tr>
    <tr>
      <th>666885</th>
      <td>182107399</td>
      <td>12/20/2017</td>
      <td>THEFT OF IDENTITY</td>
    </tr>
    <tr>
      <th>666886</th>
      <td>182107416</td>
      <td>12/01/2017</td>
      <td>CRM AGNST CHLD (13 OR UNDER) (14-15 &amp; SUSP 10 ...</td>
    </tr>
    <tr>
      <th>666887</th>
      <td>182107245</td>
      <td>11/15/2017</td>
      <td>THEFT OF IDENTITY</td>
    </tr>
    <tr>
      <th>666888</th>
      <td>182107310</td>
      <td>10/01/2017</td>
      <td>THEFT OF IDENTITY</td>
    </tr>
    <tr>
      <th>666889</th>
      <td>182107458</td>
      <td>08/05/2017</td>
      <td>THEFT OF IDENTITY</td>
    </tr>
    <tr>
      <th>666890</th>
      <td>182107476</td>
      <td>07/19/2017</td>
      <td>VIOLATION OF RESTRAINING ORDER</td>
    </tr>
    <tr>
      <th>666891</th>
      <td>182107512</td>
      <td>01/01/2017</td>
      <td>DOCUMENT FORGERY / STOLEN FELONY</td>
    </tr>
    <tr>
      <th>666892</th>
      <td>182107513</td>
      <td>11/27/2017</td>
      <td>DOCUMENT FORGERY / STOLEN FELONY</td>
    </tr>
    <tr>
      <th>666893</th>
      <td>182107534</td>
      <td>10/01/2016</td>
      <td>THEFT-GRAND ($950.01 &amp; OVER)EXCPT,GUNS,FOWL,LI...</td>
    </tr>
    <tr>
      <th>666894</th>
      <td>182107551</td>
      <td>11/12/2017</td>
      <td>BATTERY - SIMPLE ASSAULT</td>
    </tr>
  </tbody>
</table>
<p>666895 rows × 3 columns</p>
</div>




```python
la_lut = pd.read_csv("crime_types_la_1.csv")
la_lut
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Crime Code Description</th>
      <th>Category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BATTERY - SIMPLE ASSAULT</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BURGLARY FROM VEHICLE</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>2</th>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BURGLARY</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>4</th>
      <td>THEFT PLAIN - PETTY ($950 &amp; UNDER)</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>5</th>
      <td>THEFT OF IDENTITY</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>6</th>
      <td>INTIMATE PARTNER - SIMPLE ASSAULT</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>7</th>
      <td>VANDALISM - FELONY ($400 &amp; OVER, ALL CHURCH VA...</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>8</th>
      <td>VANDALISM - MISDEAMEANOR ($399 OR UNDER)</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>9</th>
      <td>ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>10</th>
      <td>THEFT FROM MOTOR VEHICLE - PETTY ($950 &amp; UNDER)</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>11</th>
      <td>ROBBERY</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>12</th>
      <td>THEFT-GRAND ($950.01 &amp; OVER)EXCPT,GUNS,FOWL,LI...</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>13</th>
      <td>CRIMINAL THREATS - NO WEAPON DISPLAYED</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>14</th>
      <td>SHOPLIFTING - PETTY THEFT ($950 &amp; UNDER)</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>15</th>
      <td>THEFT FROM MOTOR VEHICLE - GRAND ($400 AND OVER)</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>16</th>
      <td>DOCUMENT FORGERY / STOLEN FELONY</td>
      <td>White Collar</td>
    </tr>
    <tr>
      <th>17</th>
      <td>OTHER MISCELLANEOUS CRIME</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>VIOLATION OF COURT ORDER</td>
      <td>Consensual</td>
    </tr>
    <tr>
      <th>19</th>
      <td>LETTERS, LEWD</td>
      <td>Disturbance</td>
    </tr>
    <tr>
      <th>20</th>
      <td>TRESPASSING</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>21</th>
      <td>VIOLATION OF RESTRAINING ORDER</td>
      <td>Disturbance</td>
    </tr>
    <tr>
      <th>22</th>
      <td>THEFT, PERSON</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>23</th>
      <td>BURGLARY, ATTEMPTED</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>24</th>
      <td>BRANDISH WEAPON</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>25</th>
      <td>INTIMATE PARTNER - AGGRAVATED ASSAULT</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>26</th>
      <td>BIKE - STOLEN</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>27</th>
      <td>ATTEMPTED ROBBERY</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>28</th>
      <td>BATTERY WITH SEXUAL CONTACT</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>29</th>
      <td>RAPE, FORCIBLE</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>112</th>
      <td>LYNCHING</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>113</th>
      <td>DRUGS, TO A MINOR</td>
      <td>Disturbance</td>
    </tr>
    <tr>
      <th>114</th>
      <td>DISRUPT SCHOOL</td>
      <td>Disturbance</td>
    </tr>
    <tr>
      <th>115</th>
      <td>CHILD PORNOGRAPHY</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>116</th>
      <td>TELEPHONE PROPERTY - DAMAGE</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>117</th>
      <td>THEFT, COIN MACHINE - GRAND ($950.01 &amp; OVER)</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>118</th>
      <td>BIKE - ATTEMPTED STOLEN</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>119</th>
      <td>BRIBERY</td>
      <td>White Collar</td>
    </tr>
    <tr>
      <th>120</th>
      <td>DRUNK ROLL</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>121</th>
      <td>BEASTIALITY, CRIME AGAINST NATURE SEXUAL ASSLT...</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>122</th>
      <td>REPLICA FIREARMS(SALE,DISPLAY,MANUFACTURE OR D...</td>
      <td>White Collar</td>
    </tr>
    <tr>
      <th>123</th>
      <td>LYNCHING - ATTEMPTED</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>124</th>
      <td>PETTY THEFT - AUTO REPAIR</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>125</th>
      <td>THEFT, COIN MACHINE - ATTEMPT</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>126</th>
      <td>PICKPOCKET, ATTEMPT</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>127</th>
      <td>FAILURE TO DISPERSE</td>
      <td>Disturbance</td>
    </tr>
    <tr>
      <th>128</th>
      <td>TILL TAP - GRAND THEFT ($950.01 &amp; OVER)</td>
      <td>White Collar</td>
    </tr>
    <tr>
      <th>129</th>
      <td>GRAND THEFT / AUTO REPAIR</td>
      <td>Property</td>
    </tr>
    <tr>
      <th>130</th>
      <td>INCITING A RIOT</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>131</th>
      <td>HUMAN TRAFFICKING - INVOLUNTARY SERVITUDE</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>132</th>
      <td>BIGAMY</td>
      <td>Consensual</td>
    </tr>
    <tr>
      <th>133</th>
      <td>DISHONEST EMPLOYEE ATTEMPTED THEFT</td>
      <td>White Collar</td>
    </tr>
    <tr>
      <th>134</th>
      <td>INCEST (SEXUAL ACTS BETWEEN BLOOD RELATIVES)</td>
      <td>Consensual</td>
    </tr>
    <tr>
      <th>135</th>
      <td>ABORTION/ILLEGAL</td>
      <td>Consensual</td>
    </tr>
    <tr>
      <th>136</th>
      <td>MANSLAUGHTER, NEGLIGENT</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>137</th>
      <td>BLOCKING DOOR INDUCTION CENTER</td>
      <td>Disturbance</td>
    </tr>
    <tr>
      <th>138</th>
      <td>TILL TAP - ATTEMPT</td>
      <td>White Collar</td>
    </tr>
    <tr>
      <th>139</th>
      <td>TRAIN WRECKING</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>140</th>
      <td>FIREARMS RESTRAINING ORDER (FIREARMS RO)</td>
      <td>Violent</td>
    </tr>
    <tr>
      <th>141</th>
      <td>DRUNK ROLL - ATTEMPT</td>
      <td>Property</td>
    </tr>
  </tbody>
</table>
<p>142 rows × 2 columns</p>
</div>




```python
la_df_cat = la_df_laconic.merge(la_lut, on="Crime Code Description", how="outer")
la_df_cat["Year"]=la_df_cat["Date Occurred"].map(lambda x: str(x)[-4:])
la_df_cat
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DR Number</th>
      <th>Date Occurred</th>
      <th>Crime Code Description</th>
      <th>Category</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>809.0</td>
      <td>01/16/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>1</th>
      <td>150109804.0</td>
      <td>03/29/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>2</th>
      <td>150115324.0</td>
      <td>06/23/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>3</th>
      <td>150116489.0</td>
      <td>07/10/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>4</th>
      <td>150116490.0</td>
      <td>07/10/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>5</th>
      <td>150116494.0</td>
      <td>07/11/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>6</th>
      <td>150116696.0</td>
      <td>07/13/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>7</th>
      <td>150128751.0</td>
      <td>12/30/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>8</th>
      <td>150115675.0</td>
      <td>06/28/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>9</th>
      <td>150307045.0</td>
      <td>02/19/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>10</th>
      <td>150411088.0</td>
      <td>06/17/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>11</th>
      <td>150125362.0</td>
      <td>11/13/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>12</th>
      <td>150113111.0</td>
      <td>05/19/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>13</th>
      <td>150506835.0</td>
      <td>03/04/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>14</th>
      <td>150508750.0</td>
      <td>04/17/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>15</th>
      <td>150511881.0</td>
      <td>06/30/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>16</th>
      <td>150615034.0</td>
      <td>06/22/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>17</th>
      <td>150616649.0</td>
      <td>07/19/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>18</th>
      <td>150106918.0</td>
      <td>02/15/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>19</th>
      <td>150206733.0</td>
      <td>02/19/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>20</th>
      <td>150116573.0</td>
      <td>07/11/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>21</th>
      <td>150218955.0</td>
      <td>10/04/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>22</th>
      <td>150306316.0</td>
      <td>02/08/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>23</th>
      <td>150113113.0</td>
      <td>05/20/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>24</th>
      <td>150116578.0</td>
      <td>07/12/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>25</th>
      <td>150124296.0</td>
      <td>10/30/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>26</th>
      <td>150210255.0</td>
      <td>04/26/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>27</th>
      <td>150406922.0</td>
      <td>03/07/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>28</th>
      <td>150407061.0</td>
      <td>03/10/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>29</th>
      <td>150126053.0</td>
      <td>11/22/2015</td>
      <td>VEHICLE - STOLEN</td>
      <td>Property</td>
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
      <th>666866</th>
      <td>171320966.0</td>
      <td>09/24/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666867</th>
      <td>171421333.0</td>
      <td>09/12/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666868</th>
      <td>171519970.0</td>
      <td>10/05/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666869</th>
      <td>171118296.0</td>
      <td>10/14/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666870</th>
      <td>171018067.0</td>
      <td>11/01/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666871</th>
      <td>171324720.0</td>
      <td>11/22/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666872</th>
      <td>171516455.0</td>
      <td>07/26/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666873</th>
      <td>171520534.0</td>
      <td>10/16/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666874</th>
      <td>171522226.0</td>
      <td>05/01/2015</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>666875</th>
      <td>171522444.0</td>
      <td>11/19/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666876</th>
      <td>171523526.0</td>
      <td>11/30/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666877</th>
      <td>170720345.0</td>
      <td>12/23/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666878</th>
      <td>170720346.0</td>
      <td>12/23/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666879</th>
      <td>170922440.0</td>
      <td>12/18/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666880</th>
      <td>171522741.0</td>
      <td>09/11/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666881</th>
      <td>180400510.0</td>
      <td>09/27/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666882</th>
      <td>171521175.0</td>
      <td>11/01/2016</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>666883</th>
      <td>181504605.0</td>
      <td>12/06/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666884</th>
      <td>170114218.0</td>
      <td>05/09/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666885</th>
      <td>182005599.0</td>
      <td>04/01/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666886</th>
      <td>181505841.0</td>
      <td>09/01/2016</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>666887</th>
      <td>171229618.0</td>
      <td>12/20/2017</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666888</th>
      <td>181500665.0</td>
      <td>07/01/2015</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>666889</th>
      <td>181707510.0</td>
      <td>06/15/2015</td>
      <td>LEWD/LASCIVIOUS ACTS WITH CHILD</td>
      <td>Violent</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>666890</th>
      <td>172114771.0</td>
      <td>12/27/2016</td>
      <td>TRAIN WRECKING</td>
      <td>Violent</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>666891</th>
      <td>181806450.0</td>
      <td>06/01/2017</td>
      <td>TRAIN WRECKING</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666892</th>
      <td>171818746.0</td>
      <td>09/13/2017</td>
      <td>FIREARMS RESTRAINING ORDER (FIREARMS RO)</td>
      <td>Violent</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666893</th>
      <td>170919436.0</td>
      <td>10/28/2017</td>
      <td>ABORTION/ILLEGAL</td>
      <td>Consensual</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666894</th>
      <td>171323198.0</td>
      <td>10/27/2017</td>
      <td>TILL TAP - ATTEMPT</td>
      <td>White Collar</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>666895</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>DRUNK ROLL - ATTEMPT</td>
      <td>Property</td>
      <td>nan</td>
    </tr>
  </tbody>
</table>
<p>666896 rows × 5 columns</p>
</div>




```python
la_df_cat["Category"].value_counts()
```




    Property        430953
    Violent         186775
    Disturbance      20314
    White Collar     17274
    Consensual        5654
    Name: Category, dtype: int64




```python
la_df_cat.to_csv("LA_Crime_Category_2015-2017.csv")
```
