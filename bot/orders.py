from .client import Client_Binance
from .logging_configure import logger

class OrderManager:
    def __init__(self):
        self.client = Client_Binance()

    def place_order(self, symbol, side, order_type,quantity, price=None):
        endpoint = "/fapi/v1/order"

        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
        }

        if order_type.upper() == "LIMIT":
            if not price:
                raise ValueError("Price is required for LIMIT orders")
            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Preparing {order_type}{side} order for {quantity} {symbol}")
        return self.client.send_signed_request("POST",endpoint,params)
