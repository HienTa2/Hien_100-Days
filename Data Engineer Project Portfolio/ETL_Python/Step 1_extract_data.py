import pandas as pd

file_path = r'/Data Engineer Project Portfolio/dataset/churn_raw_data.csv'

# Try different encodings to see which one works
encodings = ['utf-8', 'latin1', 'ISO-8859-1', 'cp1252']

for encoding in encodings:
    try:
        data = pd.read_csv(file_path, encoding=encoding)
        print(f"Successfully read the file with encoding: {encoding}")
        # Save the data to a new file if needed
        data.to_csv(r'C:\Users\Hien Ta\OneDrive\Python_100_Days\Data Engineer Project Portfolio\extracted_data.csv', index=False)
        break
    except UnicodeDecodeError as e:
        print(f"Failed to read the file with encoding: {encoding}")
        print(e)
