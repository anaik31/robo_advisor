from fastapi import FastAPI
from pydantic import BaseModel
import yfinance as yf
import pandas as pd
import numpy as np

app = FastAPI(title="Robo-Advisor Backend")

# Input model for POST requests
class PortfolioRequest(BaseModel):
    risk_level: str  # "Conservative", "Balanced", "Aggressive"
    tickers: list = ["VOO", "BND", "VXUS"]  # default portfolio
    start_date: str = "2018-01-01"
    end_date: str = "2023-01-01"

# Map risk levels to weights
def get_weights(risk_level, num_assets):
    if risk_level.lower() == "conservative":
        weights = [0.3, 0.6, 0.1]
    elif risk_level.lower() == "balanced":
        weights = [0.6, 0.3, 0.1]
    elif risk_level.lower() == "aggressive":
        weights = [0.9, 0.05, 0.05]
    else:
        # Default to balanced
        weights = [0.6, 0.3, 0.1]
    
    # Adjust if number of tickers changes
    if len(weights) != num_assets:
        weights = [1/num_assets] * num_assets
    
    return weights