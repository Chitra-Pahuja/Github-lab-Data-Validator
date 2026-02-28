# MLOps GitHub Actions - Data Validator

A data validation utility module with automated CI/CD pipelines using GitHub Actions. This project demonstrates key MLOps practices including writing modular Python code, implementing testing frameworks (pytest & unittest), and setting up continuous integration workflows.

## Project Overview

In real-world ML pipelines, ensuring data quality before model training is critical. This project implements a **Data Validator** module that performs common data quality checks such as detecting missing values, finding duplicates, validating data types, and generating validation summaries.

The project also includes automated testing and CI/CD using **GitHub Actions**, which runs all tests automatically on every push to the repository.

## Project Structure

```
mlops-github-actions-data-validator/
├── data/
│   └── __init__.py
├── src/
│   ├── __init__.py
│   └── data_validator.py        # Core data validation functions
├── test/
│   ├── __init__.py
│   ├── test_pytest.py           # Tests using pytest framework
│   └── test_unittest.py         # Tests using unittest framework
├── workflows/
│   ├── github_lab1_pytest_action.yml      # GitHub Actions workflow for pytest
│   └── github_lab2_unittest_action.yml    # GitHub Actions workflow for unittest
├── .github/
│   └── workflows/
│       ├── github_lab1_pytest_action.yml
│       └── github_lab2_unittest_action.yml
├── requirements.txt
└── README.md
```

## Data Validator Functions

| Function | Description |
|----------|-------------|
| `fun1(data)` | Checks for missing/null values across all columns in a dataset |
| `fun2(data, column)` | Detects duplicate values in a specific column |
| `fun3(data, column, expected_type)` | Validates that all values in a column match the expected data type |
| `fun4(missing, duplicates, type_valid)` | Generates a formatted validation summary report |

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Chitra-Pahuja/mlops-github-actions-data-validator.git
   cd mlops-github-actions-data-validator
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv

   # Windows:
   venv\Scripts\activate

   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Validator

```bash
python -m src.data_validator
```

### Running Tests

**Using pytest:**
```bash
python -m pytest test/test_pytest.py -v
```

**Using unittest:**
```bash
python -m unittest test.test_unittest
```

### Expected Output

```
test/test_pytest.py::test_fun1 PASSED
test/test_pytest.py::test_fun2 PASSED
test/test_pytest.py::test_fun3 PASSED
test/test_pytest.py::test_fun4 PASSED

========================= 4 passed =========================
```

## CI/CD with GitHub Actions

This project uses two GitHub Actions workflows that trigger automatically on every push to the `main` branch:

1. **Pytest Workflow** (`github_lab1_pytest_action.yml`)
   - Runs all pytest-based tests
   - Generates a JUnit XML test report
   - Uploads test results as an artifact
   - Triggers on push to `main` and `releases/**` branches

2. **Unittest Workflow** (`github_lab2_unittest_action.yml`)
   - Runs all unittest-based tests
   - Triggers on push to `main` branch

Both workflows include success/failure notifications in the build logs.

## Example Usage

```python
from src import data_validator

sample_data = [
    {"id": 1, "name": "Alice", "score": 85},
    {"id": 2, "name": "Bob", "score": 90},
    {"id": 2, "name": None, "score": 78},
]

# Check for missing values
missing = data_validator.fun1(sample_data)
# Output: {'id': 0, 'name': 1, 'score': 0}

# Detect duplicates in 'id' column
duplicates = data_validator.fun2(sample_data, "id")
# Output: [2]

# Validate that 'score' column contains integers
type_check = data_validator.fun3(sample_data, "score", int)
# Output: True

# Generate validation summary
summary = data_validator.fun4(missing, duplicates, type_check)
# Output: "Missing: 1 | Duplicates: 1 | TypeCheck: PASS"
```

## Technologies Used

- **Python 3.8** - Core programming language
- **pytest** - Testing framework for writing concise test cases
- **unittest** - Python's built-in testing framework
- **GitHub Actions** - CI/CD pipeline for automated testing
- **Virtual Environment (venv)** - Dependency isolation
