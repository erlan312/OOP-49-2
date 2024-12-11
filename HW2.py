class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def rest(self):
        self.hp += 10
        return f"{self.name}, восстанавливаетздоровье на +10 HP^{self.hp}"

    def action(self):
        return f"{self.name} делает базовое действие"


hero = Hero("kirito", 100)

print(hero.rest())
class Warior(Hero):
    def __init__(self, name, hp, st):
        super().__init__(name, hp)
        self.st = st


    def attack(self):
        if self.st >= 10:
            return f"{self.name} превратился в Алмаза"
        else:
            return f"{self.name} стамина меньше 10"

hero_warior = Warior("Ben-10", 1000, 100)

# print(hero_warior.action())
# print(hero_warior.attack())

class Mage(Hero):
    def __init__(self, name, hp, st):

