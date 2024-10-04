from PyQt5.QtCore import QThread
from time import sleep
from datetime import datetime


class GetData(QThread):
    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        prev = ""

        while True:
            sleep(1)
            m = self.link_station.get_meta(12)

            if m != prev:
                print("Now playing", m)
                prev = m
                self.label_NameMusic.setText(m)

                name_file = self.comboBox_Name_Station.currentText()
                text = self.label_NameMusic.text()
                with open(name_file+'.txt', 'at') as file:
                    file.write(datetime.now().strftime(f"%Y:%m:%d %H:%M:%S - {text}\n"))
