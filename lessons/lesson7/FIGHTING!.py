# Global variables
fighters = []
heal_power = 10


class Characters:  # Don't write () if there is nothing to declare, lol
    # Data declaring
    name = ''
    hp = 0
    armor = 0
    power = 0
    max_hp = 0

    # Function that declares data provided further in the code
    def __init__(self, name, hp, armor, power):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.power = power
        self.max_hp = hp


class Game(Characters):

    # Function to heal fighter
    def heal(self):
        global heal_power  # Accessing the variable from the start of the code
        self.hp += heal_power  # Healing the player
        if self.hp > self.max_hp:  # In case hp gets higher than the max_hp value, equalize it to the max_hp
            self.hp = self.max_hp
        print(self.name + ' has', self.hp, 'hp left')

    # Function for attack
    def attacked(self, damage):
        if self.armor > 0:  # If armor is greater than 0, perform attack sequence
            self.armor -= damage
            if self.armor > 0:  # If armor is still more than 0, write how much armor is left
                print(self.name + ' has', self.armor, 'armor left')
                return True  # Checks the condition for "alive"
            elif self.armor == 0:
                print(self.name + ' has', self.armor, 'armor left')
                return True
            else:  # If armor became less or equal to 0, rest of the damage goes to hp
                if self.armor < 0:
                    x = abs(self.armor)  # We use the absolute function, to make rest damage into a positive number,
                    # so to avoid further adding to the hp the rest dmg (bcs of its negative value)
                    self.hp -= x
                    print(self.name + ' has', self.hp, 'hp left')
                    self.armor = 0  # Equalize to 0, so the code further ahead actually works lol
                return True
        if self.armor == 0 and self.hp > 0:  # If armor = 0, hp > 0, get rid of hp
            self.hp -= damage
            if self.hp > 0:
                print(self.name + ' has', self.hp, 'hp left')
                return True
            else:  # kill fighter section
                print(self.name, 'got killed')
                return False  # stops the program


# Read players number
# Better 2 players
nr = 2
# while 1:
#     try:
#         nr = int(input('How many characters are in game?'))
#         break
#
#     except:
#         print('Wrong data type')
#         continue

# Read data about Fighters
for i in range(0, nr):
    name = input('Name: ')
    # name = 'Amy'
    # hp = 100
    # armor = 50
    # power = 30
    # print(name, hp, armor, power)
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
alive = True  # variable to continue/stop the fight
player1 = fighters[0]  # player1 gets the nam of the first fighter
player2 = fighters[1]

cur_player = player1  # the fight process will begin always with p1
next_player = player2  # variable to change inbetween players

while alive:

    # User interface
    print('Turn to choose for', cur_player.name)
    print('Enter 1 for attack other player')
    print('Enter 2 for heal')
    print('Enter 3 to Continue')
    # Insert which option to choose from
    while True:
        try:
            move = int(input())
            break
        except ValueError:
            print('Not desired int input')

    # Game logic
    if move == 1:
        alive = next_player.attacked(cur_player.power)  # If true, perform attack on the opposite player, if false,
        # stop program, show death scene
    elif move == 2:
        cur_player.heal()
    elif move == 3:
        continue

    # Switch players
    if cur_player == player1:  # The first to act will always be 1st fighter
        cur_player = player2  # Switches current player to the 2nd one
        next_player = player1  # Next player will be 1st fighter
    else:
        cur_player = player1  # If current player isn't p1, then switch him to be one
        next_player = player2  # In the next sequence, p2 will be the current player
