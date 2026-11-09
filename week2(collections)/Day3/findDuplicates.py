class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def __eq__(self, other):
        return (
            self.id == other.id and
            self.name == other.name and
            self.salary == other.salary
        )

    def __hash__(self):
        return hash((self.id, self.name, self.salary))

    def __repr__(self):
        return f"{self.id} {self.name} {self.salary}"


def find_duplicates(employees):

    seen = set()
    duplicates = set()

    for emp in employees:
        if emp in seen:
            duplicates.add(emp)
        else:
            seen.add(emp)

    return duplicates


def main():

    employees = [
        Employee(1, "Amit", 50000),
        Employee(2, "Rahul", 40000),
        Employee(1, "Amit", 50000),
        Employee(3, "Neha", 60000),
        Employee(2, "Rahul", 40000)
    ]

    duplicates = find_duplicates(employees)

    for emp in duplicates:
        print(emp)


if __name__ == "__main__":
    main()