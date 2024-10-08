from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon, QScreen
from PyQt5.QtCore import QPoint, QRect

from Widgets.aboutWindowWidget import AboutLayouts


class AboutWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.mainLayout: AboutLayouts = AboutLayouts()
        self.setLayout(self.mainLayout.hBox)
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

    def showWindow(self) -> None:
        if self.isVisible():
            self.activateWindow()
        else:
            self.show()
