

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


```python
la_df = pd.read_csv("LA_15-17_Merged.csv")
chi_df = pd.read_csv("Chicago_15-17_Merged.csv")
```


```python
la_df
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
      <th>Date</th>
      <th>Temp (F) avg</th>
      <th>Event</th>
      <th>Consensual</th>
      <th>Disturbance</th>
      <th>Property</th>
      <th>Violent</th>
      <th>White Collar</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015-01-01</td>
      <td>48</td>
      <td>Clear</td>
      <td>12.0</td>
      <td>48.0</td>
      <td>833.0</td>
      <td>381.0</td>
      <td>25.0</td>
      <td>1299.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015-01-02</td>
      <td>50</td>
      <td>Clear</td>
      <td>3.0</td>
      <td>14.0</td>
      <td>347.0</td>
      <td>122.0</td>
      <td>26.0</td>
      <td>512.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015-01-03</td>
      <td>52</td>
      <td>Clear</td>
      <td>2.0</td>
      <td>15.0</td>
      <td>319.0</td>
      <td>139.0</td>
      <td>14.0</td>
      <td>489.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015-01-04</td>
      <td>56</td>
      <td>Clear</td>
      <td>5.0</td>
      <td>11.0</td>
      <td>325.0</td>
      <td>151.0</td>
      <td>14.0</td>
      <td>506.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015-01-05</td>
      <td>66</td>
      <td>Clear</td>
      <td>5.0</td>
      <td>21.0</td>
      <td>432.0</td>
      <td>141.0</td>
      <td>21.0</td>
      <td>620.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2015-01-06</td>
      <td>71</td>
      <td>Clear</td>
      <td>3.0</td>
      <td>9.0</td>
      <td>324.0</td>
      <td>148.0</td>
      <td>18.0</td>
      <td>502.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2015-01-07</td>
      <td>69</td>
      <td>Clear</td>
      <td>4.0</td>
      <td>20.0</td>
      <td>342.0</td>
      <td>125.0</td>
      <td>23.0</td>
      <td>514.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2015-01-08</td>
      <td>63</td>
      <td>Clear</td>
      <td>5.0</td>
      <td>16.0</td>
      <td>376.0</td>
      <td>118.0</td>
      <td>24.0</td>
      <td>539.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2015-01-09</td>
      <td>64</td>
      <td>Clear</td>
      <td>8.0</td>
      <td>12.0</td>
      <td>425.0</td>
      <td>156.0</td>
      <td>15.0</td>
      <td>616.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2015-01-10</td>
      <td>58</td>
      <td>Rain</td>
      <td>2.0</td>
      <td>17.0</td>
      <td>411.0</td>
      <td>162.0</td>
      <td>11.0</td>
      <td>603.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2015-01-11</td>
      <td>60</td>
      <td>Rain</td>
      <td>3.0</td>
      <td>10.0</td>
      <td>319.0</td>
      <td>160.0</td>
      <td>11.0</td>
      <td>503.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2015-01-12</td>
      <td>60</td>
      <td>Clear</td>
      <td>5.0</td>
      <td>15.0</td>
      <td>363.0</td>
      <td>119.0</td>
      <td>15.0</td>
      <td>517.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2015-01-13</td>
      <td>61</td>
      <td>Clear</td>
      <td>6.0</td>
      <td>20.0</td>
      <td>328.0</td>
      <td>127.0</td>
      <td>15.0</td>
      <td>496.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2015-01-14</td>
      <td>60</td>
      <td>Clear</td>
      <td>2.0</td>
      <td>21.0</td>
      <td>382.0</td>
      <td>148.0</td>
      <td>11.0</td>
      <td>564.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2015-01-15</td>
      <td>64</td>
      <td>Clear</td>
      <td>8.0</td>
      <td>25.0</td>
      <td>454.0</td>
      <td>122.0</td>
      <td>16.0</td>
      <td>625.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2015-01-16</td>
      <td>64</td>
      <td>Clear</td>
      <td>5.0</td>
      <td>18.0</td>
      <td>403.0</td>
      <td>132.0</td>
      <td>15.0</td>
      <td>573.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2015-01-17</td>
      <td>64</td>
      <td>Clear</td>
      <td>3.0</td>
      <td>14.0</td>
      <td>368.0</td>
      <td>167.0</td>
      <td>10.0</td>
      <td>562.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2015-01-18</td>
      <td>64</td>
      <td>Clear</td>
      <td>4.0</td>
      <td>10.0</td>
      <td>348.0</td>
      <td>136.0</td>
      <td>7.0</td>
      <td>505.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2015-01-19</td>
      <td>61</td>
      <td>Clear</td>
      <td>5.0</td>
      <td>16.0</td>
      <td>312.0</td>
      <td>141.0</td>
      <td>8.0</td>
      <td>482.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2015-01-20</td>
      <td>58</td>
      <td>Fog</td>
      <td>3.0</td>
      <td>17.0</td>
      <td>438.0</td>
      <td>122.0</td>
      <td>14.0</td>
      <td>594.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2015-01-21</td>
      <td>63</td>
      <td>Clear</td>
      <td>3.0</td>
      <td>23.0</td>
      <td>393.0</td>
      <td>129.0</td>
      <td>10.0</td>
      <td>558.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2015-01-22</td>
      <td>61</td>
      <td>Clear</td>
      <td>6.0</td>
      <td>15.0</td>
      <td>364.0</td>
      <td>157.0</td>
      <td>21.0</td>
      <td>563.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2015-01-23</td>
      <td>63</td>
      <td>Clear</td>
      <td>13.0</td>
      <td>17.0</td>
      <td>411.0</td>
      <td>129.0</td>
      <td>8.0</td>
      <td>578.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2015-01-24</td>
      <td>66</td>
      <td>Clear</td>
      <td>7.0</td>
      <td>15.0</td>
      <td>356.0</td>
      <td>171.0</td>
      <td>17.0</td>
      <td>566.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2015-01-25</td>
      <td>66</td>
      <td>Clear</td>
      <td>6.0</td>
      <td>18.0</td>
      <td>352.0</td>
      <td>158.0</td>
      <td>6.0</td>
      <td>540.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2015-01-26</td>
      <td>69</td>
      <td>Rain</td>
      <td>2.0</td>
      <td>14.0</td>
      <td>431.0</td>
      <td>170.0</td>
      <td>21.0</td>
      <td>638.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2015-01-27</td>
      <td>66</td>
      <td>Clear</td>
      <td>3.0</td>
      <td>28.0</td>
      <td>377.0</td>
      <td>141.0</td>
      <td>21.0</td>
      <td>570.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2015-01-28</td>
      <td>66</td>
      <td>Clear</td>
      <td>6.0</td>
      <td>18.0</td>
      <td>358.0</td>
      <td>137.0</td>
      <td>9.0</td>
      <td>528.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2015-01-29</td>
      <td>68</td>
      <td>Rain</td>
      <td>8.0</td>
      <td>16.0</td>
      <td>370.0</td>
      <td>150.0</td>
      <td>14.0</td>
      <td>558.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2015-01-30</td>
      <td>65</td>
      <td>Rain</td>
      <td>5.0</td>
      <td>18.0</td>
      <td>415.0</td>
      <td>154.0</td>
      <td>16.0</td>
      <td>608.0</td>
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
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1066</th>
      <td>2017-12-02</td>
      <td>64</td>
      <td>Clear</td>
      <td>3.0</td>
      <td>14.0</td>
      <td>396.0</td>
      <td>186.0</td>
      <td>16.0</td>
      <td>615.0</td>
    </tr>
    <tr>
      <th>1067</th>
      <td>2017-12-03</td>
      <td>61</td>
      <td>Fog</td>
      <td>4.0</td>
      <td>19.0</td>
      <td>371.0</td>
      <td>174.0</td>
      <td>11.0</td>
      <td>579.0</td>
    </tr>
    <tr>
      <th>1068</th>
      <td>2017-12-04</td>
      <td>62</td>
      <td>Clear</td>
      <td>1.0</td>
      <td>19.0</td>
      <td>403.0</td>
      <td>143.0</td>
      <td>21.0</td>
      <td>587.0</td>
    </tr>
    <tr>
      <th>1069</th>
      <td>2017-12-05</td>
      <td>58</td>
      <td>Clear</td>
      <td>10.0</td>
      <td>12.0</td>
      <td>386.0</td>
      <td>154.0</td>
      <td>15.0</td>
      <td>577.0</td>
    </tr>
    <tr>
      <th>1070</th>
      <td>2017-12-06</td>
      <td>60</td>
      <td>Clear</td>
      <td>7.0</td>
      <td>16.0</td>
      <td>385.0</td>
      <td>156.0</td>
      <td>11.0</td>
      <td>575.0</td>
    </tr>
    <tr>
      <th>1071</th>
      <td>2017-12-07</td>
      <td>62</td>
      <td>Clear</td>
      <td>5.0</td>
      <td>17.0</td>
      <td>371.0</td>
      <td>155.0</td>
      <td>12.0</td>
      <td>560.0</td>
    </tr>
    <tr>
      <th>1072</th>
      <td>2017-12-08</td>
      <td>63</td>
      <td>Clear</td>
      <td>6.0</td>
      <td>19.0</td>
      <td>426.0</td>
      <td>151.0</td>
      <td>6.0</td>
      <td>608.0</td>
    </tr>
    <tr>
      <th>1073</th>
      <td>2017-12-09</td>
      <td>67</td>
      <td>Clear</td>
      <td>3.0</td>
      <td>18.0</td>
      <td>391.0</td>
      <td>200.0</td>
      <td>9.0</td>
      <td>621.0</td>
    </tr>
    <tr>
      <th>1074</th>
      <td>2017-12-10</td>
      <td>66</td>
      <td>Clear</td>
      <td>6.0</td>
      <td>19.0</td>
      <td>396.0</td>
      <td>198.0</td>
      <td>8.0</td>
      <td>627.0</td>
    </tr>
    <tr>
      <th>1075</th>
      <td>2017-12-11</td>
      <td>67</td>
      <td>Clear</td>
      <td>10.0</td>
      <td>25.0</td>
      <td>384.0</td>
      <td>173.0</td>
      <td>11.0</td>
      <td>603.0</td>
    </tr>
    <tr>
      <th>1076</th>
      <td>2017-12-12</td>
      <td>68</td>
      <td>Clear</td>
      <td>5.0</td>
      <td>24.0</td>
      <td>410.0</td>
      <td>156.0</td>
      <td>16.0</td>
      <td>611.0</td>
    </tr>
    <tr>
      <th>1077</th>
      <td>2017-12-13</td>
      <td>65</td>
      <td>Clear</td>
      <td>8.0</td>
      <td>16.0</td>
      <td>421.0</td>
      <td>143.0</td>
      <td>13.0</td>
      <td>601.0</td>
    </tr>
    <tr>
      <th>1078</th>
      <td>2017-12-14</td>
      <td>62</td>
      <td>Clear</td>
      <td>6.0</td>
      <td>18.0</td>
      <td>421.0</td>
      <td>153.0</td>
      <td>8.0</td>
      <td>606.0</td>
    </tr>
    <tr>
      <th>1079</th>
      <td>2017-12-15</td>
      <td>66</td>
      <td>Clear</td>
      <td>6.0</td>
      <td>22.0</td>
      <td>456.0</td>
      <td>213.0</td>
      <td>29.0</td>
      <td>726.0</td>
    </tr>
    <tr>
      <th>1080</th>
      <td>2017-12-16</td>
      <td>60</td>
      <td>Clear</td>
      <td>7.0</td>
      <td>17.0</td>
      <td>373.0</td>
      <td>152.0</td>
      <td>14.0</td>
      <td>563.0</td>
    </tr>
    <tr>
      <th>1081</th>
      <td>2017-12-17</td>
      <td>60</td>
      <td>Clear</td>
      <td>6.0</td>
      <td>20.0</td>
      <td>379.0</td>
      <td>178.0</td>
      <td>11.0</td>
      <td>594.0</td>
    </tr>
    <tr>
      <th>1082</th>
      <td>2017-12-18</td>
      <td>61</td>
      <td>Clear</td>
      <td>1.0</td>
      <td>20.0</td>
      <td>469.0</td>
      <td>154.0</td>
      <td>17.0</td>
      <td>661.0</td>
    </tr>
    <tr>
      <th>1083</th>
      <td>2017-12-19</td>
      <td>58</td>
      <td>Clear</td>
      <td>6.0</td>
      <td>16.0</td>
      <td>399.0</td>
      <td>133.0</td>
      <td>21.0</td>
      <td>575.0</td>
    </tr>
    <tr>
      <th>1084</th>
      <td>2017-12-20</td>
      <td>54</td>
      <td>Rain</td>
      <td>2.0</td>
      <td>17.0</td>
      <td>451.0</td>
      <td>151.0</td>
      <td>23.0</td>
      <td>644.0</td>
    </tr>
    <tr>
      <th>1085</th>
      <td>2017-12-21</td>
      <td>54</td>
      <td>Rain</td>
      <td>1.0</td>
      <td>9.0</td>
      <td>413.0</td>
      <td>151.0</td>
      <td>14.0</td>
      <td>588.0</td>
    </tr>
    <tr>
      <th>1086</th>
      <td>2017-12-22</td>
      <td>53</td>
      <td>Clear</td>
      <td>3.0</td>
      <td>16.0</td>
      <td>449.0</td>
      <td>175.0</td>
      <td>11.0</td>
      <td>654.0</td>
    </tr>
    <tr>
      <th>1087</th>
      <td>2017-12-23</td>
      <td>57</td>
      <td>Clear</td>
      <td>3.0</td>
      <td>12.0</td>
      <td>371.0</td>
      <td>177.0</td>
      <td>5.0</td>
      <td>568.0</td>
    </tr>
    <tr>
      <th>1088</th>
      <td>2017-12-24</td>
      <td>60</td>
      <td>Clear</td>
      <td>4.0</td>
      <td>19.0</td>
      <td>370.0</td>
      <td>157.0</td>
      <td>7.0</td>
      <td>557.0</td>
    </tr>
    <tr>
      <th>1089</th>
      <td>2017-12-25</td>
      <td>57</td>
      <td>Clear</td>
      <td>8.0</td>
      <td>10.0</td>
      <td>302.0</td>
      <td>178.0</td>
      <td>3.0</td>
      <td>501.0</td>
    </tr>
    <tr>
      <th>1090</th>
      <td>2017-12-26</td>
      <td>57</td>
      <td>Clear</td>
      <td>2.0</td>
      <td>17.0</td>
      <td>374.0</td>
      <td>129.0</td>
      <td>10.0</td>
      <td>532.0</td>
    </tr>
    <tr>
      <th>1091</th>
      <td>2017-12-27</td>
      <td>61</td>
      <td>Clear</td>
      <td>7.0</td>
      <td>12.0</td>
      <td>354.0</td>
      <td>143.0</td>
      <td>14.0</td>
      <td>530.0</td>
    </tr>
    <tr>
      <th>1092</th>
      <td>2017-12-28</td>
      <td>63</td>
      <td>Clear</td>
      <td>3.0</td>
      <td>17.0</td>
      <td>380.0</td>
      <td>161.0</td>
      <td>10.0</td>
      <td>571.0</td>
    </tr>
    <tr>
      <th>1093</th>
      <td>2017-12-29</td>
      <td>68</td>
      <td>Clear</td>
      <td>6.0</td>
      <td>16.0</td>
      <td>420.0</td>
      <td>168.0</td>
      <td>11.0</td>
      <td>621.0</td>
    </tr>
    <tr>
      <th>1094</th>
      <td>2017-12-30</td>
      <td>61</td>
      <td>Fog</td>
      <td>7.0</td>
      <td>12.0</td>
      <td>368.0</td>
      <td>165.0</td>
      <td>8.0</td>
      <td>560.0</td>
    </tr>
    <tr>
      <th>1095</th>
      <td>2017-12-31</td>
      <td>59</td>
      <td>Fog</td>
      <td>4.0</td>
      <td>11.0</td>
      <td>360.0</td>
      <td>168.0</td>
      <td>7.0</td>
      <td>550.0</td>
    </tr>
  </tbody>
</table>
<p>1096 rows × 9 columns</p>
</div>




```python
chi_df
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
      <th>Date</th>
      <th>Temp (F) avg</th>
      <th>Event</th>
      <th>Consensual</th>
      <th>Disturbance</th>
      <th>Property</th>
      <th>Violent</th>
      <th>White Collar</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015-01-01</td>
      <td>23</td>
      <td>Clear</td>
      <td>67</td>
      <td>11.0</td>
      <td>334</td>
      <td>445</td>
      <td>177</td>
      <td>1124.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015-01-02</td>
      <td>25</td>
      <td>Clear</td>
      <td>101</td>
      <td>13.0</td>
      <td>306</td>
      <td>159</td>
      <td>50</td>
      <td>671.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015-01-03</td>
      <td>32</td>
      <td>Rain , Snow</td>
      <td>92</td>
      <td>11.0</td>
      <td>304</td>
      <td>175</td>
      <td>27</td>
      <td>648.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015-01-04</td>
      <td>18</td>
      <td>Fog , Snow</td>
      <td>77</td>
      <td>11.0</td>
      <td>215</td>
      <td>154</td>
      <td>19</td>
      <td>513.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015-01-05</td>
      <td>2</td>
      <td>Snow</td>
      <td>51</td>
      <td>8.0</td>
      <td>252</td>
      <td>137</td>
      <td>40</td>
      <td>521.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2015-01-06</td>
      <td>3</td>
      <td>Snow</td>
      <td>62</td>
      <td>4.0</td>
      <td>240</td>
      <td>112</td>
      <td>41</td>
      <td>502.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2015-01-07</td>
      <td>0</td>
      <td>Clear</td>
      <td>68</td>
      <td>4.0</td>
      <td>216</td>
      <td>106</td>
      <td>38</td>
      <td>472.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2015-01-08</td>
      <td>5</td>
      <td>Snow</td>
      <td>56</td>
      <td>5.0</td>
      <td>227</td>
      <td>99</td>
      <td>25</td>
      <td>445.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2015-01-09</td>
      <td>6</td>
      <td>Snow</td>
      <td>79</td>
      <td>15.0</td>
      <td>264</td>
      <td>134</td>
      <td>33</td>
      <td>586.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2015-01-10</td>
      <td>11</td>
      <td>Clear</td>
      <td>98</td>
      <td>12.0</td>
      <td>286</td>
      <td>164</td>
      <td>28</td>
      <td>644.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2015-01-11</td>
      <td>27</td>
      <td>Fog , Snow</td>
      <td>84</td>
      <td>12.0</td>
      <td>305</td>
      <td>177</td>
      <td>22</td>
      <td>648.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2015-01-12</td>
      <td>22</td>
      <td>Snow</td>
      <td>69</td>
      <td>9.0</td>
      <td>313</td>
      <td>132</td>
      <td>36</td>
      <td>606.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2015-01-13</td>
      <td>11</td>
      <td>Snow</td>
      <td>88</td>
      <td>6.0</td>
      <td>290</td>
      <td>146</td>
      <td>37</td>
      <td>609.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2015-01-14</td>
      <td>10</td>
      <td>Snow</td>
      <td>110</td>
      <td>8.0</td>
      <td>325</td>
      <td>145</td>
      <td>35</td>
      <td>674.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2015-01-15</td>
      <td>26</td>
      <td>Clear</td>
      <td>147</td>
      <td>10.0</td>
      <td>366</td>
      <td>147</td>
      <td>44</td>
      <td>758.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2015-01-16</td>
      <td>29</td>
      <td>Clear</td>
      <td>95</td>
      <td>10.0</td>
      <td>339</td>
      <td>172</td>
      <td>43</td>
      <td>708.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2015-01-17</td>
      <td>34</td>
      <td>Clear</td>
      <td>108</td>
      <td>12.0</td>
      <td>342</td>
      <td>206</td>
      <td>27</td>
      <td>741.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2015-01-18</td>
      <td>34</td>
      <td>Snow</td>
      <td>68</td>
      <td>10.0</td>
      <td>352</td>
      <td>197</td>
      <td>19</td>
      <td>694.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2015-01-19</td>
      <td>33</td>
      <td>Snow</td>
      <td>109</td>
      <td>5.0</td>
      <td>345</td>
      <td>166</td>
      <td>35</td>
      <td>707.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2015-01-20</td>
      <td>33</td>
      <td>Clear</td>
      <td>75</td>
      <td>9.0</td>
      <td>403</td>
      <td>196</td>
      <td>48</td>
      <td>791.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2015-01-21</td>
      <td>31</td>
      <td>Snow</td>
      <td>84</td>
      <td>11.0</td>
      <td>366</td>
      <td>183</td>
      <td>51</td>
      <td>741.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2015-01-22</td>
      <td>30</td>
      <td>Clear</td>
      <td>105</td>
      <td>13.0</td>
      <td>354</td>
      <td>179</td>
      <td>47</td>
      <td>748.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2015-01-23</td>
      <td>30</td>
      <td>Clear</td>
      <td>110</td>
      <td>17.0</td>
      <td>379</td>
      <td>208</td>
      <td>38</td>
      <td>799.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2015-01-24</td>
      <td>36</td>
      <td>Clear</td>
      <td>115</td>
      <td>12.0</td>
      <td>364</td>
      <td>182</td>
      <td>33</td>
      <td>756.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2015-01-25</td>
      <td>29</td>
      <td>Snow</td>
      <td>69</td>
      <td>7.0</td>
      <td>303</td>
      <td>187</td>
      <td>33</td>
      <td>644.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2015-01-26</td>
      <td>21</td>
      <td>Snow</td>
      <td>67</td>
      <td>12.0</td>
      <td>328</td>
      <td>164</td>
      <td>40</td>
      <td>656.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2015-01-27</td>
      <td>26</td>
      <td>Snow</td>
      <td>103</td>
      <td>21.0</td>
      <td>283</td>
      <td>163</td>
      <td>45</td>
      <td>673.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2015-01-28</td>
      <td>27</td>
      <td>Rain</td>
      <td>97</td>
      <td>7.0</td>
      <td>304</td>
      <td>147</td>
      <td>42</td>
      <td>645.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2015-01-29</td>
      <td>32</td>
      <td>Snow</td>
      <td>116</td>
      <td>13.0</td>
      <td>309</td>
      <td>180</td>
      <td>42</td>
      <td>702.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2015-01-30</td>
      <td>24</td>
      <td>Clear</td>
      <td>117</td>
      <td>11.0</td>
      <td>311</td>
      <td>174</td>
      <td>48</td>
      <td>714.0</td>
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
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1066</th>
      <td>2017-12-02</td>
      <td>44</td>
      <td>Clear</td>
      <td>56</td>
      <td>7.0</td>
      <td>407</td>
      <td>196</td>
      <td>47</td>
      <td>751.0</td>
    </tr>
    <tr>
      <th>1067</th>
      <td>2017-12-03</td>
      <td>44</td>
      <td>Clear</td>
      <td>25</td>
      <td>9.0</td>
      <td>352</td>
      <td>222</td>
      <td>31</td>
      <td>675.0</td>
    </tr>
    <tr>
      <th>1068</th>
      <td>2017-12-04</td>
      <td>55</td>
      <td>Rain , Thunderstorm</td>
      <td>58</td>
      <td>3.0</td>
      <td>445</td>
      <td>211</td>
      <td>54</td>
      <td>805.0</td>
    </tr>
    <tr>
      <th>1069</th>
      <td>2017-12-05</td>
      <td>36</td>
      <td>Clear</td>
      <td>44</td>
      <td>8.0</td>
      <td>360</td>
      <td>172</td>
      <td>69</td>
      <td>696.0</td>
    </tr>
    <tr>
      <th>1070</th>
      <td>2017-12-06</td>
      <td>31</td>
      <td>Clear</td>
      <td>43</td>
      <td>4.0</td>
      <td>361</td>
      <td>193</td>
      <td>53</td>
      <td>705.0</td>
    </tr>
    <tr>
      <th>1071</th>
      <td>2017-12-07</td>
      <td>24</td>
      <td>Snow</td>
      <td>32</td>
      <td>5.0</td>
      <td>334</td>
      <td>160</td>
      <td>52</td>
      <td>620.0</td>
    </tr>
    <tr>
      <th>1072</th>
      <td>2017-12-08</td>
      <td>28</td>
      <td>Snow</td>
      <td>41</td>
      <td>6.0</td>
      <td>394</td>
      <td>198</td>
      <td>50</td>
      <td>727.0</td>
    </tr>
    <tr>
      <th>1073</th>
      <td>2017-12-09</td>
      <td>26</td>
      <td>Snow</td>
      <td>31</td>
      <td>10.0</td>
      <td>365</td>
      <td>175</td>
      <td>45</td>
      <td>655.0</td>
    </tr>
    <tr>
      <th>1074</th>
      <td>2017-12-10</td>
      <td>28</td>
      <td>Clear</td>
      <td>37</td>
      <td>10.0</td>
      <td>346</td>
      <td>181</td>
      <td>42</td>
      <td>660.0</td>
    </tr>
    <tr>
      <th>1075</th>
      <td>2017-12-11</td>
      <td>31</td>
      <td>Snow</td>
      <td>27</td>
      <td>8.0</td>
      <td>405</td>
      <td>178</td>
      <td>59</td>
      <td>729.0</td>
    </tr>
    <tr>
      <th>1076</th>
      <td>2017-12-12</td>
      <td>24</td>
      <td>Snow</td>
      <td>31</td>
      <td>5.0</td>
      <td>355</td>
      <td>177</td>
      <td>67</td>
      <td>673.0</td>
    </tr>
    <tr>
      <th>1077</th>
      <td>2017-12-13</td>
      <td>30</td>
      <td>Snow</td>
      <td>42</td>
      <td>2.0</td>
      <td>363</td>
      <td>181</td>
      <td>54</td>
      <td>690.0</td>
    </tr>
    <tr>
      <th>1078</th>
      <td>2017-12-14</td>
      <td>22</td>
      <td>Snow</td>
      <td>28</td>
      <td>4.0</td>
      <td>379</td>
      <td>185</td>
      <td>61</td>
      <td>703.0</td>
    </tr>
    <tr>
      <th>1079</th>
      <td>2017-12-15</td>
      <td>29</td>
      <td>Snow</td>
      <td>32</td>
      <td>7.0</td>
      <td>387</td>
      <td>186</td>
      <td>71</td>
      <td>756.0</td>
    </tr>
    <tr>
      <th>1080</th>
      <td>2017-12-16</td>
      <td>37</td>
      <td>Clear</td>
      <td>47</td>
      <td>6.0</td>
      <td>419</td>
      <td>199</td>
      <td>58</td>
      <td>767.0</td>
    </tr>
    <tr>
      <th>1081</th>
      <td>2017-12-17</td>
      <td>36</td>
      <td>Clear</td>
      <td>50</td>
      <td>6.0</td>
      <td>378</td>
      <td>198</td>
      <td>58</td>
      <td>721.0</td>
    </tr>
    <tr>
      <th>1082</th>
      <td>2017-12-18</td>
      <td>43</td>
      <td>Rain</td>
      <td>33</td>
      <td>3.0</td>
      <td>396</td>
      <td>169</td>
      <td>64</td>
      <td>719.0</td>
    </tr>
    <tr>
      <th>1083</th>
      <td>2017-12-19</td>
      <td>43</td>
      <td>Clear</td>
      <td>33</td>
      <td>6.0</td>
      <td>430</td>
      <td>185</td>
      <td>46</td>
      <td>751.0</td>
    </tr>
    <tr>
      <th>1084</th>
      <td>2017-12-20</td>
      <td>32</td>
      <td>Clear</td>
      <td>47</td>
      <td>9.0</td>
      <td>375</td>
      <td>173</td>
      <td>43</td>
      <td>690.0</td>
    </tr>
    <tr>
      <th>1085</th>
      <td>2017-12-21</td>
      <td>36</td>
      <td>Clear</td>
      <td>43</td>
      <td>6.0</td>
      <td>412</td>
      <td>175</td>
      <td>62</td>
      <td>733.0</td>
    </tr>
    <tr>
      <th>1086</th>
      <td>2017-12-22</td>
      <td>36</td>
      <td>Clear</td>
      <td>48</td>
      <td>9.0</td>
      <td>436</td>
      <td>179</td>
      <td>61</td>
      <td>771.0</td>
    </tr>
    <tr>
      <th>1087</th>
      <td>2017-12-23</td>
      <td>26</td>
      <td>Clear</td>
      <td>30</td>
      <td>4.0</td>
      <td>391</td>
      <td>207</td>
      <td>40</td>
      <td>710.0</td>
    </tr>
    <tr>
      <th>1088</th>
      <td>2017-12-24</td>
      <td>20</td>
      <td>Fog , Snow</td>
      <td>14</td>
      <td>1.0</td>
      <td>291</td>
      <td>149</td>
      <td>21</td>
      <td>496.0</td>
    </tr>
    <tr>
      <th>1089</th>
      <td>2017-12-25</td>
      <td>12</td>
      <td>Snow</td>
      <td>5</td>
      <td>1.0</td>
      <td>190</td>
      <td>160</td>
      <td>14</td>
      <td>391.0</td>
    </tr>
    <tr>
      <th>1090</th>
      <td>2017-12-26</td>
      <td>1</td>
      <td>Clear</td>
      <td>25</td>
      <td>9.0</td>
      <td>269</td>
      <td>136</td>
      <td>46</td>
      <td>521.0</td>
    </tr>
    <tr>
      <th>1091</th>
      <td>2017-12-27</td>
      <td>2</td>
      <td>Clear</td>
      <td>32</td>
      <td>3.0</td>
      <td>266</td>
      <td>127</td>
      <td>43</td>
      <td>511.0</td>
    </tr>
    <tr>
      <th>1092</th>
      <td>2017-12-28</td>
      <td>8</td>
      <td>Snow</td>
      <td>37</td>
      <td>6.0</td>
      <td>331</td>
      <td>122</td>
      <td>51</td>
      <td>588.0</td>
    </tr>
    <tr>
      <th>1093</th>
      <td>2017-12-29</td>
      <td>12</td>
      <td>Snow</td>
      <td>31</td>
      <td>6.0</td>
      <td>302</td>
      <td>139</td>
      <td>45</td>
      <td>560.0</td>
    </tr>
    <tr>
      <th>1094</th>
      <td>2017-12-30</td>
      <td>7</td>
      <td>Snow</td>
      <td>36</td>
      <td>6.0</td>
      <td>302</td>
      <td>173</td>
      <td>60</td>
      <td>612.0</td>
    </tr>
    <tr>
      <th>1095</th>
      <td>2017-12-31</td>
      <td>6</td>
      <td>Clear</td>
      <td>32</td>
      <td>3.0</td>
      <td>287</td>
      <td>171</td>
      <td>23</td>
      <td>541.0</td>
    </tr>
  </tbody>
