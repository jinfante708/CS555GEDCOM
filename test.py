import unittest
import Parser as Parser
from US02 import US02
from US03 import US03
from US04 import US04
from US06 import US06
from US07 import US07
from US11 import US11
from US13 import US13
from US14 import US14
from US18 import US18
from US16 import US16
from US17 import US17
from US21 import US21
from US22 import US22
from US10 import US10
from US12 import US12
from US29 import US29
from US15 import US15
from US19 import US19
from US05 import US05
from US08 import US08
from US35 import US35
from US30 import US30
from US31 import US31
from US36 import US36
from US37 import US37
from US01 import US01
from US09 import US09
from US28 import US28
from US38 import US38
from US33 import US33
from US34 import US34

class TestAllUserStories(unittest.TestCase):
    def test_US02(self):
        self.assertEqual(US02('@F3@'), True)

    def test_US03(self):
        self.assertEqual(US03('@I11@'), True)

    def test_US04(self):
        self.assertEqual(US04('@F2@'), True)

    def test_US06(self):
        self.assertEqual(US06('@F2@'), True)

    def test_US07(self):
        self.assertEqual(US07('@I8@'), True)

    def test_US11(self):
        self.assertEqual(US11('@I13@'), True)

    def test_US16(self):
        self.assertEqual(US16('@F1@'), True)

    def test_US17(self):
        self.assertEqual(US17('@F6@'), True)

    def test_US21(self):
        self.assertEqual(US21('@F1@'), True)
    
    def test_US10(self):
        self.assertEqual(US10('@F2@'), True)

    def test_US12(self):
        self.assertEqual(US12('@F3@'), True)

    def test_US22(self):
        self.assertEqual(US22(), False)

    def test_US13(self):
        self.assertEqual(US13('@F2@'), True)
    
    def test_US18(self):
        self.assertEqual(US18('@I28@'), True)

    def test_US14(self):
        self.assertEqual(US14('@F8@'), True)

    def test_US15(self):
        self.assertEqual(US15('@F10@'), True)

    def test_US19(self):
        self.assertEqual(US19('@F13@'), True)

    def test_US29(self):
        self.assertEqual(len(US29()), 8)

    def test_US05(self):
        self.assertEqual(US05('@F6@'), True)

    def test_US08(self):
        self.assertEqual(US08('@F5@'), True)
        
    def test_US35(self):
    	self.assertEqual(len(US35()), 1)
    
    def test_US30(self):
        self.assertEqual(len(US30()), 15)
    
    def test_US31(self):
        self.assertEqual(len(US31()), 36)

    def test_US36(self):
        self.assertEqual(len(US36()), 1)

    def test_US37(self):
        self.assertEqual(len(US37()), 17)
    
    def test_US01(self):
        self.assertEqual(US01('@F11@'), True)

    def test_US09(self):
        self.assertEqual(US09('@F2@'), True)

    def test_US28(self):
        self.assertEqual(US28('@F1@'), ['@I5@', '@I4@', '@I1@'])

    def test_US38(self):
        self.assertEqual(len(US38()), 5)

    def test_US33(self):
        self.assertEqual(len(US33()), 3)

    def test_US34(self):
        self.assertEqual(len(US34()), 4)

if __name__ == '__main__':
	unittest.main()