from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QPoint, QRect


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        framegeometry: QRect = self.frameGeometry()
        centerPoint: QPoint = QDesktopWidget().availableGeometry().center()
        framegeometry.moveCenter(centerPoint)

        self.move(framegeometry.topLeft())
        self.resize(460, 150)
        self.setMinimumSize(455,135)
        self.setMaximumSize(600,150)
        self.setWindowTitle("XYZ RADIO")
        self.setWindowIcon(QIcon(""))