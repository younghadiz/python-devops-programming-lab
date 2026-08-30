"""Exercise 8: Calculate time remaining until the next birthday."""

from datetime import datetime


DATE_FORMAT = "%d.%m.%Y"


def calculate_next_birthday(birthday: datetime) -> datetime:
    now = datetime.now()

    try:
        next_birthday = birthday.replace(year=now.year)
    except ValueError:
        # Handles February 29 in non-leap years.
        next_birthday = birthday.replace(
            year=now.year,
            month=2,
            day=28,
        )

    if next_birthday <= now:
        try:
            next_birthday = birthday.replace(year=now.year + 1)
        except ValueError:
            next_birthday = birthday.replace(
                year=now.year + 1,
                month=2,
                day=28,
            )

    return next_birthday


def main() -> None:
    user_input = input(
        "Enter your birthday in DD.MM.YYYY format: "
    ).strip()

    try:
        birthday = datetime.strptime(user_input, DATE_FORMAT)
    except ValueError:
        print("Invalid date. Expected format: DD.MM.YYYY")
        return

    next_birthday = calculate_next_birthday(birthday)
    remaining = next_birthday - datetime.now()

    total_minutes = int(remaining.total_seconds() // 60)
    total_hours = total_minutes // 60
    total_days = total_hours // 24

    print(
        "\nTime remaining until your next birthday:\n"
        f"Days: {total_days}\n"
        f"Hours: {total_hours}\n"
        f"Minutes: {total_minutes}"
    )


if __name__ == "__main__":
    main()