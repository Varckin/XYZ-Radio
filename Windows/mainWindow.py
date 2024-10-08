from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.QtGui import QIcon, QScreen, QCloseEvent
from PyQt5.QtCore import QPoint, QRect

from Widgets.mainWindowWidget import MainLayouts

from Windows.aboutWindow import AboutWindow
from Windows.addStationWindow import AddStationWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.centralWidget: QWidget = QWidget()
        self.mainLayout: MainLayouts = MainLayouts()
        self.aboutWindow: AboutWindow = AboutWindow()
        self.addStationWindow: AddStationWindow = AddStationWindow()

        self.setupWindow()
        self.activity()

    def centerWindow(self) -> None:
        screen: QScreen = QApplication.primaryScreen()
        centerPoint: QPoint = screen.availableGeometry().center()
        framegeometry: QRect = self.frameGeometry()
        framegeometry.moveCenter(centerPoint)
        self.move(framegeometry.topLeft())

    def setupWindow(self) -> None:
        self.centralWidget.setLayout(self.mainLayout.mainGridLayout)
        self.setCentralWidget(self.centralWidget)

        self.centerWindow()
        self.setFixedSize(460, 140)
        self.setWindowTitle("XYZ RADIO")
        self.setWindowIcon(QIcon(""))

    def activity(self) -> None:
        self.mainLayout.btn_About.clicked.connect(self.aboutWindowSwitch)
        self.mainLayout.btn_Add_Station.clicked.connect(self.addStationWindowSwitch)

    def aboutWindowSwitch(self) -> None:
        self.switchWindows(self.aboutWindow, self.addStationWindow)

    def addStationWindowSwitch(self) -> None:
        self.switchWindows(self.addStationWindow, self.aboutWindow)
    
    def switchWindows(self, windowToShow: QWidget, windowToHide: QWidget) -> None:
        if windowToHide.isVisible() and not windowToShow.isVisible():
            windowToHide.hide()
        windowToShow.showWindow()

    def closeEvent(self, event: QCloseEvent) -> None:
        event.accept()
        QApplication.quit()
