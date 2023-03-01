import math


class Rational:
    """
    Een klasse van rationale getallen met een teller en een noemer
        - teller en noemer zijn gehele getallen
        - noemer is steeds positief
    """

    def is_rational(rational):
        """
          Check whether the given rational is a well-formed
          rational number.
        """

        return \
            isinstance(rational, tuple) and \
            (len(rational) == 2) and \
            isinstance(rational[0], int) and \
            isinstance(rational[1], int) and \
            (rational[1] > 0)

    # aanpassen to contructor
    def __init__(self, numerator = 1, denominator = 1):
        """
          Return a rational number involving the given
          numerator and denominator.
          - The given numerator and denominator must be integer
            numbers.
          - The denominator may not be zero.
        """

        if denominator < 0:
            numerator = - numerator
            denominator = - denominator
        self.__numerator = numerator
        self.__denominator = denominator

    def get_numerator(self):
        return self.__numerator

    def get_denominator(self):
        return self.__denominator

    def times(self, factor):
        """
          Return a rational number that is the product of the
          given rational number with the given factor.
        """



    # functie herschreven tot methode
    def simplify(self):
        """
          Return a rational number that is the simplified
          version of the given rational number.
        """

        common_fact = math.gcd(self.__numerator, self.__denominator)
        # result = Rational()
        #         # result.numerator = self.numerator / common_fact
        #         # result.denominator = self.denominator / common_fact
        return Rational(
                self.__numerator // common_fact,
                self.__denominator // common_fact)

    def have_same_values(self,other):
        """
          Check whether the given rational numbers have the
          same value.
        """

        return self.simplify() == other.Simplify()

    def less_than_or_equal(left, right):
        """
          Check whether the left rational number is less than
          or equal to the right rational number.
        """

        return left[0] * right[1] <= left[1] * right[0]

    # aangepast
    def get_value(self):
        """
          Return the value of the given rational number as a
          floating-point value.
        """

        return float(self.__numerator) / self.__denominator

    def is_normalised(self):
        self.__is_normalised = self.simplify().__denominator == 1
        return self.__is_normalised

    def __str__(self):
        return '[' + str(self.get_numerator()) + ',' + str(self.get_denominator()) + ']'

    def __eq__(self, other):
        if not isinstance(other,Rational):
            return False
        return (self.simplify().get_numerator() == other.simplify().get_numerator()) and \
               (self.simplify().get_denominator() == other.simplify().get_denominator())

    def __add__(self, other):
        numerator = self.get_numerator() * other.get_denominator() + self.get_denominator() * other.get_numerator()
        denominator = self.get_denominator() * other.get_denominator()

        return Rational(numerator,denominator)

    def __mul__(self, other):
        if isinstance(other,Rational):
            numerator = self.__numerator * other.__numerator
            denominator = self.__denominator * other.__denominator
            return Rational(numerator,denominator)
        elif isinstance(other,int):
            return Rational(self.__numerator * other,self.__denominator)

    def __rmul__(self, other):
        if isinstance(other,int):
            return Rational(self.__numerator * other,self.__denominator)

    def __lt__(self, other):
        if not isinstance(other,Rational):
            return False
        return (self.simplify().__numerator/self.simplify().__denominator) < (other.simplify().__numerator/other.simplify().__denominator)

    def __le__(self, other):
        if not isinstance(other,Rational):
            return False
        return (self == other) or (self < other)






# # Some small experiments with rational numbers.
#
# sum = add((4, 5), (30, 75))
# assert simplify(sum) == simplify((4 * 75 + 5 * 30, 5 * 75))
# assert have_same_values((3, 4), (21, 28))
# assert less_than_or_equal((30, 75), (4, 5))
# assert get_value((4, 5)) == 0.8
#
# ### Checking is_rational
# assert is_rational((3, 4))
# assert not is_rational([3, 4])
# assert not is_rational((3, 4, 5))
# assert not is_rational((3.0, 4))
# assert not is_rational((3, 4.0))
# assert not is_rational((3, 0))
#
# ### Checking make_rational
# assert make_rational(4, 12) == (4, 12)
# assert make_rational(4, -12) == (-4, 12)
#
# ### Checking add
#assert add((2, 5), (4, 7)) == (34, 35)
assert Rational(2,5) + Rational(4,7) == Rational(34,35)
#
# ### Checking times
# assert times((2, 5), 3) == (6, 5)
#
### Checking simplify
# assert simplify((14, 35)) == (2, 5)
# assert simplify((-14, 35)) == (-2, 5)
# assert simplify((0, 7)) == (0, 1)
#     rat = Rational()
#     rat.numerator = 14
#     rat.denominator = 35
rat = Rational(14, 35)
simple_rat = rat.simplify()
simple_rat = Rational.simplify(rat)
assert simple_rat.get_numerator() == 2
assert simple_rat.get_denominator() == 5
# rat = Rational()
# rat.numerator = -14
# rat.denominator = 35
# assert simplify(rat) == (-2, 5)
# rat = Rational()
# rat.numerator = 0
# rat.denominator = 7
# assert simplify(rat) == (0, 1)
# #
# ### Checking have_same_values
# assert have_same_values((2, 4), (3, 6))
# assert not have_same_values((2, 4), (4, 6))
#
# ### Checking less_than_or_equal
# assert less_than_or_equal((1, 4), (7, 27))
# assert less_than_or_equal((2, 4), (3, 6))
# assert not less_than_or_equal((8, 95), (1, 12))
#
### Checking get_value
# assert get_value((2, 5)) == 0.4
#     rat = Rational()
#     rat.numerator = 2
#     rat.denominator = 5
# rat = Rational(2, 5)
# assert rat.get_value() == 0.4
# assert Rational.get_value(rat) == 0.4

# public vs private
# rat._Rational__denominator = 0
#rat.__denominator = 0
#print(rat.get_value())
x1 = Rational(2,4)
x2 = Rational(8,8)
print(Rational.simplify(x1 + x2))

print(x1*x2)
print(x2*x1)
print(x1*4)
print(Rational.simplify(4*x1))

print(x1<=x2)
print(x2<=x1)
print(x1>=x2)
print(x2>=x1)

print(x1,x2)

print(x2.is_normalised())
print(x1.is_normalised())
print(x2)
print(x2.simplify())
print(x2)