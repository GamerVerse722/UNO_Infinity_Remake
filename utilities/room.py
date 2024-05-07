from typing import Dict, List, Any, TypedDict #ignore
from utilities.uno import Uno #ignore
import json, random, uuid, copy #ignore


class Room:
    def __init__(self) -> None:
        self.rooms: Dict[str, RoomData] = {}

    def __dict__(self) -> dict:  # type: ignore
        rooms_data_dict: dict = {}
        for code, room_data in self.rooms.items():
            rooms_data_dict[code] = room_data.__dict__()
        return rooms_data_dict

    @staticmethod
    def generate_code(code_length: int = 8) -> str:
        code: str = ""
        for _ in range(code_length):
            code += str(random.randint(0, 9))
        return code

    def create_room(self, room_name: str, code_length: int = 8) -> str:
        while True:
            code: str = self.generate_code(code_length=code_length)
            if code not in self.rooms:
                break

        self.rooms[code] = RoomData(room_name=room_name, code=code)
        return code

    def delete_room(self, code: str) -> None:
        self.rooms.pop(code)

class RoomData:
    def __init__(self, room_name: str, code: str) -> None:
        self.room_name: str = room_name
        self.code: str = code
        self.members_list: dict = {}
        self.message_history: list = []
        self.game_started: bool = False
        self.uno_game: Uno | None = None

    def __dict__(self) -> dict:  # type: ignore
        return {
            "RoomName": self.room_name,
            "MembersList": self.members_list,
            "MessageHistory": self.message_history,
            "GameStarted": self.game_started
        }