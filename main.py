import sys

from PyQt5.QtWidgets import QApplication
from Windows.mainWindow import MainWindow


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
        
    except Exception as e:
        print(e)
