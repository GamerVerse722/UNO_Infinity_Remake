import pprint

win_list = [
    [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
    ],
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ],
    [
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0],
    ],
    [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ],
    [
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1]
    ],
    [
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
    ],
    [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ],
    [
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 1]
    ]
]

my_list = [
    [2, 1, 4],
    [0, 1, 5],
    [0, 1, 0]
]

def filter_list(data, number):
    pprint.pprint(data)
    for y in range(3):
        for x in range(3):
            if data[y][x] != number:
                data[y][x] = 0
    pprint.pprint(data)

filter_list(my_list, 1)

if my_list in win_list:
    print('Win')
else:
    print('Lose')

# pprint.pprint(my_list)
