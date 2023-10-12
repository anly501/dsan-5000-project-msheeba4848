# Import Libraries


# pip install fredapi

from fredapi import Fred
import pandas as pd

fred = Fred(api_key='10fbe66f8f62ad7f44097cca867bf01f')


# INDIA 

series_id_1 = 'NAEXKP01INQ652S' # for GDP India
series_id_2='DEBTTLINA188A' # for Debt India
series_id_3='CPALTT01INQ657N' # for CPI India 
series_id_4='NAEXKP01INQ657S' # Export Values
series_id_5='XTIMVA01INQ657S' # Import Values
series_id_6='NAEXKP03INQ657S' # Government Final Consumption Expenditure
series_id_7='FPCPITOTLZGIND' # Inflation
series_id_8= 'MKTGNIINA646NWDB' # Gross National Income (Yearly)
series_id_9= 'SLEMPTOTLSPZSIND' # Employment to Population Ratio
series_id_10='SLUEM1524ZSIND' # Unemployment Rate 
series_id_11='SPDYNIMRTININD' # Infant Mortality Rate in India
series_id_12='SEADTLITRZSIND' # Literacy Rate
series_id_13='SPDYNLE00ININD' # Life Expectancy at Birth (Yearly)
series_id_14='INDNTDDRPCPPPT' #National Accounts: Real Total Domestic Demand for India (Yearly)
series_id_15='EMPENGINA148NRUG' #Number of Persons Engaged for India (Yearly)
series_id_16= 'NAEXKP02INQ189S' #Private Final Consumption Expenditure for India
series_id_17= 'GGNLBAINA188N' #General government net lending/borrowing for India
series_id_18='NNXGSRNSAXDCINQ' #Real External Balance of Goods and Services for India

# Set the start and end dates where I need data from 1990 to 2023
start_date = '2000'
end_date = '2023'

# Fetch the data
gdp_i = fred.get_series(series_id_1, start_date, end_date)
debt_i = fred.get_series(series_id_2, start_date, end_date)
cpi_i = fred.get_series(series_id_3, start_date, end_date)
export_i = fred.get_series(series_id_4, start_date, end_date)
import_i = fred.get_series(series_id_5, start_date, end_date)
govt_final_exp_i = fred.get_series(series_id_6, start_date, end_date)
inflation_i = fred.get_series(series_id_7, start_date, end_date)
gni_i= fred.get_series(series_id_8, start_date, end_date)
em_pop_i = fred.get_series(series_id_9, start_date, end_date)
unemployment_i = fred.get_series(series_id_10, start_date, end_date)
infantmor_i = fred.get_series(series_id_11, start_date, end_date)
literacy_i = fred.get_series(series_id_12, start_date, end_date)
lifeexp_i = fred.get_series(series_id_13, start_date, end_date)
domesdem_i= fred.get_series(series_id_14, start_date, end_date)
engagedwork_i = fred.get_series(series_id_15, start_date, end_date)
privatefinalcon_i = fred.get_series(series_id_16, start_date, end_date)
govt_lendingborrow_i=fred.get_series(series_id_17, start_date, end_date)
real_balan_trade=fred.get_series(series_id_18, start_date, end_date)

gdp_i.head(10)
gdp_i

# for GDP
df1= gdp_i.to_frame(name=('GDP'))
annual_gdp_i = df1.resample('A').mean()
annual_gdp_i['Year'] = annual_gdp_i.index.year
annual_gdp_i=annual_gdp_i[['Year', 'GDP']]
annual_gdp_i.reset_index(drop=True, inplace=True)
print(annual_gdp_i)

# for debt
df2 = debt_i.to_frame(name='Debt')
annual_debt_i = df2.resample('A').mean()
annual_debt_i['Year'] = annual_debt_i.index.year
annual_debt_i.reset_index(drop=True, inplace=True)
print(annual_debt_i)

# For CPI 
df3 = cpi_i.to_frame(name='CPI')
annual_cpi_i = df3.resample('A').mean()
annual_cpi_i['Year'] = annual_cpi_i.index.year
annual_cpi_i.reset_index(drop=True, inplace=True)
print(annual_cpi_i)

# For Export 
df4 = export_i.to_frame(name='Export')
annual_export_i = df4.resample('A').mean()
annual_export_i['Year'] = annual_export_i.index.year
annual_export_i.reset_index(drop=True, inplace=True)
print(annual_export_i)

# For Import 
df5 = import_i.to_frame(name='Import')
annual_import_i = df5.resample('A').mean()
annual_import_i['Year'] = annual_import_i.index.year
annual_import_i.reset_index(drop=True, inplace=True)
print(annual_import_i)

# For Government Final Expenditure  
df6 = govt_final_exp_i.to_frame(name='Government Final Expenditure')
annual_govt_final_exp_i = df6.resample('A').mean()
annual_govt_final_exp_i['Year'] = annual_govt_final_exp_i.index.year
annual_govt_final_exp_i.reset_index(drop=True, inplace=True)
print(annual_govt_final_exp_i)

# For Inflation
df7 = inflation_i.to_frame(name='Inflation')
annual_inflation_i = df7.resample('A').mean()
annual_inflation_i['Year'] = annual_inflation_i.index.year
annual_inflation_i.reset_index(drop=True, inplace=True)
print(annual_inflation_i)

