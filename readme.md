
# Have I Been Pwned Email Checker

This script interacts with the [Have I Been Pwned](https://haveibeenpwned.com) API to check email addresses for data breaches. It generates combinations of email addresses based on common mail servers and checks for breaches using the API. The results are exported to a CSV file for further analysis.

## Features

- Generates email combinations for common mail servers.
- Checks each email for breaches using the Have I Been Pwned API.
- Outputs breach details (e.g., breach name, domain, date, description, and data classes) to a CSV file.

## Prerequisites

- Python 3.7 or higher
- A valid Have I Been Pwned API key

## Installation

1. Clone the repository or save the script:
   ```bash
   git clone https://github.com/yourusername/hibp-email-checker.git
   cd hibp-email-checker
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your API key:
   ```env
   HAVE_I_BEEN_PWNED_API_KEY=your_api_key_here
   ```

4. Create a CSV file containing the email addresses you want to check.

## Usage

1. Run the script:
   ```bash
   python email_checker.py
   ```

2. Provide the name of your input CSV file when prompted.

3. The script will generate a results CSV file in the format `results-YYYY-MM-DD HHMMSS.csv`.

## Example

### Input File (emails.csv)
```
example@gmail.com
test@yahoo.com
user@outlook.com
```

### Command
```bash
python email_checker.py
```

### Output File (results-2024-12-11 130000.csv)
| Email              | Name            | Domain        | BreachDate | Description                       | Data                          | Verified | Sensitive |
|--------------------|-----------------|---------------|------------|-----------------------------------|-------------------------------|----------|-----------|
| example@gmail.com  | ExampleBreach   | example.com   | 2023-01-01 | Data leaked in breach X          | Email addresses, Passwords    | True     | False     |

## Notes

1. Ensure your API key is valid and has sufficient quota.
2. To avoid rate-limiting issues, the script includes a delay between requests.
3. The script requires the input CSV file to have email addresses in the first column.

## Directory Structure

```
hibp-email-checker/
├── email_checker.py      # Main script
├── requirements.txt      # Dependencies
├── .env                  # Environment variables
├── emails.csv            # Input email list
└── results/              # Directory for CSV results (auto-generated)
```

## Dependencies

- `requests` for making API requests
- `dotenv` for managing environment variables
- `csv` for handling CSV input/output
- `bs4` (BeautifulSoup) for parsing HTML descriptions

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
