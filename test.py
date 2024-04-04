from utilities.function import Room
from typing import TypedDict
import pprint

room = Room()

code = room.create_room('Among Us Room')
uuid = room.add_player(code=code, username='Gamer Verse')
message_data = room.add_message(code=code, player_uuid=uuid, message='Welcome to the Gamer Lobby')
print(room.rooms[code]['UnoData'].uno_deck_exists())
room.write_file('saved/test.json')

# pprint.pprint(room.__dict__())