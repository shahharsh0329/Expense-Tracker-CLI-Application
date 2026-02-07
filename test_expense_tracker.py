#!/usr/bin/env python3
"""
Test script for the Expense Tracker application
This demonstrates all the features of the expense tracker
"""

import subprocess
import os
import time

def run_command(command):
    """Run a command and print the output."""
    print(f"\n$ {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout.strip())
    if result.stderr:
        print("Error:", result.stderr.strip())
    time.sleep(0.5)  # Small delay for readability

def main():
    # Clean up any existing data file
    if os.path.exists("expenses.json"):
        os.remove("expenses.json")
    
    print("=" * 70)
    print("EXPENSE TRACKER - DEMONSTRATION")
    print("=" * 70)
    
    print("\n### 1. Adding Expenses ###")
    run_command('python expense_tracker.py add --description "Lunch" --amount 20')
    run_command('python expense_tracker.py add --description "Dinner" --amount 10')
    run_command('python expense_tracker.py add --description "Coffee" --amount 5 --category "Food"')
    run_command('python expense_tracker.py add --description "Gas" --amount 50 --category "Transport"')
    
    print("\n### 2. Listing All Expenses ###")
    run_command('python expense_tracker.py list')
    
    print("\n### 3. Viewing Summary ###")
    run_command('python expense_tracker.py summary')
    
    print("\n### 4. Viewing Monthly Summary ###")
    current_month = time.strftime("%m")
    run_command(f'python expense_tracker.py summary --month {current_month}')
    
    print("\n### 5. Updating an Expense ###")
    run_command('python expense_tracker.py update --id 1 --amount 25 --description "Business Lunch"')
    run_command('python expense_tracker.py list')
    
    print("\n### 6. Filtering by Category ###")
    run_command('python expense_tracker.py list --category "Food"')
    
    print("\n### 7. Setting a Budget ###")
    run_command(f'python expense_tracker.py set-budget --month {current_month} --amount 100')
    
    print("\n### 8. Budget Warning (adding expense that exceeds budget) ###")
    run_command('python expense_tracker.py add --description "Shopping" --amount 50')
    
    print("\n### 9. Deleting an Expense ###")
    run_command('python expense_tracker.py delete --id 2')
    run_command('python expense_tracker.py list')
    
    print("\n### 10. Updated Summary ###")
    run_command('python expense_tracker.py summary')
    
    print("\n### 11. Exporting to CSV ###")
    run_command('python expense_tracker.py export --file test_expenses.csv')
    
    print("\n### 12. Error Handling Examples ###")
    print("\n--- Trying to add negative amount ---")
    run_command('python expense_tracker.py add --description "Invalid" --amount -10')
    
    print("\n--- Trying to delete non-existent expense ---")
    run_command('python expense_tracker.py delete --id 999')
    
    print("\n--- Trying to set invalid budget ---")
    run_command('python expense_tracker.py set-budget --month 13 --amount 100')
    
    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)
    print("\nFiles created:")
    print("  - expenses.json (data file)")
    print("  - test_expenses.csv (exported expenses)")
    print("\nYou can now use the expense tracker with your own data!")

if __name__ == "__main__":
    main()
