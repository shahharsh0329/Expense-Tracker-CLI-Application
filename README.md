# Expense-Tracker-CLI-Application
A simple expense tracker application to manage your finances.
# Expense Tracker CLI Application

A simple command-line expense tracker to help you manage your personal finances.

## Features

### Core Features
- ✅ Add expenses with description and amount
- ✅ Update existing expenses
- ✅ Delete expenses
- ✅ View all expenses
- ✅ View summary of all expenses
- ✅ View summary for specific months

### Additional Features
- ✅ Expense categories with filtering
- ✅ Monthly budgets with warnings
- ✅ Export to CSV
- ✅ Data persistence (JSON file)
- ✅ Error handling for invalid inputs

## Installation

1. Make sure you have Python 3.6+ installed
2. Download the `expense_tracker.py` file
3. Make it executable (optional):
   ```bash
   chmod +x expense_tracker.py
   ```

## Usage

### Basic Commands

#### Add an Expense
```bash
python expense_tracker.py add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

python expense_tracker.py add --description "Dinner" --amount 10 --category "Food"
# Expense added successfully (ID: 2)
```

#### List All Expenses
```bash
python expense_tracker.py list
# ID    Date         Description          Amount     Category
# -----------------------------------------------------------------
# 1     2024-08-06   Lunch                $20.00     General
# 2     2024-08-06   Dinner               $10.00     Food
```

#### List Expenses by Category
```bash
python expense_tracker.py list --category "Food"
```

#### Update an Expense
```bash
python expense_tracker.py update --id 1 --amount 25
# Expense updated successfully (ID: 1)

python expense_tracker.py update --id 1 --description "Business Lunch" --category "Work"
# Expense updated successfully (ID: 1)
```

#### Delete an Expense
```bash
python expense_tracker.py delete --id 2
# Expense deleted successfully
```

#### View Summary
```bash
# Total of all expenses
python expense_tracker.py summary
# Total expenses: $30.00

# Total for specific month (current year)
python expense_tracker.py summary --month 8
# Total expenses for August: $30.00
```

### Advanced Features

#### Set a Monthly Budget
```bash
python expense_tracker.py set-budget --month 2 --amount 500
# Budget for February set to $500.00
```

When you add an expense that exceeds the budget, you'll see a warning:
```bash
python expense_tracker.py add --description "Shopping" --amount 600
# Expense added successfully (ID: 3)
# Warning: You have exceeded your budget for this month! ($600.00 / $500.00)
```

#### Export to CSV
```bash
python expense_tracker.py export
# Expenses exported to expenses.csv

python expense_tracker.py export --file my_expenses.csv
# Expenses exported to my_expenses.csv
```

## Data Storage

All data is stored in `expenses.json` in the same directory as the script. The file contains:
- All expense records
- Monthly budgets

Example structure:
```json
{
  "expenses": [
    {
      "id": 1,
      "date": "2024-08-06",
      "description": "Lunch",
      "amount": 20.0,
      "category": "Food"
    }
  ],
  "budgets": {
    "8": 500.0
  }
}
```

## Error Handling

The application handles various error cases:
- **Negative amounts**: Won't allow expenses with amount ≤ 0
- **Non-existent IDs**: Shows error when trying to update/delete missing expense
- **Invalid months**: Budget months must be 1-12
- **Corrupted data file**: Starts fresh if data file is corrupted

## Command Reference

| Command | Required Arguments | Optional Arguments | Description |
|---------|-------------------|-------------------|-------------|
| `add` | `--description`, `--amount` | `--category` | Add a new expense |
| `update` | `--id` | `--description`, `--amount`, `--category` | Update an expense |
| `delete` | `--id` | - | Delete an expense |
| `list` | - | `--category` | List expenses |
| `summary` | - | `--month` | Show expense summary |
| `set-budget` | `--month`, `--amount` | - | Set monthly budget |
| `export` | - | `--file` | Export to CSV |

## Examples

### Complete Workflow
```bash
# Add some expenses
python expense_tracker.py add --description "Groceries" --amount 150 --category "Food"
python expense_tracker.py add --description "Gas" --amount 60 --category "Transport"
python expense_tracker.py add --description "Movie tickets" --amount 30 --category "Entertainment"

# Set a budget
python expense_tracker.py set-budget --month 2 --amount 500

# View all expenses
python expense_tracker.py list

# View food expenses only
python expense_tracker.py list --category "Food"

# Check summary
python expense_tracker.py summary
python expense_tracker.py summary --month 2

# Update an expense
python expense_tracker.py update --id 1 --amount 175

# Export to CSV
python expense_tracker.py export --file february_expenses.csv

# Delete an expense
python expense_tracker.py delete --id 3
```

## Tips

1. **Categories**: Use consistent category names for better filtering
2. **Budgets**: Set budgets at the start of each month to track spending
3. **Exports**: Regularly export to CSV for backup and analysis
4. **Data Backup**: Keep a backup of `expenses.json` file

**##Project Link**
https://roadmap.sh/projects/expense-tracker
## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## License

This project is open source and available for personal use.
