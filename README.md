# Report Creator Based on Jira Tempo xls export

Reads excel with time table and exports entries for a given day forming a report for telegram bot

## Requirements
Python 3.12.6
pip 24.2

## Installation
- Clone repository

- Install virtual env (optional). That way dependencies would be installed localy
```shell
  pip install venv
  python -m venv venv
```

- Activate virtual env (optional)
Unix
```shell
bash .\venv\bin\activate
```

Windows
```powershell
.\venv\Scripts\activate
```

- Install dependencies
```shell
pip install -r requirements.txt
```

## Usage
- Activate virtual env (optional)
- To get todays report run
```shell
  python create_report.py -f path/to/report.xls
```

- To get specific date run
```shell
  python create_report.py -f path/to/report.xls -d iso-date
```