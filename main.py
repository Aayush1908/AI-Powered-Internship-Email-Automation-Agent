import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# === Settings ===
symbol = 'RELIANCE.NS'
interval = '5m'
period = '1d'  # Only today's data

# === Download Data ===
data = yf.download(tickers=symbol, interval=interval, period=period)
data.dropna(inplace=True)

# === Plot Candlestick Chart ===
fig = go.Figure(data=[go.Candlestick(
    x=data.index,
    open=data['Open'],
    high=data['High'],
    low=data['Low'],
    close=data['Close'],
    name="5-min Candles"
)])

fig.update_layout(
    title=f"{symbol} - 5-Minute Candlestick Chart (Today)",
    xaxis_title="Time",
    yaxis_title="Price (INR)",
    xaxis_rangeslider_visible=False,
    template="plotly_dark",
    height=600
)

fig.show()
