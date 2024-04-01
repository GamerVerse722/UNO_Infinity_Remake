import pprint


class Test:
    def __init__(self):
        self.main = [True]
        self.other = "String is inherited"
        self.room = {}

    def create_room(self, room_code):
        self.room[room_code] = {
            "Inheritance Data": self.Inheritance(room=self.room, main=self.main)
        }

    class Inheritance:
        def __init__(self, room=None, main=None):
            if main is None:
                main = []
            self.main = main
            self.main.append('Hi')
            self.current = room
            self.test = 'This is my new data to be put in data function'
            self.player_data = 'You have 10 cards on your'

        def add_data(self, number):
            self.main.append(number)

        def set_room(self, code):
            self.current = code

        def __dict__(self):
            return {'Other data': self.test, 'PlayerData': self.player_data}

    def __dict__(self):
        inheritance_data = {}
        for room_code, room_data in self.room.items():
            inheritance_data[room_code] = room_data["Inheritance Data"].__dict__
        print('----------------------------------------------------------------')
        return {'Main': self.main, 'other': self.other, 'Inheritance': inheritance_data}


# Create an instance of the Test class
test_instance = Test()

# Call the create_room method
test_instance.create_room('Among Us')
test_instance.create_room('Gamer Lobby')

# Access the data using the data() method
pprint.pprint(test_instance.__dict__(), indent=2)

# Accessing and running a function in the Inheritance class
test_instance.room['Among Us']["Inheritance Data"].add_data("New data")
print('----------------------------------------------------------------')
print(test_instance.room['Among Us']["Inheritance Data"].__dict__)
print('----------------------------------------------------------------')
# pprint.pprint(dir(test_instance))