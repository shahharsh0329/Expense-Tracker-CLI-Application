#!/usr/bin/env python3
"""
Expense Tracker - A simple CLI application to manage personal finances
"""

import argparse
import json
import os
import csv
from datetime import datetime
from typing import List, Dict, Optional


class ExpenseTracker:
    def __init__(self, data_file: str = "expenses.json"):
        self.data_file = data_file
        self.expenses = []
        self.budgets = {}
        self.load_data()
    
    def load_data(self):
        """Load expenses and budgets from the JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.expenses = data.get('expenses', [])
                    self.budgets = data.get('budgets', {})
            except json.JSONDecodeError:
                print("Warning: Could not read data file. Starting fresh.")
                self.expenses = []
                self.budgets = {}
    
    def save_data(self):
        """Save expenses and budgets to the JSON file."""
        data = {
            'expenses': self.expenses,
            'budgets': self.budgets
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get_next_id(self) -> int:
        """Generate the next available expense ID."""
        if not self.expenses:
            return 1
        return max(expense['id'] for expense in self.expenses) + 1
    
    def add_expense(self, description: str, amount: float, category: Optional[str] = None):
        """Add a new expense."""
        if amount <= 0:
            print("Error: Amount must be positive.")
            return
        
        expense_id = self.get_next_id()
        date = datetime.now().strftime("%Y-%m-%d")
        
        expense = {
            'id': expense_id,
            'date': date,
            'description': description,
            'amount': amount,
            'category': category or 'General'
        }
        
        self.expenses.append(expense)
        self.save_data()
        print(f"Expense added successfully (ID: {expense_id})")
        
        # Check budget warning
        month = datetime.now().month
        month_key = str(month)
        if month_key in self.budgets:
            monthly_total = self.get_monthly_total(month)
            budget = self.budgets[month_key]
            if monthly_total > budget:
                print(f"Warning: You have exceeded your budget for this month! (${monthly_total:.2f} / ${budget:.2f})")
    
    def update_expense(self, expense_id: int, description: Optional[str] = None, 
                      amount: Optional[float] = None, category: Optional[str] = None):
        """Update an existing expense."""
        expense = self.find_expense(expense_id)
        if not expense:
            print(f"Error: Expense with ID {expense_id} not found.")
            return
        
        if description:
            expense['description'] = description
        if amount is not None:
            if amount <= 0:
                print("Error: Amount must be positive.")
                return
            expense['amount'] = amount
        if category:
            expense['category'] = category
        
        self.save_data()
        print(f"Expense updated successfully (ID: {expense_id})")
    
    def delete_expense(self, expense_id: int):
        """Delete an expense by ID."""
        expense = self.find_expense(expense_id)
        if not expense:
            print(f"Error: Expense with ID {expense_id} not found.")
            return
        
        self.expenses.remove(expense)
        self.save_data()
        print("Expense deleted successfully")
    
    def find_expense(self, expense_id: int) -> Optional[Dict]:
        """Find an expense by ID."""
        for expense in self.expenses:
            if expense['id'] == expense_id:
                return expense
        return None
    
    def list_expenses(self, category: Optional[str] = None):
        """List all expenses, optionally filtered by category."""
        expenses_to_show = self.expenses
        
        if category:
            expenses_to_show = [e for e in self.expenses if e['category'].lower() == category.lower()]
            if not expenses_to_show:
                print(f"No expenses found for category: {category}")
                return
        
        if not expenses_to_show:
            print("No expenses recorded.")
            return
        
        # Print header
        print(f"{'ID':<5} {'Date':<12} {'Description':<20} {'Amount':<10} {'Category':<15}")
        print("-" * 65)
        
        # Print expenses
        for expense in expenses_to_show:
            print(f"{expense['id']:<5} {expense['date']:<12} {expense['description']:<20} "
                  f"${expense['amount']:<9.2f} {expense['category']:<15}")
    
    def get_total(self) -> float:
        """Calculate total of all expenses."""
        return sum(expense['amount'] for expense in self.expenses)
    
    def get_monthly_total(self, month: int, year: Optional[int] = None) -> float:
        """Calculate total expenses for a specific month."""
        if year is None:
            year = datetime.now().year
        
        total = 0
        for expense in self.expenses:
            expense_date = datetime.strptime(expense['date'], "%Y-%m-%d")
            if expense_date.month == month and expense_date.year == year:
                total += expense['amount']
        return total
    
    def summary(self, month: Optional[int] = None):
        """Display summary of expenses."""
        if month:
            total = self.get_monthly_total(month)
            month_name = datetime(2024, month, 1).strftime("%B")
            print(f"Total expenses for {month_name}: ${total:.2f}")
            
            # Check budget
            month_key = str(month)
            if month_key in self.budgets:
                budget = self.budgets[month_key]
                remaining = budget - total
                if remaining >= 0:
                    print(f"Budget remaining: ${remaining:.2f}")
                else:
                    print(f"Over budget by: ${-remaining:.2f}")
        else:
            total = self.get_total()
            print(f"Total expenses: ${total:.2f}")
    
    def set_budget(self, month: int, amount: float):
        """Set a budget for a specific month."""
        if amount <= 0:
            print("Error: Budget must be positive.")
            return
        
        if month < 1 or month > 12:
            print("Error: Month must be between 1 and 12.")
            return
        
        self.budgets[str(month)] = amount
        self.save_data()
        month_name = datetime(2024, month, 1).strftime("%B")
        print(f"Budget for {month_name} set to ${amount:.2f}")
    
    def export_to_csv(self, filename: str = "expenses.csv"):
        """Export expenses to a CSV file."""
        if not self.expenses:
            print("No expenses to export.")
            return
        
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'date', 'description', 'amount', 'category'])
            writer.writeheader()
            writer.writerows(self.expenses)
        
        print(f"Expenses exported to {filename}")


def main():
    parser = argparse.ArgumentParser(description="Expense Tracker - Manage your finances")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add expense command
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('--description', required=True, help='Expense description')
    add_parser.add_argument('--amount', type=float, required=True, help='Expense amount')
    add_parser.add_argument('--category', help='Expense category')
    
    # Update expense command
    update_parser = subparsers.add_parser('update', help='Update an existing expense')
    update_parser.add_argument('--id', type=int, required=True, help='Expense ID')
    update_parser.add_argument('--description', help='New description')
    update_parser.add_argument('--amount', type=float, help='New amount')
    update_parser.add_argument('--category', help='New category')
    
    # Delete expense command
    delete_parser = subparsers.add_parser('delete', help='Delete an expense')
    delete_parser.add_argument('--id', type=int, required=True, help='Expense ID')
    
    # List expenses command
    list_parser = subparsers.add_parser('list', help='List all expenses')
    list_parser.add_argument('--category', help='Filter by category')
    
    # Summary command
    summary_parser = subparsers.add_parser('summary', help='Show expense summary')
    summary_parser.add_argument('--month', type=int, help='Month number (1-12)')
    
    # Set budget command
    budget_parser = subparsers.add_parser('set-budget', help='Set monthly budget')
    budget_parser.add_argument('--month', type=int, required=True, help='Month number (1-12)')
    budget_parser.add_argument('--amount', type=float, required=True, help='Budget amount')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export expenses to CSV')
    export_parser.add_argument('--file', default='expenses.csv', help='Output file name')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    tracker = ExpenseTracker()
    
    # Execute command
    if args.command == 'add':
        tracker.add_expense(args.description, args.amount, args.category)
    
    elif args.command == 'update':
        tracker.update_expense(args.id, args.description, args.amount, args.category)
    
    elif args.command == 'delete':
        tracker.delete_expense(args.id)
    
    elif args.command == 'list':
        tracker.list_expenses(args.category)
    
    elif args.command == 'summary':
        tracker.summary(args.month)
    
    elif args.command == 'set-budget':
        tracker.set_budget(args.month, args.amount)
    
    elif args.command == 'export':
        tracker.export_to_csv(args.file)


if __name__ == "__main__":
    main()
