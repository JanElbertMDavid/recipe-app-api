# Sample tests

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    # Test calc module

    def test_add_numbers(self):
        # Test add numbers together
        res = calc.add(5, 6)

        self.assertEquals(res, 11)

    def test_subtract_numbers(self):
        # Subtract numbers

        res = calc.subtract(10, 15)

        self.assertEquals(res, 5)
