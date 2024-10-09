from typing import TYPE_CHECKING
from vlc import Instance, MediaPlayer, Media
from PyQt5.QtCore import QThread
from time import sleep
from datetime import datetime
from pathlib import Path

from URLValidator.URLValidator import isURLValid


if TYPE_CHECKING:
    from Widgets.mainWindowWidget import MainLayouts


class VlcPlayer():
    def __init__(self) -> None:
        self.vlcInstance: Instance = Instance()
        self.vlcPlayer: MediaPlayer = self.vlcInstance.media_player_new()
        self.currentMediaPlaying: Media = None
        self.linkStation: str = ""

    def currentPlayingStation(self, url: str) -> bool:
        try:
            if isURLValid(url=url):
                self.linkStation = url
                self.currentMediaPlaying= self.vlcInstance.media_new(url)
                self.vlcPlayer.set_media(self.currentMediaPlaying)
                self.vlcPlayer.play()
                return True
            else:
                return False
        except Exception as e:
            print(e)

    def isCurrentPlaying(self, url: str) -> bool:
        if self.currentMediaPlaying is not None and self.linkStation == url:
            return True
        else:
            self.currentPlayingStation(url=url)




class GetData(QThread):
    def __init__(self, player: 'VlcPlayer', widget: 'MainLayouts') -> None:
        super().__init__()
        self.player: VlcPlayer = player
        self.widget: MainLayouts = widget

    def run(self) -> None:
        musicName: str = ""

        while True:
            sleep(1)
            metaData: str = self.player.currentMediaPlaying.get_meta(12)
            
            if metaData != musicName:
                musicName = metaData
                self.widget.label_NameMusic.setText(metaData)

                name_file = self.widget.comboBox_Name_Station.currentText()
                with open(f"{str(Path.cwd())}/SavedTracks/{name_file}.txt", 'at') as file:
                    file.write(datetime.now().strftime(f"%Y:%m:%d %H:%M:%S - {musicName}\n"))
