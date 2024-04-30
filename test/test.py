from utilities.function import Room
import pprint # type: ignore

room = Room()

code = room.create_room('Among Us Room')
uuid = room.add_player(code=code, username='Gamer Verse')
room.add_message(code=code, player_uuid=uuid, message='Welcome to the Gamer Lobby')
room.rooms[code]['UnoData'].add_players(room.get_room_members_list(code))

room.write_file('saved/test.json')

# pprint.pprint(room.__dict__())