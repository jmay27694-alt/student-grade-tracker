import sys
from PyQt6.QtWidgets import QApplication
from controller import GradeController


def main() -> None:
    """Run the student grade tracker app."""
    app = QApplication(sys.argv)
    window = GradeController()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()