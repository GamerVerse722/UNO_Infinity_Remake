import random, string, psutil, os

def name_gen(length: int = 8) -> str:
    final: str = ""
    for _ in range(length):
        final += random.choice(string.ascii_letters)

    return final

def line() -> None:
    print("------------------------------------------------------------------------------------------------")


def memory_usage() -> float:
    return psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2