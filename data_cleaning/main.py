import pandas as pd
import os


def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def handle_missing_values(df):
    """Fill missing values in numeric columns with the median value of the column."""
    numeric_cols = df.select_dtypes(include='number').columns
    if not numeric_cols.empty:
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    else:
        print("No numeric columns to fill.")
    return df


def remove_duplicates(df):
    """Remove duplicate rows from the DataFrame."""
    df.drop_duplicates(inplace=True)
    return df


def handle_outliers(df, column_name):
    """Remove outliers from a numeric column based on the IQR method."""
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]
    return df


def standardize_text_data(df, column_name):
    """Standardize text data to lower case and remove non-alphanumeric characters."""
    df[column_name] = df[column_name].str.lower().str.replace(r'[^\w\s]', '', regex=True)
    return df


def handle_categorical_data(df, column_name):
    """Convert categorical data into dummy/indicator variables."""
    return pd.get_dummies(df, columns=[column_name], drop_first=True)


def standardize_datetime(df, column_name):
    """Standardize datetime columns and create additional time-related columns."""
    df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
    df['Year'] = df[column_name].dt.year
    df['Month'] = df[column_name].dt.month
    df['Day'] = df[column_name].dt.day
    df['Weekday'] = df[column_name].dt.weekday
    df['Quarter'] = df[column_name].dt.quarter
    return df


def drop_unnecessary_columns(df, columns_to_drop):
    """Drop unnecessary columns from the DataFrame."""
    df.drop(columns_to_drop, axis=1, inplace=True, errors='ignore')
    return df


def main():
    file_path = input("Enter the path to your CSV file: ").strip()
    df = load_data(file_path)

    if df is not None:
        df = handle_missing_values(df)
        df = remove_duplicates(df)

        # Uncomment the following lines and fill in the column names as needed
        # df = handle_outliers(df, 'your_column_name')
        # df = standardize_text_data(df, 'your_text_column_name')
        # df = handle_categorical_data(df, 'your_categorical_column_name')
        # df = standardize_datetime(df, 'your_datetime_column_name')
        # df = drop_unnecessary_columns(df, ['list', 'your', 'columns', 'to', 'drop'])

        output_file = input("Enter a name for the cleaned data file (default 'cleaned_data.csv'): ").strip()
        output_file = output_file if output_file else 'cleaned_data.csv'

        if os.path.isfile(output_file):
            overwrite = input(f"File '{output_file}' already exists. Overwrite? (y/n): ").strip().lower()
            if overwrite != 'y':
                print("Data cleaning was cancelled.")
                return

        df.to_csv(output_file, index=False)
        print(f"Data cleaning completed. Cleaned data saved to '{output_file}'.")


if __name__ == "__main__":
    main()
