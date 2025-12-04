from multipledispatch import dispatch

class ShoppingCartVisitor:
    @dispatch(Book)
    def visit(self, book: Book):
        pass
    
    @dispatch(Fruit)
    def visit(self, fruit: Fruit):
        pass