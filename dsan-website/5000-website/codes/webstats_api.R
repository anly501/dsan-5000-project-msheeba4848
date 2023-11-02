# Import Libraries 

#install.packages("wbstats")
library(wbstats)
library(dplyr)


# Specify the indicators you want to fetch
indicator_b= ("NY.GDP.MKTP.CD") # GDP (current US$)
#indicator_c= ("GC.DOD.TOTL.CN") # General government gross debt (current LCU)
indicator_d= ("FP.CPI.TOTL.ZG") # For CPI
indicator_e= ("NE.IMP.GNFS.CD") # Import 
indicator_f= ("FP.CPI.TOTL") # For Inflation
indicator_g= ("NY.GNP.MKTP.CD") # For GNI
indicator_h= ("SL.EMP.TOTL.SP.ZS") # For Employement Population
indicator_i= ("SL.UEM.TOTL.ZS") # For Unemployment 
indicator_j= ("SH.DYN.MORT") # For Infant Mortality Rate
indicator_k= ("SP.DYN.LE00.IN") # For Life Expectancy 
indicator_l= ("SL.EMP.VULN.ZS") # For Engaged Workers
indicator_m= ("NE.CON.PRVT.CD") # For Private Final Consumption 


# Data for Bangladesh from 2000- 2023.

data1 <- wb(indicator = indicator_b, country = "BGD", startdate = 2000, enddate = 2023)
data3 <- wb(indicator = indicator_d, country = "BGD", startdate = 2000, enddate = 2023)
data4<- wb(indicator = indicator_e, country = "BGD", startdate = 2000, enddate = 2023)
data5 <- wb(indicator = indicator_f, country = "BGD", startdate = 2000, enddate = 2023)
data6 <- wb(indicator = indicator_g, country = "BGD", startdate = 2000, enddate = 2023)
data7 <- wb(indicator = indicator_h, country = "BGD", startdate = 2000, enddate = 2023)
data8 <- wb(indicator = indicator_i, country = "BGD", startdate = 2000, enddate = 2023)
data9 <- wb(indicator = indicator_j, country = "BGD", startdate = 2000, enddate = 2023)
data10 <- wb(indicator = indicator_k, country = "BGD", startdate = 2000, enddate = 2023)
data11<- wb(indicator = indicator_l, country = "BGD", startdate = 2000, enddate = 2023)
data12<- wb(indicator = indicator_m, country = "BGD", startdate = 2000, enddate = 2023)

# Creating a dataframe.

data1= subset(data1, select= c("date", "value"))
colnames(data1)[colnames(data1) == "value"] <- "GDP"
data3= subset(data3, select= c("date", "value"))
colnames(data3)[colnames(data3) == "value"] <- "CPI"
data4= subset(data4, select=c("date", "value"))
colnames(data4)[colnames(data4) == "value"] <- "Import"
data5= subset(data5, select= c("date", "value"))
colnames(data5)[colnames(data5) == "value"] <- "Inflation"
data6= subset(data6, select= c("date", "value"))
colnames(data6)[colnames(data6) == "value"] <- "GNI"
data7= subset(data7, select= c("date", "value"))
colnames(data7)[colnames(data7) == "value"] <- "Employement Population"
data8= subset(data8, select= c("date", "value"))
colnames(data8)[colnames(data8) == "value"] <- "Unemployement"
data9= subset(data9, select= c("date", "value"))
colnames(data9)[colnames(data9) == "value"] <- "Infant Mortality"
data10= subset(data10, select= c("date", "value"))
colnames(data10)[colnames(data10) == "value"] <- "Life Expectancy"
data11= subset(data11, select= c("date", "value"))
colnames(data11)[colnames(data11) == "value"] <- "Engaged Workers"
data12= subset(data12, select= c("date", "value"))
colnames(data12)[colnames(data12) == "value"] <- "Private Final Consumption"

# Merging the dataframes
merged_df <- full_join(data1, data3, by = "date")
merged_df <- full_join(merged_df, data4, by = "date")
merged_df <- full_join(merged_df, data5, by = "date")
merged_df <- full_join(merged_df, data6, by = "date")
merged_df <- full_join(merged_df, data7, by = "date")
merged_df <- full_join(merged_df, data8, by = "date")
merged_df <- full_join(merged_df, data9, by = "date")
merged_df <- full_join(merged_df, data10, by = "date")
merged_df <- full_join(merged_df, data11, by = "date")
merged_df <- full_join(merged_df, data12, by = "date")


# Extract the year from the Date object
year <- format(date, "%Y")
row.names(merged_df) <- merged_df$date


# Checking missing value imputation
sum(is.na(merged_df)) # There are 3 

# Using mean value imputation 
for (x in names(merged_df)) {
  mean <- mean(merged_df[[x]], na.rm = TRUE)  # Calculate column mean ignoring NA
  merged_df[[x]][is.na(merged_df[[x]])] <- mean    # Replace NA with column mean
}

summary(merged_df) # Everything is in numerical except date
merged_df$date <- as.Date(merged_df$date, format = "%Y")
merged_df<- merged_df[rev(1:nrow(merged_df)), ]
class(merged_df$date) # It is date.
print(merged_df)

merged_df=subset(merged_df, select= -date)

# Specify the indicators you want to fetch
indicator_a=("BN.KLT.DINV.CD") # FDI Current Exp
indicator_b= ("NY.GDP.PCAP.KD.ZG") # GDP per capita growth
indicator_c= ("NE.CON.GOVT.ZS") # Government Final Consumption Expenditure 
indicator_d= ("NE.EXP.GNFS.ZS") # Imports of Goods and Services as a Percentage of GDP 
indicator_e= ("FP.CPI.TOTL.ZG") # Inflation (consumer prices)
indicator_f= ("FR.INR.RINR") # Real Interest Rate
indicator_g= ("GC.DOD.TOTL.GD.ZS") # Central Government Debt
indicator_h= ("SL.UEM.TOTL.ZS") # Unemployement
indicator_i= ("MS.MIL.XPND.GD.ZS") # Military Expenditure
