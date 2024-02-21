#!/usr/bin/env python

import unittest
import math
from calc import root, factorial, log, power

class TestCase(unittest.TestCase):
    def test_root(self):
        data=16
        result=root(data)
        self.assertEqual(result,4)

    def test_factorial(self):
        data=5
        result=factorial(data)
        self.assertEqual(result,120)
        self.assertRaises(ValueError, root, -1)

    def test_log(self):
        self.assertAlmostEqual(log(math.e),1)
        self.assertRaises(ValueError, log, 0)
        self.assertRaises(ValueError, log, -1)

    def test_power(self):
        result=power(2,3)
        self.assertEqual(result,8)
        self.assertEqual(power(2,-1), 0.5)
        self.assertEqual(power(2,0),1)

if __name__=="__main__":
    unittest.main()
