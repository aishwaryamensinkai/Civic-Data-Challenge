import pandas as pd # type: ignore

# Load the dataset
data = pd.read_csv('./data/Part1.csv')

# Convert DATEEND to datetime format
data['DATEEND'] = pd.to_datetime(data['DATEEND'])

# Fill missing values if any
data.fillna('', inplace=True)

# Display cleaned data
print(data.head())
