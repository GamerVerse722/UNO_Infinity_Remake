from typing import Dict, List, Any
import json, random

class Uno:
    def __init__(self, room: str = '') -> None:
        self.room: str = room
        self.game_started = False
        self.uno_deck: List[Dict[str, Any]] = []
        self.discard_pile: List[Dict[str, Any]] = []
        self.player_data: Dict[str, Dict[str, list]] = {}

    def __dict__(self) -> Dict[str, Any]:
        return {'Uno_Deck': self.uno_deck,
                'Discard_Pile': self.discard_pile,
                'Player_Data': self.player_data}

    def create_uno_deck(self, mode: str = '4-color') -> None:
        with open('unogame/uno/configuration/uno.json') as f:
            data = json.load(f)

        wild_override: Dict[str, int] = {}
        wild_cards: List[dict] = []
        wild_list: List[str] = []

        if mode == '4-color':
            wild_override = data['4-Color-Uno']['Wild_Override']
            wild_cards = data['4-Color-Uno']['Uno-Configuration']
            wild_list = data['Uno_Wildcards']

        total_uno_deck: List[dict] = []
        for x in wild_cards:
            if x['Name'] == '1-9':
                for index in range(0, 9):
                    for color in ['Red', 'Blue', 'Green', 'Yellow']:
                        for _ in range(0, x['Amount']):
                            var = {
                                "Name": '1-9',
                                "Number": index + 1,
                                "Color": color,
                                "Speed": x['Speed']
                            }
                            total_uno_deck.append(var)

            elif x['Name'] in ['0', 'Block', 'Reverse', 'Replay', '#', '+1', '+2', '+4', '-1']:
                for color in ['Red', 'Blue', 'Green', 'Yellow']:
                    zero: str = ''
                    if x['Name'] == '0':
                        zero = '0'
                    for _ in range(0, x['Amount']):
                        var = {
                            "Name": x['Name'],
                            "Number": zero,
                            "Color": color,
                            "Speed": False
                        }
                        total_uno_deck.append(var)

            elif x['Name'] == 'Colorless':
                for index in range(0, 10):
                    var = {
                        "Name": x['Name'],
                        "Number": index,
                        "Color": 'Colorless',
                        "Speed": False
                    }
                    total_uno_deck.append(var)

            elif x['Name'] == 'Wild':
                for card in wild_list:
                    number: int = 1
                    if wild_override.get(card, False):
                        number = wild_override[card]
                    for _ in range(0, int(number)):
                        var = {
                            "Name": card,
                            "Number": '',
                            "Color": 'Wild',
                            "Speed": False
                        }
                        total_uno_deck.append(var)
            else:
                print(f'----------------------------------------------------------------')
                print(f'{x=}')
                print('----------------------------------------------------------------')

        self.uno_deck = total_uno_deck

    def uno_deck_exists(self) -> bool:
        if not self.uno_deck:
            return False
        else:
            return True

    def shuffle_cards(self) -> None:
        random.shuffle(self.uno_deck)

    def add_players(self, players: List[str]) -> None:
        for player in players:
            self.player_data[player] = {
                "Cards": []
            }

    def remove_uno_deck(self) -> None:
        self.uno_deck = []

    def uno_deck_length(self) -> int:
        return len(self.uno_deck)

    def split_cards(self, split_amount: int = 7) -> None:
        for inter in range(split_amount):
            for user_uuid in self.player_data:
                self.player_data[user_uuid]['Cards'].append(self.uno_deck.pop(0))

    def start_game(self, member_list: List[str], split_amount: int = 7, mode: str = '4-color') -> None:
        self.add_players(players=member_list)
        self.create_uno_deck(mode=mode)
        print(self.uno_deck_length())
        self.shuffle_cards()
        self.split_cards(split_amount=split_amount)