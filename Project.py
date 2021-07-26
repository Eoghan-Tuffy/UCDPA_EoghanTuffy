import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import yfinance as yf


df = pd.read_csv("all_stocks_5yr.csv")

fb = df[df["Name"]=="FB"]
amzn = df[df["Name"]=="AMZN"]
tsla = df[df["Name"]=="TSLA"]
aapl = df[df["Name"]=="AAPL"]


print(df.head())
print(df.tail())

#real time stocks
end = datetime.now()
start = datetime(end.year -5, end.month, end.day)

df_aapl = yf.download("AAPL", start, end, interval = "1d")
df_amzn = yf.download("AMZN", start, end, interval = "1d")
df_tsla = yf.download("TSLA", start, end, interval = "1d")
df_fb = yf.download("FB", start, end, interval = "1d")
df_SP500 = yf.download("^GSPC", start, end, interval = "1d")

#Merging
dfnew_list = [df_aapl, df_amzn, df_tsla, df_fb, df_SP500]
dfnew_name = ["AAPL", "AMZN", "TSLA", "FB", "SP500"]

for df, com_name in zip(dfnew_list, dfnew_name):
    df["dfnew_name"] = com_name

df_new = pd.concat(dfnew_list, axis=0)
print(df_new.tail(10))


df_aapl["Open"].plot(label="Apple", figsize=(15,7))
df_amzn["Open"].plot(label="Amazon")
df_fb["Open"].plot(label="Facebook")
df_tsla["Open"].plot(label="Tesla")
plt.title("Stock Prices")
plt.xlabel("Date")
plt.ylabel("Stock Price of FB, AAPL, Amazon and TSLA")
plt.legend()
plt.show()
#df.groupby("Name")[["close", "open"]].agg([np.mean, np.median])

#Volume
df_aapl["Volume"].plot(label="Apple", figsize=(15,7))
df_fb["Volume"].plot(label="Facebook")
df_amzn["Volume"].plot(label="Amazon")
df_tsla["Volume"].plot(label="Tesla")
plt.ylabel("Volume Traded")
plt.legend()
plt.show()

df_aapl.iloc[70:90]["Open"].plot()
plt.title("Apple Stock Price Decrease")
plt.show()

#Moving Average
print(df_fb.head())

df_fb["Open"].plot(label = "No Moving Average", figsize=(15,7))
df_fb["MA50"] = df_fb["Open"].rolling(50).mean()
df_fb["MA50"].plot(label="MA50")
df_fb["MA200"] = df_fb["Open"].rolling(200).mean()
df_fb["MA200"].plot(label="MA200")
plt.legend()
plt.show()


from pandas.plotting import scatter_matrix
import pandas as pd

main_stocks = pd.concat([df_aapl["Open"], df_fb["Open"], df_tsla["Open"], df_amzn["Open"] ], axis = 1)
main_stocks.columns = ["AAPL Open", "FB Open","TSLA Open", "AMZN Open"]
scatter_matrix(main_stocks, figsize= (8,8), hist_kwds={"bins":50})
plt.show()

#Daily Percentage Change

df_fb["Returns"] = (df_fb["Close"]/df_fb["Close"].shift(1))-1
df_aapl["Returns"] = (df_aapl["Close"]/df_aapl["Close"].shift(1))-1
df_amzn["Returns"] = (df_amzn["Close"]/df_amzn["Close"].shift(1))-1
df_tsla["Returns"] = (df_tsla["Close"]/df_tsla["Close"].shift(1))-1


df_fb["Returns"].hist(bins=150, label="FB", alpha = .5, figsize= (15,5), color= "r")
df_amzn["Returns"].hist(bins=150, label="AMZN", alpha = .5, color= "b")
df_tsla["Returns"].hist(bins=150, label="TSLA", alpha = .5, color= "g")
plt.legend()
plt.show()

box_df = pd.concat([df_fb["Returns"], df_amzn["Returns"], df_tsla["Returns"] ], axis = 1)
box_df.columns = ["FB Returns", "AMZN Returns", "TSLA Returns"]
box_df.plot(kind = "box", figsize = (15,5))
plt.show()

print(fb.head())
print(aapl.tail())


#Replace Missing Data

from numpy import nan

df_fb["Returns"]=df_fb["Returns"].replace(nan,0)
df_aapl["Returns"]=df_aapl["Returns"].replace(nan,0)
df_amzn["Returns"]=df_amzn["Returns"].replace(nan,0)
print(df_fb.head(10))
print(df_aapl.head(10))
print(df_amzn.head(10))

#looping
dfnew_name = ["AAPL", "AMZN", "TSLA", "FB", "SP500"]
selected = ["SP500"]
new_list = [x for x in dfnew_name if x not in selected]
print(new_list)





