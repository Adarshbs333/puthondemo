import pytest
from wallet import wallet,InsufficientAmount
def test_defaul_initial_amount():
    wallet=wallet()
    assert wallet.bal==0
def test_setting_initial_amount():
    wallet=wallet(100)
    assert wallet.bal==100

def test_wallet_add_amount():
    wallet=wallet(100)
    wallet.add_cash(10)
    assert wallet.bal==110