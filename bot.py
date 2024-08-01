from pybit import HTTP
import pandas as pd
import ta
import time
import logging
from config import api_key, api_secret

# BybitのAPIクライアントの作成
session = HTTP("https://api.bybit.com", api_key=api_key, api_secret=api_secret)

# ログの設定
logging.basicConfig(level=logging.INFO)

def get_data(symbol, interval):
    try:
        response = session.query_kline(symbol=symbol, interval=interval, limit=200)
        data = pd.DataFrame(response['result'])
        data['timestamp'] = pd.to_datetime(data['open_time'], unit='s')
        data.set_index('timestamp', inplace=True)
        data['close'] = data['close'].astype(float)
        return data
    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        return None

def calculate_rsi(data, window=14):
    data['RSI'] = ta.momentum.RSIIndicator(data['close'], window=window).rsi()
    return data

def trade(symbol, side, qty, stop_loss=None):
    try:
        order = session.place_active_order(
            symbol=symbol,
            side=side,
            order_type="Market",
            qty=qty,
            time_in_force="GoodTillCancel"
        )
        logging.info(f"Order placed: {order}")

        if stop_loss:
            stop_loss_price = round(stop_loss, 2)
            stop_order = session.place_active_order(
                symbol=symbol,
                side="Sell" if side == "Buy" else "Buy",
                order_type="Market",
                qty=qty,
                stop_px=stop_loss_price,
                time_in_force="GoodTillCancel",
                reduce_only=True
            )
            logging.info(f"Stop-loss order placed: {stop_order}")

    except Exception as e:
        logging.error(f"Error placing order: {e}")

def run_bot():
    symbol = "BTCUSD"
    interval = "1"
    position_qty = 0

    while True:
        data = get_data(symbol, interval)
        if data is not None:
            data = calculate_rsi(data)
            rsi = data['RSI'].iloc[-1]

            if rsi < 30 and position_qty == 0:
                logging.info("RSI below 30, placing buy order")
                trade(symbol, "Buy", 1, stop_loss=data['close'].iloc[-1] * 0.95)
                position_qty = 1
            elif rsi > 70 and position_qty > 0:
                logging.info("RSI above 70, placing sell order")
                trade(symbol, "Sell", 1)
                position_qty = 0

        time.sleep(60)

if __name__ == "__main__":
    run_bot()
