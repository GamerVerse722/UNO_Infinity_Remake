from utilities.function import Room
import pprint # type: ignore

room = Room()

code = room.create_room('Among Us Room')
gamer_uuid = room.add_player(code=code, username='Gamer Verse')
admin_uuid = room.add_player(code=code, username='Admin')
room.add_message(code=code, player_uuid=gamer_uuid, message='Welcome to the Gamer Lobby')
room.start_uno_game(code=code, split_amount=7)
print(room.rooms[code]['UnoData'].uno_deck_length())
room.rooms[code]['UnoData'].remove_uno_deck()

room.write_file('test/test.json')

# pprint.pprint(room.__dict_x_())