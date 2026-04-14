import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist, squareform

# 1. Create the dataset
data = {
    'ID': ['M001', 'M002', 'M003', 'M004', 'M005', 'M006'],
    'Feature1': [5.1, 4.9, 6.2, 5.9, 5.6, 5.7],
    'Feature2': [3.5, 3.0, 3.4, 3.0, 2.9, 2.8],
    'Feature3': [1.4, 1.4, 5.4, 5.1, 3.6, 4.1],
    'Feature4': [0.2, 0.2, 2.3, 1.8, 1.3, 1.3]
}
df = pd.DataFrame(data)

# 2. Extract only the numeric features
features = df[['Feature1', 'Feature2', 'Feature3', 'Feature4']]

# 3. Compute Euclidean distances between all pairs
# pdist computes condensed distance; squareform converts it to a matrix
dist_matrix = squareform(pdist(features, metric='euclidean'))

# 4. Display as a readable DataFrame
dist_df = pd.DataFrame(dist_matrix, index=df['ID'], columns=df['ID'])
print(dist_df.round(3))
