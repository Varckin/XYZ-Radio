from PyQt5.QtWidgets import QWidget, QMessageBox, QGridLayout, QLabel, QComboBox, QPushButton, QSlider
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon
from pathlib import Path
import time
import atexit

from Player.player import VlcPlayer, GetData
from DataBase.dataBase import DataBase
from Localization.getStrLocal import getStr


class MainLayouts(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.countTimer: int = 0
        self.timerInterval: int = 1000
        self.timerFlag: bool = False

        self.player: VlcPlayer = VlcPlayer()
        self.getData: GetData = GetData(player=self.player, widget=self)
        self.dataBase: DataBase = DataBase()
        self.dataBase.createConnection()
        self.mainGridLayout: QGridLayout = QGridLayout()
        self.mainGridLayout.setSpacing(2)
        self.widget_filling()
        self.widgets_setup()
        self.mainGridLayout_filling()

        atexit.register(self.dataBase.closeConnect)

    def mainGridLayout_filling(self) -> None:
        self.mainGridLayout.addWidget(self.label_empty, 0, 0)

        self.mainGridLayout.addWidget(self.label_NameMusic, 1, 0, 1, 3)
        self.mainGridLayout.addWidget(self.label_Time_stopwatch, 1, 4, 1, 1)

        self.mainGridLayout.addWidget(self.comboBox_Name_Station, 2, 0, 1, 5)

        self.mainGridLayout.addWidget(self.btn_Add_Station, 3, 3, 1, 1)
        self.mainGridLayout.addWidget(self.btn_Delete_Station, 3, 4, 1, 1)

        self.mainGridLayout.addWidget(self.btn_Stop_or_Start_Playback, 4, 0, 1, 1)
        self.mainGridLayout.addWidget(self.volumeslider, 4, 1, 1, 1)
        self.mainGridLayout.addWidget(self.btn_About, 4, 4, 1, 1)

    def widget_filling(self) -> None:
        self.label_empty: QLabel = QLabel("")
        self.label_NameMusic: QLabel = QLabel("")
        self.label_Time_stopwatch: QLabel = QLabel("00:00")

        self.timer: QTimer = QTimer()

        self.comboBox_Name_Station: QComboBox = QComboBox()

        self.btn_Delete_Station: QPushButton = QPushButton(getStr("DeleteStation"))
        self.btn_Add_Station: QPushButton = QPushButton(getStr("AddStation"))
        self.btn_Stop_or_Start_Playback: QPushButton = QPushButton(getStr("StartPlayback"))
        self.btn_About: QPushButton = QPushButton(getStr("About"))

        self.volumeslider: QSlider = QSlider(Qt.Horizontal)
    
    def widgets_setup(self) -> None:
        self.label_Time_stopwatch.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.volumeslider.setFixedWidth(100)
        self.volumeslider.setMinimum(0)
        self.volumeslider.setMaximum(100)
        self.volumeslider.setValue(40)
        self.volumeslider.setToolTip(getStr("Volume").format(value=str(self.volumeslider.value())))

        self.fillingComboBox()

        self.timer.timeout.connect(self.timer_second)
        self.timer.setInterval(self.timerInterval)

        self.volumeslider.valueChanged.connect(self.updateVolume)
        self.btn_Stop_or_Start_Playback.clicked.connect(self.start_or_stop_listen)
        self.btn_Delete_Station.clicked.connect(self.deleteStation)

    def updateVolume(self) -> None:
        volume: int = self.volumeslider.value()
        self.player.vlcPlayer.audio_set_volume(volume)
        self.volumeslider.setToolTip(getStr("Volume").format(value=str(volume)))

    def start_or_stop_listen(self) -> None:
        if self.player.vlcPlayer.is_playing():
            self.stopPlayingStation()
        else:
            self.startPlayingStation()

    def stopPlayingStation(self) -> None:
        nameStation: str = self.comboBox_Name_Station.currentText()
        linkStation: str = self.dataBase.getLinkStation(nameStation)
        if self.player.isCurrentPlaying(url=linkStation):
            self.player.vlcPlayer.pause()
            self.getData.terminate()
            self.timerFlag = False
            self.timer.stop()
            self.countTimer: int = 0
            self.label_Time_stopwatch.setText(time.strftime('%H:%M:%S', time.gmtime(self.countTimer)))
            self.btn_Stop_or_Start_Playback.setText(getStr("StartPlayback"))
            self.label_NameMusic.setText("")

    def startPlayingStation(self) -> None:
        nameStation: str = self.comboBox_Name_Station.currentText()
        linkStation: str = self.dataBase.getLinkStation(nameStation)
        if self.player.currentPlayingStation(linkStation):
            self.getData.start()
            self.timerFlag = True
            self.timer.start()
            self.btn_Stop_or_Start_Playback.setText(getStr("StopPlayback"))
        else:
            self.label_NameMusic.setText(getStr("Error"))
            self.timer.singleShot(1000, self.clearLabel)
    
    def clearLabel(self):
        self.label_NameMusic.setText("")

    def fillingComboBox(self) -> None:
        self.comboBox_Name_Station.clear()
        for i in self.dataBase.getListNameStation():
            self.comboBox_Name_Station.addItem(i)
    
    def timer_second(self) -> None:
        if self.timerFlag:
            self.countTimer += 1
        self.label_Time_stopwatch.setText(time.strftime('%H:%M:%S', time.gmtime(self.countTimer)))

    def deleteStation(self) -> None:
        answer: QMessageBox.StandardButton = self.messageBox()
        if answer == QMessageBox.Yes:
            nameStation: str = self.comboBox_Name_Station.currentText()
            self.dataBase.delStation(name=nameStation)
            self.fillingComboBox()
    
    def messageBox(self) -> QMessageBox.StandardButton:
        logo: str = f"{str(Path.cwd())}/Resource/logo.png"
        answer: QMessageBox = QMessageBox(None)
        answer.setWindowTitle(getStr("Delete"))
        answer.setText(getStr("MessageDel"))
        answer.setWindowIcon(QIcon(logo))
        answer.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        answer.setDefaultButton(QMessageBox.No)

        return answer.exec_()
