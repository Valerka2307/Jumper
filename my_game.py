class Personality:
    def __init__(self, name):
        self.name = name


class CreatorPersonality(Personality):
    def factory(self):
        person_class = {
            "Swordsman": SwordsmanClass,
            "Archer": ArcherClass,
            "Magician": MagicianClass,
        }
        return person_class[self.name]()


class Character:
    def __init__(self, name, *args):
        self.name = name
        self.HP = args[0]
        self.damage = args[1]
        self.attack_radius = args[2]
        self.defence = args[3]

    def __str__(self):
        return f'{self.name} (HP: {self.HP}, damage: {self.damage},' \
               f' attack_radius: {self.attack_radius}, defence: {self.defence})'


class SwordsmanClass(Character):
    def __init__(self):
        super().__init__('Swordsman', 8, 10, 1, 7)


class ArcherClass(Character):
    def __init__(self):
        super().__init__('Archer', 7, 6, 5, 5)


class MagicianClass(Character):
    def __init__(self):
        super().__init__('Magician',5 , 4, 10, 3)


b = CreatorPersonality('Swordsman').factory()
print(b.HP)
print(b)
