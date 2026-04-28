from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from student import Student
from file_handler import save_student, load_student


class GradeController(QMainWindow):
    """Controls the student grade tracker GUI."""

    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("student_grade_tracker.ui", self)

        self.student = None

        self.addStudentButton.clicked.connect(self.add_student)
        self.calculateButton.clicked.connect(self.calculate_grade)
        self.saveButton.clicked.connect(self.save_student_data)
        self.loadButton.clicked.connect(self.load_student_data)
        self.clearButton.clicked.connect(self.clear_fields)

    def get_scores(self) -> list[float] | None:
        """Get and validate scores from the input boxes."""
        score_inputs = [
            self.score1Input,
            self.score2Input,
            self.score3Input,
            self.score4Input
        ]

        number_of_scores = int(self.numScoresCombo.currentText())
        scores = []

        for index in range(number_of_scores):
            score_text = score_inputs[index].text().strip()

            if score_text == "":
                self.messageLabel.setText("Score fields cannot be empty.")
                return None

            if "/" in score_text:
                self.messageLabel.setText("Do not use /100. Enter numbers only.")
                return None

            try:
                score = float(score_text)
            except ValueError:
                self.messageLabel.setText("Letter grades are not accepted. Enter 0-100.")
                return None

            if score < 0 or score > 100:
                self.messageLabel.setText("Scores must be between 0 and 100.")
                return None

            scores.append(score)

        return scores

    def add_student(self) -> None:
        """Add a student with valid scores."""
        name = self.studentNameInput.text().strip()

        if name == "":
            self.messageLabel.setText("Student name cannot be empty.")
            return

        scores = self.get_scores()

        if scores is None:
            return

        self.student = Student(name, scores)
        self.update_results()
        self.messageLabel.setText("Student added.")

    def calculate_grade(self) -> None:
        """Calculate the student's grade results."""
        name = self.studentNameInput.text().strip()

        if name == "":
            self.messageLabel.setText("Student name cannot be empty.")
            return

        scores = self.get_scores()

        if scores is None:
            return

        self.student = Student(name, scores)
        self.update_results()
        self.messageLabel.setText("Grade calculated.")

    def save_student_data(self) -> None:
        """Save the current student to a CSV file."""
        if self.student is None:
            self.messageLabel.setText("Add or calculate a student before saving.")
            return

        save_student(
            "student_data.csv",
            self.student.name,
            self.student.scores,
            self.student.get_average(),
            self.student.get_highest(),
            self.student.get_lowest(),
            self.student.get_final_grade()
        )

        self.messageLabel.setText("Student saved.")

    def load_student_data(self) -> None:
        """Load student data from the CSV file by name."""
        name = self.studentNameInput.text().strip()

        if name == "":
            self.messageLabel.setText("Enter a student name to load.")
            return

        data = load_student("student_data.csv", name)

        if data is None:
            self.messageLabel.setText("Student not found.")
            return

        scores = [float(score) for score in data["scores"].split("|")]
        self.student = Student(data["name"], scores)

        self.studentNameInput.setText(data["name"])
        self.numScoresCombo.setCurrentText(str(len(scores)))

        score_inputs = [
            self.score1Input,
            self.score2Input,
            self.score3Input,
            self.score4Input
        ]

        for score_input in score_inputs:
            score_input.clear()

        for index, score in enumerate(scores):
            score_inputs[index].setText(str(score))

        self.update_results()
        self.messageLabel.setText("Student loaded.")

    def update_results(self) -> None:
        """Update the results labels."""
        self.averageLabel.setText(f"Average: {self.student.get_average():.2f}")
        self.highestLabel.setText(f"Highest: {self.student.get_highest():.2f}")
        self.lowestLabel.setText(f"Lowest: {self.student.get_lowest():.2f}")
        self.finalGradeLabel.setText(f"Final Grade: {self.student.get_final_grade()}")

    def clear_fields(self) -> None:
        """Clear all input and output fields."""
        self.studentNameInput.clear()
        self.score1Input.clear()
        self.score2Input.clear()
        self.score3Input.clear()
        self.score4Input.clear()
        self.numScoresCombo.setCurrentIndex(0)

        self.averageLabel.setText("Average: None")
        self.highestLabel.setText("Highest: None")
        self.lowestLabel.setText("Lowest: None")
        self.finalGradeLabel.setText("Final Grade: None")
        self.messageLabel.setText("Status: Cleared.")

        self.student = None