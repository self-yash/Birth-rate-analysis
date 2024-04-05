import pandas as pd
from sklearn.preprocessing import StandardScaler
# Load the dataset
data = pd.read_csv("births.csv")
# Separate the non-numeric attributes
non_numeric_attributes = ['gender']
# Extract numeric attributes for standardization
numeric_data = data.drop(columns=non_numeric_attributes)
# Standardize the numeric attributes
scaler = StandardScaler()
numeric_data_scaled = scaler.fit_transform(numeric_data)
# Combine standardized numeric attributes with non-numeric attributes
scaled_data = pd.DataFrame(numeric_data_scaled, columns=numeric_data.columns)
scaled_data[non_numeric_attributes] = data[non_numeric_attributes]
# Save the standardized dataset
scaled_data.to_csv("standardized_birth.csv", index=False)