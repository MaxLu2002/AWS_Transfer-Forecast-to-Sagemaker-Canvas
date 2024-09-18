import pandas as pd

# load file
file_path = './FAKE_toy_sales.csv'
data = pd.read_csv(file_path)

# Modify column name : Date -> timestamp, Toy_ID -> item_id, Sales -> demand
data = data.rename(columns={'Date': 'timestamp', 'Toy_ID': 'item_id', 'Sales': 'demand'})

# 1. toy_TD.csv (timestamp, item_id, demand)
toy_TD = data[['timestamp', 'item_id', 'demand']]
toy_TD.to_csv('./Forecast_dataset/toy_TD.csv', index=False)
print("\nTD wrangling DONE\n")

# 2. toy_MD.csv (item_id, Category)
toy_MD = data[['item_id', 'Category']]
toy_MD.to_csv('./Forecast_dataset/toy_MD.csv', index=False)
print("\nMD wrangling DONE\n")

# 3. toy_RD.csv (timestamp, item_id, Price)
toy_RD = data[['timestamp', 'item_id', 'Price']]
toy_RD.to_csv('./Forecast_dataset/toy_RD.csv', index=False)
print("\nRD wrangling DONE\n")
