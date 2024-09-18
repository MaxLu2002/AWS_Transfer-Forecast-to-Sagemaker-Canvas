import pandas as pd

# Original file paths and new output path
file_path = './FAKE_toy_sales.csv'
output_path = './Canvas_dataset/cleaned_data.csv'

# Load the original data
df = pd.read_csv(file_path)
print(f"\nOrigin dataset has {len(df)} rows in total\n")

# Define the date range for the new data
start_date = "2024-01-01"
end_date = "2024-01-07"
dates = pd.date_range(start_date, end_date).strftime('%Y-%m-%d').tolist()

# Group by Toy_ID and find the max Price for each item
max_origin_price_per_item = df.groupby(['Toy_ID', 'Toy_Name', 'Category'])['Price'].max().reset_index()

# Create a list of items with the max Price per Toy_ID
v_items = [
    {'Toy_ID': row['Toy_ID'], 'Toy_Name': row['Toy_Name'], 'Category': row['Category'], 'Price': row['Price']}
    for _, row in max_origin_price_per_item.iterrows()
]

# Construct new rows with empty 'Sales' values
new_rows = []
for date in dates:
    for item in v_items:
        new_rows.append({
            'Date': date,
            'Toy_ID': item['Toy_ID'],
            'Toy_Name': item['Toy_Name'],
            'Category': item['Category'],
            'Sales': None,  # Empty sales field
            'Price': item['Price']
        })

# Create a DataFrame from the new rows
new_data_df = pd.DataFrame(new_rows)

# Concatenate the new data with the original data
df = pd.concat([df, new_data_df], ignore_index=True)

# Save the resulting DataFrame back to a CSV file
df.to_csv(output_path, index=False)

# Print out some details
print(f"\nNew data successfully inserted: {len(new_data_df)} rows\n")
print("\n",new_data_df.head(10),"\n")
print(f"\nCanvas dataset has {len(df)} rows in total\n",df.head(),"\n")
