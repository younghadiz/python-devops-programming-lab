"""Exercise 3: Working with a list of dictionaries."""

EMPLOYEES = [
    {
        "name": "Tina",
        "age": 30,
        "birthday": "1990-03-10",
        "job": "DevOps Engineer",
        "address": {
            "city": "New York",
            "country": "USA",
        },
    },
    {
        "name": "Tim",
        "age": 35,
        "birthday": "1985-02-21",
        "job": "Developer",
        "address": {
            "city": "Sydney",
            "country": "Australia",
        },
    },
]


def print_employee_details(employees: list[dict]) -> None:
    for employee in employees:
        print(
            f"Name: {employee['name']} | "
            f"Job: {employee['job']} | "
            f"City: {employee['address']['city']}"
        )


def main() -> None:
    print_employee_details(EMPLOYEES)

    second_employee_country = EMPLOYEES[1]["address"]["country"]
    print(f"\nSecond employee country: {second_employee_country}")


if __name__ == "__main__":
    main()