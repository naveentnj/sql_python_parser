Certainly! Here's a basic README template for your codes:

```markdown
# Phone Book Application

This is a simple phone book application implemented in Python. The application provides CRUD (Create, Read, Update, Delete) operations and supports SQL-like querying.

## Features

- **Create:** Add new records to the phone book.
- **Read:** Retrieve records from the phone book with optional filtering.
- **Update:** Not implemented in this version.
- **Delete:** Remove records from the phone book based on a specified condition.

## Usage

1. **Initialize Phone Book:**
   ```python
   phone_book = PhoneBook(data=[
       {"name": "John", "email": "john@example.com", "phone1": "123-456-7890"},
       {"name": "Jane", "email": "jane@example.com", "phone1": "555-1212"},
       {"name": "Doe", "email": "doe@example.com", "phone1": "987-654-3210", "phone2": "098-765-4321"},
   ])
   ```

2. **Perform SELECT Operation:**
   ```python
   # Select all records
   phone_book.select()
   
   # Select specific fields with a condition
   phone_book.select(fields="name, email", condition="name='Doe'")
   ```

3. **Insert a New Record:**
   ```python
   phone_book.insert("Test", "test@example.com", "123-456-7890", "")
   ```

4. **Delete Records:**
   ```python
   # Delete records based on a condition
   phone_book.delete(condition="name='John'")
   ```

5. **View Updated Phone Book:**
   ```python
   phone_book.select()
   ```

## Running the Examples

To run the provided examples, execute the script using a Python interpreter:

```bash
python your_script_name.py
```

## Requirements

- Python 3.x


Replace `your_script_name.py` with the actual name of your script. Additionally, you may want to include a license file (e.g., LICENSE) with the details of the license you choose for your project.