</table>
<p>1096 rows × 9 columns</p>
</div>




```python
plt.plot(la_df["Date"],la_df["Temp (F) avg"])
plt.plot(chi_df["Date"],chi_df["Temp (F) avg"],alpha=0.5)
plt.title("Crime Occurences in Temperature")
plt.xlabel("Date")
plt.ylabel("Temperature (F)")
plt.show()
plt.savefig("Crime_Temp_Line.png")

```


![png](output_4_0.png)



    <matplotlib.figure.Figure at 0x11608df60>



```python
plt.scatter(la_df["Temp (F) avg"], la_df["Total"],s=10,marker="x",alpha=0.2,label="LA")
plt.scatter(chi_df["Temp (F) avg"], chi_df["Total"],s=10,marker="+",alpha=0.2,label="Chicago")
plt.xlabel("Temperature (F)")
plt.ylabel("Total Crimes")
plt.title("Crime v. Temperature")
plt.legend()
plt.show()
```


![png](output_5_0.png)



```python
plt.scatter(la_df["Temp (F) avg"], la_df["Consensual"],s=10,marker="+")
plt.scatter(la_df["Temp (F) avg"], la_df["White Collar"],s=10,marker="x")
plt.scatter(la_df["Temp (F) avg"], la_df["Violent"],s=10,marker="x")
plt.scatter(la_df["Temp (F) avg"], la_df["Property"],s=10,marker="x")
plt.scatter(la_df["Temp (F) avg"], la_df["Disturbance"],s=10,marker="x")
plt.title("LA: Category of Crime_Temp")
plt.ylabel("Crime")
plt.xlabel("Temperature(F)")
plt.legend()
plt.show()
```


