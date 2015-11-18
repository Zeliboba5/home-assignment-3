# -*- coding: utf-8 -*-

import unittest
from calculator import calculate
from decimal import InvalidOperation


class CalculatorTestCase(unittest.TestCase):
    def testCalculator(self):
        self.assertEquals(calculate("+", "1", "3"), "4")

    def testDecimal(self):
        self.assertEquals(calculate("-", "2.1", "1.3"), "0.8")

    def testNoneAsArg(self):
        with self.assertRaises(ValueError):
            calculate("+", None, "1")
        with self.assertRaises(ValueError):
            calculate("*", None, "4")
        with self.assertRaises(ValueError):
            calculate("/", "1", None)

    def testTextAsArg(self):
        with self.assertRaises(InvalidOperation):
            calculate("*", "dsad", "dsad")

    def testArgumentNumberError(self):
        with self.assertRaises(TypeError):
            calculate("*", "1")

    def testWrongOperation(self):
        with self.assertRaises(ValueError):
            calculate("%", "5", "5")

    def testAddIntWithFloat(self):
        self.assertEquals(calculate("+", "3", "2.2"), "5.2")

    def testAddNegative(self):
        self.assertEquals(calculate("+", "-1", "-3"), "-4")

    def testAddNegativeFloat(self):
        self.assertEquals(calculate("+", "-2.5", "1"), "-1.5")

    def testSubInt(self):
        self.assertEquals(calculate("-", "4", "2"), "2")

    def testSubIntWithFloat(self):
        self.assertEquals(calculate("-", "5", "2.4"), "2.6")

    def testSubFloat(self):
        self.assertEquals(calculate("-", "5.3", "2.2"), "3.1")

    def testSubNegativeInt(self):
        self.assertEquals(calculate("-", "-5", "-2"), "-3")

    def testSubNegativeFloat(self):
        self.assertEquals(calculate("-", "-3.1", "-1.2"), "-1.9")

    def testMulInt(self):
        self.assertEquals(calculate("*", "2", "3"), "6")

    def testMulDecimial(self):
        self.assertEquals(calculate("*", "2.4", "3.4"), "8.16")

    def testMulNegativeInt(self):
        self.assertEquals(calculate("*", "-12", "2"), "-24")

    def testMulNegativeDec(self):
        self.assertEquals(calculate("*", "-2.2", "-1"), "2.2")

    def testMulNegativeDecWithInt(self):
        self.assertEquals(calculate("*", "-2.4", "3.4"), "-8.16")

    def testDivInt(self):
        self.assertEquals(calculate("/", "4", "2"), "2")

    def testDivFloat(self):
        self.assertEquals(calculate("/", "4.2", "2"), "2.1")

    def testDivDecimalLessThenOne(self):
        self.assertEquals(calculate("/", "2.1", "0.5"), "4.2")

    def testDivNegative(self):
        self.assertEquals(calculate("/", "5", "-1"), "-5")

    def testDivZeroDiv(self):
        with self.assertRaises(ZeroDivisionError):
            calculate("/", "1", "0")

    def testFactInt(self):
        self.assertEquals(calculate("!", "4"), "24")

    def testFactFloat(self):
        with self.assertRaises(ValueError):
            calculate("!", "2.1")

    def testFactNegative(self):
        with self.assertRaises(ValueError):
            calculate("!", "-1")

    def testFactZero(self):
        self.assertEquals(calculate("!", "0"), "1")
