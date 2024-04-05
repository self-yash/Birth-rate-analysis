import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the standardized dataset
standardized_data = pd.read_csv("standardized_birth without missing values.csv")

# Separate non-numeric attributes
non_numeric_attributes = ['gender']

# Extract numeric attributes for SVD
numeric_data = standardized_data.drop(columns=non_numeric_attributes)

# Perform Singular Value Decomposition (SVD)
U, s, Vt = np.linalg.svd(numeric_data, full_matrices=False)

# Print explained variance ratio
explained_variance_ratio = np.square(s) / np.sum(np.square(s))
print("Explained variance ratio:", explained_variance_ratio)

# Print the first few singular values
print("First few singular values:", s[:5])

# You can use U, s, and Vt matrices for further analysis or reconstruction
