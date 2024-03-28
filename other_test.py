import json
from typing import Dict, List, TypedDict
import pprint


class MyDict(TypedDict):
    Name: str
    Amount: int
    Speed: bool


with open('utilities/uno.json') as f:
    data = json.load(f)

final_list = []
my_dict = data['4_Color_Uno']
wild_cards = [
            'Wild',
            'Block Wild',
            'Reverse Wild',
            'Replay Wild',
            '# Wild',
            'Recycle',
            'Eye',
            'Shield',
            'Joker',
            '+2 Wild',
            '+4 Wild',
            '+6 Wild',
            '+8 Wild',
            '+10 Wild',
            '-1 Wild',
            '-2 Wild',
            '2x Wild',
            'Divide 2 Wild',
            '+4T Wild',
            '++4 Wild',
            'D4',
            'D6',
            'D8',
            'D12',
            'D20',
            'Trade',
            'Steel',
            'Gift',
            '777',
            'NO U']

wild_override: Dict[str, int] = {'Wild': 4,
                                 'Eye': 2,
                                 'Shield': 4,
                                 '+2 Wild': 2,
                                 '+4 Wild': 2,
                                 'Trade': 2}
number: int = 1
for x in my_dict:
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
                    final_list.append(var)

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
                final_list.append(var)

    elif x['Name'] == 'Colorless':
        for index in range(0, 10):
            var = {
                "Name": x['Name'],
                "Number": index,
                "Color": 'Colorless',
                "Speed": False
            }
            final_list.append(var)

    elif x['Name'] == 'Wild':
        for card in wild_cards:
            if wild_override.get(card, False):
                number = wild_override[card]
            else:
                number = 1
            for _ in range(0, int(number)):
                var = {
                    "Name": card,
                    "Number": '',
                    "Color": 'Wild',
                    "Speed": False
                }
                final_list.append(var)
    else:
        print(f'----------------------------------------------------------------')
        print(f'{x=}')
        print('----------------------------------------------------------------')

pprint.pprint(final_list)
pprint.pprint(len(final_list))
with open('utilities/uno_data_test.json', 'w') as f:
    json.dump(final_list, f, indent=4)
