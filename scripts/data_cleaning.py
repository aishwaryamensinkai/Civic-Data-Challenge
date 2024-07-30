import pandas as pd  # type: ignore

# Load the dataset
data = pd.read_csv('./data/Part1.csv')

# Convert DATEEND to datetime format
data['DATEEND'] = pd.to_datetime(data['DATEEND'])

# Fill missing values in CODE_DEFINED, ARREST, and LARCENYCODE with 'Unknown'
data['CODE_DEFINED'].fillna('Unknown', inplace=True)
data['ARREST'].fillna('Unknown', inplace=True)
data['LARCENYCODE'].fillna('Unknown', inplace=True)

# Fill missing values in all other columns with empty strings
data.fillna('', inplace=True)

# Display cleaned data
print(data.head())

# Save cleaned data to a new CSV file
data.to_csv('./data/cleaned_data.csv', index=False)

print("Cleaned data has been saved to 'cleaned_data.csv'.")
