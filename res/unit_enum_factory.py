from enum import Enum
from res.units.spearmen import Spearmen
from res.units.bowman import Bowman 
from res.units.crossbowman import Crossbowman
from res.units.healer import Healer
from res.units.knight import Knight
from res.units.wizard import Wizard 

class Units(Enum):
    Копейщики = 1
    Рыцари = 2
    Лучники = 3
    Арбалетчики = 4
    Колдуны = 5
    Целители = 6

class UnitFactory():
    @staticmethod
    def CreateUnit(unit):
        if  (unit == Units.Копейщики):
            return Spearmen()
        elif (unit == Units.Рыцари):
            return Knight()
        elif (unit == Units.Лучники):
            return Bowman()
        elif (unit == Units.Арбалетчики):
            return Crossbowman()
        elif (unit == Units.Колдуны):
            return Wizard()
        elif (unit == Units.Целители):
            return Healer()
