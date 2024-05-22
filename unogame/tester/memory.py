from unogame.room.room import Room
from unogame.logging.log_wrapper import LoggerWrapper
from unogame.tester.helper.utils import name_gen, line, memory_usage
import psutil, os, objgraph, gc, subprocess  # type: ignore

logger = LoggerWrapper(filename="logger.log", console=None)
room = Room(log_wrapper=logger)
starting_memory = memory_usage()

for _ in range(5):
    code: str = room.create_room(room_name=name_gen(length=12), code_length=12, max_user=12)
    for _ in range(12):
        uuid = room.rooms[code].add_user(name_gen(length=12))
        room.rooms[code].add_message(user_uuid=uuid, message=name_gen(length=50))
    # room.rooms[code].start_uno_game()
    # room.rooms[code].uno_game.create_uno_deck()  # type: ignore

max_memory = memory_usage()

# room.delete_every_room()
room.__write__("test.json")

end_memory = memory_usage()

line()
objgraph.show_most_common_types(limit=20)
line()

objgraph.show_backrefs(objgraph.by_type('Uno'), max_depth=8, too_many=20, filename='/tmp/roomdata_backrefs.dot')
subprocess.run(['dot', '-Tpng', '/tmp/roomdata_backrefs.dot', '-o', '/Users/cristianrios/roomdata_backrefs.png'])

print("Graph written to /tmp/roomdata_backrefs.png")
line()
print(gc.collect())
print(gc.garbage)
line()

print(f"Start Memory usage: {starting_memory:.3f} MB")
print(f"Max Memory usage: {max_memory:.3f} MB")
print(f"End Memory usage: {end_memory:.3f} MB")