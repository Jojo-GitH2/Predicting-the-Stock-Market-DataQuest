import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = pd.read_csv("/home/dq/scripts/sphist.csv")

data["Date"] = pd.to_datetime(data["Date"])

data.sort_values(by = ["Date"], ascending = True, inplace = True)
# data = data.set_index("Date")

data["close_next_5"] = data.shift(-1)["Close"].rolling(5).mean()

data["close_next_30"] = data.shift(-1)["Close"].rolling(30).mean()

data["close_next_365"] = data.shift(-1)["Close"].rolling(365).mean()

data["volume_next_5"] = data.shift(-1)["Volume"].rolling(5).mean()

data["volume_next_365"] = data.shift(-1)["Volume"].rolling(365).mean()

data["ratio_vol_5_365"] = data["volume_next_5"]/data["volume_next_365"]

data["std_vol_5"] = data["volume_next_5"] = data.shift(-1)["Volume"].rolling(5).std()

data["std_vol_365"] = data["volume_next_365"] = data.shift(-1)["Volume"].rolling(365).std()




data = data[data["Date"] > datetime(year=1951, month=1, day=2)].copy()

data.dropna(axis = 0, inplace = True)
train = data[data["Date"] < datetime(year=2013, month=1, day=1)]
test = data[data["Date"] > datetime(year=2012, month=12, day=30)]
features = ['close_next_5', 'close_next_30', 'close_next_365', 'volume_next_5', 'volume_next_365',"ratio_vol_5_365","std_vol_5",
           "std_vol_365"]
lin_reg = LinearRegression()
lin_reg.fit(train[features], train["Close"])
predictions = lin_reg.predict(test[features])
MAE = mean_absolute_error(test["Close"], predictions)
# data = data.reset_index(drop =True)
print(MAE)
# print(data[["Close" , "close_next"]])