import pytest
import unittest
import leapyearWOE

def pytest():
    #pytest test
    s = input("Give me good input for 4 case: ")
    assert leapyearWOE.again(int(s)) == True
    s = input("Give me bad input for 4 case: ")
    assert leapyearWOE.again(int(s)) == False
    s = input("Give me bad input for 100: ")
    assert leapyearWOE.again(int(s)) == False
    s = input("Give me good input for 400: ")
    assert leapyearWOE.again(int(s)) == True
    s = input("Give me bad input for 400: ")
    assert leapyearWOE.again(int(s)) == False

print("----------PYTEST----------")
pytest()
print("----------END TEST--------")