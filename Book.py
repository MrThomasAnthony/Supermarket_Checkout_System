from Element import Element

class Book(Element):
    def __init__(self, isbn: str, price: float):
        self._isbn = isbn
        self._price = price

    def getPrice(self) -> float:
        return self._price
    
    def getIsbnNumber(self) -> str:
        return self._isbn

    def accept(self, visitor):
        visitor.visit(self)