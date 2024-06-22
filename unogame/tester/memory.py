from unogame.room.room import Room
from unogame.logging.log_wrapper import LoggerWrapper
from unogame.tester.helper.utils import name_gen, line, memory_usage
import objgraph, os

logger = LoggerWrapper(filename="logger.log", console=None)
room = Room(log_wrapper=logger)
starting_memory = memory_usage()

location: str = "unogame/tester/graph/"

for _ in range(500):
    code: str = room.create_room(room_name=name_gen(length=12), code_length=12, max_user=12)
    for _ in range(12):
        uuid = room.rooms[code].add_user(name_gen(length=12))
        room.rooms[code].add_message(user_uuid=uuid, message=name_gen(length=50))
    room.rooms[code].start_uno_game()
    room.rooms[code].uno_game.create_uno_deck()  # type: ignore

max_memory = memory_usage()

room.delete_every_room()
room.__write__(f"unogame/tester/test.json")

end_memory = memory_usage()

line()
objgraph.show_most_common_types(limit=20)
line()
# print(gc.collect())
# line()

print(room.rooms)

objgraph.show_backrefs(objs=[room], filename=f'{location}roomdata_backrefs.dot', max_depth=10, too_many=5)
os.system(f'dot -Tsvg {location}roomdata_backrefs.dot -o {location}roomdata_backrefs.svg')

print(f"Graph written to {location}roomdata_backrefs.svg")

print(f"Start Memory usage: {starting_memory:.3f} MB")
print(f"Max Memory usage: {max_memory:.3f} MB")
print(f"End Memory usage: {end_memory:.3f} MB")