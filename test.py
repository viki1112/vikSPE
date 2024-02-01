#!/usr/bin/env python

import unittest

from prog import summation

class Testsum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add 2 nos.
        """
        data = [23,33]
        result = summation(data)
        self.assertEqual(result, 55)

if __name__ == "__main__":
    unittest.main()
