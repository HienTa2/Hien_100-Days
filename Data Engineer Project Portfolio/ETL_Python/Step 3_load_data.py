import pandas as pd

# Load the transformed data
file_path = r'/Data Engineer Project Portfolio/ETL_Python/transformed_data.csv'
transformed_data = pd.read_csv(file_path)

# Define the path for the final output CSV
output_file_path = r'/Data Engineer Project Portfolio/ETL_Python/final_output.csv'

# Save the data to the output CSV
transformed_data.to_csv(output_file_path, index=False)

print("Data saved successfully to", output_file_path)
