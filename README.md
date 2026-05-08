# Binance Futures Testnet Trading Bot

A simplified trading bot built using Python and Binance Futures Testnet API.

## Features
- Market Orders
- Limit Orders
- BUY / SELL support
- CLI input support
- Logging
- Exception handling

## Technologies Used
- Python
- python-binance
- argparse
- logging

## Run Project

```bash
pip install -r requirements.tx
python app.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001
python app.py --symbol BTCUSDT --side BUY --order_type LIMIT --quantity 0.001 --price 60000
