class PhoneBook:
    """
    Class representing a phone book with CRUD operations and SQL-like parsing.
    """

    def __init__(self, data=None):
        """
        Initializes the phone book with data (list of dictionaries).
        """
        self.data = data or []

    def parse_query(self, query):
        """
        Parses a SQL-like query and returns a dictionary with parsed components.
        """
        query = query.strip().lower()
        tokens = query.split()
        if tokens[0] not in ("select", "insert", "delete"):
            raise ValueError(f"Invalid query type: {tokens[0]}")
        return {
            "type": tokens[0],
            "fields": tokens[2] if tokens[1] == "select" else None,
            "condition": " ".join(tokens[4:]) if "where" in query else None,
        }

    def select(self, fields="*", condition=None):
        """
        Performs a SELECT operation on the phone book data.
        """
        results = self.data
        if condition:
            results = [
                record
                for record in results
                if self._evaluate_condition(record, condition)
            ]
        return [
            {field: record.get(field, "") for field in fields}
            for record in results
        ]

    def insert(self, name, email, phone1, phone2):
        """
        Inserts a new record into the phone book data.
        """
        new_record = {"name": name, "email": email, "phone1": phone1, "phone2": phone2}
        self.data.append(new_record)
        return f"Record inserted: {new_record}"

    def delete(self, condition):
        """
        Deletes records from the phone book data based on a condition.
        """
        deleted_records = []
        for i, record in enumerate(self.data):
            if self._evaluate_condition(record, condition):
                deleted_records.append(record)
                del self.data[i]
        return f"Deleted records: {deleted_records}"

    def _evaluate_condition(self, record, condition):
        """
        Evaluates a condition string (e.g., "name='Doe'") on a phone book record.
        """
        field, operator, value = condition.split(" ")
        return eval(f"{record[field]}{operator}{value}")

# Example usage

phone_book = PhoneBook([
    {"name": "John", "email": "john@example.com", "phone1": "123-456-7890"},
    {"name": "Jane", "email": "jane@example.com", "phone1": "555-1212"},
    {"name": "Doe", "email": "doe@example.com", "phone1": "987-654-3210", "phone2": "098-765-4321"},
])

# Select all records
print("SELECT * FROM phone_records:")
print(phone_book.select())

# Select name and email for records where name is 'Doe'
print("SELECT name, email FROM phone_records WHERE name='Doe':")
print(phone_book.select("name, email", condition="name='Doe'"))

# Insert a new record
print(phone_book.insert("Test", "test@example.com", "123-456-7890", ""))

# Delete record where name is 'John'
print(phone_book.delete(condition="name='John'"))

# Select all records after insert and delete
print("SELECT * FROM phone_records:")
print(phone_book.select())
