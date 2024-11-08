import pytest
from bank import Account

def test_initial_balance():
    '''
    Testing initial balance as well as owner name is correct upon creating a new instance of the Account class
    '''
    account = Account("Kobe Pane", 1000.0)
    assert account.owner == "Kobe Pane"
    assert account.balance == 1000.0

def test_deposit():
    account = Account("Kobe Pane", 1000.0)
    account.deposit(550.0)
    assert account.balance == 1550.0

def test_withdraw():
    account = Account("Kobe Pane", 1000.0)
    account.withdraw(999.0)
    assert account.balance == 1.0