from __future__ import division

import logging

#Set Logging configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('rational.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Custom Exception class
class RationalError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Rational:

    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        if (numer != None and denom != None):
            self.__lowest_term__(numer, denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __valid__(self):
        return self.denom != 0 and self.numer != None and self.denom != None

    def __lowest_term__(self, p_numer, p_denom):
        numer = p_numer
        denom = p_denom

        for x in range(2, min(abs(numer), abs(denom))+1):
            while numer%x == 0 and denom%x == 0 and denom != 1 and denom != 0:
                numer = int(numer/x)
                denom = int(denom/x)

        if numer == 0: denom = 1

        if denom < 0:
            numer = numer * -1
            denom = denom * -1

        self.numer = numer
        self.denom = denom
        logger.debug("Least value = " + self.__repr__())
        
        
    def __add__(self, other):
        ''' The sum of two rational numbers `r1 = a1/b1` and `r2 = a2/b2` is r1 + r2 = a1/b1 + a2/b2 = (a1 * b2 + a2 * b1) / (b1 * b2) '''
        
        if not self.__valid__() or not other.__valid__():
            raise RationalError("Invalid Arguments passed to funtion, not valid rational number")

        rsum = Rational(None, None)
        try:
            rsum.numer = (self.numer * other.denom) + (self.denom * other.numer)
            rsum.denom = self.denom * other.denom
            rsum.__lowest_term__(rsum.numer, rsum.denom)
        except ValueError as e:
            logger.error(e)
        except Exception as e:
            logger.error(e)

        logger.info("Sum value = " + rsum.__repr__())
        return rsum

    def __sub__(self, other):
        '''The difference of two rational numbers `r1 = a1/b1` and `r2 = a2/b2` is r1 - r2 = a1/b1 - a2/b2 = (a1 * b2 - a2 * b1) / (b1 * b2) '''

        if not self.__valid__() or not other.__valid__():
            raise RationalError("Invalid Arguments passed to funtion, not valid rational number")

        rdiff = Rational(None, None)
        try:
            rdiff.numer = (self.numer * other.denom) - (self.denom * other.numer)
            rdiff.denom = self.denom * other.denom
            rdiff.__lowest_term__(rdiff.numer, rdiff.denom)
        except ValueError as e:
            logger.error(e)
        except Exception as e:
            logger.error(e)

        logger.info("Sub value = " + rdiff.__repr__())
        return rdiff

    def __mul__(self, other):
        '''The product (multiplication) of two rational numbers r1 = a1/b1` and `r2 = a2/b2` is `r1 * r2 = (a1 * a2) / (b1 * b2) '''

        if not self.__valid__() or not other.__valid__():
            raise RationalError("Invalid Arguments passed to funtion, not valid rational number")

        rprod = Rational(None, None)
        try:
            rprod.numer = self.numer *  other.numer
            rprod.denom = self.denom * other.denom
            rprod.__lowest_term__(rprod.numer, rprod.denom)
        except ValueError as e:
            logger.error(e)
        except Exception as e:
            logger.error(e)

        logger.info("Mul value = " + rprod.__repr__())
        return rprod

    def __truediv__(self, other):
        '''Dividing a rational number `r1 = a1/b1` by another `r2 = a2/b2` is `r1 / r2 = (a1 * b2) / (a2 * b1)` if `a2 * b1` is not zero '''

        if not self.__valid__() or not other.__valid__():
            raise RationalError("Invalid Arguments passed to funtion, not valid rational number")

        rdiv = Rational(None, None)
        try:
            rdiv.numer = self.numer *  other.denom
            rdiv.denom = self.denom * other.numer
            if rdiv.denom == 0:
                raise RationalError("Invalid, denominator is 0")
            rdiv.__lowest_term__(rdiv.numer, rdiv.denom)
        except ValueError as e:
            logger.error(e)
        except Exception as e:
            logger.error(e)

        logger.info("TrueDiv value = " + rdiv.__repr__())
        return rdiv

    def __abs__(self):
        '''The absolute value `|r|` of the rational number r = a/b` is equal to `|a|/|b|'''

        rabs = Rational(None, None)
        rabs.numer = abs(self.numer)
        rabs.denom = abs(self.denom)
        logger.info("Abs value = " + rabs.__repr__())
        return rabs
          
    def __pow__(self, power):
        '''Exponentiation of a rational number `r = a/b` to a non-negative integer power `n` is `r^n = (a^n)/(b^n)`
           Exponentiation of a rational number `r = a/b` to a negative integer power `n` is `r^n = (b^m)/(a^m)`, where `m = |n|`.'''

        if not self.__valid__():
            raise RationalError("Invalid Arguments passed to funtion, not valid rational number")

        rpower = Rational(None, None)
        try:
            if (power > 0):
                rpower.numer = self.numer ** power
                rpower.denom = self.denom ** power
            elif (power < 0):
                rpower.numer = self.denom ** abs(power)
                rpower.denom = self.numer ** abs(power)
            else:
                rpower.numer = 1
                rpower.denom = 1

            if rpower.denom == 0:
                raise RationalError("Invalid, denominator is 0")
            rpower.__lowest_term__(rpower.numer, rpower.denom)
        except ValueError as e:
            logger.error(e)
        except Exception as e:
            logger.error(e)

        logger.info("Power value = " + rpower.__repr__())
        return rpower

    def __rpow__(self, base):
        '''Exponentiation of a real number `x` to a rational number `r = a/b` is `x^(a/b) = root(x^a, b)`, where `root(p, q)` is the `q`th root of `p` '''
        
        if not self.__valid__():
            raise RationalError("Invalid Arguments passed to funtion, not valid rational number")

        try:
            num = base ** self.numer
            power = self.denom       
            #nth root of a is a**(1/n)
            return num**(1/power)
        except ValueError as e:
            logger.error(e)
        except Exception as e:
            logger.error(e)

        
