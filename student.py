class Student:
    """Represents a student and their scores."""

    def __init__(self, name: str, scores: list[float]) -> None:
        self.name = name
        self.scores = scores

    def get_average(self) -> float:
        """Return the average score."""
        return sum(self.scores) / len(self.scores)

    def get_highest(self) -> float:
        """Return the highest score."""
        return max(self.scores)

    def get_lowest(self) -> float:
        """Return the lowest score."""
        return min(self.scores)

    def get_final_grade(self) -> str:
        """Return the final letter grade."""
        average = self.get_average()

        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"