from vlc import Instance, MediaPlayer


class VlcPlayer():
    def __init__(self) -> None:
        self.vlcInstance: Instance = Instance()
        self.vlcPlayer: MediaPlayer = self.vlcInstance.media_player_new()
