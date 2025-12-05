from typing import List, Any
from Book import Book
from Fruit import Fruit
from ShoppingCartVisitor import ShoppingCartVisitor
from PriceCalculatorVisitor import PriceCalculatorVisitor

class ShoppingCartManagementSystem:
    def __init__(self, groceryItems: List[Any], visitor: ShoppingCartVisitor):
        self._groceryItems = groceryItems
        self._visitor = visitor
        
    def runPriceCalculations(self, visitor):
        for item in self._groceryItems:
            item.accept(self._visitor)
        return self._visitor.getTotal()
    
if __name__ == "__main__":
    items = [
        Book("12345", 29.99),
        Fruit("Apple", 3.0, 2.0),
        Book("67890", 15.99),
        Fruit("Banana", 1.5, 3.0)
    ]
    
    priceCalculator = PriceCalculatorVisitor()
    system = ShoppingCartManagementSystem(items, priceCalculator)
    total = system.runPriceCalculations(priceCalculator)
    print(f"{10*'-'}Receipt{10*'-'}")
    
    for item in items:
        if isinstance(item, Book):
            print(f"[Book] \n\tISBN: {item.getIsbnNumber()}, \n\tPrice: ${item.getPrice():.2f}")
        elif isinstance(item, Fruit):
            item_price = item.getPricePerKg() * item.getWeight()
            print(f"[Fruit] \n\t{item.getName()}, \n\tWeight: {item.getWeight()}kg, \n\tPrice per kg: ${item.getPricePerKg():.2f}, \n\tTotal Price: ${item_price:.2f}")
    print(f"Total Price: ${total:.2f}")