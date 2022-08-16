"""Operadores Logicos

@see: https://www.w3schools.com/python/python_operators.asp

Operadores Logicos são usados de forma a combinar condições.
"""


def test_logical_operators():
    """Operadores Lógicos"""

    primeiro_numero = 5
    segundo_numero = 10

    # Operador and (e), não confundir com operador binário &
    # Retorna True (verdadeiro) se ambas as condições são verdadeiras.
    assert primeiro_numero > 0 and segundo_numero < 20

    # Operador or (ou), não confundir com operador binário |
    # Returns True se pelo menos uma das condições é verdadeira.
    assert primeiro_numero > 5 or segundo_numero < 20

    # Operador not (não), não confundir com operador binário ~
    # Inverte o resultado retorna False se True e True se False.
    # pylint: disable=unneeded-not
    assert not primeiro_numero == segundo_numero
    assert primeiro_numero != segundo_numero
