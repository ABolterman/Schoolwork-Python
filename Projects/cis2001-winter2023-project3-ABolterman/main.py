from PolynomialClass import Polynomial


poly2 = Polynomial(2,3) # makes the polynomial 2.00x^3
poly3 = Polynomial(3,4) # makes the polynomial 3.00x^4
poly7 = Polynomial(4,5)

poly1 = poly2 + poly3 # makes poly1 = 3.00x^4 + 2.00x^3
poly6 = poly7 + poly2 # mekes poly6 = 4x^5 + 2x^3
print(poly1) # prints out 3.0x^4 + 2.00x^3
print(poly6)
print(poly6 + poly1)

poly3 = poly1*poly2 # sets poly3 to 6.00x^7+4.00x^6
print(poly3)

poly4 = poly3.differentiate() # sets poly4 to 42.00x^6+24.00x^5
print(poly4)

poly5 = poly1.integrate() # sets poly5 to .60x^5+.50x^4
print(poly5)

poly8 = Polynomial(5.389, 0)
print(poly8 + poly1)

