from PyQt5.QtWidgets import QWidget, QPushButton


class Buttons(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.btm_Delete_Station: QPushButton = QPushButton("Delete station")
        self.btm_Add_Station: QPushButton = QPushButton("Add station")
        self.btm_Stop_or_Start_Playback: QPushButton = QPushButton("Start")
        self.btm_About: QPushButton = QPushButton("About")