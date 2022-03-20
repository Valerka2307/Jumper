class Personality:
    def __init__(self, name):
        self.name = name


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
