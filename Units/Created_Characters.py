from Creators import Character


class SwordsmanClass(Character):
    def __init__(self):
        super().__init__('Swordsman', 8, 10, 1, 7)


class ArcherClass(Character):
    def __init__(self):
        super().__init__('Archer', 7, 6, 5, 5)


class MagicianClass(Character):
    def __init__(self):
        super().__init__('Magician', 5, 4, 10, 3)
