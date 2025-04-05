import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers

# Load data
df = pd.read_excel(r"C:\Users\MBSPL-Ayush\Desktop\irfc.xlsx")

# Calculate RSI
def calculate_rsi(data, period=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))
df['RSI'] = calculate_rsi(df)

# Calculate Bollinger Bands
df['SMA'] = df['Close'].rolling(window=20).mean()
df['STD'] = df['Close'].rolling(window=20).std()
df['Upper_BB'] = df['SMA'] + (2 * df['STD'])
df['Lower_BB'] = df['SMA'] - (2 * df['STD'])

# Calculate DEMA
def dema(data, period=20):
    ema = data['Close'].ewm(span=period, adjust=False).mean()
    dema = (2 * ema) - ema.ewm(span=period, adjust=False).mean()
    return dema
df['DEMA'] = dema(df)

# Calculate Support and Resistance
def calculate_support_resistance(data, window=14):
    data['Support'] = data['Low'].rolling(window=window).min()
    data['Resistance'] = data['High'].rolling(window=window).max()
calculate_support_resistance(df)

# Detect Breakout Possibility
def detect_breakout(data):
    data['Breakout_Possibility'] = np.where(
        (data['Close'] > data['Resistance']) | (data['Close'] < data['Support']), 1, 0
    )
    data['Breakout_Probability'] = np.where(
        (data['Close'] > data['Resistance']), (data['Close'] - data['Resistance']) / data['Close'] * 100,
        np.where((data['Close'] < data['Support']), (data['Support'] - data['Close']) / data['Close'] * 100, 0)
    )
detect_breakout(df)

# Feature engineering
df['Volume_Change'] = df['Volume'].pct_change()
df['Price_Change'] = df['Close'].pct_change()
df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)

# Drop NaN values
df.dropna(inplace=True)

# Prepare data for training
features = ['RSI', 'Upper_BB', 'Lower_BB', 'DEMA', 'Volume_Change', 'Price_Change', 'Support', 'Resistance', 'Breakout_Possibility', 'Breakout_Probability']
x = df[features]
y = df['Target']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Standardization
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Build model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(len(features),)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(x_train, y_train, epochs=50, batch_size=32, validation_data=(x_test, y_test))

# Evaluate model
loss, accuracy = model.evaluate(x_test, y_test)
print(f'Accuracy: {accuracy * 100:.2f}%')
