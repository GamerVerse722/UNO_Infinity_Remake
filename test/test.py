from utilities.function import Room
import pprint # type: ignore

room = Room()

code = room.create_room('Among Us Room')
gamer_uuid = room.add_player(code=code, username='Gamer Verse')
admin_uuid = room.add_player(code=code, username='Admin')
room.add_message(code=code, player_uuid=gamer_uuid, message='Welcome to the Gamer Lobby')
room.rooms[code]['UnoData'].add_players(room.get_room_members_list(code))
room.rooms[code]['UnoData'].create_uno_deck()
room.rooms[code]['UnoData'].shuffle_cards()
room.rooms[code]['UnoData'].split_cards(split_amount=2)
room.rooms[code]['UnoData'].remove_uno_deck()

room.write_file('test/test.json')

# pprint.pprint(room.__dict_x_())