# For GNI
df8 = gni_i.to_frame(name='Government National Expenditure')
annual_gni_i = df8.resample('A').mean()
annual_gni_i['Year'] = annual_gni_i.index.year
annual_gni_i.reset_index(drop=True, inplace=True)
print(annual_gni_i)

# For Employment Population
df9 = em_pop_i.to_frame(name='Employment Population')
annual_em_pop_i = df9.resample('A').mean()
annual_em_pop_i['Year'] = annual_em_pop_i.index.year
annual_em_pop_i.reset_index(drop=True, inplace=True)
print(annual_em_pop_i)

# For Unemployment Population
df10 = unemployment_i.to_frame(name='Unmployment Population')
annual_unemployment_i = df10.resample('A').mean()
annual_unemployment_i['Year'] = annual_unemployment_i.index.year
annual_unemployment_i.reset_index(drop=True, inplace=True)
print(annual_unemployment_i)

# For Infant Mortality
df11 = infantmor_i.to_frame(name='Infant Mortality')
annual_infantmor_i = df11.resample('A').mean()
annual_infantmor_i['Year'] = annual_infantmor_i.index.year
annual_infantmor_i.reset_index(drop=True, inplace=True)
print(annual_infantmor_i)

# For Literacy Rate
df12 = literacy_i.to_frame(name='Literacy Rate')
annual_literacy_i = df12.resample('A').mean()
annual_literacy_i['Year'] = annual_literacy_i.index.year
annual_literacy_i.reset_index(drop=True, inplace=True)
print(annual_literacy_i)


# For Life Expectancy 
df13 = lifeexp_i.to_frame(name='Life Expectancy')
annual_lifeexp_i = df13.resample('A').mean()
annual_lifeexp_i['Year'] = annual_lifeexp_i.index.year
annual_lifeexp_i.reset_index(drop=True, inplace=True)
print(annual_lifeexp_i)


# For Domestic Demand
df14 = domesdem_i.to_frame(name='Domestic Demand')
annual_domesdem_i = df14.resample('A').mean()
annual_domesdem_i['Year'] = annual_domesdem_i.index.year
annual_domesdem_i.reset_index(drop=True, inplace=True)
print(annual_domesdem_i)

# For Engaged Employees
df15 = engagedwork_i.to_frame(name='Engaged Employees')
annual_engagedwork_i= df15.resample('A').mean()
annual_engagedwork_i['Year'] = annual_engagedwork_i.index.year
annual_engagedwork_i.reset_index(drop=True, inplace=True)
print(annual_engagedwork_i)


# For Private Final Consumption Expenditure 
df16 = privatefinalcon_i.to_frame(name='Private Final Consumption Expenditure')
annual_privatefinalcon_i= df16.resample('A').mean()
annual_privatefinalcon_i['Year'] = annual_privatefinalcon_i.index.year
annual_privatefinalcon_i.reset_index(drop=True, inplace=True)
print(annual_privatefinalcon_i)

# For Government Lending and Borrrowing
df17 = govt_lendingborrow_i.to_frame(name='Government Lending and Borrrowing')
annual_govt_lendingborrow_i= df17.resample('A').mean()
annual_govt_lendingborrow_i['Year'] = annual_govt_lendingborrow_i.index.year
annual_govt_lendingborrow_i.reset_index(drop=True, inplace=True)
print(annual_govt_lendingborrow_i)

# For Real Trade Balance
df18 = real_balan_trade.to_frame(name='Government Lending and Borrrowing')
annual_real_balan_trade= df18.resample('A').mean()
annual_real_balan_trade['Year'] = annual_real_balan_trade.index.year
annual_real_balan_trade.reset_index(drop=True, inplace=True)
print(annual_real_balan_trade)
type(annual_gni_i)

merged_df= pd.merge(annual_gdp_i, annual_debt_i, how= 'outer', on= 'Year' )
merged_df= pd.merge(merged_df, annual_cpi_i, how= 'outer', on= 'Year')
merged_df= pd.merge(merged_df, annual_import_i, how= 'outer', on= 'Year' )
merged_df= pd.merge(merged_df, annual_inflation_i, how= 'outer', on= 'Year' )
merged_df= pd.merge(merged_df, annual_em_pop_i, how= 'outer', on= 'Year' )
merged_df= pd.merge(merged_df, annual_unemployment_i, how= 'outer', on= 'Year' )
merged_df= pd.merge(merged_df, annual_infantmor_i, how= 'outer', on= 'Year' )
merged_df= pd.merge(merged_df, annual_lifeexp_i, how= 'outer', on= 'Year' )
merged_df= pd.merge(merged_df, annual_engagedwork_i, how= 'outer', on= 'Year' )
merged_df= pd.merge(merged_df, annual_privatefinalcon_i, how= 'outer', on= 'Year' )
merged_df= pd.merge(merged_df, annual_govt_lendingborrow_i, how= 'outer', on= 'Year')
merged_df = merged_df.set_index('Year')


missing = merged_df.isna().sum()
print(missing)

merged_df = merged_df.fillna(merged_df.mean()) # Did using mean value imputation 

# Finding the nature of the data
#merged_df['Year']=pd.to_datetime(merged_df['Year'])

merged_df.info()

merged_df.head(20)
