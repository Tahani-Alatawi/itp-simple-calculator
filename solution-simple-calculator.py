
def test_add(a,b):
    results = a+b
    return results


def test_subtract(a,b):
    results =a-b
    return results


def test_multiply(a,b):
    results = a*b
    return results

def test_divide(a,b):
    if b==0 :
      return "Invalid value for denominator, cant't divide by 0!"
    results = a/b
    return results

def test_squar(a):
    results=a*a
    return results

def test_power(a,b):
    results=a**b
    return results

from math import sqrt
def test_sqrt(a):
    if a <0:
        return"Invalid Value"
    results= sqrt(a)
    return results