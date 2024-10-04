from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout


class Layouts(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.mainGridLayout: QGridLayout = QGridLayout()
        self.hBox1: QHBoxLayout = QHBoxLayout()
        self.hBox2: QHBoxLayout = QHBoxLayout()
        self.hBox3: QHBoxLayout = QHBoxLayout()