import pandas as pd
import numpy as np

# Load the Excel file
file_path = r"C:\Users\MBSPL-Ayush\Desktop\irfc.xlsx"
df = pd.read_excel(file_path, header=4)

# Clean and format data
df.columns = df.iloc[0]
df = df[1:].reset_index(drop=True)
df = df.dropna(how='all')  # Remove empty rows

# Convert data types
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df[['Price', 'Open', 'High', 'Low', 'Volume', 'Change(%)']] = df[
    ['Price', 'Open', 'High', 'Low', 'Volume', 'Change(%)']
].apply(pd.to_numeric, errors='coerce')

# Remove invalid or missing values
df = df.dropna(subset=['Date', 'Price', 'High', 'Low'])

# Sort by Date (if needed)
df = df.sort_values(by='Date', ascending=True).reset_index(drop=True)

# Calculate the True Range (TR)
df['True Range'] = df[['High', 'Low', 'Price']].apply(
    lambda x: max(x['High'] - x['Low'], abs(x['High'] - x['Price']), abs(x['Low'] - x['Price'])),
    axis=1
)

# Calculate the ATR using a 14-day rolling window
if len(df) >= 14:
    df['ATR'] = df['True Range'].rolling(window=14).mean()

    # Get the latest values
    latest_price = df['Price'].iloc[-1]
    latest_atr = df['ATR'].iloc[-1]

    # Calculate Stop-Loss and Target Price using a 2:1 risk-reward ratio
    stop_loss = latest_price - latest_atr
    target_price = latest_price + 2 * (latest_price - stop_loss)

    print(f"Entry Price: ₹{latest_price:.2f}")
    print(f"Stop-Loss: ₹{stop_loss:.2f}")
    print(f"Target Price: ₹{target_price:.2f}")
    print(f"ATR (Volatility): ₹{latest_atr:.2f}")
else:
    print("Insufficient data for ATR calculation (requires at least 14 days of data).")