![png](output_6_0.png)



```python
#plt.scatter(chi_df["Temp (F) avg"], chi_df["Consensual"],s=10,marker="+")
#plt.scatter(chi_df["Temp (F) avg"], chi_df["White Collar"],s=10,marker="x")
#plt.scatter(chi_df["Temp (F) avg"], chi_df["Violent"],s=10,marker="x")
#plt.scatter(chi_df["Temp (F) avg"], chi_df["Property"],s=10,marker="x")
#plt.scatter(chi_df["Temp (F) avg"], chi_df["Disturbance"],s=10,marker="x")
plt.legend()
plt.show()
```

    No handles with labels found to put in legend.



![png](output_7_1.png)



```python
chi_temp = chi_df.groupby("Temp (F) avg").mean()
```


```python
plt.plot(chi_temp["Total"],linestyle="--")
plt.plot(chi_temp["Violent"])
plt.plot(chi_temp["Property"])
plt.plot(chi_temp["Disturbance"])
plt.plot(chi_temp["Consensual"])
plt.plot(chi_temp["White Collar"])
plt.title("Chicago:Crime Category v. Temperature")
plt.xlabel("Temperature (F)")
plt.ylabel("Average Crime Occurence")
plt.legend()
plt.show()
```


![png](output_9_0.png)



