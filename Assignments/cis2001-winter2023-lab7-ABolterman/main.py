from LessThanPriorityQueue import LeastPriorityQueue
from CartClass import Cart

Checkout = LeastPriorityQueue()
for shopper in range(30):
    cart = Cart(shopper)
    Checkout.add(cart)

Checkout.__repr__()
