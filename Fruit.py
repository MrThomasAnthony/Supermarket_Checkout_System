from Element import Element

class Fruit(Element):
    def __init__(self, name: str, price_per_kg: float, weight: float):
        self._name = name
        self._price_per_kg = price_per_kg
        self._weight = weight

    def getPricePerKg(self) -> float:
        return self._price_per_kg
    
    def getWeight(self) -> float:
        return self._weight
    
    def getName(self) -> str:
        return self._name

    def accept(self, visitor):
        visitor.visit(self)