```python
plt.stackplot(chi_temp.index,[chi_temp["Violent"],chi_temp["Property"],chi_temp["Consensual"],
                              chi_temp["White Collar"],chi_temp["Disturbance"]])
plt.title("Chicago: Crime Category v. Temp")
plt.xlabel("Temperature (F)")
plt.ylabel("Average Occurences of Crime")
plt.legend()
plt.show()
```

    No handles with labels found to put in legend.



![png](output_10_1.png)



```python
la_temp = la_df.groupby("Temp (F) avg").mean()
```


```python
plt.plot(la_temp["Total"], linestyle="--")
plt.plot(la_temp["Violent"])
plt.plot(la_temp["Property"])
plt.plot(la_temp["Disturbance"])
plt.plot(la_temp["Consensual"])
plt.plot(la_temp["White Collar"])
plt.title("LA: Crime Category v. Temp")
plt.xlabel("Temperature (F)")
plt.ylabel("Average Occurences of Crime")
plt.legend()
plt.show()
```


![png](output_12_0.png)



```python
plt.stackplot(la_temp.index,[la_temp["Violent"],la_temp["Property"],la_temp["Consensual"],
                              la_temp["White Collar"],la_temp["Disturbance"]])
plt.title("LA: Crime Category v. Temp")
plt.xlabel("Temperature (F)")
plt.ylabel("Average Occurences of Crime")
plt.legend()
plt.show()
```

    No handles with labels found to put in legend.



