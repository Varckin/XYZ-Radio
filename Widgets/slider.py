from PyQt5.QtWidgets import QWidget, QSlider
from PyQt5.QtCore import Qt


class Sliders(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.volumeslider: QSlider = QSlider(Qt.Horizontal)
        self.volumeslider.setMinimum(0)
        self.volumeslider.setMaximum(100)
        self.volumeslider.setValue(40)