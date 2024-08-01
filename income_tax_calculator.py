def calculate_tax(income):
    if income <= 10000:
        tax = income * 0.10
    elif income <= 30000:
        tax = 10000 * 0.10 + (income - 10000) * 0.20
    else:
        tax = 10000 * 0.10 + 20000 * 0.20 + (income - 30000) * 0.30


    if income < 0:
        print("Income cannot be negative.")
    print(tax)

import pytest
def test_calculate_tax():
    assert calculate_tax(1000)==100
