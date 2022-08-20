"""Numeros.

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_numbers.asp

Existem três tipos de números em Python:
- int (ex 2, 4, 20)
    - bool (False e True, onde Falso também pode ser representado como 0 e True como 1)
- float (números decimais ex 5.0, 1.6)
- complex (números complexos ex 5+6j, 4-3j)
"""


def test_integer_numbers():
    """Tipo Integer

    Int, ou integer, é um número inteiro, positivo ou negativo,
    não tem casas deicimais e tem dimensão ilimitada
    """

    positive_integer = 1 
    negative_integer = -3255522
    big_integer = 35656222554887711

    assert isinstance(positive_integer, int) # ints podem ser positivos
    assert isinstance(negative_integer, int) # ints podem ser negativos
    assert isinstance(big_integer, int) # ints podem ser MUITO grandes


def test_booleans():
    """Tipo Boolean

    Booleans representam valores de verdade, verdadeiro (True) e falso (False). 
    Um boolean só pode ser ter os valores True ou False. 
    O tipo Boolean é um subtipo do tipo Integer, e os valores Boolean comportam-se como os valores 0 e 1,
    em praticamente todos os contextos, a exceção é quando convertemos o valor para string em que é retornado as 
    strings "True" e "False".
    """

    true_boolean = True
    false_boolean = False

    assert true_boolean 
    assert not false_boolean # Não Falso é verdadeiro

    assert isinstance(true_boolean, bool)
    assert isinstance(false_boolean, bool)

    # Vamos tentar converter um boolean para uma string
    assert str(true_boolean) == "True"
    assert str(false_boolean) == "False"

    # 1 representa True e 0 representa False
    assert True == 1
    assert False == 0 

def test_float_numbers():
    """Tipo Float 

    Float, ou  "numero de virgula flutuante" é um numero, positivo ou negativo,
    contendo um ou mais casas decimais.
    """

    float_number = 7.0

    # Outra maneira (pouco usada) de declara um float é usando a função float().
    float_number_via_function = float(7)
    float_negative = -35.59

    assert float_number == float_number_via_function
    assert isinstance(float_number, float)
    assert isinstance(float_number_via_function, float)
    assert isinstance(float_negative, float)

    # Os floats também podem ser numeros em notação cientifica, seguindo a seguinte notação:
    # <base>E<potencia>, ou <base>e<potencia>

    float_with_small_e = 35e3
    float_with_big_e = 12E4

    assert float_with_small_e == 35000 # 35 * 10^3
    assert float_with_big_e == 120000 # 12 * 10^4
    assert isinstance(12E4, float)
    assert isinstance(-87.7e100, float)


def test_complex_numbers():
    """Tipo complexo"""

    # o Tipo complexo tem uma parte real e outra imaginaria que é indicada por um j no final
    complex_number_1 = 5 + 6j
    complex_number_2 = 3 - 2j

    assert isinstance(complex_number_1, complex)
    assert isinstance(complex_number_2, complex)
    assert complex_number_1 * complex_number_2 == 27 + 8j


