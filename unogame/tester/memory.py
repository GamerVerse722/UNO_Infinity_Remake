from unogame.room.room import Room
from unogame.logging.log_wrapper import LoggerWrapper
import random
import string
import psutil
import os

def name_gen(length: int = 8) -> str:
    final: str = ""
    for _ in range(length):
        final += random.choice(string.ascii_letters)

    return final

logger = LoggerWrapper(filename="logger.log", console=None)
room = Room(log_wrapper=logger)
starting_memory = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2


for _ in range(200):
    code: str = room.create_room(room_name=name_gen(length=12), code_length=12, max_user=12)
    for _ in range(12):
        uuid = room.rooms[code].add_user(name_gen(length=12))
        room.rooms[code].add_message(user_uuid=uuid, message=name_gen(length=50))
        room.rooms[code].start_uno_game()

max_memory = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2

room.rooms = {}

end_memory = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2

print(f"Start Memory usage: {starting_memory:.2f} MB")
print(f"Max Memory usage: {max_memory:.2f} MB")
print(f"End Memory usage: {end_memory:.2f} MB")