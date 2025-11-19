import pandas as pd
import pandas_ta as ta
import vectorbt as vbt
import yaml
import os
import sys

def check_if_config_file_exist(path):
    if os.path.exists(path):
        print("Found your Configuration file!")
    else:
        print("\nYour Configuration file doesn't exist!\nDo you want to create it?")

        def type_choise():
            choise = input("\nType\nY if YES\nQ if NO\n")
            choise = choise.upper().strip()
            if choise == "Q":
                sys.exit("\nCreate your Configuration file and try once more time!")
            elif choise == "Y":
                with open(path, "w") as file:
                    file.write("{'Data_filename': '*.csv', 'RSI': {'length': 7, 'overbought': 70, 'oversold': 30}, 'Trade': {'size': 1, 'size_type': 'amount'}, 'Broker': {'fees': 0.0003, 'fixed_fees': 0}, 'Slippage': 0.02, 'Initial_cash': 55000, 'Frequency': '1h'}")
            else:
                type_choise()
        type_choise()

def check_if_csv_file_exist(config):
    if os.path.exists(config['Data_filename']):
        print("Found your Data file!")
    else:
        print("Your Data file doesn't exist!")
        exit("\nPlease, check your configuration file for correct Data filename.")

def check_config(config):
    try:
        filename = config['Data_filename']
        len = config['RSI']['length']
        overbought = config['RSI']['overbought']
        oversold = config['RSI']['oversold']
        size = config['Trade']['size']
        size_type = config['Trade']['size_type']
        fees = config['Broker']['fees']
        fixed_fees = config['Broker']['fixed_fees']
        slippage = config['Slippage']
        init_cash = config['Initial_cash']
        freq = config['Frequency']
    except KeyError as e:
        exit(f"Your Configuration file is missing a key: {e}\nPlease, check your configuration file.")
    if len <= 0:
        exit("RSI length must be a positive integer.")
    if not (0 <= overbought <= 100) or not (0 <= oversold <= 100):
        exit("Overbought and Oversold levels must be between 0 and 100.")
    if overbought <= oversold:
        exit("Overbought level must be greater than Oversold level.")
    if size <= 0:
        exit("Trade size must be a positive number.")
    if size_type not in ['amount', 'percent', 'value']:
        exit("Trade size_type must be either 'amount' 'percent' or 'value'.")
    if not (0 <= fees <= 100):
        exit("Broker fees must be between 0 and 100.")
    if fixed_fees < 0:
        exit("Broker fixed_fees must be a non-negative number.")
    if slippage < 0:
        exit("Slippage must be a non-negative number.")
    if init_cash < 0:
        exit("Initial_cash must be a non-negative number.")
    if not isinstance(freq, str):
        exit("Frequency must be a string like ('1h', '15min').")

if __name__ == "__main__":
    check_if_config_file_exist("config.yaml")
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
        check_config(config)
        check_if_csv_file_exist(config)
        len = config['RSI']['length']
        overbought = config['RSI']['overbought']
        oversold = config['RSI']['oversold']

    df = pd.read_csv(config['Data_filename'])
    if 'Time' in df.columns:
        df.index = pd.to_datetime(df['Time'])
    df[f'RSI_{len}'] = ta.rsi(df['Close'], length=len)

    entries = (df[f'RSI_{len}'] < oversold) & (df[f'RSI_{len}'].shift(1) >= oversold)
    exits = (df[f'RSI_{len}'] > overbought) & (df[f'RSI_{len}'].shift(1) <= overbought)

    pf = vbt.Portfolio.from_signals(
    entries = entries,
    exits = exits,
    open = df["Open"],
    close = df["Close"],
    high = df["High"],
    low = df["Low"],
    size = config['Trade']['size'],
    size_type = config['Trade']['size_type'],
    fees = config['Broker']['fees'],
    fixed_fees = config['Broker']['fixed_fees'],
    slippage = config['Slippage'],
    init_cash = config['Initial_cash'],
    freq = config['Frequency']
    )
    print(pf.stats())
    pf.stats().to_csv("portfolio_results.csv")
    print("Statistics saved to portfolio_results.csv. Bye!")