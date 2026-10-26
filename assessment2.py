class Employee:
    def __init__(self, emp_id, name, role, salary):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.salary = salary

    def display_details(self):
        print(self.emp_id, self.name, self.role, self.salary)


def add_employee(emp):
    with open("employees.txt", "a") as file:
        file.write(f"{emp.emp_id},{emp.name},{emp.role},{emp.salary}\n")


def read_employees():
    try:
        with open("employees.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print("File not found")
        return []



e1 = Employee(1, "Malavika", "Python Developer", 50000)
e2 = Employee(2, "krishna", "Tester", 45000)
e3 = Employee(103, "manju", "Developer", 60000)
e4 = Employee(104, "karthika", "Tester", 48000)


open("employees.txt", "w").close()

add_employee(e1)
add_employee(e2)
add_employee(e3)
add_employee(e4)

employees = read_employees()

print("All Employees:")
for emp in employees:
    print(emp.strip())

print("\nSalary Greater Than 50000:")
for emp in employees:
    data = emp.strip().split(",")
    if int(data[3]) > 50000:
        print(emp.strip())

highest = 0
highest_emp = ""

for emp in employees:
    data = emp.strip().split(",")
    if int(data[3]) > highest:
        highest = int(data[3])
        highest_emp = emp.strip()

print("\nHighest Salary Employee:")
print(highest_emp)


roles = {}
for emp in employees:
    data = emp.strip().split(",")
    role = data[2]
    roles[role] = roles.get(role, 0) + 1

print("\nRole Count:")
for role, count in roles.items():
    print(role, ":", count)