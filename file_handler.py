# AI used to help brainstorm on how I wanted to arrange the files after inputted.
import csv
import os


def save_student(
    filename: str,
    name: str,
    scores: list[float],
    average: float,
    highest: float,
    lowest: float,
    final_grade: str
) -> None:
    """Save or update a student in a CSV file."""
    students = []

    if os.path.exists(filename):
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if "name" in row and row["name"]:
                    students.append(row)

    score_text = "|".join(str(score) for score in scores)
    updated = False

    for student in students:
        if student["name"].lower() == name.lower():
            student["scores"] = score_text
            student["average"] = f"{average:.2f}"
            student["highest"] = f"{highest:.2f}"
            student["lowest"] = f"{lowest:.2f}"
            student["final_grade"] = final_grade
            updated = True

    if not updated:
        students.append({
            "name": name,
            "scores": score_text,
            "average": f"{average:.2f}",
            "highest": f"{highest:.2f}",
            "lowest": f"{lowest:.2f}",
            "final_grade": final_grade
        })

    with open(filename, "w", newline="") as file:
        fieldnames = ["name", "scores", "average", "highest", "lowest", "final_grade"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)


def load_student(filename: str, name: str) -> dict[str, str] | None:
    """Load a student by name from a CSV file."""
    if not os.path.exists(filename):
        return None

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if "name" in row and row["name"].lower() == name.lower():
                return row

    return None