![png](output_13_1.png)



```python
x1 = list(chi_df["Event"].value_counts().index)

chi_df["Clear"]=["Clear" in x for x in chi_df["Event"]]
chi_df["Thunder"]=["Thunder" in x for x in chi_df["Event"]]
chi_df["Fog"]=["Fog" in x for x in chi_df["Event"]]
chi_df["Rain"]=["Rain" in x for x in chi_df["Event"]]
chi_df["Hail"]=["Hail" in x for x in chi_df["Event"]]

#chi_df.loc[chi_df["Thunder"]==True]
chi_df.head(15)
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
      <th>Date</th>
      <th>Temp (F) avg</th>
      <th>Event</th>
      <th>Consensual</th>
      <th>Disturbance</th>
      <th>Property</th>
      <th>Violent</th>
      <th>White Collar</th>
      <th>Total</th>
      <th>Clear</th>
      <th>Thunder</th>
      <th>Fog</th>
      <th>Rain</th>
      <th>Hail</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015-01-01</td>
      <td>23</td>
      <td>Clear</td>
      <td>67</td>
      <td>11.0</td>
      <td>334</td>
      <td>445</td>
      <td>177</td>
      <td>1124.0</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2015-01-02</td>
      <td>25</td>
      <td>Clear</td>
      <td>101</td>
      <td>13.0</td>
      <td>306</td>
      <td>159</td>
      <td>50</td>
      <td>671.0</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2015-01-03</td>
      <td>32</td>
      <td>Rain , Snow</td>
      <td>92</td>
      <td>11.0</td>
      <td>304</td>
      <td>175</td>
      <td>27</td>
      <td>648.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2015-01-04</td>
      <td>18</td>
      <td>Fog , Snow</td>
      <td>77</td>
      <td>11.0</td>
      <td>215</td>
      <td>154</td>
      <td>19</td>
      <td>513.0</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2015-01-05</td>
      <td>2</td>
      <td>Snow</td>
      <td>51</td>
      <td>8.0</td>
      <td>252</td>
      <td>137</td>
      <td>40</td>
      <td>521.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2015-01-06</td>
      <td>3</td>
      <td>Snow</td>
      <td>62</td>
      <td>4.0</td>
      <td>240</td>
      <td>112</td>
      <td>41</td>
      <td>502.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2015-01-07</td>
      <td>0</td>
      <td>Clear</td>
      <td>68</td>
      <td>4.0</td>
      <td>216</td>
      <td>106</td>
      <td>38</td>
      <td>472.0</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2015-01-08</td>
      <td>5</td>
      <td>Snow</td>
      <td>56</td>
      <td>5.0</td>
      <td>227</td>
      <td>99</td>
      <td>25</td>
      <td>445.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2015-01-09</td>
      <td>6</td>
      <td>Snow</td>
      <td>79</td>
      <td>15.0</td>
      <td>264</td>
      <td>134</td>
      <td>33</td>
      <td>586.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2015-01-10</td>
      <td>11</td>
      <td>Clear</td>
      <td>98</td>
      <td>12.0</td>
      <td>286</td>
      <td>164</td>
      <td>28</td>
      <td>644.0</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2015-01-11</td>
      <td>27</td>
      <td>Fog , Snow</td>
      <td>84</td>
      <td>12.0</td>
      <td>305</td>
      <td>177</td>
      <td>22</td>
      <td>648.0</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2015-01-12</td>
      <td>22</td>
      <td>Snow</td>
      <td>69</td>
      <td>9.0</td>
      <td>313</td>
      <td>132</td>
      <td>36</td>
      <td>606.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2015-01-13</td>
      <td>11</td>
      <td>Snow</td>
      <td>88</td>
      <td>6.0</td>
      <td>290</td>
      <td>146</td>
      <td>37</td>
      <td>609.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2015-01-14</td>
      <td>10</td>
      <td>Snow</td>
      <td>110</td>
      <td>8.0</td>
      <td>325</td>
      <td>145</td>
      <td>35</td>
      <td>674.0</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2015-01-15</td>
      <td>26</td>
      <td>Clear</td>
      <td>147</td>
      <td>10.0</td>
      <td>366</td>
      <td>147</td>
      <td>44</td>
      <td>758.0</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
chi_thunder = chi_df.loc[chi_df["Thunder"]==True]
plt.scatter(chi_thunder["Temp (F) avg"],chi_thunder["Total"],s=5)
plt.scatter(chi_thunder["Temp (F) avg"],chi_thunder["Violent"],s=5)
plt.scatter(chi_thunder["Temp (F) avg"],chi_thunder["Property"],s=5)
plt.scatter(chi_thunder["Temp (F) avg"],chi_thunder["Consensual"],s=5)
plt.scatter(chi_thunder["Temp (F) avg"],chi_thunder["White Collar"],s=5)
plt.scatter(chi_thunder["Temp (F) avg"],chi_thunder["Disturbance"],s=5)
plt.title("Chicago: Crime Category v. Temp")
plt.xlabel("Temperature (F)")
plt.ylabel("Average Occurences of Crime")
plt.legend()
plt.show()
```


