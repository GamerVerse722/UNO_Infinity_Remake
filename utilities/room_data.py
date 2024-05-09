from utilities.log_wrapper import LoggerWrapper
from utilities.uno import Uno
from typing import List, Dict, Union
from datetime import datetime
import uuid, json


class RoomData:
    def __init__(self, room_name: str, code: str, log_wrapper: LoggerWrapper, room_instance: 'Room') -> None:  # type: ignore
        self.logger = log_wrapper
        self.room_name: str = room_name
        self.code: str = code
        self.members_list: dict = {}
        self.message_history: list = []
        self.game_started: bool = False
        self.uno_game: Uno | None = None
        self.room_instance = room_instance
        self.logger.info(f"RoomData Class for room ( {room_name} ), code = {code}")

    def __dict__(self) -> Dict[str, Union[str, dict, list, bool, dict, None]]:  # type: ignore
        data: Dict[str, Union[str, dict, list, bool, dict, None]] = {
            "RoomName": self.room_name,
            "MembersList": self.members_list,
            "MessageHistory": self.message_history,
            "GameStarted": self.game_started,
            "UnoData": self.uno_game  # type: ignore
        }
        self.logger.info(f"Converted Class Room to json, code = {self.code}")
        return data

    def __write__(self, output_location: str) -> None:
        file = open(output_location, 'w')
        file.write(json.dumps(self.__dict__(), indent=4))
        file.close()
        self.logger.info(f"Written to file {output_location}")

    def add_user(self, username: str) -> str:
        user_uuid: str = uuid.uuid4().__str__()
        self.members_list[user_uuid] = username
        self.logger.info(f"User added ( {username}, user_uuid = {user_uuid} ), code = {self.code}")
        return user_uuid

    def remove_user(self, user_uuid: str) -> None:
        if self.user_exist(user_uuid, logging=False):
            self.logger.info(f"User removed ( {self.members_list[user_uuid]}, user_uuid = {user_uuid}), code = {self.code}")
            self.members_list.pop(user_uuid, None)
            if len(self.members_list) <= 0:
                self.room_instance.delete_room(self.code)
        else:
            self.logger.warning(f"User does not exist, user_uuid = {user_uuid}, code = {self.code}")

    def user_exist(self, user_uuid: str, logging: bool = True) -> bool:
        if user_uuid in self.members_list:
            if logging:
                self.logger.info(f"User exists ( {self.members_list[user_uuid]} ), user_uuid = {user_uuid}, code = {self.code}")
            return True
        else:
            if logging:
                self.logger.info(f"User does not exist, user_uuid = {user_uuid}, code = {self.code}")
            return False

    def get_user_uuid_list(self, logging: bool = True) -> List[str]:
        members_key: List[str] = list(self.members_list.keys())
        if logging:
            self.logger.info(f"User uuid's = {members_key}, code = {self.code}")
        return members_key

    def get_user_names_list(self, logging: bool = True) -> List[str]:
        member_value: List[str] = list(self.members_list.values())
        if logging:
            self.logger.info(f'Members name"s = {member_value}, code = {self.code}')
        return member_value

    def add_message(self, user_uuid: str, message: str) -> dict | None:
        if self.user_exist(user_uuid, logging=False) is False:
            self.logger.warning(f'Message failed to add, user uuid does not exist, user_uuid = {user_uuid}, code = {self.code}')
            return None

        message_metadata: dict = {
            'PlayerName': self.members_list.get(user_uuid),
            'Message': message,
            'Time': datetime.now().strftime("%I:%M:%S %p")
        }
        self.message_history.append(message_metadata)
        self.logger.info(f'User ( {self.members_list.get(user_uuid)} ) send message ( {message} ), code: {self.code}')
        return message_metadata

    def get_message_history(self) -> list:
        self.logger.info(f'Get message history, code = {self.code}')
        return self.message_history
