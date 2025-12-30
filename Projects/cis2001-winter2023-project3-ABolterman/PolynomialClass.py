class Polynomial:

    class TermNode:
        def __init__(self, coefficient, exponent, next=None):
            self._exp = exponent
            self._coeff = coefficient
            self._next = next

        def __eq__(self, other):
            if other == None or self == None:
                return False
            return self._exp == other._exp and self._coeff == other._coeff

        def __ne__(self, other):
            if other == None or self == None:
                return True
            return not self._exp == other._exp and self._coeff == other._coeff

    def __init__(self, coefficient, exponent):
        self._first_node = self.TermNode(coefficient, exponent)

    def __add__(self, other):
        return_poly = Polynomial(None, None)

        # Makes return_poly a copy of self
        current_node = self._first_node
        while current_node != None:
            return_poly_last = return_poly.find_last_node()
            return_poly_last._next = self.TermNode(current_node._coeff, current_node._exp)
            current_node = current_node._next

        # Goes through each term of other, compares to each term of return.
        # If exponents equal, ads coefficients. Else adds to end
        node_other = other._first_node
        node_rp = return_poly._first_node
        while node_other is not None:
            found = False
            node_rp_prev = None
            while node_rp is not None:
                if node_other._exp == node_rp._exp:
                    if node_rp_prev == None:
                        return_poly._first_node = self.TermNode(node_rp._coeff + node_other._coeff, node_other._exp, node_rp)
                    else:
                        node_rp_prev._next = self.TermNode(node_rp._coeff + node_other._coeff, node_other._exp, node_rp._next)
                    found = True
                node_rp_prev = node_rp
                node_rp = node_rp._next
            if not found:
                return_poly_last = return_poly.find_last_node()
                return_poly_last._next = self.TermNode(node_other._coeff, node_other._exp)
            node_other = node_other._next
            node_rp = return_poly._first_node

        return_poly._first_node = return_poly._first_node._next
        return_poly = return_poly._reorder()
        return return_poly

    def __mul__(self, other):
        return_poly = Polynomial(None, None)
        node_other = other._first_node
        node_self = self._first_node
        while node_other is not None:
            while node_self is not None:
                coef_product = node_self._coeff * node_other._coeff
                exp_sum = node_self._exp + node_other._exp

                # Goes through return_poly to look for same exp & adds
                current_node = return_poly._first_node
                previous_node = None
                found = False
                while current_node != None:
                    if exp_sum == current_node._exp:
                        found = True
                        current_node = self.TermNode(current_node._coeff + coef_product, exp_sum, current_node._next)
                        if previous_node != None:
                            previous_node._next = current_node
                    previous_node = current_node
                    current_node = current_node._next
                # If no equal exp found, adds to end
                if not found:
                    return_poly_last = return_poly.find_last_node()
                    return_poly_last._next = return_poly.TermNode(coef_product, exp_sum)
                node_self = node_self._next
            node_other = node_other._next
            node_self = self._first_node

        return_poly._first_node = return_poly._first_node._next
        return_poly = return_poly._reorder()
        return return_poly

    def differentiate(self):
        return_poly = Polynomial(None, None)
        return_poly_last = return_poly._first_node
        current_node = self._first_node
        while current_node != None:
            if current_node._exp != 0:
                return_poly_last._next = self.TermNode(current_node._exp * current_node._coeff, current_node._exp-1)
                return_poly_last = return_poly_last._next
            current_node = current_node._next
        return_poly._first_node = return_poly._first_node._next
        return return_poly

    def integrate(self):
        return_poly = Polynomial(None, None)
        return_poly_last = return_poly._first_node
        current_node = self._first_node
        while current_node != None:
            return_poly_last._next = self.TermNode(current_node._coeff / (current_node._exp +1), current_node._exp + 1)
            return_poly_last = return_poly_last._next
            current_node = current_node._next
        return_poly._first_node = return_poly._first_node._next
        return return_poly

    def __str__(self):
        return_string = ""
        current_node = self._first_node
        while current_node != None:
            if current_node._exp == 0:
                string = f"{current_node._coeff:.2f} + "
            else:
                string = f"{current_node._coeff:.2f}x^{current_node._exp} + "
            return_string = return_string + string
            current_node = current_node._next
        return return_string[0:-2]

    def __eq__(self, other):
        node_other = other._first_node
        node_self = self._first_node
        while node_other != None or node_self != None:
            if node_other.ne(node_self):
                return False
            node_self = node_self._next
            node_other = node_other._next
        return True

    def __ne__(self, other):
        node_other = other._first_node
        node_self = self._first_node
        while node_other != None or node_self != None:
            if node_other.eq(node_self):
                return False
            node_self = node_self._next
            node_other = node_other._next
        return True

    def _reorder(self):
        return_poly = Polynomial(self._first_node._coeff, self._first_node._exp)
        return_poly_last = return_poly._first_node
        current_self_node = self._first_node._next
        while current_self_node != None:
            prev_rp_node = None
            current_rp_node = return_poly._first_node
            found = False
            while current_rp_node != None:
                if current_self_node._exp > current_rp_node._exp:
                    if prev_rp_node != None:
                        prev_rp_node._next = self.TermNode(current_self_node._coeff, current_self_node._exp, current_rp_node)
                    else:
                        return_poly._first_node = self.TermNode(current_self_node._coeff, current_self_node._exp, current_rp_node)
                    found = True
                    break
                prev_rp_node = current_rp_node
                current_rp_node = current_rp_node._next
            if not found:
                return_poly_last._next = self.TermNode(current_self_node._coeff, current_self_node._exp)
                return_poly_last = return_poly_last._next
            current_self_node = current_self_node._next
        return return_poly

    def find_last_node(self):
        current_node = self._first_node
        while current_node._next != None:
            current_node = current_node._next
        return current_node
