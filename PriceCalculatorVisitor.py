from ShoppingCartVisitor import ShoppingCartVisitor
from multipledispatch import dispatch

class PriceCalculatorVisitor(ShoppingCartVisitor):
    def __init__(self):
        self._total = 0.0
        
    @dispatch(Book)
        def visit(self, book: Book):
            pass