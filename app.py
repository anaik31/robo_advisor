import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Download data with auto-adjusted prices
tickers = ["VOO", "BND", "VXUS"]
data = yf.download(tickers, start="2018-01-01", end="2023-01-01", auto_adjust=True)

# The 'Close' column now contains adjusted prices
if 'Close' in data.columns:
    data = data['Close']  # For single-level columns
else:
    # If multiple tickers, 'Close' is at top level
    data = data['Close'] if isinstance(data.columns, pd.MultiIndex) else data

# Step 2: Calculate returns
returns = data.pct_change().dropna()

# Step 3: Portfolio weights (balanced)
weights = [0.6, 0.3, 0.1]
portfolio_returns = (returns * weights).sum(axis=1)
cumulative_returns = (1 + portfolio_returns).cumprod()

# Step 4: Plot results
cumulative_returns.plot(figsize=(10,6), title="Balanced Portfolio Growth (2018-2023)")
plt.ylabel("Growth of $1")
plt.show()

# Step 5: Performance metrics
annual_return = portfolio_returns.mean() * 252
annual_volatility = portfolio_returns.std() * np.sqrt(252)
sharpe_ratio = annual_return / annual_volatility

print("Annual Return:", round(annual_return*100, 2), "%")
print("Annual Volatility:", round(annual_volatility*100, 2), "%")
print("Sharpe Ratio:", round(sharpe_ratio, 2))
