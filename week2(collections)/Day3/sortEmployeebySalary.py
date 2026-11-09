class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

employees = [
    Employee(1, "Amit", 50000),
    Employee(2, "Rahul", 30000),
    Employee(3, "Priya", 70000),
    Employee(4, "Neha", 40000)
]

# Ascending
sorted_employees = sorted(employees, key=lambda e: e.salary)

for emp in sorted_employees:
    print(emp.name, emp.salary)


print("Descending")
#Descending
sorted_employees = sorted(
    employees,
    key=lambda e: e.salary,
    reverse=True
)
for emp in sorted_employees:
    print(emp.name, emp.salary)