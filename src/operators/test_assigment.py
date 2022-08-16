"""Operadores de atribuição

@see: https://www.w3schools.com/python/python_operators.asp

Os operadores de atribuição são usados para atribuir valores a variaveis
"""


def test_assignment_operator():
    """Operador de atribuição """

    # Atribuição: Operador =
    number = 5
    assert number == 5

    # Atribuição multipla.
    # às variaveis primeira e segunda são atribuidos simultaneamente os valores 0 e 1.
    primeira, segunda = 0, 1
    assert primeira == 0
    assert segunda == 1

    # É possivel da mesma forma trocar os valores das variaveis.
    primeira, segunda = segunda, primeira
    assert primeira == 1
    assert segunda == 0


def test_augmented_assignment_operators():
    """Operador de atribuição combinado com operadores aritmetricos e binarios"""

    # Operador: +=
    # x += y é o mesmo que x = x + y
    number = 5
    number += 3
    assert number == 8

    # Operador: -=
    # x -= y é o mesmo que x = x - y
    number = 5
    number -= 3
    assert number == 2

    # Operador: *=
    # x *= y é o mesmo que x = x * y
    number = 5
    number *= 3
    assert number == 15

    # Operador: /=
    # x /= y é o mesmo que x = x / y
    number = 8
    number /= 4
    assert number == 2

    # Operador: %=
    # x %= y é o mesmo que x = x % y
    number = 8
    number %= 3
    assert number == 2

    # Operador: %=
    number = 5
    number %= 3
    assert number == 2 

    # Operador: //=
    # x //= y é o mesmo que x = x // y
    number = 5
    number //= 3
    assert number == 1

    # Operador: **=
    # x **= y é o mesmo que x = x ** y
    number = 5
    number **= 3
    assert number == 125

    # Operador: &=
    # x &= y é o mesmo que x = x & y
    number = 5  # 0b0101
    number &= 3  # 0b0011
    assert number == 1  # 0b0001

    # Operador: |=
    # x |= y é o mesmo que x = x | y
    number = 5  # 0b0101
    number |= 3  # 0b0011
    assert number == 7  # 0b0111

    # Operador: ^=
    # x ^= y é o mesmo que x = x ^ y
    number = 5  # 0b0101
    number ^= 3  # 0b0011
    assert number == 6  # 0b0110

    # Operador: >>=
    # x >>= y é o mesmo que x = x >> y
    number = 5
    number >>= 3
    assert number == 0  # (((5 // 2) // 2) // 2)

    # Operador: <<=
    # x <<= y é o mesmo que x = x << y
    number = 5
    number <<= 3
    assert number == 40  # 5 * 2 * 2 * 2
