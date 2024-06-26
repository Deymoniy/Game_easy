import random
the_boss_alive = True
player_alive = True
class_chosen = False
user_name = input("\033[34mEnter your name: ")
print('')
player = {'name':user_name, 
          'max_health':100,
          'current_health':100, 
          'min_damage':6, 
          'max_damage':10, 
          'crit':5,
          'armour':2,
          'evasion':5
        }
class_player = input("Choose your class traveler: Rogue, Archer, Warrior or Knight.")
while class_chosen == False:
    if class_player.lower() == 'rogue':
        player['crit'] += 10
        player['evasion'] += 10
        class_chosen = True
    elif class_player.lower() == 'archer':
        player['crit'] += 10
        player['min_damage'] += 4
        player['max_damage'] += 5
        class_chosen = True
    elif class_player.lower() == 'warrior':
        player['max_health'] += 50
        player['min_damage'] += 4
        player['max_damage'] += 5
        class_chosen = True
    elif class_player.lower() == 'knight':
        player['max_health'] += 50
        player['armour'] += 4
        class_chosen = True
    else:
                    print('Oops. Try again! Type the class')

print(f"You've entered dark temple of the Old One, oh brave {class_player} {user_name}.")
print('The temple floor is covered with blood and bones of the others who came here before you.')
print('The Old One is a terror torturing you lands. And you are the one to save them or at least die trying.')
print('Good Luck! And let the Gods help you!')   

def evasion(ev_chance, damage, pl_health, armor):
    ev_chance = player['evasion']
    hit = random.randint(1,100)
    if ev_chance >= hit:
        print("You've EVADED an attack. Huh!")
    else:
        dm_rec = damage - armor
        pl_health = pl_health - (damage - armor)
        print(f"You've received {dm_rec}. You've got {pl_health} hp")
    return pl_health


print(f'Here comes {user_name}')
print('')
enemy_min_damage = {'slime':5,'wolf':8,'skeleton': 15,'werewolf':20,'the boss':35}
enemy_max_damage = {'slime':9,'wolf':15,'skeleton': 20,'werewolf':30,'the boss':50}
slime = {'name':"Slime", 'health':30, 'min_damage':enemy_min_damage['slime'], 'max_damage':enemy_max_damage['slime'], 'exp':random.randint(6,10)}
wolf = {'name':"Wolf", 'health':60, 'min_damage':enemy_min_damage['wolf'], 'max_damage':enemy_max_damage['wolf'], 'exp':random.randint(15,20)}
skeleton = {'name':"Skeleteon", 'health':100, 'min_damage':enemy_min_damage['skeleton'], 'max_damage':enemy_max_damage['skeleton'],'exp':random.randint(40,60)}
werewolf = {'name':"Werewolf", 'health':150, 'min_damage':enemy_min_damage['werewolf'], 'max_damage':enemy_max_damage['werewolf'], 'exp':random.randint(70,100)}
the_boss = {'name':"The Old One", 'health':250, 'min_damage':enemy_min_damage['the boss'], 'max_damage':enemy_max_damage['the boss'], 'exp':100}
enemies = {'slime':slime,'wolf':wolf,'skeleton':skeleton,'werewolf':werewolf,'the old one':the_boss}
exp = 0
level = 1
need_exp = 20
potions= {'small':0, 'med':0,'big':0}
potion_drop = 30
def healing(player, potion):
    command = input(" What potion small, med or big?: ") 
    if potion['small'] > 0 and command == 'small':
        player['current_health'] += random.randint(30, 45)
        potions['small'] -= 1
        if player['current_health'] > player['max_health']:
            player['current_health'] = player['max_health']
        print(f"You've healed. Your health now is {player['current_health']}")
    elif potion['med'] > 0 and command == 'med':
        player['current_health'] += random.randint(50, 65)
        potions['med'] -= 1
        if player['current_health'] > player['max_health']:
            player['current_health'] = player['max_health']
        print(f"You've healed. Your health now is {player['current_health']}")
    elif potion['big'] > 0 and command == 'small':
        player['current_health'] += random.randint(70, 90)
        potions['big'] -= 1
        if player['current_health'] > player['max_health']:
            player['current_health'] = player['max_health']
        print(f"You've healed. Your health now is {player['current_health']}")
    else: 
        print('It seems that you have no potions')

