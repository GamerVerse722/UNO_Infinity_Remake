from typing import Dict, List, Any # Ignore
from datetime import datetime
import random
import uuid
import json


def generate_code(length: int = 8) -> str:
    code: str = ""
    for _ in range(length):
        code += str(random.randint(0, 9))
    return code


class Newsession:
    def __init__(self) -> None:
        """
        Initialize a newsession as an alternative to flask session
        """
        self.session: Dict[str, Dict[str, Any]] = {}

    def user_add(self, user_uuid: str) -> None:
        """
        Adds a user to section off their data given user_uuid
        :param user_uuid: str
        :return: None
        """
        self.session[user_uuid] = {
            'Room': '',
            'Connected': False,
        }

    def user_delete(self, user_uuid: str) -> None:
        """
        Deletes a user data given their user_uuid
        :param user_uuid: str
        :return: None
        """
        self.session.pop(user_uuid, None)

    def user_room_add(self, user_uuid: str, room_code: str) -> None:
        """
        Sets user room code given their user_uuid and room_code
        :param user_uuid: str
        :param room_code: str
        :return: None
        """
        self.session[user_uuid]['Room'] = room_code

    def get_user_exist(self, user_uuid: str) -> bool:
        """
        Returns if user exists
        :param user_uuid: str
        :return: bool
        """
        if self.session.get(user_uuid, None) is not None:
            return True
        else:
            return False

    def get_user_room(self, user_uuid: str) -> str | None:
        """
        Gets the current user's room code given their user_uuid
        :param user_uuid: str
        :return: str | None
        """
        return self.session.get(user_uuid, {}).get('Room', None)

    def get_user_connected(self, player_uuid: str) -> bool | None:
        """
        Gets bool if user is connected given user_uuid
        :param player_uuid: str
        :return: bool | None
        """
        return self.session.get(player_uuid, {}).get('Connected', None)



class Usertime:
    def __init__(self, timelimit: int = 10, time_interval: float | int = 1) -> None:
        """
        Initialize Usertime to store user online time given a optional timelimit
        :param timelimit: int
        """
        self.time: Dict[str, int | float] = {}
        self.timelimit: int = timelimit
        self.time_interval: float | int = time_interval

    def add_user(self, user_uuid: str) -> None:
        """
        Register a user given a user_uuid
        :param user_uuid: str
        :return: None
        """
        self.time[user_uuid] = 0

    def remove_user(self, user_uuid: str) -> None:
        """
        Removes user given user_uuid
        :param user_uuid: str
        :return: None
        """
        self.time.pop(user_uuid, None)

    def reset_user_timer(self, user_uuid: str) -> None:
        """
        Resets user timer given user_uuid
        :param user_uuid: str
        :return: None
        """
        self.time[user_uuid] = 0

    def user_timer_up(self) -> None:
        """
        Counts up all timers up by the specified amount of time specified from instance
        :return: None
        """
        for x in self.time:
            if self.user_over_timelimit(x) is False:
                self.time[x] += self.time_interval

    def user_over_timelimit(self, user_uuid: str) -> bool:
        """
        Checks if user is over time limit given user_uuid
        :param user_uuid: str
        :return: bool
        """
        if self.time[user_uuid] >= self.timelimit:
            return True
        else:
            return False


class Room:
    def __init__(self) -> None:
        self.rooms: Dict[str, dict] = {}

    def write_file(self, output_dir: str) -> None:
        d = open(output_dir, 'w')
        d.write(json.dumps(self.rooms, indent=4))
        d.close()

    def create_room(self, room_name: str, length: int = 8) -> str:
        while True:
            code: str = generate_code(length)
            if code not in self.rooms:
                break
        room_data: Dict[str, str | dict | list] = {
            'RoomName': room_name,
            'MembersList': {},
            'MessageHistory': []
        }
        self.rooms.update({code: room_data})
        return code

    def delete_room(self, room_code: str) -> None:
        self.rooms.pop(room_code)

    def add_player(self, code: str, username: str) -> str:
        user_uuid: str = uuid.uuid4().__str__()
        self.rooms[code]['MembersList'][user_uuid] = username
        return user_uuid

    def remove_player(self, code: str, player_uuid: str) -> bool | None:
        self.rooms[code]['MembersList'].pop(player_uuid)
        if len(self.rooms[code]['MembersList']) <= 0:
            self.delete_room(code)
            return True
        return False

    def get_player_name(self, code: str, player_uuid: str) -> str:
        return self.rooms[code]['MembersList'][player_uuid]

    def add_message(self, code: str, player_uuid: str, message) -> dict:
        message_metadata: Dict[str, str] = {
            'PlayerName': self.get_player_name(code, player_uuid),
            'Message': message,
            'Time': datetime.now().strftime("%I:%M:%S %p")
        }
        self.rooms[code]['MessageHistory'].append(message_metadata)
        return message_metadata

    def get_message_history(self, code: str) -> list:
        return self.rooms[code]['MessageHistory']

    def room_exist(self, code: str) -> bool:
        if self.rooms.get(code) is not None:
            return True
        else:
            return False

    def room_member_exist(self, code: str, player_uuid: str) -> bool:
        if self.rooms[code]['MembersList'].get(player_uuid, False):
            return True
        else:
            return False

    def get_room_name(self, code: str) -> str:
        return self.rooms[code]['RoomName']

    def get_room_members(self, code: str) -> dict:
        return self.rooms[code]['MembersList']

    class Uno:
        def __init__(self):
            pass