"""Operadores de comparação

@see: https://www.w3schools.com/python/python_operators.asp

Os operadores de comparação são usados para comparar dois valores.
"""


def test_comparison_operators():
    """Comparison operators"""

    # É Igual.
    # Atribuição: =  Comparação: ==
    number = 5
    assert number == 5

    # Não é igual.
    number = 5
    assert number != 3

    # Maior que.
    number = 5
    assert number > 3

    # Menor que.
    number = 5
    assert number < 8

    # Maior ou igual a 
    number = 5
    assert number >= 5
    assert number >= 4

    # Menor ou igual a 
    number = 5
    assert number <= 5
    assert number <= 6
