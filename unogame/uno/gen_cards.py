from typing import List
import json

class GenerateCards:
    def __init__(self) -> None:
        with open('utilities/data/uno.json') as f:
            data = json.load(f)
        self.configuration = data
        self.cards: List[dict] = []


    def cards_generate(self) -> None:
        pass