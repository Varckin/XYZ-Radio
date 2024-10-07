from PyQt5.QtWidgets import QWidget, QPushButton


class Buttons(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.btn_Delete_Station: QPushButton = QPushButton("Delete station")
        self.btn_Add_Station: QPushButton = QPushButton("Add station")
        self.btn_Stop_or_Start_Playback: QPushButton = QPushButton("Start")
        self.btn_About: QPushButton = QPushButton("About")
        self.btn_Save: QPushButton = QPushButton("Save")
        self.btn_Cancel: QPushButton = QPushButton("Cancel")
