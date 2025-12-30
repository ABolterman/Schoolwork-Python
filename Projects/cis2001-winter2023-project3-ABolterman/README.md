Your task is to write the implementation for a class of polynomial operations. 

You will write the code for: addition, multiplication , differentiation and integration of polynomials. 

The polynomials will be links of TermNodes


class TermNode

 exponent : int
 
coefficient : float

 next : TermNode

 __eq__(other: TermNode) : bool

 __ne__(other: TermNode) : bool


class Polynomial

 _first_node : TermNode 

__init__( coefficient, exponent ) 

 __add__ (Polynomial) : Polynomial 

 __mul__(Polynomial) : Polynomial

 differentiate() : Polynomial

 integrate() : Polynomial #(with 0 as the constant) 

__str__ : string # in descending exponential order - clean up anything x^0 

- coefficient to 2 decimal places 

__eq__(other: Polynomial ) : bool

__ne__(other: Polynomial ) : bool

 
remember - the originals don't change, you create a new polynomial result



TermNode class: 3 Points

Polynomial __add__: 3 Points

Polynomial __mul__: 3 Points

Polynomial differentiate: 3 Points

Polynomial integrate: 3 Points

Polynomial __str__: 3 Points

Polynomial __eq__ and __ne__: 3 Points