import pandas as pd  # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
data = pd.read_csv('./data/cleaned_data.csv')

# Summary Statistics
print("Summary Statistics:")
print(data.describe(include='all'))

# Check the data types and missing values
print("\nData Types and Missing Values:")
print(data.info())

# Distribution of 'CODE_DEFINED'
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='CODE_DEFINED', order=data['CODE_DEFINED'].value_counts().index)
plt.title('Distribution of CODE_DEFINED')
plt.xticks(rotation=45)
plt.show()

# Distribution of 'ARREST'
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='ARREST', order=data['ARREST'].value_counts().index)
plt.title('Distribution of ARREST')
plt.xticks(rotation=45)
plt.show()

# Distribution of 'LARCENYCODE'
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='LARCENYCODE', order=data['LARCENYCODE'].value_counts().index)
plt.title('Distribution of LARCENYCODE')
plt.xticks(rotation=45)
plt.show()

# Analysis of crime occurrences over time
data['DATEEND'] = pd.to_datetime(data['DATEEND'])
data['Month'] = data['DATEEND'].dt.to_period('M')
data['Year'] = data['DATEEND'].dt.year

# Count of incidents per month
plt.figure(figsize=(12, 8))
data.groupby('Month').size().plot(kind='line', marker='o')
plt.title('Number of Incidents Per Month')
plt.xlabel('Month')
plt.ylabel('Number of Incidents')
plt.grid(True)
plt.show()

# Count of incidents per year
plt.figure(figsize=(12, 8))
data.groupby('Year').size().plot(kind='line', marker='o', color='teal')
plt.title('Number of Incidents Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Incidents')
plt.grid(True)
plt.show()

# Convert 'TIMESTART' to hours if it's in minutes
def convert_to_hours(time_str):
    try:
        return int(time_str) // 100
    except ValueError:
        return None

data['Hour'] = data['TIMESTART'].astype(str).apply(convert_to_hours)

# Heatmap of incidents by hour of the day
incident_heatmap = pd.crosstab(data['Hour'], data['CODE_DEFINED'])
plt.figure(figsize=(12, 8))
sns.heatmap(incident_heatmap, cmap='YlGnBu', annot=True, fmt='d')
plt.title('Heatmap of Incidents by Hour and CODE_DEFINED')
plt.xlabel('CODE_DEFINED')
plt.ylabel('Hour of the Day')
plt.show()

# Analysis of incidents by location
plt.figure(figsize=(12, 8))
data['ADDRESS'] = data['ADDRESS'].str.strip()  # Clean up any extra spaces
address_counts = data['ADDRESS'].value_counts().head(10)  # Top 10 locations
address_counts.plot(kind='bar', color='skyblue')
plt.title('Top 10 Locations with Most Incidents')
plt.xlabel('Address')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=45)
plt.show()

# Additional Plots

# 1. Bar Plot of Top Crime Types
plt.figure(figsize=(12, 8))
top_crimes = data['CODE_DEFINED'].value_counts().head(10)
top_crimes.plot(kind='bar', color='lightcoral')
plt.title('Top 10 Crime Types')
plt.xlabel('Crime Type')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=45)
plt.show()

# 2. Pie Chart of Arrests
plt.figure(figsize=(8, 8))
arrest_counts = data['ARREST'].value_counts()
plt.pie(arrest_counts, labels=arrest_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'salmon'])
plt.title('Proportion of Arrests vs Non-Arrests')
plt.show()

# 3. Histogram of Incident Counts by Hour
plt.figure(figsize=(12, 8))
sns.histplot(data['Hour'], bins=24, kde=False, color='orange')
plt.title('Histogram of Incident Counts by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Incidents')
plt.grid(True)
plt.show()

# 4. Box Plot of Incident Counts by Day of the Week
data['DayOfWeek'] = data['DATEEND'].dt.day_name()
plt.figure(figsize=(12, 8))
sns.boxplot(data=data, x='DayOfWeek', y='Hour', palette='Set2')
plt.title('Box Plot of Incident Counts by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Hour of the Day')
plt.xticks(rotation=45)
plt.show()

# 5. Pair Plot of Numerical Features (if any)
numerical_features = ['Hour']  # Add any other numerical features you have
if numerical_features:
    plt.figure(figsize=(12, 8))
    sns.pairplot(data[numerical_features])
    plt.title('Pair Plot of Numerical Features')
    plt.show()

# 6. Scatter Plot of Incidents vs. Hour
plt.figure(figsize=(12, 8))
sns.scatterplot(data=data, x='Hour', y=data.index, hue='CODE_DEFINED', palette='viridis', alpha=0.5)
plt.title('Scatter Plot of Incidents vs. Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Incident Count')
plt.show()

# 7. Box Plot of Incident Duration by Crime Type (if duration column exists)
if 'DURATION' in data.columns:
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=data, x='CODE_DEFINED', y='DURATION', palette='pastel')
    plt.title('Box Plot of Incident Duration by Crime Type')
    plt.xlabel('Crime Type')
    plt.ylabel('Duration')
    plt.xticks(rotation=45)
    plt.show()

# 8. Correlation Heatmap
numerical_features = data.select_dtypes(include=['float64', 'int64']).columns
plt.figure(figsize=(12, 10))
correlation_matrix = data[numerical_features].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
