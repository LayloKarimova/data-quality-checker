import re
import pandas as pd


def check_missing_values(df):
    """Находит пропущенные обязательные значения."""

    required_columns = [
        "Employee_ID",
        "Full_Name",
        "Email",
        "Birth_Date",
        "Salary",
        "Department"
    ]

    errors = []

    for column in required_columns:
        missing_rows = df[df[column].isna()]

        for index in missing_rows.index:
            errors.append({
                "Row": index + 2,
                "Column": column,
                "Error": "Missing value"
            })

    return errors


def check_duplicate_ids(df):
    """Находит повторяющиеся Employee_ID."""

    errors = []

    duplicates = df[df.duplicated(
        subset=["Employee_ID"],
        keep=False
    )]

    for index in duplicates.index:
        errors.append({
            "Row": index + 2,
            "Column": "Employee_ID",
            "Error": "Duplicate Employee_ID"
        })

    return errors


def check_emails(df):
    """Проверяет корректность email-адресов."""

    errors = []

    email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    for index, email in df["Email"].items():

        if pd.isna(email):
            continue

        if not re.match(email_pattern, str(email)):
            errors.append({
                "Row": index + 2,
                "Column": "Email",
                "Error": "Invalid email"
            })

    return errors


def check_birth_dates(df):
    """Проверяет корректность даты рождения."""

    errors = []

    for index, birth_date in df["Birth_Date"].items():

        if pd.isna(birth_date):
            continue

        try:
            pd.to_datetime(
                str(birth_date),
                format="%d.%m.%Y",
                errors="raise"
            )

        except (ValueError, TypeError):
            errors.append({
                "Row": index + 2,
                "Column": "Birth_Date",
                "Error": "Invalid birth date"
            })

    return errors


def check_salary(df):
    """Проверяет корректность зарплаты."""

    errors = []

    for index, salary in df["Salary"].items():

        if pd.isna(salary):
            continue

        try:
            salary_value = float(salary)

            if salary_value <= 0:
                errors.append({
                    "Row": index + 2,
                    "Column": "Salary",
                    "Error": "Salary must be greater than 0"
                })

        except (ValueError, TypeError):
            errors.append({
                "Row": index + 2,
                "Column": "Salary",
                "Error": "Invalid salary"
            })

    return errors


def validate_data(df):
    """Запускает все проверки качества данных."""

    errors = []

    errors.extend(check_missing_values(df))
    errors.extend(check_duplicate_ids(df))
    errors.extend(check_emails(df))
    errors.extend(check_birth_dates(df))
    errors.extend(check_salary(df))

    return errors