![png](output_15_0.png)



```python
#chi_thunder = chi_df.loc[chi_df["Thunder"]==True]
chi_rain = chi_df.loc[chi_df["Rain"]==True]
chi_fog = chi_df.loc[chi_df["Fog"]==True]
chi_hail = chi_df.loc[chi_df["Hail"]==True]
chi_clear = chi_df.loc[chi_df["Clear"]==True]

chi_w_dfs = [chi_thunder, chi_rain, chi_fog, chi_hail, chi_clear]
chi_w_labels = ["Thunder", "Rain", "Fog", "Hail", "Clear"]

for x in range(len(chi_w_dfs)):
    df = chi_w_dfs[x]
    l = chi_w_labels[x]
    plt.scatter(df["Temp (F) avg"],df["Total"], s=5, label=l)
    
plt.title("Chicago: Weather Occurences v. Temp")
plt.xlabel("Temperature (F)")
plt.ylabel("Weather Occurence")
    
plt.legend()
plt.show()
```


![png](output_16_0.png)



```python
chi_df["Year"] = chi_df["Date"].map(lambda x: x[:4])
chi_df.groupby("Year").sum()
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
      <th>Temp (F) avg</th>
      <th>Consensual</th>
      <th>Disturbance</th>
      <th>Property</th>
      <th>Violent</th>
      <th>White Collar</th>
      <th>Total</th>
      <th>Clear</th>
      <th>Thunder</th>
      <th>Fog</th>
      <th>Rain</th>
      <th>Hail</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015</th>
      <td>18440</td>
      <td>29169</td>
      <td>3944.0</td>
      <td>125745</td>
      <td>71413</td>
      <td>15787</td>
      <td>263639.0</td>
      <td>197.0</td>
      <td>33.0</td>
      <td>30.0</td>
      <td>116.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>19231</td>
      <td>17977</td>
      <td>2778.0</td>
      <td>136951</td>
      <td>74908</td>
      <td>18502</td>
      <td>268426.0</td>
      <td>198.0</td>
      <td>47.0</td>
      <td>21.0</td>
      <td>124.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>19281</td>
      <td>17431</td>
      <td>2860.0</td>
      <td>136715</td>
      <td>74288</td>
      <td>18235</td>
      <td>266669.0</td>
      <td>199.0</td>
      <td>57.0</td>
      <td>20.0</td>
      <td>131.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
la_df["Year"] = la_df["Date"].map(lambda x: x[:4])
la_df.groupby("Year").sum()
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
      <th>Temp (F) avg</th>
      <th>Consensual</th>
      <th>Disturbance</th>
      <th>Property</th>
      <th>Violent</th>
      <th>White Collar</th>
      <th>Total</th>
    </tr>
    <tr>
      <th>Year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015</th>
      <td>25027</td>
      <td>1783.0</td>
      <td>6658.0</td>
      <td>138613.0</td>
      <td>59876.0</td>
      <td>5377.0</td>
      <td>208388.0</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>24640</td>
      <td>1935.0</td>
      <td>6643.0</td>
      <td>145170.0</td>
      <td>61920.0</td>
      <td>6204.0</td>
      <td>221278.0</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>24994</td>
      <td>1936.0</td>
      <td>7013.0</td>
      <td>147169.0</td>
      <td>64979.0</td>
      <td>5693.0</td>
      <td>224945.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
la_std = la_df.groupby("Temp (F) avg").std().fillna(0)
```


