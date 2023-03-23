import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_positive_multiply(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_positive_division(self):
        assert self.calc.division(self, 9, 3) == 3

    def test_positive_subtraction(self):
        assert self.calc.subtraction(self, 5, 2) == 3

    def test_positive_adding(self):
        assert self.calc.adding(self, 1, 1) == 2

    def teardown(self):
        print('Выполнение метода Teardown')