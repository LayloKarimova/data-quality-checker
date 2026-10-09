import argparse
from pathlib import Path

import pandas as pd

from validators import validate_data
from report_generator import generate_report


def load_data(file_path):
    """Загружает данные из Excel или CSV файла."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = path.suffix.lower()

    if extension == ".xlsx":
        return pd.read_excel(path)

    elif extension == ".csv":
        return pd.read_csv(path)

    else:
        raise ValueError(
            "Unsupported file format. Please use .xlsx or .csv"
        )


def main():
    parser = argparse.ArgumentParser(
        description="Automated Data Quality Checker"
    )

    parser.add_argument(
        "--input",
        default="data/sample_employees.xlsx",
        help="Path to the input Excel or CSV file"
    )

    parser.add_argument(
        "--output",
        default="reports/data_quality_report.xlsx",
        help="Path for the generated Excel report"
    )

    args = parser.parse_args()

    print("=" * 55)
    print("          AUTOMATED DATA QUALITY CHECKER")
    print("=" * 55)

    try:
        # Загружаем данные
        df = load_data(args.input)

        print(f"\nInput file: {args.input}")
        print(f"Total rows: {len(df)}")
        print(f"Total columns: {len(df.columns)}")

        # Проверяем данные
        errors = validate_data(df)

        print("\n" + "=" * 55)
        print("DATA QUALITY RESULTS")
        print("=" * 55)

        if errors:
            for error in errors:
                print(
                    f"Row {error['Row']} | "
                    f"Column: {error['Column']} | "
                    f"Error: {error['Error']}"
                )
        else:
            print("No data quality errors found.")

        print(f"\nTotal errors found: {len(errors)}")

        # Создаём Excel-отчёт
        report_path = generate_report(
            df,
            errors,
            args.output
        )

        print("\n" + "=" * 55)
        print("REPORT GENERATED SUCCESSFULLY")
        print("=" * 55)

        print(f"Report saved to: {report_path}")

    except FileNotFoundError as error:
        print(f"\nERROR: {error}")

    except ValueError as error:
        print(f"\nERROR: {error}")

    except Exception as error:
        print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()