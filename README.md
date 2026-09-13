# Employee System

A Python employee management project for practicing data processing, business logic, modular project structure, reporting, and Git version control.

## Features

- Search for an employee by name
- Find employees by department
- Find the employee with the highest salary
- Calculate employee bonuses
- Generate detailed employee reports
- Summarize employee data by department
- Calculate average salary, bonus, and total income by department
- Find the employee with the highest bonus
- Find the top earner in each department

## Bonus Rules

- Active employee with salary >= 30,000: 10% bonus
- Active employee with salary < 30,000: 5% bonus
- Inactive employee: 0% bonus

## Project Structure

```text
employee-system/
├── main.py
├── data.py
├── config.py
├── services/
│   ├── __init__.py
│   ├── employee.py
│   ├── bonus.py
│   └── report.py
├── utils/
│   ├── __init__.py
│   └── formatter.py
├── .gitignore
└── README.md
```

## How to Run

Make sure Python is installed on your computer.

Run the project from the project directory:

```bash
python main.py
```

## Example Output

```text
=== SEARCH EMPLOYEE ===
Name: Game
Department: Sales
Salary: 35000
Active: True

=== HIGHEST SALARY ===
Name: Boss
Department: IT
Salary: 45000

=== AVERAGE SALARY BY DEPARTMENT ===
IT: 39000.00
HR: 27000.00
Sales: 31500.00

=== TOP EARNER BY DEPARTMENT ===
IT: Boss - 49500.00
HR: Ploy - 31000.00
Sales: Game - 38500.00
```

## What I Practiced

- Organizing Python code into modules and packages
- Separating data, business logic, and output formatting
- Working with lists and dictionaries
- Writing reusable functions
- Searching and filtering employee data
- Grouping and summarizing data by department
- Calculating totals and averages
- Finding maximum values from datasets
- Refactoring duplicated logic into reusable functions
- Using Git for version control
- Publishing and maintaining a project on GitHub

## Technologies

- Python
- Git
- GitHub

## Purpose

This project was created as part of my Python learning journey to practice building a small application with a structured codebase instead of writing all logic in a single file.