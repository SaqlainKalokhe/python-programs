'''
Exp 12:-Write a python Program to demonstrate series and dataframe in Pandas
             Name:- Saqlain Kalokhe
             RollNo:- 20CO22
             Academic Year :- 2021-22

'''
import pandas as pd 

#Series
'''
Pandas Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.). 
The axis labels are collectively called index. Pandas Series is nothing but a column in an excel sheet.
Labels need not be unique but must be a hashable type. The object supports both integer and label-based indexing and provides a 
host of methods for performing operations involving the index.
'''
s = pd.Series([10,20,30,40,50])
print(s)
print(s[0])

#some slicing, indexing, other features of Series

#Dataframe
'''
Pandas DataFrame is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns).
A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. Pandas DataFrame consists 
of three principal components, the data, rows, and columns.
'''
df = pd.DataFrame([10,20,30,40,50])
print(df)
#some slicing, indexing, other features of Dataframe

#Dataframe operations using csv dataset
df = pd.read_csv("true_car_listings.csv")
print('First 10 rows:\n',df.head(10))
print('Last 5 rows:\n',df.tail(5))
print('Total Columns/Attributes/Features:',df.columns)

print('Displaying Make Column:\n',df['Make'])
print('Displaying first 5 rows with 4 columns:\n',df[['Make','Model','Year','Price']].head())
print('Displaying rows 5 and 6:\n',df[5:7])
print('Displaying rows 1, 10 and 20:\n',df.loc[[1,10,20]])
print('Displaying rows 1 to 9 and columns 6 and 7:\n',df.iloc[1:10,6:8])
print('Displaying rows with Price less than 5000:\n',df.loc[df['Price']<5000])
print('Null Values count for all columns:\n',df.isna().sum())

#filling na values of Price col with mean value of Price
df['Price'].fillna(df['Price'].mean)

#Grouping records based on Year value.
groupby = df.groupby('Year')
for year, group in groupby:
    print(year)
    print(group)


