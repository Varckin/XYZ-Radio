from PyQt5.QtWidgets import QWidget, QComboBox


class ComboBoxs(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.comboBox_Name_Station: QComboBox = QComboBox()