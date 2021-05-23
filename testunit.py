import unittest
import leapyearWOE

class testcalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(leapyearWOE.again(4),True)
        self.assertEqual(leapyearWOE.again(5),False)
        self.assertEqual(leapyearWOE.again(103),False)
        self.assertEqual(leapyearWOE.again(400),True)
        self.assertEqual(leapyearWOE.again(10001),False)

if __name__ == "__main__":
    unittest.main()