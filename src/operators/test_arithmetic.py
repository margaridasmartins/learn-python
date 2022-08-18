"""Operadores aritmétricos

@see: https://www.w3schools.com/python/python_operators.asp

Os operadores aritmétricos são usados com valores númericos de forma a fazer operações matematicas comuns
"""


def test_arithmetic_operators():
    """Arithmetic operators"""

    # Adição: Operador + .
    assert 5 + 3 == 8

    # Subtração: Operador -.
    assert 5 - 3 == 2

    # Multiplicação: Operador *.
    assert 5 * 3 == 15
    assert isinstance(5 * 3, int) # Quando multiplicamos dois inteiros o resultado é sempre inteiro

    # Divisão.
    # O resultado da divisão é sempre um numero decimal (float).
    assert 5 / 3 == 1.6666666666666667
    assert 8 / 4 == 2
    assert isinstance(5 / 3, float)
    assert isinstance(8 / 4, float)

    # Modulo.
    # O modulo é o resto da divisão inteira
    assert 5 % 3 == 2 # 5 = 3*1 + 2

    # Potencia.
    # x ** y significa x elevado a y
    assert 5 ** 3 == 125
    assert 2 ** 3 == 8
    assert 2 ** 4 == 16
    assert 2 ** 5 == 32
    assert isinstance(5 ** 3, int)

    # Divisão inteira.
    # O resultado é a divisão do numero arredondada às unidades para baixo
    assert 5 // 3 == 1 # 5 / 3 ~= 1.67 e floor(1.67) == 1
    assert 6 // 3 == 2
    assert 7 // 3 == 2
    assert 9 // 3 == 3
    assert isinstance(5 // 3, int)

    # O Python respeita a ordem das operações sendo que também se pode usar parenteses curvos 
    # Altera os seguintes testes de forma a que estes passem
    assert 15//4 + 12%7 == None
    assert 3 ** 2 * (1/2 + 3/2) == None # O valor resultante será do tipo int ou float? (Podes verificar imprimindo o resultado, se tiver uma virgula é float caso contrario é int)


    # O Python permite adicionar e multiplicar strings
    assert "ba" + "na"*2 == "banana"