from typing import Dict, Any

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