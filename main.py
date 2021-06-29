import pandas as pd
from python_bitvavo_api.bitvavo import Bitvavo
import datetime as dt
import os

CSV_INPUT = "purchases.csv"
CSV_OUTPUT = "analysis.csv"


def get_current_rates():
    """
    Get latest rates for all markets available in Bitvavo
    :return: {market: rate (as float)}
    """
    bitvavo = Bitvavo()
    responses = bitvavo.tickerPrice({})
    return {entry["market"]: float(entry["price"]) for entry in responses}


def get_24h_rates(market_name):
    """
    Return 24h details for one market
    :param market_name: market name, e.g. BCN-EUR
    :return: dictionary with rate-, volume- and bid/ask information
    """
    bitvavo = Bitvavo()
    response = bitvavo.ticker24h({"market": market_name})
    return response


def two_digits(number):
    if pd.isnull(number):
        number = 0
    return round(number, 2)


def main():
    in_pycharm = "RUNNING_INSIDE_PYCHARM" in os.environ
    now = dt.datetime.now()
    date = now.strftime("%d-%m-%Y")

    df = pd.read_csv(CSV_INPUT)
    if df.empty:
        print(f"Please enter your purchases in '{CSV_INPUT}'")
        return
    for index, row in df.iterrows():
        market = f"{row.currency}-{row.base}"
        rates = get_24h_rates(market)
        df.at[index, "opening_rate"] = float(rates["open"])
        df.at[index, "current_price"] = float(rates["last"])

    df["purchase_rate"] = (df.investment / df.number)
    df["current_value"] = (df.number * df.current_price).apply(two_digits)
    df["increase"] = (df.current_value - df.investment).apply(two_digits)
    df["percentage"] = (df.increase / df.investment * 100).apply(two_digits)
    df["day_delta"] = (100 * (df.current_price - df.opening_rate) / df.current_price).apply(two_digits)
    df["date"] = date
    df["time"] = now.strftime("%H:%M:%S")
    print("\n")

    print(df[["currency", "current_value", "increase", "percentage"]])
    print(f"\nVirtual result €{df.increase.sum():.2f}")

    df.to_csv("%s" % CSV_OUTPUT, index=False)
    if not in_pycharm:
        input("\n\nPress enter to continue")


if __name__ == '__main__':
    main()
