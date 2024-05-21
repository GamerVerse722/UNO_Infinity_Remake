# from utilities.log_wrapper import LoggerWrapper
# from utilities.room import Room
from unogame.logging.log_wrapper import LoggerWrapper
from unogame.room.room import Room
import pprint # type: ignore

logger: LoggerWrapper = LoggerWrapper('logs/new.log', console=True)
room: Room = Room(log_wrapper=logger)

code = room.create_room('Among Us Lobby', max_user=-1)
# pprint.pprint(room.__dict__())
user_uuid = room.rooms[code].add_user("Gamer Verse")
room.rooms[code].add_user("Gamer Verse")
room.rooms[code].add_user("Gamer Verse")
room.rooms[code].add_user("Gamer Verse")
room.rooms[code].add_user("Gamer Verse")
room.rooms[code].add_user("Gamer Verse")
room.rooms[code].add_user("Gamer Verse")
room.rooms[code].add_user("Gamer Verse")
room.rooms[code].add_user("Gamer Verse")
room.rooms[code].add_user("Gamer Verse")
room.rooms[code].add_user("Gamer Verse")
room.rooms[code].user_exist(user_uuid)
room.room_exist(code, logging=True)
# pprint.pprint(room.rooms[code].get_user_uuid_list())
# pprint.pprint(room.rooms[code].get_user_names_list())
# pprint.pprint(room.rooms[code].add_message(user_uuid=user_uuid, message="Among is the best game ever"))
# pprint.pprint(room.rooms[code].get_message_history())
room.__write__('test/output.json')
room.rooms[code].remove_user(user_uuid)
room.delete_room(code)
