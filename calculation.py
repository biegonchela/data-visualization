import pandas as pd

# Create dataset
data = {
    "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
    "PassengerCount": [112,118,132,129,121,135],
    "AvgTemp": [23,24,26,27,28,30],
    "Rainfall": [12,8,10,9,15,11]
}

df = pd.DataFrame(data)

# 1. Variance
variance = df["PassengerCount"].var()

# 2. Standard Deviation

std_dev = df["PassengerCount"].std()

# 3. Correlation 
correlation = df[["PassengerCount", "AvgTemp", "Rainfall"]].corr()

# Output
print("Variance (PassengerCount):", variance)
print("Standard Deviation (PassengerCount):", std_dev)
print("\nCorrelation Matrix:\n", correlation)