from data import employees
from services import (
    get_active_employees, 
    find_employee_by_name, 
    get_highest_salary_employee, 
    build_employee_report,
    build_employee_reports,
    summarize_by_department,
    get_highest_bonus_employee,
    calculate_average_by_department
)
from utils import format_employee_report

print("=== ACTIVE EMPLOYEES ===")
active_employees = get_active_employees(employees)
for active_employee in active_employees:
    print(active_employee["name"])

print()
print("=== SEARCH EMPLOYEE ===")
employee1 = find_employee_by_name(employees, "Game")
employee2 = find_employee_by_name(employees, "John")

if employee1 is None:
    print("Employee not found")
else:
    print(employee1)

if employee2 is None:
    print("Employee not found")
else:
    print(employee2)

print()
print("=== HIGHEST SALARY ===")
highest_employee = get_highest_salary_employee(employees)
if highest_employee is None:
    print("Employee not found")
else:
    print("Highest Salary Employee")
    print("Name:", highest_employee["name"])
    print("Department:", highest_employee["department"])
    print("Salary:", highest_employee["salary"])
    print()

print("=== EMPLOYEE REPORT ===")
if employee1 is None:
    print("Employee not found")
else:
    employee_report = build_employee_report(employee1)
    print(format_employee_report(employee_report))
    print()

print("=== ALL EMPLOYEE REPORTS ===")
employee_reports = build_employee_reports(employees)
for employee_report in employee_reports:
    print(format_employee_report(employee_report))
    print()

print("=== DEPARTMENT SUMMARY ===")
department_summary = summarize_by_department(employee_reports)
for department, summary in department_summary.items():
    print("Department:", department)
    print("Employee Count:", summary["employee_count"])
    print("Total Salary:", summary["total_salary"])
    print("Total Bonus:", summary["total_bonus"])
    print("Total Income:", summary["total_income"])
    print()

print("=== HIGHEST BONUS ===")
highest_bonus_employee = get_highest_bonus_employee(employee_reports)
if highest_bonus_employee is None:
    print("Employee not found")
    print()
else:
    print("Highest Bonus Employee")
    print("Name:", highest_bonus_employee["name"])
    print("Department:", highest_bonus_employee["department"])
    print("Salary:", highest_bonus_employee["salary"])
    print("Bonus:", highest_bonus_employee["bonus"])
    print("Total Income:", highest_bonus_employee["total_income"])
    print()

print("=== AVERAGE SALARY BY DEPARTMENT ===")
average_salary_by_department = calculate_average_by_department(department_summary, "total_salary")
for department, average in average_salary_by_department.items():
    print(f"{department}: {average:.2f}")

print()
print("=== AVERAGE BONUS BY DEPARTMENT ===")
average_bonus_by_department = calculate_average_by_department(department_summary, "total_bonus")
for department, average in average_bonus_by_department.items():
    print(f"{department}: {average:.2f}")

print()
print("=== AVERAGE INCOME BY DEPARTMENT ===")
average_income_by_department = calculate_average_by_department(department_summary, "total_income")
for department, average in average_income_by_department.items():
    print(f"{department}: {average:.2f}")