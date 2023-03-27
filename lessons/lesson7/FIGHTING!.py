# Global variables
fighters = []
heal_power = 10

class Characters():
    # Data declaring
    name = ''
    hp = 0
    armor = 0
    power = 0
    def __init__(self, name, hp, armor, power):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.power = power

class Game(Characters):

    # Function to heal fighter
    def heal(self):
        global heal_power
        self.hp += heal_power
        print(self.name + ' have ', self.hp, ' hp left')

    # function for attack
    def attacked(self, damage):
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
    hp = int(input('Hp: '))
    armor = int(input('Armor: '))
    power = int(input('Power: '))
    fighters.append(Game(name, hp, armor, power))

# Declaring Game Data
alive = True
player1 = fighters[0]
player2 = fighters[1]

cur_player = player1
next_player = player2
