"""

@Author: Naveen Madev Naik
@Date: 2024-08-16
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-08-16
@Title: Python program to validate first name,last name and email of user by unit testing

"""
        
import pytest
from user_registration import validate_name, validate_email

def test_validate_first_name():

    """
    Description:
        Checks if the first is valid according to the validation rule.

    Parameter:
        None

    Return:
        None
    """


    assert validate_name("Naveen") is not None
    assert validate_name("Girish") is not None
    assert validate_name("auhsh") is None
    assert validate_name("sja") is None


def test_validate_last_name():

    """
    Description:
        Checks if the last is valid according to the validation rule.

    Parameter:
        None

    Return:
        None
    """


    assert validate_name("Naik") is not None
    assert validate_name("Nekar") is not None
    assert validate_name("hjdj") is None
    assert validate_name("isdh") is None


def test_validate_email():

    """
    Description:
        Checks if email is valid according to the validation rule.

    Parameter:
        None

    Return:
        None
    """

    assert validate_email("abc.xyz@bl.co.in") is not None
    assert validate_email("naveen@domain.co") is not None
    assert validate_email("naveen@blco") is None
    assert validate_email("naveec@bl.co.in.") is None
