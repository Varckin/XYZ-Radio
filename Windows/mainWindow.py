from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.QtGui import QIcon, QScreen
from PyQt5.QtCore import QPoint, QRect

from Widgets.layout import MainLayouts


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.centralWidget: QWidget = QWidget()
        self.mainLayout: MainLayouts = MainLayouts()

        self.centralWidget.setLayout(self.mainLayout.mainGridLayout)
        self.setCentralWidget(self.centralWidget)

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
