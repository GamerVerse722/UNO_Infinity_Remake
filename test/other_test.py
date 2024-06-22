from typing import Dict
from pprint import pprint

class Room:
    def __init__(self):
        self.room: Dict[str, RoomData] = {}

    def create_room(self, code):
        self.room[code] = RoomData()

class RoomData:
    def __init__(self):
        self.members_list = {}

    def __del__(self):
        del self

    def remove_user(self):
        self.__del__()



rooms = Room()
rooms.create_room('1234')
pprint(rooms.room)
rooms.room['1234'].remove_user()
pprint(rooms.room)
