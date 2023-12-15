import csv
import json

def read_phonebook(filename):
    """
    Reads phone book records from a CSV or JSON file.

    Args:
        filename (str): The path to the CSV or JSON file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a phone book record
        with keys "name", "email", "phone1", and "phone2".
    """
    extension = filename.split(".")[-1]
    records = []

    if extension == "csv":
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                records.append(row)
    elif extension == "json":
        with open(filename, "r") as file:
            data = json.load(file)
            records = data
    else:
        raise ValueError(f"Unsupported file format: {extension}")

    # Check for required fields
    required_fields = ["name", "email", "phone1"]
    for record in records:
        if not all(field in record for field in required_fields):
            raise ValueError(f"Missing required fields in record: {record}")

    return records

# Example usage
phonebook_filename = "mock_data/phonebook.csv"
phonebook_records = read_phonebook(phonebook_filename)
for record in phonebook_records:
    print(f"Name: {record['name']}, Email: {record['email']}, "
          f"Phone 1: {record['phone1']}, Phone 2: {record.get('phone2', '')}")
