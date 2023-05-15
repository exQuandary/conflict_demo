<< << << < HEAD


def hello_world(state):
    print(f'Hello World! {state}')


def main():
    hello_world('New York')


== == == =


def hello_world(city, state):
    print(f'Hello World {city}, {state}!')


def main():
    hello_world('NYC', 'New York')


main()
