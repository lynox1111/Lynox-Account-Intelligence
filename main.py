import pandas as pd

# 1. DATA LOADING (Raw data ko software mein lana)
# Ye line hamari CSV file ko read karti hai taaki hum calculation kar sakein.
data = pd.read_csv('sales_data.csv')

# 2. ACCOUNTING LOGIC (Har transaction ka calculation)
# Hum naye columns bana rahe hain jo automatically calculation karenge.
data['Total_Sales'] = data['Quantity'] * data['Price']
data['GST_18_Percent'] = data['Total_Sales'] * 0.18
data['Net_Profit_22_Percent'] = data['Total_Sales'] * 0.22

# 3. AGGREGATION (Poore business ka summary nikalna)
# Yahan hum sabhi sales, tax aur profit ko jod rahe hain.
grand_total_sales = data['Total_Sales'].sum()
total_gst = data['GST_18_Percent'].sum()
total_net_profit = data['Net_Profit_22_Percent'].sum()

# 4. REPORT GENERATION (Result ko saaf tarike se dikhana)
print("-" * 40)
print("     LYNOX ACCOUNTING INTELLIGENCE     ")
print("-" * 40)
print(f"Total Revenue Generated:  INR {grand_total_sales}")
print(f"Government GST (18%):     INR {total_gst}")
print(f"Clean Net Profit (22%):   INR {total_net_profit}")
print("-" * 40)