```python
plt.plot(la_std.index, la_temp["Total"],c="b")
plt.plot(la_std.index, la_temp["Total"]+la_std["Total"],c="b",linestyle="--",alpha=0.5)
plt.plot(la_std.index, la_temp["Total"]-la_std["Total"],c="b",linestyle="--",alpha=0.5)
plt.title("LA: Crime Category v. Temp")
plt.xlabel("Temperature (F)")
plt.ylabel("Total Occurences of Crime")
plt.show()
```


![png](output_20_0.png)



```python
la_df.loc[la_df["Temp (F) avg"]==48]
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
      <th>Date</th>
      <th>Temp (F) avg</th>
      <th>Event</th>
      <th>Consensual</th>
      <th>Disturbance</th>
      <th>Property</th>
      <th>Violent</th>
      <th>White Collar</th>
      <th>Total</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2015-01-01</td>
      <td>48</td>
      <td>Clear</td>
      <td>12.0</td>
      <td>48.0</td>
      <td>833.0</td>
      <td>381.0</td>
      <td>25.0</td>
      <td>1299.0</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>361</th>
      <td>2015-12-28</td>
      <td>48</td>
      <td>Clear</td>
      <td>3.0</td>
      <td>11.0</td>
      <td>364.0</td>
      <td>135.0</td>
      <td>28.0</td>
      <td>541.0</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.plot(la_df["Date"],la_df["Total"],alpha=.8)
plt.plot(chi_df["Date"],chi_df["Total"],alpha=.8)
plt.xticks([])
plt.title("Crime Category v. Temp")
plt.xlabel("Date")
plt.ylabel("Total Occurences of Crime")
plt.show()
```


![png](output_22_0.png)



```python
plt.plot(chi_df["Date"],chi_df["Total"])
plt.xticks([])
plt.show()
```


