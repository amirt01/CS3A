class Tapir:
    def __init__(self):
        self.animalType: str = 'Tapir'
        self.idTag: int = 0
        self.minTemperature: int = 65
        self.maxTemperature: int = 85

    def getAnimalType(self) -> str:
        return self.animalType

    def getIdTag(self) -> int:
        return self.idTag

    def setIdTag(self, anIdTag: int) -> None:
        self.idTag = anIdTag

    def getMinTemperature(self) -> int:
        return self.minTemperature

    def getMaxTemperature(self) -> int:
        return self.maxTemperature
