from PyQt5.QtWidgets import QWidget, QLabel


class Labels(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.label_NameMusic: QLabel = QLabel("")
        self.label_Time_stopwatch: QLabel = QLabel("")