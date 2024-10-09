from typing import TYPE_CHECKING
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton
from DataBase.dataBase import DataBase

if TYPE_CHECKING:
    from Windows.addStationWindow import AddStationWindow
    from Windows.mainWindow import MainLayouts


class AddStationLayout(QWidget):
    def __init__(self, window: 'AddStationWindow', mainLayouts: 'MainLayouts') -> None:
        super().__init__()
        self.addStationWindow: AddStationWindow = window
        self.mainLayouts: MainLayouts = mainLayouts
        self.dataBase: DataBase = DataBase()
        self.widget_filling()
        self.mainVBoxLayout_filling()
        self.widgets_setup()

    def mainVBoxLayout_filling(self) -> None:
        self.hBox.addWidget(self.btn_Cancel)
        self.hBox.addWidget(self.btn_Save)

        self.vBox.addWidget(self.label_Name_Station)
        self.vBox.addWidget(self.lineNameStation)
        self.vBox.addWidget(self.label_Link_Station)
        self.vBox.addWidget(self.lineLinkStation)
        self.vBox.addLayout(self.hBox)

    def widget_filling(self) -> None:
        self.label_Name_Station: QLabel = QLabel("")
        self.label_Link_Station: QLabel = QLabel("")

        self.lineNameStation: QLineEdit = QLineEdit()
        self.lineLinkStation: QLineEdit = QLineEdit()

        self.btn_Save: QPushButton = QPushButton("Save")
        self.btn_Cancel: QPushButton = QPushButton("Cancel")

        self.vBox: QVBoxLayout = QVBoxLayout()
        self.hBox: QHBoxLayout = QHBoxLayout()
    
    def widgets_setup(self) -> None:
        self.btn_Save.setDisabled(True)
        self.lineNameStation.textChanged.connect(self.changerLineEdit)
        self.lineLinkStation.textChanged.connect(self.changerLineEdit)
        self.btn_Cancel.clicked.connect(self.pressBtnCancel)
        self.btn_Save.clicked.connect(self.pressBtnSave)

    def changerLineEdit(self) -> None:
        title: str = self.lineNameStation.text()
        link: str = self.lineLinkStation.text()

        if title == "" or link == "":
            self.btn_Save.setDisabled(True)
        else:
            self.btn_Save.setEnabled(True)

    def pressBtnCancel(self) -> None:
        self.lineNameStation.setText("")
        self.lineLinkStation.setText("")
        self.btn_Save.setDisabled(True)
        self.addStationWindow.close()

    def pressBtnSave(self) -> None:
        self.dataBase.createConnection()
        self.dataBase.addStation(name=self.lineNameStation.text(),
                                 link=self.lineLinkStation.text())
        self.dataBase.closeConnect()
        self.mainLayouts.fillingComboBox()
        self.pressBtnCancel()
