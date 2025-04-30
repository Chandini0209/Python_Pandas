# Data setup
# Data file: https://raw.githubusercontent.com/asarfraaz/Litmus/refs/heads/main/data/sales_24.csv
# Download the contents of the above file and store it as "sales_24.csv"

# Question
# Write a Python script to fix anomalies in "sales_24.csv" file
# - Open the downloaded "sales_24.csv" file using csv module.
# - All values in Amount column should be rounded down to the nearest integer
# 	- You can use the appropriate function in “math” module for this
# - Ignore any missing values ( and leave them as it is )
# - Create a new file called "sales_updated.csv" with the modified Amount column
# - All the other columns should contain the same data as in the original file

# Hint:
# https://docs.python.org/3/library/csv.html#csv.writer


# Answer

import csv
import math

# Open the input and output files
with open('sales_24.csv', mode='r', newline='', encoding='utf-8') as infile, \
     open('sales_updated.csv', mode='w', newline='', encoding='utf-8') as outfile:

    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        amount_value = row.get("Amount")

        # Check if Amount is not missing and can be converted to float
        if amount_value and amount_value.strip():
            try:
                amount_float = float(amount_value)
                row["Amount"] = str(math.floor(amount_float))
            except ValueError:
                # If conversion fails, keep the original value
                pass

        # Write the updated or original row to the output file
        writer.writerow(row)

print("File 'sales_updated.csv' created successfully.")
