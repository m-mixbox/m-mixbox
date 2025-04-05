import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load data
def load_data(file_path):
    df = pd.read_excel(file_path)
    header_row_index = df[df.iloc[:, 0] == 'Date'].index[0]
    data = pd.read_excel(file_path, skiprows=header_row_index + 1)
    return data

def calculate_indicators(df):
    df['SMA_20'] = df['Price'].rolling(window=20).mean()
    df['SMA_50'] = df['Price'].rolling(window=50).mean()
    df['EMA_20'] = df['Price'].ewm(span=20, adjust=False).mean()

    delta = df['Price'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))

    df['High-Low'] = df['High'] - df['Low']
    df['High-Close'] = abs(df['High'] - df['Price'].shift())
    df['Low-Close'] = abs(df['Low'] - df['Price'].shift())
    df['True Range'] = df[['High-Low', 'High-Close', 'Low-Close']].max(axis=1)
    df['ATR'] = df['True Range'].rolling(window=14).mean()
    df['Days'] = np.arange(len(df))
    return df.dropna()

def predict_future_prices(df):
    # Ensure the data is in ascending chronological order
    df_sorted = df.sort_values(by='Date', ascending=True).reset_index(drop=True)
    features = ['Days', 'SMA_20', 'SMA_50', 'EMA_20', 'RSI', 'ATR']

    # Polynomial regression
    poly = PolynomialFeatures(degree=3)
    X_poly = poly.fit_transform(df_sorted[features])
    model = LinearRegression()
    model.fit(X_poly, df_sorted['Price'])

    # Predict on training data for evaluation
    predicted_train = model.predict(X_poly)
    mae = mean_absolute_error(df_sorted['Price'], predicted_train)
    mse = mean_squared_error(df_sorted['Price'], predicted_train)
    r2 = r2_score(df_sorted['Price'], predicted_train)

    print(f'MAE: {mae}, MSE: {mse}, R2 Score: {r2}')

    # Predict future prices for 30 days
    future_days = np.arange(len(df_sorted), len(df_sorted) + 30).reshape(-1, 1)
    future_features = poly.fit_transform(np.column_stack((future_days, *([df_sorted[feat].iloc[-1]] * 30 for feat in features[1:]))))
    predicted_prices = model.predict(future_features)

    # Plot results
    plt.figure(figsize=(12, 8))
    plt.plot(df_sorted['Days'], df_sorted['Price'], label='Actual Price', color='blue')
    plt.plot(df_sorted['Days'], predicted_train, label='Training Prediction', color='green')
    plt.plot(future_days, predicted_prices, label='Future Prediction', color='red', linestyle='dashed')
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.title('Stock Price Prediction')
    plt.legend()
    plt.show()

    print('Predicted Future Prices:', predicted_prices)

# File Path
file_path =r"C:\Users\MBSPL-Ayush\Desktop\irfc.xlsx"
data = load_data(file_path)
data_cleaned = calculate_indicators(data)
predict_future_prices(data_cleaned)
