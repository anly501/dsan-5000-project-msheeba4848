# Import Libraries 

#install.packages("wbstats")
library(wbstats)
library(dplyr)


# Specify the indicators you want to fetch
indicator_a= ("BN.KLT.DINV.CD") #FDI Current Expenditure for the United States
indicator_b= ("NY.GDP.PCAP.KD.ZG") # GDP per capita growth for the United States
indicator_c= ("NE.CON.GOVT.ZS") # Government Final Consumption Expenditure for the United States
indicator_d= ("NE.EXP.GNFS.ZS") # Imports of Goods and Services as a Percentage of GDP for the United States
indicator_e= ("FP.CPI.TOTL.ZG") # Inflation (consumer prices) for the United States
indicator_f= ("FR.INR.RINR") # Real Interest Rate for the United States
indicator_g= ("GC.DOD.TOTL.GD.ZS") # Central Government Debt Total (% of GDP) for the United States
indicator_h= ("SL.UEM.TOTL.ZS")  # Unemployment Rate for the United States
indicator_i= ("MS.MIL.XPND.GD.ZS") # Military Expenditure for the United States

# Data for United States from 2000- 2023.

data1 <- wb(indicator = indicator_a, country = "US", startdate = 1973, enddate = 2023)
data2 <- wb(indicator = indicator_b, country = "US", startdate = 1973, enddate = 2023)
data3 <- wb(indicator = indicator_c, country = "US", startdate = 1973, enddate = 2023)
data4 <- wb(indicator = indicator_d, country = "US", startdate = 1973, enddate = 2023)
data5<- wb(indicator = indicator_e, country = "US", startdate = 1973, enddate = 2023)
data6 <- wb(indicator = indicator_f, country = "US", startdate = 1973, enddate = 2023)
data7 <- wb(indicator = indicator_g, country = "US", startdate = 1973, enddate = 2023)
data8 <- wb(indicator = indicator_h, country = "US", startdate = 1973, enddate = 2023)
data9 <- wb(indicator = indicator_i, country = "US", startdate = 1973, enddate = 2023)

# Creating a dataframe.

data1= subset(data1, select= c("date", "value"))
colnames(data1)[colnames(data1) == "value"] <- "FDI Current Exp"
data2=subset(data2, select= c("date", "value"))
colnames(data2)[colnames(data2) == "value"] <- "GDP Per Capita Growth"
data3= subset(data3, select= c("date", "value"))
colnames(data3)[colnames(data3) == "value"] <- "Government Final Consumption Expenditure"
data4= subset(data4, select=c("date", "value"))
colnames(data4)[colnames(data4) == "value"] <- "Imports of Goods and Services"
data5= subset(data5, select= c("date", "value"))
colnames(data5)[colnames(data5) == "value"] <- "Inflation (Consumer Prices)"
data6= subset(data6, select= c("date", "value"))
colnames(data6)[colnames(data6) == "value"] <- "Real Interest Rate"
data7= subset(data7, select= c("date", "value"))
colnames(data7)[colnames(data7) == "value"] <- "Central Government Debt"
data8= subset(data8, select= c("date", "value"))
colnames(data8)[colnames(data8) == "value"] <- "Unemployement"
data9= subset(data9, select= c("date", "value"))
colnames(data9)[colnames(data9) == "value"] <- "Military Expenditure"

# Merging the dataframes
merged_df <- full_join(data1, data2, by = "date")
merged_df <- full_join(merged_df, data3, by = "date")
merged_df <- full_join(merged_df, data4, by = "date")
merged_df <- full_join(merged_df, data5, by = "date")
merged_df <- full_join(merged_df, data6, by = "date")
merged_df <- full_join(merged_df, data7, by = "date")
merged_df <- full_join(merged_df, data8, by = "date")
merged_df <- full_join(merged_df, data9, by = "date")

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


