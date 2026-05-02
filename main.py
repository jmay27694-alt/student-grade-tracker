import sys
from PyQt6.QtWidgets import QApplication
from controller import BankController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BankController()
    window.show()
    sys.exit(app.exec())
