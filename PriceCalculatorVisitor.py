from ShoppingCartVisitor import ShoppingCartVisitor
from multipledispatch import dispatch

class PriceCalculatorVisitor(ShoppingCartVisitor):
    def __init__(self):
        self._total = 0.0
        
    @dispatch(Book)
    def visit(self, book: Book):
        self._total += book.get_price()
        
    @dispatch(Fruit)
    def visit(self, fruit: Fruit):
        self._total += fruit.get_price_per_kg() * fruit.get_weight()
        
    def getTotal(self):
        return self._total