from Creators import Personality
from Created_Characters import SwordsmanClass, ArcherClass, MagicianClass


class CreatorPersonality(Personality):
    def factory(self):
        person_class = {
            "Swordsman": SwordsmanClass,
            "Archer": ArcherClass,
            "Magician": MagicianClass,
        }
        return person_class[self.name]()
