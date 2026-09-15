from .bonus import calculate_bonus

def build_employee_report(employee):
    salary = employee["salary"]
    active = employee["active"]
    bonus = calculate_bonus(salary, active)
    total_income = salary + bonus

    employee_report = {
        "name": employee["name"],
        "department": employee["department"],
        "salary": salary,
        "active": active,
        "bonus": bonus,
        "total_income": total_income
    }

    return employee_report

def build_employee_report_if_found(employee):
    if employee is None:
        return None

    return build_employee_report(employee)

def build_employee_reports(employees):
    employee_reports = []

    for employee in employees:
        employee_report = build_employee_report(employee)
        employee_reports.append(employee_report)

    return employee_reports

def summarize_by_department(employee_reports):
    department_summary = {}

    for employee in employee_reports:
        department = employee["department"]
        salary = employee["salary"]
        bonus = employee["bonus"]
        income = employee["total_income"]

        if department not in department_summary:
            department_summary[department] = {
                "employee_count": 0,
                "total_salary": 0,
                "total_bonus": 0,
                "total_income":0
            }

        department_summary[department]["employee_count"] += 1
        department_summary[department]["total_salary"] += salary
        department_summary[department]["total_bonus"] += bonus
        department_summary[department]["total_income"] += income

    return department_summary

def get_highest_bonus_employee(employee_reports):
    highest_bonus_employee = None
    highest_bonus = None

    for employee in employee_reports:
        if highest_bonus is None or employee["bonus"] > highest_bonus:
            highest_bonus_employee = employee
            highest_bonus = employee["bonus"]

    return highest_bonus_employee

def calculate_average_by_department(department_summary, total_key):
    average_by_department = {}
    for department, summary in department_summary.items():
        average = summary[total_key] / summary["employee_count"]

        average_by_department[department] = average

    return average_by_department


def get_top_earner_by_department(employee_reports):
    top_earners = {}

    for employee in employee_reports:
        department = employee["department"]
        total_income = employee["total_income"]

        if department not in top_earners:
            top_earners[department] = employee
        else:
            if total_income > top_earners[department]["total_income"]:
                top_earners[department] = employee

    return top_earners

def find_minimum_total_income(employee_reports, minimum_income):
    total_income_reports = []

    for employee in employee_reports:
        total_income = employee["total_income"]

        if total_income >= minimum_income:
            total_income_reports.append(employee)

    for i in range(len(total_income_reports)):
        max_income = i

        for j in range(i + 1 , len(total_income_reports)):
            if total_income_reports[j]["total_income"] > total_income_reports[max_income]["total_income"]:
                max_income = j

        total_income_reports[i], total_income_reports[max_income] = total_income_reports[max_income], total_income_reports[i]

    return total_income_reports
