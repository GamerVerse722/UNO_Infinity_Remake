from utilities.log_wrapper import LoggerWrapper
from utilities.uno import Uno
import uuid


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

    def __dict__(self) -> dict:  # type: ignore
        return {
            "RoomName": self.room_name,
            "MembersList": self.members_list,
            "MessageHistory": self.message_history,
            "GameStarted": self.game_started,
            "UnoData": self.uno_game
        }

    def member_exist(self, user_uuid: str, logging: bool = True) -> bool:
        if user_uuid in self.members_list:
            if logging:
                self.logger.info(f"User exists ( {self.members_list[user_uuid]} ), user_uuid = {user_uuid}, code = {self.code}")
            return True
        else:
            if logging:
                self.logger.info(f"User does not exist, user_uuid = {user_uuid}, code = {self.code}")
            return False


    def add_user(self, username: str) -> str:
        user_uuid: str = uuid.uuid4().__str__()
        self.members_list[user_uuid] = username
        self.logger.info(f"User added ( {username}, user_uuid = {user_uuid} ), code = {self.code}")
        return user_uuid

    def remove_user(self, user_uuid: str) -> None:
        if self.member_exist(user_uuid, logging=False):
            self.logger.info(f"User removed ( {self.members_list[user_uuid]}, user_uuid = {user_uuid}), code = {self.code}")
            self.members_list.pop(user_uuid, None)
            if len(self.members_list) <= 0:
                self.room_instance.delete_room(self.code)
        else:
            self.logger.warning(f"User does not exist, user_uuid = {user_uuid}, code = {self.code}")
