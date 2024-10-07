from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QVBoxLayout

from Widgets.button import Buttons
from Widgets.comboBox import ComboBoxs
from Widgets.label import Labels
from Widgets.slider import Sliders
from Widgets.lineEdit import LineEdits


class MainLayouts(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.buttons: Buttons = Buttons()
        self.comboxs: ComboBoxs = ComboBoxs()
        self.labels: Labels = Labels()
        self.sliders: Sliders = Sliders()

        self.mainGridLayout: QGridLayout = QGridLayout()

        self.mainGridLayout.setSpacing(2)
        self.mainGridLayout_filling()


    def mainGridLayout_filling(self) -> None:
        self.mainGridLayout.addWidget(self.labels.label_empty, 0, 0)

        self.mainGridLayout.addWidget(self.labels.label_NameMusic, 1, 0, 1, 3)
        self.mainGridLayout.addWidget(self.labels.label_Time_stopwatch, 1, 4, 1, 1)

        self.mainGridLayout.addWidget(self.comboxs.comboBox_Name_Station, 2, 0, 1, 5)

        self.mainGridLayout.addWidget(self.buttons.btn_Add_Station, 3, 3, 1, 1)
        self.mainGridLayout.addWidget(self.buttons.btn_Delete_Station, 3, 4, 1, 1)

        self.mainGridLayout.addWidget(self.buttons.btn_Stop_or_Start_Playback, 4, 0, 1, 1)
        self.mainGridLayout.addWidget(self.sliders.volumeslider, 4, 1, 1, 1)
        self.mainGridLayout.addWidget(self.buttons.btn_About, 4, 4, 1, 1)


class AboutLayouts(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.labels: Labels = Labels()

        self.hBox: QHBoxLayout = QHBoxLayout()
        self.hBox.addWidget(self.labels.label_about)


class AddStationLayout(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.labels: Labels = Labels()
        self.lineEdits: LineEdits = LineEdits()
        self.buttons: Buttons = Buttons()

        self.vBox: QVBoxLayout = QVBoxLayout()
        self.hBox: QHBoxLayout = QHBoxLayout()

        self.hBox.addWidget(self.buttons.btn_Cancel)
        self.hBox.addWidget(self.buttons.btn_Save)

        self.vBox.addWidget(self.labels.label_Name_Station)
        self.vBox.addWidget(self.lineEdits.lineNameStation)
        self.vBox.addWidget(self.labels.label_Link_Station)
        self.vBox.addWidget(self.lineEdits.lineLinkStation)
        self.vBox.addLayout(self.hBox)
