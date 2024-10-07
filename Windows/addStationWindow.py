from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon, QScreen
from PyQt5.QtCore import QPoint, QRect

from Widgets.layout import AddStationLayout


class AddStationWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.mainLayout: AddStationLayout = AddStationLayout()

        self.setLayout(self.mainLayout.vBox)
        self.centerWindow()
        self.setFixedSize(460, 140)
        self.setWindowTitle("XYZ RADIO")
        self.setWindowIcon(QIcon(""))

    def centerWindow(self) -> None:
        screen: QScreen = QApplication.primaryScreen()
        centerPoint: QPoint = screen.availableGeometry().center()
        framegeometry: QRect = self.frameGeometry()
        framegeometry.moveCenter(centerPoint)
        self.move(framegeometry.topLeft())