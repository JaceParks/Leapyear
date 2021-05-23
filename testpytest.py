import pytest
import unittest
import leapyearWOE
import sys

def pytest():
    #pytest test
    assert leapyearWOE.again(sys.argv[0]) == True
    assert leapyearWOE.again(int(sys.argv[1])) == False
    assert leapyearWOE.again(int(sys.argv[2])) == False
    assert leapyearWOE.again(int(sys.argv[3])) == True
    assert leapyearWOE.again(int(sys.argv[4])) == False

print("----------PYTEST----------")
pytest()
print("----------END TEST--------")