'''
Output:
0    10     
1    20     
2    30     
3    40     
4    50     
dtype: int64
10
    0
0  10
1  20
2  30
3  40
4  50
First 10 rows:
    Price  Year  Mileage              City State                Vin   Make         Model
0   8995  2014    35725           El Paso    TX  19VDE2E53EE000083  Acura    ILX6-Speed
1  10888  2013    19606  Long Island City    NY  19VDE1F52DE012636  Acura    ILX5-Speed
2   8995  2013    48851           El Paso    TX  19VDE2E52DE000025  Acura    ILX6-Speed
3  10999  2014    39922           Windsor    CO  19VDE1F71EE003817  Acura    ILX5-Speed
4  14799  2016    22142            Lindon    UT  19UDE2F32GA001284  Acura  ILXAutomatic
5   7989  2012   105246             Miami    FL  JH4CU2F83CC019895  Acura  TSXAutomatic
6  14490  2014    34032         Greatneck    NY  JH4CU2F84EC002686  Acura    TSXSpecial
7  13995  2013    32384       West Jordan    UT  JH4CU2F64DC006203  Acura    TSX5-Speed
8  10495  2013    57596         Waterbury    CT  19VDE2E50DE000234  Acura    ILX6-Speed
9   9995  2013    63887           El Paso    TX  19VDE1F50DE010450  Acura    ILX5-Speed
Last 5 rows:
         Price  Year  Mileage          City State                Vin   Make    Model
852117  63215  2017        9   Culver City    CA  YV1A22MK9H1013237  Volvo    S90T6
852118  72260  2017     3201     Englewood    NJ  YV4A22PL3H1186162  Volvo   XC90T6
852119  55999  2016    28941  Fort Collins    CO  YV4A22PL4G1000868  Volvo  XC90AWD
852120  60240  2017     3005   San Leandro    CA  YV4A22NLXH1006162  Volvo      V90
852121  76995  2017     2502      New York    NY  YV4BC0ZX1H1109845  Volvo   XC90T8
Total Columns/Attributes/Features: Index(['Price', 'Year', 'Mileage', 'City', 'State', 'Vin', 'Make', 'Model'], dtype='object')
Displaying Make Column:
 0         Acura
1         Acura
2         Acura
3         Acura
4         Acura
          ...
852117    Volvo
852118    Volvo
852119    Volvo
852120    Volvo
852121    Volvo
Name: Make, Length: 852122, dtype: object
Displaying first 5 rows with 4 columns:
     Make         Model  Year  Price
0  Acura    ILX6-Speed  2014   8995
1  Acura    ILX5-Speed  2013  10888
2  Acura    ILX6-Speed  2013   8995
3  Acura    ILX5-Speed  2014  10999
4  Acura  ILXAutomatic  2016  14799
Displaying rows 5 and 6:
    Price  Year  Mileage       City State                Vin   Make         Model
5   7989  2012   105246      Miami    FL  JH4CU2F83CC019895  Acura  TSXAutomatic
6  14490  2014    34032  Greatneck    NY  JH4CU2F84EC002686  Acura    TSXSpecial
Displaying rows 1, 10 and 20:
     Price  Year  Mileage              City State                Vin   Make         Model
1   10888  2013    19606  Long Island City    NY  19VDE1F52DE012636  Acura    ILX5-Speed
10  12921  2012    58550             Boise    ID  JH4CU2F44CC003220  Acura  TSXAutomatic
20  16994  2015    23946     St. Augustine    FL  19VDE1F32FE000651  Acura    ILX5-Speed
Displaying rows 1 to 9 and columns 6 and 7:
     Make         Model
1  Acura    ILX5-Speed
2  Acura    ILX6-Speed
3  Acura    ILX5-Speed
4  Acura  ILXAutomatic
5  Acura  TSXAutomatic
6  Acura    TSXSpecial
7  Acura    TSX5-Speed
8  Acura    ILX6-Speed
9  Acura    ILX5-Speed
Displaying rows with Price less than 5000:
         Price  Year  Mileage           City State                Vin   Make         Model
648      4950  2006   142587      Littleton    CO  JH4CL96826C031231  Acura  TSXAutomatic
1179     4990  2008   159601       Boardman    OH  JH4CL96878C000866  Acura        TSX4dr
1222     4899  2006   144259      Haverhill    MA  JH4CL96806C012614  Acura  TSXAutomatic
1298     4599  2005    90008  PINELLAS PARK    FL  19UUA66245A038764  Acura   TLAutomatic
1448     4990  2006   170470  Brooklyn Park    MN  JH4CL96846C007545  Acura  TSXAutomatic
...       ...   ...      ...            ...   ...                ...    ...           ...
851712   3999  2004   154898       Longwood    FL  YV1SW64AX42429597  Volvo       V702.4L
851771   4990  1998    96543        Fairfax    VA  YV1LS5577W1535110  Volvo        S704dr
851774   3999  1998   109198       Longmont    CO  YV1LS5549W2445313  Volvo        S704dr
851785   3998  2006   204001       Marietta    GA  YV4CY592861284131  Volvo      XC902.5L
851925   3111  2001   202691         Odessa    TX  YV1SW61R512089006  Volvo        V702.4

[18111 rows x 8 columns]
Null Values count for all columns:
 Price      0
Year       0
Mileage    0
City       0
State      0
Vin        0
Make       0
Model      0
dtype: int64
1997
        Price  Year  Mileage             City State                Vin        Make              Model
6144     4995  1997   121462     Sneads Ferry    NC  19UYA2246VL003892       Acura        CLAutomatic
6433     3175  1997   154352        Allentown    PA  JH4KA9655VC012209       Acura        RLAutomatic
7219     3990  1997   165613       Pleasanton    CA  19UYA2259VL011624       Acura        CLAutomatic
7407     4929  1997    89018  Hoffman Estates    IL  JH4UA3658VC011027       Acura        TLAutomatic
7842     2991  1997   161764    Oklahoma City    OK  JH4DC4352VS020218       Acura          IntegraLS
...       ...   ...      ...              ...   ...                ...         ...                ...
823545   7999  1997   287618         Longmont    CO  JT3HN86R7V0117577      Toyota         4Runner4dr
823616  48995  1997   108500            Tempe    AZ  JT2DE82AXV0038228      Toyota           Supra3dr
843916   5500  1997    47727         Pasadena    CA  3VWAA81E3VM806605  Volkswagen          Cabrio2dr
845871   1950  1997   166616            Alsip    IL  3VWAA81E6VM800197  Volkswagen  CabrioCONVERTIBLE
849538   2990  1997   138854       Miamisburg    OH  YV1KW9603V1040927       Volvo             9605dr

[596 rows x 8 columns]
1998
        Price  Year  Mileage             City State                Vin   Make        Model
2808     1998  1998   149446           Murray    UT  JH4UA3641WC003098  Acura  TLAutomatic
4443     4495  1998    93969          Danbury    CT  19UYA2251WL010730  Acura  CLAutomatic
5892     3990  1998    98099        Arlington    TX  JH4DC4454WS018955  Acura    IntegraLS
7763     3875  1998   147500        Chantilly    VA  JH4DC4454WS002089  Acura    IntegraLS
8213     3400  1998   191641           Conroe    TX  JH4DC4456WS011702  Acura    IntegraLS
...       ...   ...      ...              ...   ...                ...    ...          ...
851257   3800  1998   179027  North Hollywood    CA  YV1LS5673W1507500  Volvo       S704dr
851311   2850  1998   200158  North Hollywood    CA  YV1LS5574W1532522  Volvo       S704dr
851376   4852  1998   200049       Burlington    WA  YV1LS5578W1484605  Volvo       S704dr
851771   4990  1998    96543          Fairfax    VA  YV1LS5577W1535110  Volvo       S704dr
851774   3999  1998   109198         Longmont    CO  YV1LS5549W2445313  Volvo       S704dr

[774 rows x 8 columns]
1999
        Price  Year  Mileage            City State                Vin   Make        Model
2010     5000  1999    93845         Houston    TX  19UUA5657XA025997  Acura  TLAutomatic
2726     3950  1999   138861       Fairfield    OH  19UUA5647XA008382  Acura  TLAutomatic
2818     3199  1999   140723         Wahiawa    HI  19UUA5643XA009707  Acura  TLAutomatic
3000     5995  1999    68830       Westfield    IN  JAEDJ58X6X7B00076  Acura       SLX4WD
3067     3988  1999   143790    Jacksonville    FL  19UUA564XXA052036  Acura  TLAutomatic
...       ...   ...      ...             ...   ...                ...    ...          ...
850968   2595  1999   199076         Houston    TX  YV1TS97D1X1018963  Volvo       S804dr
850994   2995  1999   167733  Virginia Beach    VA  YV1LT56D8X2600169  Volvo       S70AWD
851141   2199  1999   192440       Shoreline    WA  YV1LS56D4X2600236  Volvo       S70GLT
851443   4999  1999   224767  Spokane Valley    WA  YV1LV62D9X2582139  Volvo         V70R
851804   5000  1999   149857       Bremerton    WA  YV1LW55A2X2566891  Volvo         V70A

[1254 rows x 8 columns]
2000
        Price  Year  Mileage               City State                Vin   Make        Model
2111     5495  2000    85329           Elmhurst    IL  19UUA5664YA058725  Acura  TLAutomatic
2280     4950  2000   108702             Irving    TX  19UUA5665YA010764  Acura  TLAutomatic
2456     3978  2000   120152  Arlington Heights    IL  19UUA5668YA029311  Acura  TLAutomatic
2487     4988  2000   109624       Jacksonville    FL  19UUA5666YA026763  Acura  TLAutomatic
3096     2990  2000   186044         Minnetonka    MN  19UUA5672YA011086  Acura  TLAutomatic
...       ...   ...      ...                ...   ...                ...    ...          ...
850240   2495  2000   134121           Pasadena    TX  YV1LS61J6Y2627197  Volvo         S70A
850399   6990  2000    96746             TACOMA    WA  YV1LZ56D3Y2685499  Volvo        V70XC
850753   5261  2000   144118      Winston Salem    NC  YV1LS61J8Y2624558  Volvo         S70A
850975   2495  2000   190148            Memphis    TN  YV1LW61J6Y2689879  Volvo         V70A
851045   3000  2000   138691           Danville    KY  YV1TS94D4Y1105455  Volvo       S804dr

[1933 rows x 8 columns]
2001
        Price  Year  Mileage            City State                Vin   Make        Model
2089     3700  2001   114453        Honolulu    HI  19UUA56611A031276  Acura  TLAutomatic
2369     3997  2001   124846        Stafford    VA  19UUA56771A019755  Acura  TLAutomatic
2539     2995  2001   144995      Morristown    NJ  19UUA56771A000591  Acura  TLAutomatic
2872     1999  2001   174950  Spokane Valley    WA  19UUA56671A032626  Acura  TLAutomatic
3140     4295  2001   161276        San Jose    CA  19UUA56621A005849  Acura  TLAutomatic
...       ...   ...      ...             ...   ...                ...    ...          ...
851078   3495  2001   181050         Detroit    MI  YV1TS94D311209330  Volvo       S802.9
851148   3900  2001   200257          Tucker    GA  YV1SW58D911139139  Volvo      V702.4T
851535   4987  2001   194632        Puyallup    WA  YV1RS61R512077917  Volvo       S602.4
851615   2998  2001   123926     Spartanburg    SC  YV1SZ58D911037797  Volvo        V70XC
851925   3111  2001   202691          Odessa    TX  YV1SW61R512089006  Volvo       V702.4

[2584 rows x 8 columns]
2002
        Price  Year  Mileage           City State                Vin   Make        Model
1689     2995  2002   120001        Kahului    HI  19UUA56882A057201  Acura     TLType-S
1839     1985  2002   131239    Des Plaines    IL  19UUA56612A047740  Acura  TLAutomatic
1897     8744  2002    71044          Ocala    FL  19UUA56802A008882  Acura     TLType-S
1987     1950  2002   139802      Levittown    PA  19UUA56712A059721  Acura  TLAutomatic
1995     4500  2002   127218       Lynnwood    WA  19UUA566X2A038602  Acura  TLAutomatic
...       ...   ...      ...            ...   ...                ...    ...          ...
851237   8990  2002   113060  Winston Salem    NC  YV1RH58D722146479  Volvo      S602.4T
851287   2595  2002   180707      Bethlehem    PA  YV1RH58D322191256  Volvo      S602.4T
851347   3950  2002   166828      Levittown    PA  YV1VW29562F845783  Volvo         V40A
851625   3500  2002   128620        Norfork    VA  YV1SJ58DX21224992  Volvo      V702.4T
851629   6990  2002    87622        Addison    IL  YV1SZ58D221070383  Volvo        V70XC

[3800 rows x 8 columns]
2003
        Price  Year  Mileage               City State                Vin   Make        Model
1447     6995  2003    64047            Seekonk    MA  19UUA56663A088995  Acura  TLAutomatic
1598     4995  2003    89165           Leesburg    VA  19UUA56603A018103  Acura  TLAutomatic
1606     6000  2003   102450           Westmont    IL  19UUA56883A084531  Acura     TLType-S
1670     6997  2003    71840    East Petersburg    PA  19UUA56693A067283  Acura  TLAutomatic
1717     7995  2003    59991          Chantilly    VA  19UUA56733A077882  Acura  TLAutomatic
...       ...   ...      ...                ...   ...                ...    ...          ...
850548   4462  2003   158142             Monroe    NC  YV1SW61T032295168  Volvo       V705dr
850651   2976  2003   191487         Louisville    KY  YV1SW58DX32321171  Volvo       V705dr
851095   4700  2003   127612          Swannanoa    NC  YV1VW27553F985800  Volvo       V405dr
851603   3500  2003   175099             Garner    NC  YV1SW61T732325573  Volvo       V705dr
852012   5995  2003   144538  Fort Walton Beach    FL  YV1SZ59H831096165  Volvo       V705dr

[5649 rows x 8 columns]
2004
        Price  Year  Mileage             City State                Vin   Make         Model
97       8572  2004    51293          Fairfax    VA  JH4CL96834C036838  Acura  TSXAutomatic
821      8195  2004    71572       Streamwood    IL  JH4CL96894C040747  Acura  TSXAutomatic
1000     7995  2004    80404          Houston    TX  JH4CL96854C033617  Acura  TSXAutomatic
1282     5995  2004   116690   Fredericksburg    VA  JH4CL96854C018793  Acura  TSXAutomatic
1311     6985  2004   106252  North Hollywood    CA  JH4CL96864C043332  Acura  TSXAutomatic
...       ...   ...      ...              ...   ...                ...    ...           ...
851296   2694  2004   259757    Nicholasville    KY  YV1SZ59H441139059  Volvo       V70XC70
851323   4900  2004   178378   Salt Lake City    UT  YV1CZ91H441095989  Volvo       XC904dr
851506   3999  2004   235365          Ontario    OR  YV1CY59H841102264  Volvo       XC904dr
851543   6000  2004   107276     BROKEN ARROW    OK  YV1SW61T042378021  Volvo       V702.4L
851712   3999  2004   154898         Longwood    FL  YV1SW64AX42429597  Volvo       V702.4L

[8117 rows x 8 columns]
2005
        Price  Year  Mileage            City State                Vin   Make         Model
590      8998  2005    73406      Burlington    MA  JH4CL96935C003820  Acura  TSXAutomatic
694      7488  2005    93940       Lake Park    FL  JH4CL96895C018118  Acura  TSXAutomatic
782      5995  2005   105743       Riverdale    NJ  JH4CL968X5C005197  Acura  TSXAutomatic
817      7990  2005    82451    Downtingtown    PA  JH4CL96815C032417  Acura  TSXAutomatic
837      7498  2005   107916       Chantilly    VA  JH4CL96865C006377  Acura  TSXAutomatic
...       ...   ...      ...             ...   ...                ...    ...           ...
850869   8499  2005   102931    Fort Collins    CO  YV1CZ911951186549  Volvo       XC904dr
850882   5584  2005   103512          Golden    CO  YV1MS382952079273  Volvo       S402.4L
850903   7494  2005   110535  Salt Lake City    UT  YV1CM592751217737  Volvo       XC904dr
851022   8848  2005   139079       Pensacola    FL  YV1CN592051168961  Volvo       XC904dr
851100   6498  2005   167107         Raleigh    NC  YV1SZ592051181239  Volvo      XC702.5L

[11005 rows x 8 columns]
2006
        Price  Year  Mileage           City State                Vin   Make         Model
55       9995  2006    62983          Omaha    NE  JH4CL96886C009248  Acura  TSXAutomatic
124      7750  2006    83324       Woodside    NY  JH4CL96966C037574  Acura  TSXAutomatic
648      4950  2006   142587      Littleton    CO  JH4CL96826C031231  Acura  TSXAutomatic
760      9499  2006    69656     Schaumburg    IL  JH4CL96986C035549  Acura  TSXAutomatic
845      8495  2006    96261        Milford    MA  JH4CL96946C033703  Acura  TSXAutomatic
...       ...   ...      ...            ...   ...                ...    ...           ...
851240  15705  2006    52621  Pompano Beach    FL  YV1MC68226J004405  Volvo       C702.5L
851258   7999  2006   159489   Fort Collins    CO  YV4CZ592061233977  Volvo      XC902.5L
851570   4990  2006   250857        Thomson    GA  YV4CY592261290992  Volvo      XC902.5T
851643  10250  2006    70399         Summit    NJ  YV4CZ592661224295  Volvo      XC902.5L
851785   3998  2006   204001       Marietta    GA  YV4CY592861284131  Volvo      XC902.5L

[15079 rows x 8 columns]
2007
        Price  Year  Mileage              City State                Vin   Make    Model
19       7990  2007    60552          Fairlawn    NJ  JH4CL96857C019060  Acura   TSX4dr
46       8995  2007    53525  South Hackensack    NJ  JH4CL96807C008922  Acura   TSX4dr
206      9717  2007    74429         Tewksbury    MA  JH4CL96847C007238  Acura   TSX4dr
457      9191  2007    94682     Oklahoma City    OK  JH4CL96867C001103  Acura   TSX4dr
563      7849  2007    96769         Henderson    NV  JH4CL96867C011291  Acura   TSX4dr
...       ...   ...      ...               ...   ...                ...    ...      ...
851119   4500  2007   174225           Houston    TX  YV4CY982971330768  Volvo  XC90FWD
851128   7499  2007   142754         Frederick    MD  YV4SZ592471263657  Volvo  XC704dr
851176   5988  2007   181996      Jacksonville    FL  YV1MS382072299078  Volvo   S404dr
851189   4865  2007   188984     Winston Salem    NC  YV4SZ592671266429  Volvo  XC704dr
851233  10999  2007   110664          Longmont    CO  YV4CZ982571343837  Volvo  XC90AWD

[21171 rows x 8 columns]
2008
        Price  Year  Mileage             City State                Vin   Make    Model
77      11991  2008    59594      Albuquerque    NM  JH4CL968X8C011232  Acura   TSX4dr
280      8999  2008    85390        Allentown    PA  JH4CL96808C006590  Acura   TSX4dr
377      9990  2008    70244          Raleigh    NC  JH4CL96878C003931  Acura   TSX4dr
410      9555  2008    84559       Jenkintown    PA  JH4CL96938C015079  Acura   TSX4dr
446      8888  2008   100528         Freehold    NJ  JH4CL96948C009601  Acura   TSX4dr
...       ...   ...      ...              ...   ...                ...    ...      ...
851232  10900  2008    58630  Rolling Meadows    IL  YV1MK672582052966  Volvo   C302dr
851303  14985  2008    92028    Mission Viejo    CA  YV4CT852881482829  Volvo  XC90AWD
851409  11995  2008    90891         Marietta    GA  YV1MK672982052856  Volvo   C302dr
851573  10991  2008    96929      San Antonio    TX  YV1BW982X81035632  Volvo   V704dr
851578   9988  2008   105311          El Paso    TX  YV1MK672782065055  Volvo   C302dr

[24713 rows x 8 columns]
2009
        Price  Year  Mileage            City State                Vin   Make    Model
12       7750  2009    91980     San Antonio    TX  JH4CU26639C015787  Acura   TSX4dr
121      7783  2009   109568           Hurst    TX  JH4CU26639C015823  Acura   TSX4dr
230     11995  2009    49153      Schaumburg    IL  JH4CU266X9C021537  Acura   TSX4dr
300     11988  2009    71466        Waukesha    WI  JH4CU26699C008696  Acura   TSX4dr
312     14610  2009    32576      Chesapeake    VA  JH4CU26649C035384  Acura   TSX4dr
...       ...   ...      ...             ...   ...                ...    ...      ...
851072  11998  2009    98524       Westbrook    CT  YV4BZ982791064405  Volvo  XC704dr
851086  11995  2009    72414   National City    CA  YV1MS382192465563  Volvo   S404dr
851098   9990  2009   116169   Winston Salem    NC  YV1MS382392451874  Volvo   S404dr
851262   9997  2009   115075    Falls Church    VA  YV1BW982591102686  Volvo   V704dr
851297   8595  2009   104912  BRODHEADSVILLE    PA  YV1MK672592132172  Volvo   C302dr

[19061 rows x 8 columns]
2010
        Price  Year  Mileage             City State                Vin   Make    Model
17      14590  2010    19250       Clearwater    FL  JH4CU2F6XAC041680  Acura   TSX4dr
26      14500  2010    25926         Columbus    OH  JH4CU2F69AC027155  Acura   TSX4dr
33      12500  2010    50821  Fort Lauderdale    FL  JH4CU2F68AC029706  Acura   TSX4dr
57      13495  2010    41234          Wantagh    NY  JH4CU2F60AC014472  Acura   TSX4dr
61      13473  2010    29875  West Palm Beach    FL  JH4CU2F69AC026376  Acura   TSX4dr
...       ...   ...      ...              ...   ...                ...    ...      ...
851088  16000  2010    56738         PORTLAND    OR  YV4992DZ3A2033711  Volvo  XC60AWD
851115  15950  2010    87542        St. Louis    MO  YV4960DL8A2101848  Volvo  XC60FWD
851147  13333  2010   147537         Syracuse    NY  YV4992BZXA1078783  Volvo  XC704dr
851284  14990  2010    35160        Baltimore    MD  YV1672MK6A2172871  Volvo   C302dr
851356  13559  2010   109813        Littleton    CO  YV4992DZ6A2024579  Volvo  XC60AWD

[27539 rows x 8 columns]
2011
        Price  Year  Mileage          City State                Vin   Make    Model
18       9500  2011    68289       Arcadia    FL  JH4CU2F62BC007928  Acura   TSX4dr
44      12933  2011    54050    Fort Myers    FL  JH4CU2F66BC009536  Acura   TSX4dr
47      13987  2011    44330  Indianapolis    IN  JH4CU2F62BC018296  Acura   TSX4dr
53      11995  2011    53000        Topeka    KS  JH4CU2F66BC003400  Acura   TSX4dr
68      13419  2011    58105    Minnetonka    MN  JH4CU2F68BC010431  Acura   TSX4dr
...       ...   ...      ...           ...   ...                ...    ...      ...
851364  14950  2011    93074    Midlothian    VA  YV4902DZ5B2174193  Volvo  XC60AWD
851497  15000  2011    47398     Baltimore    MD  YV1672MK4B2209868  Volvo   C302dr
851542  21999  2011    79847      Syracuse    NY  YV4902BZ4B1099771  Volvo   XC70T6
851554  24995  2011    42340        Berwyn    PA  YV4902BZ5B1099911  Volvo  XC704dr
852028  25900  2011    64519      Stamford    CT  YV4902DZ9B2158580  Volvo  XC60AWD

[39768 rows x 8 columns]
2012
        Price  Year  Mileage          City State                Vin   Make         Model
5        7989  2012   105246         Miami    FL  JH4CU2F83CC019895  Acura  TSXAutomatic
10      12921  2012    58550         Boise    ID  JH4CU2F44CC003220  Acura  TSXAutomatic
43      13699  2012    39342    Bellflower    CA  JH4CU2F45CC008409  Acura  TSXAutomatic
54      11888  2012    84126      Manassas    VA  JH4CU2F43CC016959  Acura  TSXAutomatic
91      10990  2012    81301     Homestead    FL  JH4CU2F80CC018400  Acura  TSXAutomatic
...       ...   ...      ...           ...   ...                ...    ...           ...
851392  20589  2012    71589      Simsbury    CT  YV4940BZXC1118463  Volvo       XC70AWD
851397  19295  2012   100109      Branford    CT  YV4902DZ4C2298490  Volvo       XC60AWD
851424  18900  2012    60762  Jacksonville    FL  YV1672MC8CJ126198  Volvo        C702dr
851454  16790  2012   111174     Maplewood    MN  YV4902DZ4C2239827  Volvo       XC60AWD
851972  32995  2012    81426        Berwyn    PA  YV4952CZ2C1625087  Volvo       XC90AWD

[49764 rows x 8 columns]
2013
        Price  Year  Mileage              City State                Vin   Make       Model
1       10888  2013    19606  Long Island City    NY  19VDE1F52DE012636  Acura  ILX5-Speed
2        8995  2013    48851           El Paso    TX  19VDE2E52DE000025  Acura  ILX6-Speed
7       13995  2013    32384       West Jordan    UT  JH4CU2F64DC006203  Acura  TSX5-Speed
8       10495  2013    57596         Waterbury    CT  19VDE2E50DE000234  Acura  ILX6-Speed
9        9995  2013    63887           El Paso    TX  19VDE1F50DE010450  Acura  ILX5-Speed
...       ...   ...      ...               ...   ...                ...    ...         ...
851666  26991  2013    36426             Tempe    AZ  YV4902DZ0D2440920  Volvo      XC60T6
851702  27999  2013    35649          Lakewood    NJ  YV4902DZ5D2409842  Volvo      XC60T6
851706  31495  2013    26830            Berwyn    PA  YV1672MC0DJ140856  Volvo       C70T5
851810  28981  2013    37864       Culver City    CA  YV1672MC7DJ143186  Volvo       C70T5
852030  26986  2013    68189            Renton    WA  YV4902DZ2D2385810  Volvo      XC60T6

[74701 rows x 8 columns]
2014
        Price  Year  Mileage             City State                Vin   Make       Model
0        8995  2014    35725          El Paso    TX  19VDE2E53EE000083  Acura  ILX6-Speed
3       10999  2014    39922          Windsor    CO  19VDE1F71EE003817  Acura  ILX5-Speed
6       14490  2014    34032        Greatneck    NY  JH4CU2F84EC002686  Acura  TSXSpecial
15      14995  2014    23454     Hackettstown    NJ  19VDE1F31EE009243  Acura  ILX5-Speed
21      15499  2014    27171        Santa Ana    CA  JH4CU2F49EC005287  Acura  TSX5-Speed
...       ...   ...      ...              ...   ...                ...    ...         ...
851815  33955  2014    37299  Fort Washington    PA  YV4902DZ3E2553035  Volvo      XC60T6
851817  32791  2014    39309            Tempe    AZ  YV4952CZ1E1689799  Volvo     XC90AWD
851895  39500  2014    17800  East Petersburg    PA  YV4902DZ9E2549720  Volvo      XC60T6
852011  33900  2014    26155  East Petersburg    PA  YV4902DZ9E2548387  Volvo      XC60T6
852070  30995  2014   392123           Berwyn    PA  YV4902DZ8E2543908  Volvo      XC60T6

[162432 rows x 8 columns]
2015
        Price  Year  Mileage             City State                Vin   Make       Model
13      17628  2015    13797            Fargo    ND  19VDE1F38FE001240  Acura  ILX5-Speed
16      14990  2015    23603         Freeport    NY  19VDE1F3XFE007606  Acura  ILX5-Speed
20      16994  2015    23946    St. Augustine    FL  19VDE1F32FE000651  Acura  ILX5-Speed
28      16000  2015    30881         Pasadena    CA  19VDE1F34FE008878  Acura  ILX5-Speed
29      17419  2015    15390     Indianapolis    IN  19VDE1F37FE002458  Acura  ILX5-Speed
...       ...   ...      ...              ...   ...                ...    ...         ...
851998  31720  2015    19560        Englewood    NJ  YV1612TK4F2362422  Volvo   S602015.5
852017  33995  2015    20520           Berwyn    PA  YV4902RB0F2589715  Volvo      XC60T6
852023  32995  2015    39670           Berwyn    PA  YV4902RC7F2620371  Volvo      XC60T6
852051  35995  2015    39854           Berwyn    PA  YV4902RG8F2587612  Volvo      XC60T6
852052  35900  2015    26956  East Petersburg    PA  YV4902RB2F2621371  Volvo      XC60T6

[157516 rows x 8 columns]
2016
        Price  Year  Mileage           City State                Vin   Make         Model
4       14799  2016    22142         Lindon    UT  19UDE2F32GA001284  Acura  ILXAutomatic
89      17376  2016    27384      Watertown    MA  19UDE2F39GA016641  Acura  ILXAutomatic
100     19444  2016    20905         Daphne    AL  19UDE2F39GA023427  Acura  ILXAutomatic
166     16986  2016    28443  Windsor Locks    CT  19UDE2F35GA018242  Acura  ILXAutomatic
173     18998  2016    19847     Woodbridge    VA  19UDE2F31GA024328  Acura  ILXAutomatic
...       ...   ...      ...            ...   ...                ...    ...           ...
852094  54995  2016    16578      Anchorage    AK  YV4A22PL0G1017599  Volvo       XC90AWD
852098  56995  2016    13041          Salem    OR  YV4A22PM4G1051814  Volvo       XC90AWD
852099  56789  2016    19250         Summit    NJ  YV4A22PM8G1050830  Volvo       XC90AWD
852110  57222  2016    15070      Frederick    MD  YV4BC0PK4G1078614  Volvo          XC90
852119  55999  2016    28941   Fort Collins    CO  YV4A22PL4G1000868  Volvo       XC90AWD

[132136 rows x 8 columns]
2017
        Price  Year  Mileage         City State                Vin   Make          Model
147     21000  2017     4279      Chicago    IL  19UDE2F30HA004475  Acura   ILXAutomatic
310     17250  2017    40101     Norcross    GA  19UDE2F32HA001240  Acura  ILXAcuraWatch
313     22000  2017       10      Chicago    IL  19UDE2F34HA011879  Acura   ILXAutomatic
314     22000  2017       10      Chicago    IL  19UDE2F35HA011597  Acura   ILXAutomatic
340     22000  2017      853      Chicago    IL  19UDE2F31HA011418  Acura   ILXAutomatic
...       ...   ...      ...          ...   ...                ...    ...            ...
852116  54995  2017     2474       Berwyn    PA  YV1A22MK1H1010445  Volvo          S90T6
852117  63215  2017        9  Culver City    CA  YV1A22MK9H1013237  Volvo          S90T6
852118  72260  2017     3201    Englewood    NJ  YV4A22PL3H1186162  Volvo         XC90T6
852120  60240  2017     3005  San Leandro    CA  YV4A22NLXH1006162  Volvo            V90
852121  76995  2017     2502     New York    NY  YV4BC0ZX1H1109845  Volvo         XC90T8

[91608 rows x 8 columns]
2018
        Price  Year  Mileage               City State                Vin   Make   Model
6129    35721  2018        5          Littleton    CO  5J8TB4H37JL004139  Acura  RDXAWD
6257    36000  2018        5          Littleton    CO  5J8TB4H37JL005209  Acura  RDXAWD
6258    36000  2018        5          Littleton    CO  5J8TB4H34JL003045  Acura  RDXAWD
6529    32995  2018      250           Cerritos    CA  19UUB1F30JA004453  Acura  TLXFWD
6640    33929  2018      239    Hoffman Estates    IL  19UUB1F55JA000321  Acura  TLXFWD
...       ...   ...      ...                ...   ...                ...    ...     ...
851987  59997  2018      248         Charleston    SC  YV4A22PL9J1207795  Volvo  XC90T6
852038  46885  2018       15  Hasbrouck Heights    NJ  YV440MWK2J2044182  Volvo     V60
852066  51555  2018       30          Englewood    NJ  YV4102RL1J1004130  Volvo  XC60T5
852073  52455  2018       10  Hasbrouck Heights    NJ  YV4A22RK8J1005471  Volvo  XC60T6
852082  66240  2018       14           Nazareth    PA  LVY992ML7JP006733  Volvo   S90T6

[922 rows x 8 columns]

Conclusion: We have successfully learned and implemented Pandas in python
'''