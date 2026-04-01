"""Find airports in CSV files by IATA code or name."""

import csv
import sys


def find_airport(query, filepath="airports.csv"):
    """Search for airports in a CSV file by IATA code or name.

    Args:
        query: IATA code (e.g. 'LAX') or partial airport/city name.
        filepath: Path to the CSV file containing airport data.

    Returns:
        List of matching airport records as dicts.
    """
    query = query.strip().lower()
    required_columns = {"iata_code", "name", "city", "country"}
    matches = []
    try:
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None or not required_columns.issubset(
                reader.fieldnames
            ):
                raise ValueError(
                    f"CSV file '{filepath}' is missing required columns: "
                    f"{required_columns - set(reader.fieldnames or [])}"
                )
            for row in reader:
                if (
                    query == row["iata_code"].lower()
                    or query in row["name"].lower()
                    or query in row["city"].lower()
                    or query in row["country"].lower()
                ):
                    matches.append(row)
    except FileNotFoundError:
        raise FileNotFoundError(f"Airport data file not found: '{filepath}'")
    return matches


def main():
    if len(sys.argv) < 2:
        print("Usage: python find_airport.py <query> [csv_file]")
        print("  query     IATA code or partial name/city/country")
        print("  csv_file  Path to airports CSV (default: airports.csv)")
        sys.exit(1)

    query = sys.argv[1]
    filepath = sys.argv[2] if len(sys.argv) > 2 else "airports.csv"

    try:
        results = find_airport(query, filepath)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}")
        sys.exit(1)
    if results:
        print(f"Found {len(results)} airport(s) matching '{query}':\n")
        for airport in results:
            print(
                f"  [{airport['iata_code']}] {airport['name']}"
                f" — {airport['city']}, {airport['country']}"
            )
    else:
        print(f"No airports found matching '{query}'.")


if __name__ == "__main__":
    main()
