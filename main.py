from data import employees
from services import (
    get_active_employees, 
    find_employee_by_name, 
    get_highest_salary_employee,
    build_employee_reports,
    summarize_by_department,
    get_highest_bonus_employee,
    calculate_average_by_department,
    find_employees_by_department,
    get_top_earner_by_department,
    build_employee_report_if_found
)
from utils import (
    format_employee_report, 
    format_employee_names,
    format_employee,
    format_employee_summary
)

print("=== ACTIVE EMPLOYEES ===")
active_employees = get_active_employees(employees)
for active_employee in active_employees:
    print(active_employee["name"])

print()
print("=== SEARCH EMPLOYEE ===")
employee1 = find_employee_by_name(employees, "Game")
print(format_employee(employee1))
print()
employee2 = find_employee_by_name(employees, "John")
print(format_employee(employee2))

print()
print("=== HIGHEST SALARY ===")
highest_employee = get_highest_salary_employee(employees)
print(format_employee_summary(highest_employee))
print()

print("=== EMPLOYEE REPORT ===")
employee_report = build_employee_report_if_found(employee1)
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
print(format_employee_report(highest_bonus_employee))
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

print()
print("=== SEARCH BY DEPARTMENT ===")
department1 = find_employees_by_department(employees, "IT")
print(format_employee_names(department1))

print()
department2 = find_employees_by_department(employees, "Marketing")
print(format_employee_names(department2))

print()
print("=== TOP EARNER BY DEPARTMENT ===")
top_earners = get_top_earner_by_department(employee_reports)
for department, earner in top_earners.items():
    print(f"{department}: {earner['name']} - {earner['total_income']:.2f}")