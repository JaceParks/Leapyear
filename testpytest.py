import pytest
import unittest
import leapyearWOE

def pytest():
    #pytest test
    s = input("Give me good input: ")
    assert again(s) == True
    s = input("Give me bad input: ")
    assert again(s) == False
    s = input("Give me good input: ")
    assert again(s) == True
    s = input("Give me bad input: ")
    assert again(s) == False
    s = input("Give me bad input: ")
    assert again(s) == False

print("----------PYTEST----------")
pytest()
print("----------END TEST--------")