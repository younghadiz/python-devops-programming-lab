"""Student class."""

from person import Person


class Student(Person):
    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        lectures: list[str] | None = None,
    ) -> None:
        super().__init__(first_name, last_name, age)
        self.lectures = lectures if lectures is not None else []

    def list_lectures(self) -> None:
        if not self.lectures:
            print(f"{self.first_name} is not attending any lectures.")
            return

        print(
            f"{self.first_name}'s lectures: "
            f"{', '.join(self.lectures)}"
        )

    def attend_lecture(self, lecture: str) -> None:
        if lecture not in self.lectures:
            self.lectures.append(lecture)

    def leave_lecture(self, lecture: str) -> None:
        if lecture in self.lectures:
            self.lectures.remove(lecture)