import pandas as pd
import matplotlib.pyplot as plot

data=pd.read_excel(r"C:\Users\HP\Downloads\HINDALCO_1D.xlsx")

n=data.shape[0]
fast=10
slow=100

data["fast_ma"]=data["close"].rolling(fast).mean()
data["slow_ma"]=data["close"].rolling(slow).mean()

buy=[]
sell=[]

for i in range(n):
	if not (pd.isna(data["fast_ma"][i]) or pd.isna(data["slow_ma"][i])):
		if (data["fast_ma"][i]>data["slow_ma"][i]) and (data["fast_ma"][i-1]<data["slow_ma"][i-1]):
			buy.append((i,data["close"][i]))
		elif (data["fast_ma"][i]<data["slow_ma"][i]) and (data["fast_ma"][i-1]>data["slow_ma"][i-1]):
			sell.append((i,data["close"][i]))

plot.plot(data["close"],label="asset price",color="blue")
plot.plot(data["fast_ma"],label="fast moving average",color="yellow")
plot.plot(data["slow_ma"],label="slow moving average",color="orange")
plot.scatter([i[0] for i in buy],[i[1] for i in buy],marker='o',label="buy",color="green",s=100,alpha=1)
plot.scatter([i[0] for i in sell],[i[1] for i in sell],marker='x',label="sell",color="black",s=100,alpha=1,)
plot.legend(loc="best")
plot.show()
