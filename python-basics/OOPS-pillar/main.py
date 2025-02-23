import Enemy as E 

enemy1 = E.Enemy()
enemy2 = E.Enemy()

enemy1.type_of_enemy = "Zombie"
enemy2.type_of_enemy = "Terrorist"

enemy1.attack_damage = 12 
enemy2.attack_damage = 20

print(f"{enemy1.type_of_enemy} has {enemy1.health_point} health points and {enemy1.attack_damage} attack damage")
print(f"{enemy2.type_of_enemy} has {enemy2.health_point} health points and {enemy2.attack_damage} attack damage")
