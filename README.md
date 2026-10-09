# Automated Data Quality Checker

A Python-based data validation tool for detecting common data quality issues in employee datasets and automatically generating structured Excel reports.

## Overview

Manual data validation can be time-consuming and error-prone, especially when working with large Excel or CSV files.

Automated Data Quality Checker processes employee datasets, identifies common data quality problems, calculates a data quality score, and generates a formatted Excel report containing validation results.

## Features

- Detects missing required values
- Identifies duplicate employee IDs
- Validates email addresses
- Validates birth date formats
- Detects invalid salary values
- Calculates a Data Quality Score
- Generates automated Excel reports
- Supports Excel (`.xlsx`) and CSV (`.csv`) input files
- Provides command-line arguments for input and output files
- Handles missing files and unsupported formats

## Technologies

- Python
- pandas
- openpyxl
- Regular Expressions (Regex)
- argparse

## Project Structure

```text
data-quality-checker/
│
├── data/
│   └── sample_employees.xlsx
│
├── examples/
│   └── sample_report.xlsx
│
├── reports/
│
├── screenshots/
│
├── src/
│   ├── main.py
│   ├── validators.py
│   └── report_generator.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd data-quality-checker
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the checker using the included sample dataset:

```bash
python src/main.py --input data/sample_employees.xlsx
```

You can also specify a custom output location:

```bash
python src/main.py --input data/sample_employees.xlsx --output reports/report.xlsx
```

Display command-line help:

```bash
python src/main.py --help
```

## Validation Rules

The current version validates employee datasets containing the following fields:

- `Employee_ID`
- `Full_Name`
- `Email`
- `Birth_Date`
- `Salary`
- `Department`

The application checks for missing required values, duplicate employee IDs, invalid email formats, invalid birth dates and non-positive salary values.

## Generated Report

The generated Excel workbook contains three worksheets:

### Summary

Provides an overview of the validation results, including:

- Total number of rows
- Number of valid rows
- Number of rows containing errors
- Total number of detected errors
- Data Quality Score

### Errors

Contains detailed information about every detected issue, including the Excel row number, affected column and error type.

### Clean Data

Contains the original dataset with an additional `Status` column indicating whether each record is `Valid` or contains an `Error`.

## Data Quality Score

The score is calculated as:

```text
Valid Rows / Total Rows × 100
```

This provides a simple high-level indicator of dataset quality.

## Example

Using the included sample dataset, the application detects issues such as:

```text
Missing value
Duplicate Employee_ID
Invalid email
Invalid birth date
Salary must be greater than 0
```

A sample generated report is available in:

```text
examples/sample_report.xlsx
```

## Privacy

The sample dataset contains synthetic data created solely for demonstration purposes. No real personal or confidential information is included.

## Future Improvements

- Configurable validation rules
- Support for custom dataset schemas
- Automatic anomaly detection
- Interactive dashboard
- Database integration
- Automated validation summary charts

## Report Preview

![Data Quality Report](screenshots/report_summary.png)