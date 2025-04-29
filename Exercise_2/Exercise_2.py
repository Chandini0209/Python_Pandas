# Data setup
# - Use the "sales_updated.csv" file from Exercise_01_Python

# Question
# - Load the data file using Pandas module
# - Rules for Region column
#         - All Region entries should be in title case
#         - Blazers are only sold in one Region
# - Find the anomalies in Region column based on the above Rules
# - Fill missing values in Region column based on the above Rules

# P1> Find which month had the highest sales
# P2> Plot region wise sales data showing the highest sales first
# P3> Plot month wise sales data. What is your inference from this plot?
              
# - Bonus questions ( optional )
#         - Fill missing values in Amount with the average amount for that product
#         - And solve questions P1, P2 and P3 as mentioned above


# Answer

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("sales_updated.csv")

# --- Clean 'Region' column ---
# Convert to title case
df["Region"] = df["Region"].astype(str).str.title()

# Find Region for Blazer (assuming all Blazers belong to one region)
blazer_region = df.loc[df["Product"] == "Blazer", "Region"].dropna().mode()
if not blazer_region.empty:
    blazer_region = blazer_region[0]
    # Fill missing Region values where Product is Blazer
    df.loc[(df["Product"] == "Blazer") & (df["Region"].isna() | (df["Region"] == "nan")), "Region"] = blazer_region

# --- P1: Find which month had the highest sales ---
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
df['Month'] = df['Date'].dt.month_name()
monthly_sales = df.groupby('Month')['Amount'].sum().sort_values(ascending=False)
print("Month with highest sales:\n", monthly_sales.head(1))

# --- P2: Region-wise sales plot ---
region_sales = df.groupby("Region")["Amount"].sum().sort_values(ascending=False)
region_sales.plot(kind="bar", title="Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# --- P3: Month-wise sales plot ---
month_sales = df.groupby("Month")["Amount"].sum()
month_sales.plot(kind="line", marker='o', title="Month-wise Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# OR
# --- P3: Month-wise sales plot ---
plt.figure(figsize=(8,5))
monthly_sales.plot(kind='bar', color='orange')
plt.title('Month-wise Sales')
plt.ylabel('Total Sales')
plt.xlabel('Month')
plt.tight_layout()
plt.show()

print("P3> Inference: The trend line shows sales fluctuation over months. Look for peaks and drops.")

# --- Bonus: Fill missing Amount with avg per Product ---
df["Amount"] = df.groupby("Product")["Amount"].transform(lambda x: x.fillna(x.mean()))

# Re-run P1, P2, P3 with updated values
# P1
p1_bonus = df.groupby("Month")["Amount"].sum().idxmax()
print("Bonus P1> Month with highest sales after filling Amounts:", p1_bonus)

# P2
region_sales_bonus = df.groupby("Region")["Amount"].sum().sort_values(ascending=False)
region_sales_bonus.plot(kind="bar", title="Region-wise Sales (After Filling Amounts)")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# P3
month_sales_bonus = df.groupby("Month")["Amount"].sum()
month_sales_bonus.plot(kind="line", marker='o', title="Month-wise Sales (After Filling Amounts)")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.show()
