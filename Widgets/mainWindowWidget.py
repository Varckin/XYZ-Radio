from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QComboBox, QPushButton, QSlider
from PyQt5.QtCore import Qt, QTimer
import time

from Player.player import VlcPlayer, GetData


class MainLayouts(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.countTimer: int = 0
        self.timerInterval: int = 1000
        self.timerFlag: bool = False

        self.player: VlcPlayer = VlcPlayer(url="wer")
        self.getData: GetData = GetData(player=self.player, widget=self)
        self.mainGridLayout: QGridLayout = QGridLayout()
        self.mainGridLayout.setSpacing(2)
        self.widget_filling()
        self.widgets_setup()
        self.mainGridLayout_filling()

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

        self.btn_Delete_Station: QPushButton = QPushButton("Delete station")
        self.btn_Add_Station: QPushButton = QPushButton("Add station")
        self.btn_Stop_or_Start_Playback: QPushButton = QPushButton("Start")
        self.btn_About: QPushButton = QPushButton("About")

        self.volumeslider: QSlider = QSlider(Qt.Horizontal)
    
    def widgets_setup(self) -> None:
        self.label_Time_stopwatch.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.volumeslider.setFixedWidth(100)
        self.volumeslider.setMinimum(0)
        self.volumeslider.setMaximum(100)
        self.volumeslider.setValue(40)
        self.volumeslider.setToolTip(f"Volume 40")

        self.timer.timeout.connect(self.timer_second)
        self.timer.setInterval(self.timerInterval)

        self.volumeslider.valueChanged.connect(self.updateVolume)
        self.btn_Stop_or_Start_Playback.clicked.connect(self.start_or_stop_listen)

    def updateVolume(self) -> None:
        self.player.vlcPlayer.audio_set_volume(self.volumeslider.value())
        self.volumeslider.setToolTip(f"Volume {str(self.player.vlcPlayer.audio_get_volume())}")

    def start_or_stop_listen(self) -> None:
        if self.player.vlcPlayer.is_playing():
            self.player.vlcPlayer.pause()


    def timer_second(self) -> None:
        if self.timerFlag:
            self.countTimer += 1
        self.label_Time_stopwatch.setText(time.strftime('%H:%M:%S', time.gmtime(self.countTimer)))