class Enemy():
    type_of_enemy : str 
    attack_damage : int = 3 
    health_point : int = 10 

    def talk(self):
        print(f"I am a {self.type_of_enemy}")

    def attack(self):
        print(f"I am attacking with {self.attack_damage} damage")

    def walk_forward(self):
        print(f"I am walking forward")