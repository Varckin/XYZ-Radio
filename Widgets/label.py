from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt


class Labels(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.label_empty: QLabel = QLabel("")

        self.label_NameMusic: QLabel = QLabel("")

        self.label_Time_stopwatch: QLabel = QLabel("00:00")
        self.label_Time_stopwatch.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.label_about: QLabel = QLabel("")

        self.label_Name_Station: QLabel = QLabel("")
        self.label_Link_Station: QLabel = QLabel("")
