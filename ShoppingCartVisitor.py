from multipledispatch import dispatch
from Book import Book
from Fruit import Fruit

class ShoppingCartVisitor:
    @dispatch(Book)
    def visit(self, book: Book):
        pass

    @dispatch(Fruit)
    def visit(self, fruit: Fruit):
        pass