"""Exercise 2: Working with dictionaries."""


def employee_dictionary_demo() -> None:
    employee = {
        "name": "Tim",
        "age": 30,
        "birthday": "1990-03-10",
        "job": "DevOps Engineer",
    }

    employee["job"] = "Software Engineer"
    employee.pop("age")

    print("Updated employee:")
    for key, value in employee.items():
        print(f"{key}: {value}")


def merge_dictionary_demo() -> None:
    dict_one = {"a": 100, "b": 400}
    dict_two = {"x": 300, "y": 200}

    merged_dictionary = {**dict_one, **dict_two}

    print("\nMerged dictionary:")
    print(merged_dictionary)

    values = merged_dictionary.values()

    print(f"Sum: {sum(values)}")
    print(f"Maximum value: {max(values)}")
    print(f"Minimum value: {min(values)}")


def main() -> None:
    employee_dictionary_demo()
    merge_dictionary_demo()


if __name__ == "__main__":
    main()