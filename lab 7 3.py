print("om shrivastav")
print("24BEE083")
employees = [
    {"dept_no": 1, "emp_roll_no": 101, "salary": 50000},
    {"dept_no": 1, "emp_roll_no": 102, "salary": 55000},
    {"dept_no": 2, "emp_roll_no": 201, "salary": 60000},
    {"dept_no": 2, "emp_roll_no": 202, "salary": 58000},
    {"dept_no": 3, "emp_roll_no": 301, "salary": 52000},
    {"dept_no": 3, "emp_roll_no": 302, "salary": 53000}
]


def find_min_max_salary(employees):
    dept_salaries = {}

    for emp in employees:
        dept_no = emp["dept_no"]
        salary = emp["salary"]

        if dept_no not in dept_salaries:
            dept_salaries[dept_no] = {"min_salary": salary, "max_salary": salary}
        else:
            if salary < dept_salaries[dept_no]["min_salary"]:
                dept_salaries[dept_no]["min_salary"] = salary
            if salary > dept_salaries[dept_no]["max_salary"]:
                dept_salaries[dept_no]["max_salary"] = salary

    return dept_salaries


dept_min_max_salary = find_min_max_salary(employees)


for dept_no, salaries in dept_min_max_salary.items():
    print(f"Department {dept_no}: Min Salary = {salaries['min_salary']}, Max Salary = {salaries['max_salary']}")
