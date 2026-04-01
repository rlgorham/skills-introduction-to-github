# Airport Finder

Search for airports in CSV files by IATA code, name, city, or country.

## Files

| File | Description |
|------|-------------|
| `airports.csv` | Sample airport data (IATA code, name, city, country) |
| `find_airport.py` | Script to search for airports |

## Usage

```bash
python find_airport.py <query> [csv_file]
```

- **query** — IATA code (e.g. `LAX`) or partial name, city, or country
- **csv_file** — path to the CSV file (default: `airports.csv`)

## Examples

Search by IATA code:
```bash
python find_airport.py LAX
# [LAX] Los Angeles International Airport — Los Angeles, United States
```

Search by city:
```bash
python find_airport.py london
# [LHR] London Heathrow Airport — London, United Kingdom
```

Search by country:
```bash
python find_airport.py france
# [CDG] Charles de Gaulle Airport — Paris, France
```

## CSV Format

The airports CSV must have the following columns:

```
iata_code,name,city,country
LAX,Los Angeles International Airport,Los Angeles,United States
```

## Python API

```python
from find_airport import find_airport

results = find_airport("tokyo")
for airport in results:
    print(airport["iata_code"], airport["name"])
```
