"""Operadores binários

@see: https://www.w3schools.com/python/python_operators.asp

Operadores binários manipulam os números ao nível dos bits 
"""


def test_bitwise_operators():
    """Operadores binários"""

    # NOTA: Nos seguintes exemplos o 0b serve para indicar que é uma representação binária.

    # AND (e)
    # O bit é um se ambos os bits forem 1.
    #
    # Example:
    # 5 = 0b0101
    # 3 = 0b0011
    assert 5 & 3 == 1  # 0b0001

    # OR (ou)
    # O bit é 1 se pelo menos um dos bits for 1.
    #
    # Example:
    # 5 = 0b0101
    # 3 = 0b0011
    assert 5 | 3 == 7  # 0b0111

    # NOT (não)
    # Invert todos os bits. (O bit mais à esquerda é reponsavel pelo sinal do numero, por isso a negação de um numero positivo será sempre um numero negativo e vice-versa à exceção do 0)
    assert ~5 == -6

    # XOR (ou exclusivo)
    # O bit é 1 apenas quando um dos bits é 1 e o outro 0.
    #
    # Example:
    # 5 = 0b0101
    # 3 = 0b0011
    number = 5  # 0b0101
    number ^= 3  # 0b0011
    assert 5 ^ 3 == 6  # 0b0110

    # Shift à direita
    # Os bits vão ser empurrados n vezes para a direita, sendo que os n bits mais à direita desaparecem.
    #
    # Example:
    # 5 = 0b0101
    assert 5 >> 1 == 2  # 0b0010, 1 shit à direita
    assert 5 >> 2 == 1  # 0b0001, 2 shifts à direita

    # Shift à esquerda 
    # Os bits movem-se para a esquerda n vezes sendo que à direita são adicionados n 0s .
    #
    # Example:
    # 5 = 0b0101
    assert 5 << 1 == 10  # 0b1010
    assert 5 << 2 == 20  # 0b10100
