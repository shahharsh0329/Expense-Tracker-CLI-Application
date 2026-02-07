# Quick Start Guide

## Setup (60 seconds)

1. **Save the file**: Download `expense_tracker.py` to your computer

2. **Make it easy to use** (optional):
   
   **Option A - Create an alias (Mac/Linux):**
   ```bash
   # Add to your ~/.bashrc or ~/.zshrc
   alias expense-tracker='python3 /path/to/expense_tracker.py'
   
   # Then use like:
   expense-tracker add --description "Lunch" --amount 20
   ```
   
   **Option B - Add to PATH (Mac/Linux):**
   ```bash
   chmod +x expense_tracker.py
   mv expense_tracker.py /usr/local/bin/expense-tracker
   
   # Then use like:
   expense-tracker add --description "Lunch" --amount 20
   ```
   
   **Option C - Use directly:**
   ```bash
   python expense_tracker.py add --description "Lunch" --amount 20
   ```

## Common Commands Cheat Sheet

```bash
# Add expense
expense-tracker add --description "Groceries" --amount 150 --category "Food"

# List all
expense-tracker list

# Summary
expense-tracker summary
expense-tracker summary --month 2

# Update
expense-tracker update --id 1 --amount 160

# Delete
expense-tracker delete --id 1

# Set budget
expense-tracker set-budget --month 2 --amount 500

# Export
expense-tracker export
```

## Features Overview

✅ **All Required Features:**
- Add/Update/Delete expenses
- View all expenses
- Summary (total and monthly)

✅ **Bonus Features:**
- Categories with filtering
- Monthly budgets with warnings
- CSV export
- Full error handling

## Data Storage

All data saved in `expenses.json` in the same directory.
Backup this file to preserve your data!

## Need Help?

Run without arguments to see all commands:
```bash
expense-tracker
```

Or use `--help` on any command:
```bash
expense-tracker add --help
```
