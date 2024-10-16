"""

@Author: Naveen Madev Naik
@Date: 2024-08-16
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-08-16
@Title: Python program to validate first name of user

"""

import pytest
from user_registration import validate_firstName


def test_validate_firstName():
        
    """
    Description:
        Checks if the name is valid according to the validation rule.

    Parameter:
        None

    Return:
        None
    """
        
    assert validate_firstName("Naveen") is not None
    assert validate_firstName("Girish") is not None
    assert validate_firstName("Ho") is None  
    assert validate_firstName("Mi") is None 
