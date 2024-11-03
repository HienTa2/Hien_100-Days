import random
import string
from faker import Faker
from google.cloud import storage
import csv
import re

# Initialize Faker
fake = Faker()

# Define the characters set for the password
password_characters = string.ascii_letters + string.digits + 'm'


# Function to clean up phone numbers by removing non-digit characters
def clean_phone_number(phone_number):
    return re.sub(r'\D', '', phone_number)  # Removes all non-digit characters


# Function to generate a single employee record
def generate_employee_record():
    return {
        "EmployeeID": str(fake.random_number(digits=6, fix_len=True)).strip(),
        "FirstName": fake.first_name().strip(),
        "LastName": fake.last_name().strip(),
        "Email": fake.email().strip(),
        "PhoneNumber": clean_phone_number(fake.phone_number()).strip(),  # Cleaned phone number without apostrophe
        "SSN": fake.ssn().strip(),
        "Address": fake.address().replace("\n", ", ").strip(),  # Replace newline with comma and space
        "DateOfBirth": fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%m/%d/%Y').strip(),
        "JobTitle": fake.job().strip(),
        "Department": fake.company().strip(),
        "HireDate": fake.date_this_decade().strftime('%m/%d/%Y').strip(),
        "Salary": str(fake.random_number(digits=5, fix_len=True)).strip(),
        "Password": ''.join(random.choice(password_characters) for _ in range(8)).strip()
    }


# Function to generate multiple employee records
def generate_employee_data(num_records):
    return [generate_employee_record() for _ in range(num_records)]


# Function to write the data to a CSV file
def write_to_csv(data, filename="employee_data.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys(), quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for record in data:
            # Convert the phone number to a string and ensure all values are properly stripped
            cleaned_record = {key: str(value).strip() if isinstance(value, (str, int)) else value for key, value in
                              record.items()}
            writer.writerow(cleaned_record)


# Generate data for 10 employees
employee_data = generate_employee_data(10)

# Write the data to a CSV file
write_to_csv(employee_data)


# Upload the CSV file to the GCS bucket
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f'File {source_file_name} uploaded to {destination_blob_name} in {bucket_name}.')


# Set your GCS bucket name and destination name
bucket_name = 'etl-bucket-employee'
source_file_name = 'employee_data.csv'
destination_blob_name = 'employee_data.csv'

# Upload the file
upload_to_gcs(bucket_name, source_file_name, destination_blob_name)

# Print confirmation of generation and upload
print(f"Generated {len(employee_data)} employee records and saved to {source_file_name}")
