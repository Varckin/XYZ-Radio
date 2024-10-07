from PyQt5.QtWidgets import QWidget, QLineEdit


class LineEdits(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.lineNameStation: QLineEdit = QLineEdit()
        self.lineLinkStation: QLineEdit = QLineEdit()
