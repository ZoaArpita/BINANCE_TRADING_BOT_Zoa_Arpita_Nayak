import os
import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
from .logging_configure import logger

load_dotenv()

class Client_Binance:
    BASE_URL="https://testnet.binancefuture.com"

    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            logger. error ("API credentials missing in .env file")
            raise ValueError("Mising Binance API credentials")

    def send_signed_request(self,method,endpoint,params = None):
        if params is None:
            params = {}

        params['timestamp'] = int(time.time()*1000)
        query_string = urlencode(params)

        signature = hmac.new(
            self.api_secret.encode('utf-8'),
            query_string.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

        params['signature'] = signature
        headers = {'X-MBX-APIKEY': self.api_key}
        url = f"{self.BASE_URL}{endpoint}"

        logger.info(f"Sending {method}  to {endpoint}")

        try:
            if method == "POST":
                response = requests.post(url, headers=headers, params=params)
            else:
                response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            logger.error(f"Binance API Error: {e.response.text}")
            raise Exception(f"API Error: {e.response.json().get('msg', 'Unknown Error')}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Network Failure: {e}")
            raise Exception("Failed to connect to Binance servers.")