def attack(player,enemy):
    enemy_health = enemy['health']
    player_health = player['current_health']
    armour = player['armour']
    enemy_alive = True
    player_alive = True
    turn = 1
    print(f"You're fighting a {enemy['name']}")
    while enemy_alive & player_alive == True:
        crit_chance = random.randint(1,100)
        enemy_damage = random.randint(enemy['min_damage'],enemy['max_damage'])
        player_damage = random.randint(player['min_damage'],player['max_damage'])
        print(f'Round {turn}')
        if crit_chance <= player['crit']:
            enemy_health = enemy_health - player_damage * 2
            print(f'You did CRITICAL DAMAGE {player_damage * 2} damage. ENEMY has {enemy_health} hp')
            if enemy_health <= 0:
                print(f'Your ENEMY is DEAD. Your HEALTH is {player_health}')
                enemy_alive= False
                if random.randint(1,100) < potion_drop:
                    if enemy == enemies['slime']:
                        potions['small'] += 1
                        print('You found a small potion!')  
                    elif enemy == enemies['wolf']:
                        potions['small'] += 1
                        print('You found a small potion!')
                    elif enemy == enemies['skeleton']:
                        potions['med'] += 1
                        print('You found med potion!')
                    elif enemy == enemies['werewolf']:
                        potions['big'] +=1
                        print('You found a big potion.')
                return player_health, enemy['exp']
                break
        else:
            enemy_health = enemy_health - player_damage
            if enemy_health <= 0:
                print(f'Enemy received {player_damage} dmg. Your enemy is dead, {class_player}. Your health is {player_health}')
                enemy_alive= False
                if random.randint(1,100) < potion_drop:
                    if enemy == enemies['slime']:
                        potions['small'] += 1
                        print('You found a small potion!')  
                    elif enemy == enemies['wolf']:
                        potions['small'] += 1
                        print('You found a small potion!')
                    elif enemy == enemies['skeleton']:
                        potions['med'] += 1
                        print('You found med potion!')
                    elif enemy == enemies['werewolf']:
                        potions['big'] +=1
                        print('You found a big potion.')
                return player_health, enemy['exp']
                break
            else:
                print(f'Enemy received {player_damage} dmg. Enemy has {enemy_health}')

        
        player_health = evasion(player['evasion'], enemy_damage, player_health, armour)
        if player_health <= 0:
            print("You've lost, biatch!")
            player_alive = False
        print('Next round!')
        print('')
        turn += 1
        
            

def handle_battle( player, enemy, level, exp, need_exp, min_damage, max_damage):
        result = attack(player,enemy)
        player['current_health'] = result[0]
        exp += result[1]
        if exp >= need_exp:
            level += 1
            exp = exp - need_exp
            need_exp = need_exp * (level - 1) + need_exp * (level - 1) * 0.1 
            print('')
            print(f"LEVEL UP! your level now is {level}. You need {need_exp - exp} to get a new level!")
            player['min_damage'] += 3
            player['max_damage'] += 3
            player['max_health'] +=30
            player['armour'] += 2
            player['current_health'] = player['max_health']
            player['crit'] += 3
            player['evasion'] +=3
            print(f"Your minimum damage and max damage are risen by 3 and equals {player['min_damage']} - {player['max_damage']}. ")
            print(f"Your hp now {player['max_health']}, your armour is {player['armour']} and you're healed")
            print(f'Your crit chance is {player['crit']}% and your evasion is {player['evasion']}%.')
            print('')
            return exp, level, need_exp
        else:
            print(f"You get {result[1]} exp. You need {need_exp - exp} to get a new level!")
            print('------------'*10)
            return exp, level, need_exp,

while the_boss_alive and player_alive: 
    print(f'Whom do you want to fight sir {user_name}: slime, wolf, skeleton, werewolf or The Old One?')
    do_what = (input('Or would you like to check potions, heal, check stats or stop? '))
    print('')
    if do_what.lower() == 'check potions':
        print(f"{potions}")
    elif do_what.lower() == 'check stats':
        print(f"{player}")
    elif do_what.lower() == 'heal':
        healing(player, potions)
    elif do_what.lower() in enemies:
        b_result = handle_battle(player, enemies[do_what.lower()], level, exp, need_exp, player['min_damage'], player['max_damage'])
        exp = b_result[0]
        level = b_result[1]
        need_exp = b_result[2]
    elif do_what.lower() == 'stop':
        break
