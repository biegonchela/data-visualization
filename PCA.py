import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. Prepare the dataset
data = {
    'Feature1': [5.1, 4.9, 6.2, 5.9, 5.6, 5.7],
    'Feature2': [3.5, 3.0, 3.4, 3.0, 2.9, 2.8],
    'Feature3': [1.4, 1.4, 5.4, 5.1, 3.6, 4.1],
    'Feature4': [0.2, 0.2, 2.3, 1.8, 1.3, 1.3]
}
df = pd.DataFrame(data)

# 2. Standardize features (mean=0, variance=1)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# 3. Apply PCA
pca = PCA()
pca.fit(scaled_data)

# 4. View Variance Explained
explained_var = pca.explained_variance_ratio_
cumulative_var = np.cumsum(explained_var)

print(f"Variance explained by each PCA: {explained_var}")
print(f"Cumulative variance: {cumulative_var}")
