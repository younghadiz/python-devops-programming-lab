"""Exercise 7: Classes, objects, and inheritance."""

from lecture import Lecture
from professor import Professor
from student import Student


def main() -> None:
    student = Student(
        "Tina",
        "Morgan",
        22,
        ["Python Fundamentals"],
    )

    professor = Professor(
        "Tim",
        "Smith",
        45,
        ["Cloud Computing"],
    )

    lecture = Lecture(
        "DevOps Engineering",
        max_students=40,
        duration=120,
    )

    student.print_name()
    student.list_lectures()

    student.attend_lecture("DevOps Engineering")
    student.list_lectures()

    student.leave_lecture("Python Fundamentals")
    student.list_lectures()

    professor.print_name()
    professor.list_subjects()

    professor.add_subject("DevOps Engineering")
    professor.list_subjects()

    professor.remove_subject("Cloud Computing")
    professor.list_subjects()

    lecture.add_professor(
        f"{professor.first_name} {professor.last_name}"
    )

    lecture.print_lecture_info()
    print(f"Professors: {', '.join(lecture.professors)}")


if __name__ == "__main__":
    main()