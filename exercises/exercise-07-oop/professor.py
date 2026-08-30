"""Professor class."""

from person import Person


class Professor(Person):
    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        subjects: list[str] | None = None,
    ) -> None:
        super().__init__(first_name, last_name, age)
        self.subjects = subjects if subjects is not None else []

    def list_subjects(self) -> None:
        if not self.subjects:
            print(f"{self.first_name} is not teaching any subjects.")
            return

        print(
            f"{self.first_name}'s subjects: "
            f"{', '.join(self.subjects)}"
        )

    def add_subject(self, subject: str) -> None:
        if subject not in self.subjects:
            self.subjects.append(subject)

    def remove_subject(self, subject: str) -> None:
        if subject in self.subjects:
            self.subjects.remove(subject)