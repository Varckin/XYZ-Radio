from typing import TYPE_CHECKING
from vlc import Instance, MediaPlayer, Media
from PyQt5.QtCore import QThread
from time import sleep
from datetime import datetime


if TYPE_CHECKING:
    from Widgets.mainWindowWidget import MainLayouts


class VlcPlayer():
    def __init__(self, url: str) -> None:
        self.vlcInstance: Instance = Instance()
        self.vlcPlayer: MediaPlayer = self.vlcInstance.media_player_new()
        self.urlStation: str = url

        self.linkStation: Media = self.vlcInstance.media_new(self.urlStation)


class GetData(QThread):
    def __init__(self, player: VlcPlayer, widget: MainLayouts) -> None:
        super().__init__()
        self.player: VlcPlayer = player
        self.widget: MainLayouts = widget

    def run(self) -> None:
        musicName: str = ""

        while True:
            sleep(1)
            metaData: str = self.player.linkStation.get_meta(12)
            
            if metaData != musicName:
                print("Now playing: ", metaData)
                musicName = metaData
                self.widget.label_NameMusic.setText(metaData)

                name_file = self.widget.comboBox_Name_Station.currentText()
                with open(name_file+'.txt', 'at') as file:
                    file.write(datetime.now().strftime(f"%Y:%m:%d %H:%M:%S - {musicName}\n"))
