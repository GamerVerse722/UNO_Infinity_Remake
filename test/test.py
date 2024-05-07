from utilities.room import Room
import pprint # type: ignore

room = Room()

code = room.create_room('Among Us Room')
pprint.pprint(room.__dict__())
room.delete_room(code)
pprint.pprint(room.__dict__())
