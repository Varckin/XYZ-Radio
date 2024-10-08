from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton


class AddStationLayout(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.widget_filling()
        self.mainVBoxLayout_filling()

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
        pass
