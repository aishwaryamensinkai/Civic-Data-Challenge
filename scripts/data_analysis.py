import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Load the dataset
data = pd.read_csv('./data/Part1.csv')

# Convert DATEEND to datetime format
data['DATEEND'] = pd.to_datetime(data['DATEEND'])

# Display the first few rows of the dataset
print(data.head())

# Count the number of each type of crime
crime_counts = data['CODE_DEFINED'].value_counts()

# Plot the distribution of crimes
crime_counts.plot(kind='bar')
plt.title('Distribution of Different Types of Crimes')
plt.xlabel('Crime Type')
plt.ylabel('Count')
plt.show()

# Group by date and count the number of crimes each day
time_series = data.groupby(data['DATEEND'].dt.date).size()

# Plot the time series
time_series.plot()
plt.title('Trend of Crimes Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Crimes')
plt.show()
