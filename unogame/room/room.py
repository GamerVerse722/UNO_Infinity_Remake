from typing import Dict
from unogame.room.room_data import RoomData
from unogame.logging.log_wrapper import LoggerWrapper
import json, random


class Room:
    def __init__(self, log_wrapper: LoggerWrapper) -> None:
        self.rooms: Dict[str, RoomData] = {}
        self.logger = log_wrapper
        self.logger.info("Room Class Initialized")

    def __dict__(self) -> dict:  # type: ignore
        rooms_data_dict: dict = {}
        for code, room_data in self.rooms.items():
            rooms_data_dict[code] = room_data.__dict__()

        self.logger.info("Converted Class Room to json")
        return rooms_data_dict

    def __write__(self, output_location: str) -> None:
        file = open(output_location, 'w')
        file.write(json.dumps(self.__dict__(), indent=4))
        file.close()
        self.logger.info(f"Written to file {output_location}")

    def generate_code(self, code_length: int = 8) -> str:
        code: str = ""
        for _ in range(code_length):
            code += str(random.randint(0, 9))

        self.logger.info(f"Generated code: {code}")
        return code

    def create_room(self, room_name: str, code_length: int = 8, max_user: int = 8) -> str:
        if max_user < 0:
            self.logger.warning(f"Room can't be created max user less than 0 > {max_user}, resting to 8 max user")
            max_user = 8

        while True:
            code: str = self.generate_code(code_length=code_length)
            if code not in self.rooms:
                break

        self.logger.info(f"Room created ( {room_name} ), code = {code}")
        self.rooms[code] = RoomData(room_name=room_name, code=code, log_wrapper=self.logger, room_instance=self, max_user=max_user)
        return code

    def delete_room(self, code: str) -> None:
        if self.room_exist(code, logging=False):
            self.logger.info(f"Room deleted ( {self.rooms[code].room_name} ), code = {code}")
            self.rooms.pop(code)
        else:
            self.logger.warning(f"Room not found ( {code} ) ")

    def room_exist(self, code: str, logging: bool = False) -> bool:
        if code in self.rooms:
            if logging:
                self.logger.info(f"Room exists, code = {code}")
            return True
        else:
            if logging:
                self.logger.warning(f"Room does not exist, code = {code}")
            return False

    def delete_every_room(self) -> None:
        for code in list(self.rooms.keys()):
            self.delete_room(code)