![png](output_23_0.png)



```python
crime_type_list = ["Violent", "Property", "White Collar", "Consensual", "Disturbance"]
bar_means=np.array([[x.mean()[y] for x in chi_w_dfs] for y in crime_type_list])

plt.bar(np.arange(5), bar_means[0])
plt.bar(np.arange(5), bar_means[1], bottom = bar_means[0])
plt.bar(np.arange(5), bar_means[2], bottom = sum(bar_means[:2]))
plt.bar(np.arange(5), bar_means[3], bottom = sum(bar_means[:3]))
plt.bar(np.arange(5), bar_means[4], bottom = sum(bar_means[:4]))
plt.xticks(np.arange(5),chi_w_labels)
plt.show()
```


![png](output_24_0.png)



```python
la_group_w=la_df.groupby("Event").mean()[["Violent","Property","Disturbance","White Collar","Consensual"]]
la_group_w
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
      <th>Violent</th>
      <th>Property</th>
      <th>Disturbance</th>
      <th>White Collar</th>
      <th>Consensual</th>
    </tr>
    <tr>
      <th>Event</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Clear</th>
      <td>171.986430</td>
      <td>393.340292</td>
      <td>18.766180</td>
      <td>15.845511</td>
      <td>5.271579</td>
    </tr>
    <tr>
      <th>Fog</th>
      <td>168.846154</td>
      <td>376.923077</td>
      <td>16.500000</td>
      <td>14.153846</td>
      <td>5.458333</td>
    </tr>
    <tr>
      <th>Fog , Rain</th>
      <td>157.750000</td>
      <td>380.375000</td>
      <td>21.625000</td>
      <td>13.375000</td>
      <td>5.875000</td>
    </tr>
    <tr>
      <th>Rain</th>
      <td>157.307692</td>
      <td>397.009615</td>
      <td>16.673077</td>
      <td>15.567308</td>
      <td>4.543689</td>
    </tr>
  </tbody>
</table>
</div>




```python
chi_group_w=chi_df.groupby("Event").mean()[["Violent","Property","Disturbance","White Collar","Consensual"]]
chi_group_w
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
      <th>Violent</th>
      <th>Property</th>
      <th>Disturbance</th>
      <th>White Collar</th>
      <th>Consensual</th>
    </tr>
    <tr>
      <th>Event</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Clear</th>
      <td>206.725589</td>
      <td>372.744108</td>
      <td>9.151771</td>
      <td>48.114478</td>
      <td>60.749158</td>
    </tr>
    <tr>
      <th>Fog</th>
      <td>197.923077</td>
      <td>366.307692</td>
      <td>9.076923</td>
      <td>49.230769</td>
      <td>65.384615</td>
    </tr>
    <tr>
      <th>Fog , Rain</th>
      <td>196.352941</td>
      <td>351.588235</td>
      <td>8.294118</td>
      <td>40.941176</td>
      <td>48.823529</td>
    </tr>
    <tr>
      <th>Fog , Rain , Snow</th>
      <td>170.666667</td>
      <td>336.000000</td>
      <td>7.833333</td>
      <td>66.166667</td>
      <td>58.000000</td>
    </tr>
    <tr>
      <th>Fog , Rain , Thunderstorm</th>
      <td>195.062500</td>
      <td>365.312500</td>
      <td>9.062500</td>
      <td>49.937500</td>
      <td>55.625000</td>
    </tr>
    <tr>
      <th>Fog , Snow</th>
      <td>162.388889</td>
      <td>280.333333</td>
      <td>7.176471</td>
      <td>41.388889</td>
      <td>49.111111</td>
    </tr>
    <tr>
      <th>Fog , Snow , Thunderstorm</th>
      <td>132.000000</td>
      <td>206.000000</td>
      <td>5.000000</td>
      <td>55.000000</td>
      <td>27.000000</td>
    </tr>
    <tr>
      <th>Rain</th>
      <td>202.197044</td>
      <td>365.448276</td>
      <td>8.931034</td>
      <td>47.310345</td>
      <td>59.187192</td>
    </tr>
    <tr>
      <th>Rain , Hail , Thunderstorm</th>
      <td>215.000000</td>
      <td>352.333333</td>
      <td>8.000000</td>
      <td>40.666667</td>
      <td>58.000000</td>
    </tr>
    <tr>
      <th>Rain , Snow</th>
      <td>173.500000</td>
      <td>332.062500</td>
      <td>7.875000</td>
      <td>43.250000</td>
      <td>58.187500</td>
    </tr>
    <tr>
      <th>Rain , Thunderstorm</th>
      <td>212.245455</td>
      <td>383.318182</td>
      <td>8.090909</td>
      <td>49.472727</td>
      <td>52.918182</td>
    </tr>
    <tr>
      <th>Snow</th>
      <td>164.565217</td>
      <td>311.597826</td>
      <td>7.119565</td>
      <td>48.239130</td>
      <td>58.510870</td>
    </tr>
    <tr>
      <th>Thunderstorm</th>
      <td>249.857143</td>
      <td>394.428571</td>
      <td>9.857143</td>
      <td>44.857143</td>
      <td>48.428571</td>
    </tr>
  </tbody>
</table>
</div>




```python
i=0
n=8
color_list = ["r","g","b","c","k"]
for row in la_group_w.iterrows():
    plt.bar(np.arange(i*n,5+i*n), row[1],color=color_list)
    i+=1
    
for j in range(len(chi_group_w.columns)):
    plt.scatter([],[],color=color_list[j],label=chi_group_w.columns[j],marker="s")
plt.title("LA: Crime Category v. Weather")
plt.xlabel("Weather Condition")
plt.ylabel("Average Occurences of Crime")
    
plt.xticks(np.arange(len(la_group_w.index))*n+2, la_group_w.index)
plt.legend()
plt.show()
```


![png](output_27_0.png)



```python
i=0
n=8
color_list = ["r","g","b","c","k"]

plt.figure(figsize=[15,4])
for row in chi_group_w.iterrows():
    plt.bar(np.arange(i*n,5+i*n), row[1],color=color_list)
    i+=1
    
for j in range(len(chi_group_w.columns)):
    plt.scatter([],[],color=color_list[j],label=chi_group_w.columns[j],marker="s")

plt.title("Chicago: Crime Category v. Weather")
plt.xlabel("Weather Condition")
plt.ylabel("Average Occurences of Crime")
    
plt.xticks(np.arange(len(chi_group_w.index))*n+2, chi_group_w.index,rotation=45,ha="right")
plt.legend()
plt.show()
```


![png](output_28_0.png)



```python

```




    'Property'


