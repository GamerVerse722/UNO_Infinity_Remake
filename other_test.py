import random
from typing import Dict

# class Room:
#     def __init__(self, code: str = '123') -> None:
#         self.rooms: dict[str, dict[str, object]] = {}
#
#     def create_room(self, room_code: str) -> None:
#         self.rooms[room_code] = {'UnoData': self.Uno()}
#
#     class Uno:
#         def __init__(self) -> None:
#             self.uno_deck: list[str] = []
#
#         def shuffle_cards(self) -> None:
#             """
#             Shuffles the cards in the uno deck
#             :return: None
#             """
#             random.shuffle(self.uno_deck)
class Room:
    class Uno:
        def __init__(self) -> None:
            self.uno_deck: list[str] = []

        def shuffle_cards(self) -> None:
            random.shuffle(self.uno_deck)

    def __init__(self, code: str = '123') -> None:
        self.rooms: Dict[str, Dict[str, 'Room.Uno']] = {}  # Specify type of UnoData

    def create_room(self, room_code: str) -> None:
        self.rooms[room_code] = {'UnoData': self.Uno()}

room = Room()
room.create_room('12345')
print(type(room.rooms['12345']['UnoData']))
room.rooms['12345']['UnoData'].shuffle_cards()  # You should now see suggestions for `shuffle_cards()`
print(room.rooms['12345']['UnoData'].uno_deck)
print(room.rooms)
