# API Project — Web Infrastructure

This project focuses on interacting with RESTful APIs, manipulating JSON data structures, and exporting them into various formats (plain text, CSV, and JSON) using Python.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- First line of all files: `#!/usr/bin/python3`
- All files end with a newline
- Code adheres to PEP 8 style guide (`pycodestyle`)
- Imports organized in alphabetical order
- All modules have documentation (`__doc__`)
- Uses `.get()` to access dictionary values by key
- Code will not execute when imported (`if __name__ == '__main__':`)

## Tasks Description

| File | Description |
| --- | --- |
| `0-gather_data_from_an_API.py` | Python script that uses JSONPlaceholder REST API to display an employee's TODO list progress for a given employee ID. |
| `1-export_to_CSV.py` | Extends Task 0 to export employee tasks into a CSV file (`USER_ID.csv`). |
| `2-export_to_JSON.py` | Extends Task 0 to export employee tasks into a JSON file (`USER_ID.json`). |
| `3-dictionary_of_list_of_dictionaries.py` | Extends Task 0 to export all tasks for all employees into `todo_all_employees.json`. |

## Usage Examples

```bash
# Task 0
python3 0-gather_data_from_an_API.py 2

# Task 1
python3 1-export_to_CSV.py 2

# Task 2
python3 2-export_to_JSON.py 2

# Task 3
python3 3-dictionary_of_list_of_dictionaries.py
```
