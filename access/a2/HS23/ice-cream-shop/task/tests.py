from unittest import TestCase
import script

class PublicTestSuite(TestCase):

    def test_example(self):
        actual = script.get_price(0.70, 1.00, 1.10, 1, 3)
        expected = 4.8
        self.assertAlmostEqual(expected, actual, 5)

