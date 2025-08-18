# Robo-Advisor Portfolio Simulator

## Project Overview
This project is a **Python-based robo-advisor simulator** that allows users to simulate investment portfolios using historical stock and ETF data. The app calculates portfolio growth, annualized return, volatility, and Sharpe ratio based on user-selected risk tolerance or individual stocks.

The project demonstrates skills in:
- Financial data analysis with Python (`pandas`, `yfinance`, `numpy`)  
- Portfolio calculations and performance metrics  
- Data visualization using `matplotlib`  
- Full-stack app potential (can be extended with FastAPI + React)  

---

## Features
- Pulls historical price data from Yahoo Finance via `yfinance`  
- Calculates daily returns, cumulative growth, and key performance metrics  
- Supports:
  - Weighted portfolios with multiple ETFs (e.g., VOO, BND, VXUS)  
  - Single-stock analysis (e.g., MSFT)  
- Plots cumulative portfolio growth over time  
- Displays annualized return, volatility, and Sharpe ratio  
