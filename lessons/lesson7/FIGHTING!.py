# Global variables
fighters = []
heal_power = 10
alive = True


class PlayerStats:
    def __init__(self):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.power = power
        self.max_hp = hp


class DifferentFunctions(PlayerStats):
    def heal(self):
        global heal_power  # Accessing the variable from the start of the code
        self.hp += heal_power  # Healing the player
        if self.hp > self.max_hp:  # In case hp gets higher than the max_hp value, equalize it to the max_hp
            self.hp = self.max_hp
        print(self.name, 'has', self.hp, 'hp left')

    def attack_armor(self, damage):
        self.armor -= damage
        if self.armor > 0:
            print(self.name, 'has', self.armor, 'armor left')
            return True
        else:
            print('The armor has been broken!')
            return True

    def attack_hp(self, damage):
        self.hp -= damage
        if self.hp > 0:
            print(self.name, 'has', self.hp, 'hp left')
            return True
        else:
            print(self.name, 'died')
            return False


for i in range(0, 2):
    print(name, hp, armor, power)
    name = 'A'  # input('Name: ')
    hp = 100
    armor = 50
    power = 30
    # while True:
    #     try:
    #         hp = int(input('Hp: '))
    #         break
    #     except ValueError:
    #         print('Wrong data input')
    #
    # while True:
    #     try:
    #         armor = int(input('Armor: '))
    #         break
    #     except ValueError:
    #         print('Wrong data input')
    #
    # while True:
    #     try:
    #         power = int(input('Power: '))
    #         break
    #     except ValueError:
    #         print('Wrong data input')
    fighters.append(Game(name, hp, armor, power))

    while alive:
        player1 = fighters[0]
        player2 = fighters[1]

        cur_player = player1
        next_player = player2

        print('Turn to choose for', cur_player.name)
        print('Enter 1 for attack other player')
        print('Enter 2 for heal')
        print('Enter 3 to Continue')

        while True:
            try:
                move = int(input())
                break
            except ValueError:
                print('Wrong data input')

    if move == 1:
        if armor > 0:
            alive = next_player.attack_armor(cur_player.power)
        else:
            alive = next.player.attack_hp(cur_player.power)
    elif move == 2:
        cur_player.heal()
    elif move == 3:
        continue

    if cur_player == player1:
        cur_player = player2
        next_player = player1
    else:
        cur_player = player1
        next_player = player2
