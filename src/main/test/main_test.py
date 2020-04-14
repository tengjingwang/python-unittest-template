import unittest
from unittest import TestCase

from .. import main


class Test_Sample(TestCase):
    def test_sample(self):
        data = [1, 2]
        expected = 3
        self.assertEqual(main.dummy_function(*data), expected)
