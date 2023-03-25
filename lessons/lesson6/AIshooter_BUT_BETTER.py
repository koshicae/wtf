# ch_name = input('State the name of your character: ')
ch_name = 'kiwi'
import random

pers_hp = 100
armor = 50
hp = 10
list_of_num = list(range(0, 10001, 5))
# Attack function
def attack(dmg):
    global armor, pers_hp, healing
    if dmg > armor:
        rest_dmg = dmg - armor
        pers_hp -= rest_dmg
        armor = 0
    else:
        armor = armor - dmg
    if pers_hp <= 0:
        pers_hp = 0
        print(ch_name, 'got hit for', dmg, 'points of dmg!')
        stats()
        print(ch_name.upper() + ' died!'.upper())
    return pers_hp

# Character statistics function
def stats():
    print('Character hp:', pers_hp,
          'Character armor:', armor, end=' ')
    if pers_hp < 100 and pers_hp != 0:
        if i not in list_of_num:
            print('Healing received:', hp, 'Total character hp:', heal(hp))
        elif i in list_of_num:
            print('Oops! You just spilled your healing potion. Healing wasn\'t received for this iteration :(')
    else:
        print()

    if pers_hp == 0:
        print()

# Heal function
def heal(hp):
    global pers_hp
    pers_hp += hp
    if pers_hp > 100:
        pers_hp = 100
    return pers_hp

# Critical damage function
def crit_atk(dmg):
    p = random.random()
    if p <= 0.1:
        dmg *= 2
        print('Critical shot!')
    return dmg

def random_damage():
    global rng_damage_value
    rng_damage_value = list(range(5, 21, 5))
    dmg = random.choice(rng_damage_value)
    return dmg

# Battle loop
for i in range(0, 10000):
    print('Current iteration:', i)
    z = random.random()
    print('The enemy is ready to hit...')
    if z <= 0.5:
        print('The enemy missed their hit!')
        print()
        continue
    else:
        dmg = random_damage()
        dmg = crit_atk(dmg)
        attack(dmg)
        if pers_hp > 0:
            print(ch_name, 'got hit for', dmg, 'points of dmg!')
        if pers_hp != 0:
            stats()
            print()
        if pers_hp == 0:
            pass
            break
