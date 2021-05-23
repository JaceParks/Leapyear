import unittest
import leapyearWOE

class testcalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(leapyearWE.again(4),True)
        self.assertEqual(leapyearWE.again(5),False)
        self.assertEqual(leapyearWE.again(100),True)
        self.assertEqual(leapyearWE.again(103),False)
        self.assertEqual(leapyearWE.again(400),True)
        self.assertEqual(leapyearWE.again(10001),False)

if __name__ == "__main__":
    unittest.main()