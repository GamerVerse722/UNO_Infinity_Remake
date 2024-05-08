from utilities.log_wrapper import LoggerWrapper
from utilities.room import Room
import pprint # type: ignore

logger: LoggerWrapper = LoggerWrapper('logs/latest.log')
room: Room = Room(log_wrapper=logger)

code = room.create_room('Among Us Lobby')
pprint.pprint(room.__dict__())
user_uuid = room.rooms[code].add_user("Gamer Verse")
room.rooms[code].member_exist(user_uuid)
# room.rooms[code].remove_user(user_uuid)
# room.delete_room(code)
room.room_exist(code)
room.__write__('test/output.json')
