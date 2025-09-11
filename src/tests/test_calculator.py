"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

import math
from calculator import Calculator


def test_app():
    my_calculator = Calculator()
    assert(my_calculator.last_result == 0)
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

def test_addition():
    my_calculator = Calculator()

    assert my_calculator.addition(2, 3) == 5
    assert my_calculator.addition(-2, 2) == 0
    assert my_calculator.addition(2.1, 3.4) == 5.5

def test_substraction():
    my_calculator = Calculator()

    assert my_calculator.subtraction(7, 2) == 5
    assert my_calculator.subtraction(-2, 2) == -4
    assert math.isclose(my_calculator.subtraction(2.1, 3.4), -1.3, rel_tol=1e-9)

def test_multiplication():
    my_calculator = Calculator()

    assert my_calculator.multiplication(7, 2) == 14
    assert my_calculator.multiplication(-2, 2) == -4
    assert my_calculator.multiplication(2.5, 2) == 5.0

def division():
    my_calculator = Calculator()

    assert my_calculator.multiplication(9, 3) == 3
    assert my_calculator.multiplication(-2, 2) == -1
    assert my_calculator.multiplication(5, 2) == 2.5
    assert my_calculator.multiplication(5, 0) == "Erreur : division par zéro"

