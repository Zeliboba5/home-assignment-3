# -*- coding: utf-8 -*-

import unittest
from calculator import calculate 
from decimal import Decimal

class CalculatorTestCase(unittest.TestCase):
    def testCalculator(self):
    	self.assertEquals(calculate("+", 1, 3), Decimal(4))

    def testDecimial(self):
    	self.assertAlmostEquals(calculate("-", 2.1, 1.3), Decimal(0.8))

    def testArgumentNumberError(self):
    	with self.assertRaises(IndexError):
    		calculate("*", 1)

    def testWrongOperation(self):
    	with self.assertRaises(ValueError):
    		calculate("%", 5, 5)




    def testAddIntWithDecimal(self):
    	self.assertAlmostEquals(calculate("+", 3, 2.2), Decimal(5.2))

    def testAddNegative(self):
    	self.assertEquals(calculate("+", -1, -3), Decimal(-4))

    def testAddNegativeDecimal(self):
    	self.assertAlmostEquals(calculate("+", -2.5, 1), Decimal(-1.5))



    def testSubInt(self):
    	self.assertEquals(calculate("-", 4, 2), Decimal(2))

    def testSubIntWithDecimal(self):
    	self.assertAlmostEquals(calculate("-", 5, 2.4), Decimal(2.6))

    def testSubDecimal(self):
    	self.assertAlmostEquals(calculate("-", 5.3, 2.2), Decimal(3.1))

    def testSubNegativeInt(self):
    	self.assertEquals(calculate("-", -5, -2), Decimal(-3))

    def testSubNegativeDecimal(self):
    	self.assertAlmostEquals(calculate("-", -3.1, -1.2), Decimal(-1.9))



    def testMulInt(self):
    	self.assertEquals(calculate("*", 2, 3), Decimal(6))

    def testMulDecimial(self):
    	self.assertAlmostEquals(calculate("*", 2.4, 3.4), Decimal(8.16))

    def testMulNegativeInt(self):
    	self.assertEquals(calculate("*", -12, 2), Decimal(-24))

    def testMulNegativeDec(self):
    	self.assertAlmostEquals(calculate("*", -2.2, -1), Decimal(2.2))

    def testMulNegativeDecWithInt(self):
    	self.assertAlmostEquals(calculate("*", -2.4, 3.4), Decimal(-8.16))


    def testDivInt(self):
    	self.assertEquals(calculate("/", 4, 2), Decimal(2))

    def testDivDecimal(self):
    	self.assertAlmostEquals(calculate("/", 4.2, 2), Decimal(2.1))

    def testDivDecimalLessThenOne(self):
    	self.assertAlmostEquals(calculate("/", 2.1, 0.5), Decimal(4.2))

    def testDivNegative(self):
    	self.assertEquals(calculate("/", 5, -1), Decimal(-5))

    def testDivZeroDiv(self):
    	with self.assertRaises(ValueError):
    		calculate("/", 1, 0)



    def testFactInt(self):
    	self.assertEquals(calculate("!", 4), Decimal(24))

    def testFactFloat(self):
    	with self.assertRaises(ValueError):
    		calculate("!", 2.1)

    def testFactNegative(self):
    	with self.assertRaises(ValueError):
    		calculate("!", -1)

    def testFactZero(self):
    	self.assertEquals(calculate("!", 0), Decimal(1))
    	
