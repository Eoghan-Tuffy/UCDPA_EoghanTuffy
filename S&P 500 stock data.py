
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import yfinance as yf




df = pd.read_csv("all_stocks_5yr.csv")
#real time stocks
end = datetime.now()
start = datetime(end.year -1, end.month, end.day)

df_aapl = yf.download("AAPL", start, end, interval = "1d")
df_amzn = yf.download("AMZN", start, end, interval = "1d")
df_tsla = yf.download("TSLA", start, end, interval = "1d")
df_fb = yf.download("FB", start, end, interval = "1d")
df_SP500 = yf.download("^GSPC", start, end, interval = "1d")

dfnew_list = [df_aapl, df_amzn, df_tsla, df_fb, df_SP500]
dfnew_name = ["AAPL", "AMZN", "TSLA", "FB", "SP500"]

for df, com_name in zip(dfnew_list, dfnew_name):
    df["dfnew_name"] = com_name

df_new = pd.concat(dfnew_list, axis=0)
print(df_new.tail(10))


#plt.figure(figsize=(15,5))
#plt.plot(top=1.25, bottom=1.2)


#for i, df in enumerate(dfnew_list, 1):
    #plt.plot(1, 2, i)
    #df_new["Close"].plot()
    #plt.ylabel("Close Price")
    #plt.xlabel("Month")
    #plt.title(f"Closing Price of {dfnew_name[i-1]}")

#plt.show()
#df_aapl["Open"].plot(label ='Apple Open Price', figsize=(15,7))
#df_aapl["Close"].plot(label ='Apple Close Price')
#df_aapl["High"].plot(label ='Apple High Price')
#df_aapl["Low"].plot(label ='Apple Low Price')
#plt.legend()
#plt.title("Apple Stock Prices")
#plt.ylabel("Stock Price")
#plt.show()

#df_aapl["Volume"].plot(figsize=(17,5))
#plt.title("Volume Traded by Apple")
#plt.show()

df_aapl["Open"].plot(label="Apple", figsize=(15,7))
df_fb["Open"].plot(label="Facebook")
df_amzn["Open"].plot(label="Amazon")
df_tsla["Open"].plot(label="Tesla")
df_SP500["Open"].plot(label="S&P 500")
plt.title("Stock Prices")
plt.ylabel("Stock Price of FB, AMZN, TSLA and S&P500")
plt.legend()
plt.show()
#df.groupby("Name")[["close", "open"]].agg([np.mean, np.median])

#Volume
df_aapl["Volume"].plot(label="Apple", figsize=(15,7))
df_fb["Volume"].plot(label="Facebook")
df_amzn["Volume"].plot(label="Amazon")
df_tsla["Volume"].plot(label="Tesla")
df_SP500["Volume"].plot(label="S&P 500")
plt.ylabel("Volume Traded")
plt.legend()
plt.show()

df_aapl.iloc[10:30]["Open"].plot()
plt.show()

df_tsla["Total Traded"]= df_tsla["Open"]*df_tsla["Volume"]
df_fb["Total Traded"]= df_fb["Open"]*df_fb["Volume"]
df_amzn["Total Traded"]= df_amzn["Open"]*df_amzn["Volume"]
df_aapl["Total Traded"]= df_aapl["Open"]*df_aapl["Volume"]
df_tsla["Total Traded"].plot(label="Tesla", figsize= (15, 7))
df_fb["Total Traded"].plot(label="FB")
df_amzn["Total Traded"].plot(label="AMZN")
df_aapl["Total Traded"].plot(label="AAPL")
plt.ylabel("Total Traded")
plt.legend()
plt.show()

print(df_tsla["Total Traded"].argmax())
print(df_tsla.iloc[[df_tsla["Total Traded"].argmax()]])

#Moving Average

df_fb["Open"].plot(label = "MA50", figsize=(15,7))
df_fb["MA50"] = df_fb["Open"].rolling(50).mean()
df_fb["MA50"].plot(label="MA50")
plt.legend()
plt.show()


from pandas.plotting import scatter_matrix
import pandas as pd

main_stocks = pd.concat([df_aapl["Open"], df_fb["Open"], df_tsla["Open"], df_amzn["Open"] ], axis = 1)
main_stocks.columns = ["AAPL Open", "FB Open","TSLA Open", "AMZN Open"]
scatter_matrix(main_stocks, figsize= (8,8), hist_kwds={"bins":50})
plt.show()

from mpl_finance import candlestick_ohlc
