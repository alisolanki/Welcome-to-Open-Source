import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('walmart.db')
cursor = conn.cursor()

# Load the spreadsheets into Pandas DataFrames
spreadsheet_0 = pd.read_excel('spreadsheet_0.xlsx')
spreadsheet_1 = pd.read_excel('spreadsheet_1.xlsx')
spreadsheet_2 = pd.read_excel('spreadsheet_2.xlsx')

# Step 4: Insert Data from Spreadsheet 0 (Self-contained)
# This spreadsheet can be directly inserted into the database
# Loop through each row in spreadsheet 0 and insert it into the database
for index, row in spreadsheet_0.iterrows():
    cursor.execute('''
        INSERT INTO your_table_name (column1, column2, column3, ...)
        VALUES (?, ?, ?, ?)
    ''', (row['column1'], row['column2'], row['column3'], ...))

# Commit the changes
conn.commit()

# Step 5: Handle Data from Spreadsheet 1 and 2 (Dependent Data)
# Spreadsheet 1 contains the products, and spreadsheet 2 contains the shipping info
# Merge spreadsheet_1 and spreadsheet_2 based on the "shipping_identifier" column
merged_data = pd.merge(spreadsheet_1, spreadsheet_2, on="shipping_identifier", how="inner")

# Now insert the merged data into the database
for index, row in merged_data.iterrows():
    cursor.execute('''
        INSERT INTO your_shipment_table_name (product_id, quantity, origin, destination)
        VALUES (?, ?, ?, ?)
    ''', (row['product_id'], row['quantity'], row['origin'], row['destination']))

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
