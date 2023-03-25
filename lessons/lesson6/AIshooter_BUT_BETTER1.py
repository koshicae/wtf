# ch_name = input('State the name of your character: ')
ch_name = 'kiwi' #name by default
import random

pers_hp = 100
armor = 50
hp = 10
# Attack function
def attack(dmg):
    global armor, pers_hp
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
    print()
    if pers_hp == 0:
        print()


def crit_heal():
    global pers_hp, hp
    hp = int(heal())
    r = random.random()
    if r <= 0.1:
        hp *= 2
        print('Critical heal!')
        pers_hp += hp
    else:
        pers_hp += hp
    if pers_hp > 100:
        pers_hp = 100
    return pers_hp

# Heal function
def heal(): #random heal
    global rng_hp_value, hp
    rng_hp_value = list(range(10, 21, 5))
    hp = random.choice(rng_hp_value)
    return hp

# Critical damage function
def crit_atk(dmg):
    p = random.random()
    if p <= 0.1:
        dmg *= 2
        print('Critical shot!')
    return dmg

def random_damage():
    global rng_damage_value
    rng_damage_value = list(range(5, 76, 5))
    dmg = random.choice(rng_damage_value)
    return dmg

# Battle loop
for i in range(0, 10000):
    z = random.random()
    print('The enemy is ready to hit...')
    if z <= 0.5:
        print('The enemy missed their hit!')
        if pers_hp < 100:
            print('This is your chance! Try to heal yourself!')
            if pers_hp < 100 and pers_hp != 0:
                o = random.random()
                if o >= 0.2:
                    stats()
                    crit_heal()
                    print('Healing received:', hp, 'Total character hp:', pers_hp)
                else:
                    print('Oops! You just spilled your healing potion. Healing wasn\'t received for this iteration :(')
            print()
        else:
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
