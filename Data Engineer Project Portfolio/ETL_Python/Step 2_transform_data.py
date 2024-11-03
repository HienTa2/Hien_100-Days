import pandas as pd

# Load the dataset
file_path = r'/Data Engineer Project Portfolio/dataset/churn_raw_data.csv'
encodings = ['utf-8', 'latin1', 'ISO-8859-1', 'cp1252']

for encoding in encodings:
    try:
        data = pd.read_csv(file_path, encoding=encoding)
        print(f"Successfully read the file with encoding: {encoding}")
        break
    except UnicodeDecodeError as e:
        print(f"Failed to read the file with encoding: {encoding}")
        print(e)

# Inspect columns
print(data.columns)

# Handle missing values with ffill (method will be deprecated, so use the alternative)
data.ffill(inplace=True)

# Aggregating monthly charges by tenure
data['Tenure'] = pd.to_numeric(data['Tenure'], errors='coerce')
data['MonthlyCharge'] = pd.to_numeric(data['MonthlyCharge'], errors='coerce')

# Group by tenure and sum the monthly charges
tenure_aggregated = data.groupby('Tenure')['MonthlyCharge'].sum().reset_index()

# Save the transformed data
transformed_file_path = r'/Data Engineer Project Portfolio/ETL_Python/transformed_data.csv'
tenure_aggregated.to_csv(transformed_file_path, index=False)

print(tenure_aggregated.head())
