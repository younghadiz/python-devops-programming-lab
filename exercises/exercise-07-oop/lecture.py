"""Lecture class."""


class Lecture:
    def __init__(
        self,
        name: str,
        max_students: int,
        duration: int,
        professors: list[str] | None = None,
    ) -> None:
        self.name = name
        self.max_students = max_students
        self.duration = duration
        self.professors = professors if professors is not None else []

    def print_lecture_info(self) -> None:
        print(
            f"Lecture: {self.name} | "
            f"Duration: {self.duration} minutes"
        )

    def add_professor(self, professor_name: str) -> None:
        if professor_name not in self.professors:
            self.professors.append(professor_name)