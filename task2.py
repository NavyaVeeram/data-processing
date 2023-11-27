import pandas as pd
import matplotlib.pyplot as plt
import sys

# Read the CSV file into a DataFrame
file_path = 'sales_data_sample.csv'
data = pd.read_csv(file_path, encoding='latin1')

# Display the first few rows of the dataset
#print(data)
print("Column Names:")
print(data.columns)
print("\n")

# Get summary statistics of numerical columns
print("Summary Statistics:")
print(data.describe())
print("\n")

# Filter data based on specific conditions (Example: filtering by country)
country_filter = data[data['COUNTRY'] == 'USA']
print("Data for USA:")
print(country_filter.head())
print("\n")

# Group data by a particular column and calculate aggregated values
grouped_data = data.groupby('ORDERNUMBER').agg({'SALES': 'sum', 'QUANTITYORDERED': 'sum'})
print("Grouped Data by Order Number:")
print(grouped_data.head())
print("\n")

# Calculate total sales
total_sales = data['SALES'].sum()
print(f"Total Sales: ${total_sales}")

numerical_cols = data.select_dtypes(include=['float64', 'int64'])  # Selecting numerical columns

# Calculate mean
mean_values = numerical_cols.mean()

# Calculate median
median_values = numerical_cols.median()

# Calculate standard deviation
std_values = numerical_cols.std()

# Display the calculated statistics
statistics = pd.DataFrame({
    'Mean': mean_values,
    'Median': median_values,
    'Standard Deviation': std_values
})

print("Statistics for Numerical Columns:")
print(statistics)

sales_threshold = 5000
filtered_data = data[data['SALES'] > sales_threshold]

# Display the filtered data
print("Filtered Data where Sales > $5000:")
print(filtered_data.head())

# Generate a histogram for the 'SALES' column
plt.figure(figsize=(5, 4))
plt.hist(data['SALES'], bins=20, color='deeppink')
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Generate a bar chart for the count of sales by country
country_sales = data['COUNTRY'].value_counts().head(10)  # considering the top 10 countries for illustration
plt.figure(figsize=(10, 6))
country_sales.plot(kind='bar', color='salmon')
plt.title('Sales Count by Country (Top 10)')
plt.xlabel('Country')
plt.ylabel('Sales Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

processed_file_path = 'processed_sales_data.csv'
data.to_csv(processed_file_path, index=False)
