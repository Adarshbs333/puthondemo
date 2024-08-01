import pytest
def capital_case(x):
    if not isinstance(x,str):
        raise TypeError("enter a string")
    return x.capitalize()

def test_capital_case():
    assert capital_case("Python training")=="Python training"
