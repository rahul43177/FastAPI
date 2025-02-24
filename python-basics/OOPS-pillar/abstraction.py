class Enemy():
    type_of_enemy : str 
    health : int = 12 
    damage : int = 100 

    def talk(self):
        print(f"I am {self.type_of_enemy}. Be prepared to fight!")
    def walk_forward(self):
        print(f"I am {self.type_of_enemy} and i am moving forward")
    def attack(self):
        print(f"The attack damage i do is {self.damage}")
    def get_health(self):
        print(f"The health i have is {self.health}")
