import sqlite3
from pathlib import Path


class DataBase():
    def __init__(self) -> None:
        pass

    def createConnection(self) -> None:
        self.db: sqlite3.Connection = sqlite3.connect(f"{str(Path.cwd())}/Resource/Stations.xyz")
        self.cursor: sqlite3.Cursor = self.db.cursor()

        self.checkingTableInDataBase()
        self.checkingDatabaseIsEmpty()

    def createTable(self) -> None:
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS STATION (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    link TEXT
                    );
                """)
            self.db.commit()
        except sqlite3.Error:
            pass

    def firstStation(self) -> None:
        try:
            add_command: str = 'INSERT INTO STATION (name, link) VALUES(?, ?)'
            first_data_station: list = [
                ('Record', 'https://radiorecord.hostingradio.ru/rr_main96.aacp'),
                ('Chill House', 'http://radio-srv1.11one.ru/record192k.mp3'),
                ('Innocence', 'https://radiorecord.hostingradio.ru/ibiza96.aacp'),
                ('VIP House', 'https://radiorecord.hostingradio.ru/vip96.aacp'),
                ('Progressive', 'https://radiorecord.hostingradio.ru/progr96.aacp'),
                ('Future House', 'https://radiorecord.hostingradio.ru/fut96.aacp'),
                ('Radio None', 'http://uk2.internet-radio.com:8024/')
            ]

            self.cursor.executemany(add_command, first_data_station)
            self.db.commit()
        except sqlite3.Error:
            pass

    def getListNameStation(self) -> list:
        self.cursor.execute("SELECT name FROM STATION")
        return [name[0] for name in self.cursor.fetchall()]
    
    def getLinkStation(self, stationName: str) -> str:
        self.cursor.execute("SELECT link FROM STATION WHERE name = ?", (stationName,))
        return self.cursor.fetchone()[0]
    
    def addStation(self, name: str, link: str) -> None:
        try:
            self.cursor.execute("INSERT INTO STATION (name, link) VALUES (?, ?)", (name, link))
            self.db.commit()
        except sqlite3.Error:
            pass

    def delStation(self, name: str) -> None:
        try:
            del_command: str = "DELETE FROM STATION WHERE NAME = ?"
            self.cursor.execute(del_command, (name,))
            self.db.commit()
        except sqlite3.Error:
            pass

    def checkingDatabaseIsEmpty(self) -> None:
        request: list = self.cursor.execute("SELECT * FROM STATION").fetchall()
        if request == []:
            self.firstStation()

    def checkingTableInDataBase(self) -> None:
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name = ?", ("STATION",))
        table_exists: tuple = self.cursor.fetchone()
        if not table_exists:
            self.createTable()

    def closeConnect(self) -> None:
        self.db.close()
