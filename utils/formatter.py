def format_employee_report(employee):
    if employee is None:
        return "Employee not found"
    
    return (
        f"Name: {employee['name']}\n"
        f"Department: {employee['department']}\n"
        f"Salary: {employee['salary']}\n"
        f"Active: {employee['active']}\n"
        f"Bonus: {employee['bonus']}\n"
        f"Total Income: {employee['total_income']}"
    )

def format_employee(employee):
    if employee is None:
        return "Employee not found"
    
    return (
        f"Name: {employee['name']}\n"
        f"Department: {employee['department']}\n"
        f"Salary: {employee['salary']}\n"
        f"Active: {employee['active']}"
    )

def format_employee_names(employees):
    if not employees:
        return "Employee not found"

    names = []

    for employee in employees:
        names.append(employee["name"])

    return "\n".join(names)

def format_employee_summary(employee):
    if employee is None:
        return "Employee not found"

    return (
        f"Name: {employee['name']}\n"
        f"Department: {employee['department']}\n"
        f"Salary: {employee['salary']}"
    )

def format_minimum_income(employees):
    if not employees:
        return "Employee not found"

    employee_incomes = []

    for employee in employees:
        employee_incomes.append(f"{employee['name']} - {employee['total_income']:.2f}")

    return "\n".join(employee_incomes)
