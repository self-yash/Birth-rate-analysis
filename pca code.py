import pandas as pd
from sklearn.decomposition import PCA

# Load the standardized dataset
standardized_data = pd.read_csv("standardized_birth without missing values.csv")

# Separate non-numeric attributes
non_numeric_attributes = ['gender']

# Extract numeric attributes for PCA
numeric_data = standardized_data.drop(columns=non_numeric_attributes)

# Perform PCA
pca = PCA(n_components=2)  # You can specify the number of components
pca.fit(numeric_data)

# Transform the data into the new feature space
transformed_data = pca.transform(numeric_data)

# Add the transformed data to the DataFrame
standardized_data['PC1'] = transformed_data[:, 0]
standardized_data['PC2'] = transformed_data[:, 1]

# Print explained variance ratio
print("Explained variance ratio:", pca.explained_variance_ratio_)

# Print principal components
print("Principal components:")
print(pca.components_)

# You can do further analysis or visualization with the transformed data
