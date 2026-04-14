import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Revenue": [120, 135, 150, 160, 155],
    "Expenses": [80, 85, 95, 100, 98],
    "ProfitMargin": [33, 37, 35, 38, 37],
    "CustomerGrowth": [5, 6, 8, 9, 7],
    "MarketingIndex": [1.2, 1.3, 1.5, 1.6, 1.4]
}

df = pd.DataFrame(data)

# Line plot
plt.figure()
plt.plot(df["Month"], df["Revenue"], label="Revenue")
plt.plot(df["Month"], df["Expenses"], label="Expenses")
plt.legend()
plt.title("Revenue vs Expenses")
plt.show()

# Correlation heatmap
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Matrix")
plt.show()

# Pairplot
sns.pairplot(df)
plt.show()