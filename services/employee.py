def get_active_employees(employees):
    active_employees = []

    for employee in employees:
        if employee["active"]:
            active_employees.append(employee)

    return active_employees

def find_employee_by_name(employees, name):
    for employee in employees:
        if employee["name"] == name:
            return employee
            
    return None

def get_highest_salary_employee(employees):
    highest_salary = None
    highest_employee = None

    for employee in employees:
        if highest_salary is None or employee["salary"] > highest_salary:
            highest_employee = employee
            highest_salary = employee["salary"]

    return highest_employee

def find_employees_by_department(employees, department):
    employees_by_department = []
    for employee in employees:
        if employee["department"] == department:
            employees_by_department.append(employee)

    return employees_by_department