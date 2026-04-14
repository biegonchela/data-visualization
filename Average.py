import pandas as pd

data = {
    "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
    "PassengerCount": [112,118,132,129,121,135],
    "AvgTemp": [23,24,26,27,28,30],
    "Rainfall": [12,8,10,9,15,11]
}

df = pd.DataFrame(data)

# Rolling mean
df["RollingAvg"] = df["PassengerCount"].rolling(3).mean()

# Percentage change
df["PctChange"] = df["PassengerCount"].pct_change() * 100

print(df)

