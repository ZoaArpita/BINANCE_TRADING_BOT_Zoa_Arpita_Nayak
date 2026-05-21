# Binance Futures Testnet Trading Bot

This is a Python-based trading bot built for the Binance Futures Testnet (USDT-M). It features a fully modular backend architecture for order execution and includes both a Command Line Interface (CLI) and a live web-based UI.

**[Here is the light UI that you can place orders from](https://binancetradingbotzoaarpitanayak-9lexliys8rwuylg8vvlpvr.streamlit.app/)**


**[Here is the website that gets affected, as the API is preloaded you cant replace the affected account in this UI](https://testnet.binancefuture.com)**

*(Note: The live UI is pre-configured with secure demo testnet API keys. No setup required.)*

---

## Proof of Execution UI based
Check the timing for each

LIMIT BUY
<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/dbc26906-3697-432f-bfd6-73f60d580755" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/c88f4710-2e1e-4fd4-a89e-4f6daee24d01" />


LIMIT SELL
<img width="1914" height="1079" alt="image" src="https://github.com/user-attachments/assets/74cc6a99-4bb3-49b1-9437-55de82d7a507" />
<img width="1918" height="1076" alt="image" src="https://github.com/user-attachments/assets/d505ec06-46ef-4be8-bcc6-b1ba61cad103" />

MARKET BUY
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/deef8714-02be-4dcb-a91f-6f5c843affe5" />
<img width="1919" height="1075" alt="image" src="https://github.com/user-attachments/assets/39dac07b-4a55-4e0f-91ba-043773d37824" />

MARKET SELL
<img width="1918" height="1079" alt="image" src="https://github.com/user-attachments/assets/8e1faa65-0f01-4c0f-a5ce-79bfc510f235" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/df45d365-aa2c-4abd-b981-5c77d2988335" />


## Proof of Execution CLI Based
Check the timing for each

LIMIT BUY
<img width="1919" height="1071" alt="image" src="https://github.com/user-attachments/assets/3a1b5748-7d29-4715-9898-9537f234cab0" />
<img width="1917" height="1079" alt="image" src="https://github.com/user-attachments/assets/849f7fa7-ffc5-4bbc-bdd7-6eed73b90649" />

LIMIT SELL
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/10e2d654-4f07-4438-904c-8179390ded11" />
<img width="1919" height="1077" alt="image" src="https://github.com/user-attachments/assets/c9b41ca7-6d75-48e7-b8fd-ffec9cfa6be7" />

MARKET BUY 
<img width="1917" height="1079" alt="image" src="https://github.com/user-attachments/assets/9d440637-c354-4616-b801-1b845a7ed983" />
<img width="1919" height="1062" alt="image" src="https://github.com/user-attachments/assets/569b7aa8-4415-4ce5-8e99-55763105b671" />

MARKET SELL
<img width="1899" height="1061" alt="image" src="https://github.com/user-attachments/assets/4d7b53f7-9907-4a7d-bddc-f1712dbf7578" />
<img width="1914" height="1078" alt="image" src="https://github.com/user-attachments/assets/83390005-4aa6-4cae-bc7e-3c48b29f4a14" />

Keep in mind if you use the UI then the logs dont show up in log files. If done in venv terminal then it'll show up in logs.
--

## Features
* **Order Types:** MARKET and LIMIT
* **Sides:** BUY (Long) and SELL (Short)
* **Markets:** USDT-M Futures (Testnet)
* **Interfaces:** Interactive Streamlit UI & robust Typer/Argparse CLI
* **Logging:** Comprehensive logging of all API requests, responses, and raw Binance errors to `logs/binance.log`.

---

## Local Setup Instructions

If you wish to run the CLI locally, follow these steps:

### 1. Prerequisites
* Python 3.9+
* A Binance Futures Testnet Account


### 2. Installation
Clone the repository and install the required dependencies:

```
git clone https://github.com/ZoaArpita/BINANCE_TRADING_BOT_Zoa_Arpita_Nayak.git
cd BINANCE_TRADING_BOT_Zoa_Arpita_Nayak
pip install -r requirements.txt
```

3. Environment Variables

To run the bot locally, you must provide your own Binance Testnet API keys.
Create a file named .env in the root directory and add your credentials:
Code snippet

BINANCE_API_KEY="your_testnet_api_key_here"

BINANCE_API_SECRET="your_testnet_api_secret_here"

CLI Usage Examples

The CLI provides a clean interface for executing testnet trades. Ensure your virtual environment is active and your .env file is configured.

Place a Market Buy Order:
```

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```
Place a Limit Sell Order:
```

python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.05 --price 3500
```
Place a Limit Buy Order (Catch a dip):
```
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 40000
```
Assumptions & Design Decisions

    Network: The bot strictly interacts with https://testnet.binancefuture.com. It is not configured for the live Binance mainnet.

    Account Funding: The bot assumes the provided testnet API keys correspond to an account with sufficient USDT margin to execute the requested trades.

    API Key Management: Local execution relies on .env files for security. The hosted Streamlit deployment utilizes Streamlit Community Cloud's native Secrets management. If one decides to use the UI then they have to creat a Streamlit account and upload the files with the secret key and api key.

    Time In Force: Limit orders are assumed to default to GTC (Good 'Til Canceled) via the Binance API unless otherwise specified.

