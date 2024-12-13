class Hero:
    def __init__(self, name="John Doe", hp=100):
        self.name = name
        self.hp = hp

    def rest(self):
        self.hp += 10
        return f"{self.name}, восстанавливает здоровье на +10 HP^{self.hp}"

    def action(self):
        return f"{self.name} делает базовое действие"

    def status(self):
        return f"Имя:{self.name}, Здоровье:{self.hp}"


hero = Hero("Kirtito")

print(hero.action())
# print(hero.)

# Наследование
class Warrior(Hero):

    def __init__(self, name, hp, st):
        super().__init__(name, hp)
        self.st = st

    def attack(self):
        if self.st >= 10:
            self.st -= 10
            return f"{self.name} Превращается в Алмаза"
        else:
            return f"{self.name} стамина меньше 10"

    def charge(self):
        if self.st >= 20:
            self.st -= 20
            self.hp += 50
            return f"{self.name} Пополнил здоровье на 50 единиц  использовав 20 станины. Здоровье:{self.hp} Станина:{self.st}"
        else:
            f"Не достаточно станины"

hero_warrior = Warrior("Ben-10", 1000, 100)


# # print(hero_warrior.rest())
# print(hero_warrior.attack())

class Mage(Hero):

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self.mp = mp

    def rest(self):
        self.mp += 10
        return f"{self.name} , восстанавливает  ману на +10 MP^{self.mp}"

    def attack(self):
        if self.mp >= 10:
            self.mp -= 10
            return f"{self.name} Колдует в Огненый щар"
        else:
            return f"{self.name} Мана меньше 10"

    def action(self):
        old_action = super().action()
        attack = self.attack()

        return f"{old_action}  {attack}"
    def teleport(self):
        if self.mp >= 30:
            self.mp -= 30
            return f"{self.name} использовал 30 маны чтобы телепортироваться, остаток маны{self.mp}"
        else:
            f"У вас не достаточно маны"


class Archer(Hero):

    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows >= 1:
            self.arrows -= 1
            if self.precision >= 65:
                return f"{self.name} Успешно совершил атаку, осталось стрел:{self.arrows}"
            else:
                return f"{self.name} Не попал в цель, осталось стрел:{self.arrows}"
        else:
            return f"Не достаточно стрел"

    def rest(self):
        self.arrows += 5
        return f"{self.name} Успешно пополнено 5 стрел, всего стрел:{self.arrows}"

def hero_actions(hero):
    print(hero.status())
    print(hero.rest())
    print(hero.action())


hero_archer = Archer("strelok", 500, 20, 70)
hero_mage = Mage("Гендальф", 100, 1000)

print(hero_archer.rest())
print(hero_archer.attack())
print(hero_mage.rest())
print(hero_mage.action())
print(hero_mage.teleport())
print(hero_archer.action())
print(hero_warrior.charge())


print("\nДействия для Лучника:")
hero_actions(hero_archer)

print("\nДействия для Мага:")
hero_actions(hero_mage)

print("\nДействия для Воина:")
hero_actions(hero_warrior)

print("\nПроверка наследования:")
print(isinstance(hero, Hero))
print(isinstance(Warrior, Hero))
print(isinstance(Mage, Hero))
print(isinstance(Archer, Hero))
print(isinstance(Mage, Warrior))
print(isinstance(Archer, Mage))