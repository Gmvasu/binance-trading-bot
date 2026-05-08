from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()


class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_SECRET_KEY")

        self.client = Client(api_key, api_secret)

        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        response = self.client.futures_create_order(**params)

        return response