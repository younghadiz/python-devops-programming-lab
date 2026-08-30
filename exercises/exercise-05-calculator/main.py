"""Exercise 5: Interactive calculator with validation."""


def calculate(first: float, second: float, operation: str) -> float:
    if operation == "plus":
        return first + second
    if operation == "minus":
        return first - second
    if operation == "multiply":
        return first * second
    if operation == "divide":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first / second

    raise ValueError(f"Unsupported operation: {operation}")


def read_number(prompt: str) -> float | None:
    while True:
        value = input(prompt).strip()

        if value.lower() == "exit":
            return None

        try:
            return float(value)
        except ValueError:
            print("Invalid input. Only numbers are allowed.")


def main() -> None:
    calculation_count = 0
    supported_operations = {"plus", "minus", "multiply", "divide"}

    print("Python Calculator")
    print("Operations: plus, minus, multiply, divide")
    print("Type 'exit' at a number prompt to quit.")

    while True:
        first_number = read_number("\nFirst number: ")

        if first_number is None:
            break

        operation = input(
            "Operation (plus/minus/multiply/divide): "
        ).strip().lower()

        if operation == "exit":
            break

        if operation not in supported_operations:
            print("Unsupported operation.")
            continue

        second_number = read_number("Second number: ")

        if second_number is None:
            break

        try:
            result = calculate(first_number, second_number, operation)
        except ZeroDivisionError as error:
            print(error)
            continue

        calculation_count += 1
        print(f"Result: {result:g}")

    print(
        f"\nCalculator stopped. "
        f"You completed {calculation_count} calculation(s)."
    )


if __name__ == "__main__":
    main()