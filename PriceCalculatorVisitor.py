from ShoppingCartVisitor import ShoppingCartVisitor
from multipledispatch import dispatch
from Book import Book
from Fruit import Fruit

class PriceCalculatorVisitor(ShoppingCartVisitor):
    def __init__(self):
        self._total = 0.0
        
    @dispatch(Book)
    def visit(self, book: Book):
        self._total += book.getPrice()
        
    @dispatch(Fruit)
    def visit(self, fruit: Fruit):
        self._total += fruit.getPricePerKg() * fruit.getWeight()
        
    def getTotal(self):
        return self._total