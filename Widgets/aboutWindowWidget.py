from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from Localization.getStrLocal import getStr

class AboutLayouts(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.widget_filling()
        self.widgets_setup()
        self.mainHBoxLayout_filling()

    def mainHBoxLayout_filling(self) -> None:
        self.hBox.addWidget(self.label_about)

    def widget_filling(self) -> None:
        self.label_about: QLabel = QLabel(getStr("AboutText"))

        self.hBox: QHBoxLayout = QHBoxLayout()

    def widgets_setup(self) -> None:
        self.label_about.setOpenExternalLinks(True)
