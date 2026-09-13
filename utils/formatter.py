def format_employee_report(employee):
    return (
        f"Name: {employee['name']}\n"
        f"Department: {employee['department']}\n"
        f"Salary: {employee['salary']}\n"
        f"Active: {employee['active']}\n"
        f"Bonus: {employee['bonus']}\n"
        f"Total Income: {employee['total_income']}"
    )