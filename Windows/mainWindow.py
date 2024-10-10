from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon, QScreen, QCloseEvent, QCursor
from PyQt5.QtCore import QEvent, QPoint, QRect
from pathlib import Path
from Localization.getStrLocal import getStr

from Widgets.mainWindowWidget import MainLayouts
from Windows.aboutWindow import AboutWindow
from Windows.addStationWindow import AddStationWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.logo: str = f"{str(Path.cwd())}/Resource/logo.png"
        self.systemTray: SystemTray = SystemTray(window=self)
        self.centralWidget: QWidget = QWidget()
        self.mainLayout: MainLayouts = MainLayouts()
        self.aboutWindow: AboutWindow = AboutWindow()
        self.addStationWindow: AddStationWindow = AddStationWindow(mainLayouts=self.mainLayout)

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
        self.setWindowTitle(getStr("NameApp"))
        self.setWindowIcon(QIcon(self.logo))

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

    def changeEvent(self, event: QEvent) -> None:
        if event.type() == QEvent.WindowStateChange:
            if self.isMinimized():
                self.hide()
                self.systemTray.systemTray.show()
                self.systemTray.systemTray.showMessage(getStr("AppHide"),
                                            getStr("MessageHide"),
                                            QSystemTrayIcon.Information,
                                            2000)


class SystemTray:
    def __init__(self, window: MainWindow):
        self.window: MainWindow = window
        self.systemTray: QSystemTrayIcon = QSystemTrayIcon()
        self.systemTray.setIcon(QIcon(self.window.logo))
        self.systemTray.setToolTip(getStr("NameApp"))

        self.setupTray()

    def setupTray(self) -> None:
        self.trayMenu: QMenu = QMenu()

        restore: QAction = QAction(getStr("OpenApp"), self.window)
        restore.triggered.connect(self.activatedForegroundWindow)
        self.trayMenu.addAction(restore)

        quit: QAction = QAction(getStr("Quit"), self.window)
        quit.triggered.connect(QApplication.quit)
        self.trayMenu.addAction(quit)

        self.systemTray.setContextMenu(self.trayMenu)
        self.systemTray.activated.connect(self.trayActivated)

    def trayActivated(self, reason):
        if reason == QSystemTrayIcon.Context:
            self.trayMenu.exec_(QCursor.pos())
        if reason == QSystemTrayIcon.DoubleClick:
            self.activatedForegroundWindow()

    def activatedForegroundWindow(self) -> None:
        self.window.showNormal()
        self.window.activateWindow()
