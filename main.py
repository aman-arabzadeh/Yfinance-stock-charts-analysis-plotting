import sys
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def normalize_tickers(aktier):
    return [s.upper().strip() for s in aktier]


def download_data(stockData, start, end):
    df = yf.download(stockData, start=start, end=end, progress=False)
    if df.empty:
        raise ValueError(f"Ingen data för {stockData}")
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel(1)
    return df


def plot_data(df, ticker, i):
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.plot(df['Close'], label='Closing Price', color='blue')
    plt.plot(df['High'], label='High Price', color='red')
    plt.plot(df['Low'], label='Low Price', color='green')
    plt.title("Stock Closing, High, Low Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    ax.set_title(f'{ticker} yfinance')
    plt.savefig('stock' + str(i))
    plt.show()


def main():
    # Global data
    globala = [
        'GOOGL', 'SPY', 'AAPL', 'MSFT', 'AMZN',
        'NVDA', 'AMD', 'TSM', 'TSLA', 'NIO', 'META', 'ASML.AS',
        'PLTR', 'VRSN', 'CORT', 'HOOD', 'SFM', 'AVGO', 'WMT'
    ]

    # Svenska data
    svenska = [
        'ERIC-B.ST', 'VOLV-B.ST', 'ATCO-A.ST', 'HM-B.ST', 'INVE-B.ST'
    ]

    alla_aktier = globala
    tickers = normalize_tickers(alla_aktier)

    i = 0
    for ticker in tickers:
        try:
            data = download_data(ticker, '2021-01-21', '2025-01-21')
            plot_data(data, ticker, i)
            i += 1

        except Exception as e:
            print(f"Misslyckades för {ticker}: {e}", file=sys.stderr)


if __name__ == '__main__':
    main()
