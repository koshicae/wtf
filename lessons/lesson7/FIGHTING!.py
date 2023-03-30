# Global variables
fighters = []
heal_power = 10


class Characters():
    # Data declaring
    name = ''
    hp = 0
    armor = 0
    power = 0
    max_hp = 0

    def __init__(self, name, hp, armor, power):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.power = power
        self.max_hp = hp


class Game(Characters):

    # Function to heal fighter
    def heal(self):
        global heal_power
        self.hp += heal_power
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(self.name + ' have ', self.hp, ' hp left')

    # function for attack
    def attacked(self, damage):
        if self.armor > 0:
            self.armor -= damage
            print(self.name + ' has ', self.armor, ' armor left')
            return True
        elif self.armor <= 0:
            self.armor == 0
            if self.hp - damage > 0:
                self.hp -= damage
                print(self.name + ' have ', self.hp, ' hp left')
                return True
            else:
                print(self.name, ' is death')
                return False


# Read players number
# Better 2 players
while 1:
    try:
        nr = int(input('How many characters are in game?'))
        break

    except:
        print('Wrong data type')
        continue

# Read data about Fighters
for i in range(0, nr):
    name = input('Name: ')
    while True:
        try:
            hp = int(input('Hp: '))
            break
        except ValueError:
            print('Not desired int input')

    while True:
        try:
            armor = int(input('Armor: '))
            break
        except ValueError:
            print('Not desired int input')
    power = int(input('Power: '))
    fighters.append(Game(name, hp, armor, power))

# Declaring Game Data
alive = True
player1 = fighters[0]
player2 = fighters[1]

cur_player = player1
next_player = player2

while alive:

    # User interface
    print('Turn to choose for', cur_player.name)
    print('Enter 1 for attack other player')
    print('Enter 2 for heal')
    print('Enter 3 to Continue')
    while True:
        try:
            move = int(input())
            break
        except ValueError:
            print('Not desired int input')

    # game logic
    if move == 1:
        alive = next_player.attacked(cur_player.power)
    elif move == 2:
        cur_player.heal()
    elif move == 3:
        continue

    # switch players
    if cur_player == player1:
        cur_player = player2
        next_player = player1
    else:
        cur_player = player1
        next_player = player2
