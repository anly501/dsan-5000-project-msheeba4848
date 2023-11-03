from fredapi import Fred
import pandas as pd

fred = Fred(api_key='10fbe66f8f62ad7f44097cca867bf01f')

series_id_1 = 'GDP' # for GDP US
series_id_2='GDPC1' # for Real Gross GDP
series_id_3='W207RC1Q156SBEA' # Adjusted Saving (% of GNI)
series_id_4='USAB6BLTT02STSAQ' # Current account balance (% of GDP)
series_id_5='A019RE1Q156NBEA' # Export of Goods and Services as percentage of GDP
series_id_6='MKTGNIUSA646NWDB' # GNI

# Set the start and end dates where I need data from 1990 to 2023
start_date = '1973'
end_date = '2023'

# Fetch the data
gdp_u = fred.get_series(series_id_1, start_date, end_date)
realgdp_u = fred.get_series(series_id_2, start_date, end_date)
adjsavings_u = fred.get_series(series_id_3, start_date, end_date)
currentaccbalance_u = fred.get_series(series_id_4, start_date, end_date)
exportsofgoods_u = fred.get_series(series_id_5, start_date, end_date)
gni_u= fred.get_series(series_id_6, start_date, end_date)

# for GDP
df1= gdp_u.to_frame(name=('GDP'))
annual_gdp_u = df1.resample('A').mean()
annual_gdp_u['Year'] = annual_gdp_u.index.year
annual_gdp_u=annual_gdp_u[['Year', 'GDP']]
annual_gdp_u.reset_index(drop=True, inplace=True)
print(annual_gdp_u.head(5))

# Real GDP
df2= realgdp_u.to_frame(name=('Real GDP'))
annual_realgdp_u = df2.resample('A').mean()
annual_realgdp_u['Year'] = annual_realgdp_u.index.year
annual_realgdp_u.reset_index(drop=True, inplace=True)
annual_realgdp_u.head(16)

# Adjusted Savings
df3= adjsavings_u.to_frame(name=('Adjusted Savings'))
annual_adjsavings_u = df3.resample('A').mean()
annual_adjsavings_u['Year'] = annual_adjsavings_u.index.year
annual_adjsavings_u.reset_index(drop=True, inplace=True)
annual_adjsavings_u.head(2)

# Current Account Balance % of GDP
df4= currentaccbalance_u.to_frame(name=('Current Account Balance'))
annual_currentaccbalance_u = df4.resample('A').mean()
annual_currentaccbalance_u['Year'] = annual_currentaccbalance_u.index.year
annual_currentaccbalance_u.reset_index(drop=True, inplace=True)
annual_currentaccbalance_u.head(2)

# Current Account Balance % of GDP
df5= exportsofgoods_u.to_frame(name=('Exports of Goods and Services'))
annual_exportsofgoods_u = df5.resample('A').mean()
annual_exportsofgoods_u['Year'] = annual_exportsofgoods_u.index.year
annual_exportsofgoods_u.reset_index(drop=True, inplace=True)
annual_exportsofgoods_u.head(2)

# GNI
df6= gni_u.to_frame(name=('GNI'))
annual_gni_u = df6.resample('A').mean()
annual_gni_u['Year'] = annual_gni_u.index.year
annual_gni_u.reset_index(drop=True, inplace=True)
annual_gni_u.head(10)

merged_df= pd.merge(annual_gdp_u, annual_realgdp_u, how= 'outer', on= 'Year' )
merged_df= pd.merge(merged_df, annual_adjsavings_u, how= 'outer', on= 'Year')
merged_df= pd.merge(merged_df, annual_currentaccbalance_u, how= 'outer', on= 'Year' )
merged_df= pd.merge(merged_df, annual_exportsofgoods_u, how= 'outer', on= 'Year' )
merged_df= pd.merge(merged_df, annual_gni_u, how= 'outer', on= 'Year' )

merged_df['GNI'] = merged_df['GNI'].fillna(merged_df['GNI'].mean())
merged_df.isna().sum()


merged_df.head(10)

merged_df.describe()

merged_df.info()
merged_df['Year']=pd.to_datetime(merged_df['Year'])