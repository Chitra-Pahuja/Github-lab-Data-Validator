def fun1(data):
    """
    Checks for missing values in a dataset (list of dicts).
    Args:
        data (list): A list of dictionaries representing rows.
    Returns:
        dict: A dictionary with column names as keys and count of missing values.
    Raises:
        TypeError: If input is not a list of dictionaries.
    """
    if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
        raise TypeError("Input must be a list of dictionaries.")

    if len(data) == 0:
        return {}

    all_keys = set()
    for row in data:
        all_keys.update(row.keys())

    missing_counts = {}
    for key in all_keys:
        count = sum(1 for row in data if key not in row or row[key] is None)
        missing_counts[key] = count

    return missing_counts


def fun2(data, column):
    """
    Detects duplicate values in a specific column.
    Args:
        data (list): A list of dictionaries representing rows.
        column (str): The column name to check for duplicates.
    Returns:
        list: A list of duplicate values found.
    Raises:
        TypeError: If input is not a list of dictionaries.
    """
    if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
        raise TypeError("Input must be a list of dictionaries.")

    values = [row.get(column) for row in data if row.get(column) is not None]
    seen = set()
    duplicates = set()
    for val in values:
        if val in seen:
            duplicates.add(val)
        seen.add(val)

    return sorted(list(duplicates))


def fun3(data, column, expected_type):
    """
    Validates that all values in a column match the expected data type.
    Args:
        data (list): A list of dictionaries representing rows.
        column (str): The column name to validate.
        expected_type (type): The expected Python type (e.g., int, float, str).
    Returns:
        bool: True if all values match the expected type, False otherwise.
    Raises:
        TypeError: If input is not a list of dictionaries.
    """
    if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
        raise TypeError("Input must be a list of dictionaries.")

    for row in data:
        value = row.get(column)
        if value is not None and not isinstance(value, expected_type):
            return False
    return True


def fun4(missing, duplicates, type_valid):
    """
    Generates a validation summary from individual check results.
    Args:
        missing (dict): Missing value counts per column.
        duplicates (list): List of duplicate values.
        type_valid (bool): Whether type validation passed.
    Returns:
        str: A formatted summary string of all validation checks.
    """
    total_missing = sum(missing.values())
    dup_count = len(duplicates)
    summary = f"Missing: {total_missing} | Duplicates: {dup_count} | TypeCheck: {'PASS' if type_valid else 'FAIL'}"
    return summary


# sample_data = [
#     {"id": 1, "name": "Alice", "score": 85},
#     {"id": 2, "name": "Bob", "score": 90},
#     {"id": 2, "name": None, "score": 78},
# ]
# f1_op = fun1(sample_data)
# f2_op = fun2(sample_data, "id")
# f3_op = fun3(sample_data, "score", int)
# f4_op = fun4(f1_op, f2_op, f3_op)