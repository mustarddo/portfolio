# Final Project - Analyzing Sales Data

#**Date**: 25 Febuary 2024

#**Author**: Arnon Sudyoddee (MUD)

#**Tools**: `Pandas`

# import data
import pandas as pd
df = pd.read_csv("/data/notebook_files/sample-store.csv")

# preview top 5 rows
df.head()

# check row & columns & info of dataset
df.shape
df.info()

# Edit columns name
df.columns.str.lower().str.replace(" ", "_")

# Convert order date and ship date to datetime in the original dataframe
df['order_date'] = pd.to_datetime(df['order_date'], format = '%m/%d/%Y')
df['ship_date'] = pd.to_datetime(df['ship_date'], format = '%m/%d/%Y')

# Check nan value
df.isna().sum()

# TODO - filter rows with missing values
df[df['postal_code'].isna() == True]

## Analysis part
# 1 what is the average time range between each ship mode
df['time_ship'] = (df['ship_date']-df['order_date'])
df.groupby(['ship_mode'])['time_ship'].agg(['mean']).sort_values(by = 'mean')

# 2 Filter California sales and export to csv 
df_california = df[df['country/region'] == 'California']
df_california.to_csv("california_data.csv")

# 3 Filter California & Texus sales in 2017 only and export to csv file
df_2ct = df[(df['country/region'] == 'California')\
   | (df['country/region'] == 'Texus')\
   & (pd.DatetimeIndex(df['order_date']).year == 2017)]
df_2ct.to_csv('California_Texus_data.csv')

# 4 how much total sales, average sales, and standard deviation of sales the company make in 2017

import datetime as dt
df_2017 = df[df['order_date'].dt.year == 2017] # 1st way
df_2017 = df[df['order_date'].dt.strftime('%Y') == '2017'] # 2nd way
df_2017_sales = df_2017['sales'].agg(['sum','mean','std'])
for i in range (3):
    if i == 0:
        print("--- Answer of this question are ---")
        print(f"Total Sales of Company : {df_2017_sales[i]}")
    elif i == 1:
        print(f"Average Sales of Company : {df_2017_sales[i]}")
    else:
        print(f"Standard Deviation of Company : {df_2017_sales[i]}")

# 5 - which Segment has the highest profit in 2018

df[df['order_date'].dt.strftime('%Y') == '2018'].groupby(['segment'])['profit']\
    .agg(['max']).sort_values(by = 'max' ,ascending = False).iloc[[0]]

# 6 - which top 5 States have the least total sales between 15 April 2019 - 31 December 2019

least_state = df.groupby(['state'])['sales'].agg('sum').sort_values().head()
print(least_state)

# 7 what is the proportion of total sales (%) in West + Central in 2019 
df_2019 = df[df['order_date'].dt.strftime('%Y') == '2019']
p_wc_2019 = df_2019.query("region == 'West' | state == 'Central'")['sales'].sum()/df_2019['sales'].sum()*100
print(f"Proportion of total sales(%) in West + Central in 2019 = {round(p_wc_2019,2)}%")


# 08 - find top 10 popular products in terms of number of orders vs. total sales during 2019-2020

df_19to20 = df.query("order_date >= '2019-01-01' & order_date <= '2020-12-31'")
df_19_mostsales = df_19to20.groupby(['product_name'])['sales'].agg('sum').sort_values(ascending = False).head(10) 
df_19_mostorders = df_19to20.groupby(['product_name'])['product_name'].agg('count').sort_values(ascending = False).head(10) 
print("---------------------------------------------------------------------------")
print("This is the list of products that have the most total sales." )
print(df_19_mostsales)
print("---------------------------------------------------------------------------")
print("This is the list of products that have the most sales orders.")
print(df_19_mostorders)
print("---------------------------------------------------------------------------")

df.groupby(df['order_date'].dt.strftime('%Y'))['sales'].agg('sum').plot(kind = 'bar' )
