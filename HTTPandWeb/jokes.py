import requests

class JokeMaker:
    def __init__(self, name='Chuck Norris'):
        self.status_code = None
        self.name = name

        # Call the controller function
        self.controller()

    def get_name(self):
        self.name = input('Enter your name: ')
        if self.name is not None:
            return self.name

    def make_a_joke(self):
        names = self.name.split()
        if len(names) < 2:
            print('We\'d prefer both first and second name :)')
            names = self.get_name().split()
            
        response = requests.get('http://api.icndb.com/jokes/random?firstName={0}&lastName={1}'
                                .format(names[0], names[1]))

        if response.status_code == 200:
            result = response.json()
            if result["type"] == 'success':
                value = result["value"]
                print('\n{}\n'.format(value["joke"]))
            else:
                print('We couldn\'t a joke for you :(')

    def controller(self):
        print('Hi there! Wanna hear a Chuck Norris joke?')
        print('1. Yes!')
        print('2. Yes, but with my name in it')

        selection = input()

        if selection == '1':
            self.make_a_joke()
        elif selection == '2':
            self.get_name()
            self.make_a_joke()
        else:
            print('Umm, that\'s not valid input. I\'ll just make the joke anyway :)\n')
            self.make_a_joke()

if __name__ == '__main__':
    JokeMaker()
