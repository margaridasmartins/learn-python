""" Variáveis

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_variables.asp
@see: https://www.learnpython.org/en/Variables_and_Types

O Python é completamente orientado a objetosd, e não "estaticamente escrito".
Não é preciso declarar variaveis antes de as usar, ou declarar o seu tipo. 
Cada variável no Python é um objeto.

Ao invés de outras linguagens de programação, o Python não tem nenhum commando
para declarar uma variavel. A variavel é criada no momento em que lhe é atribuido  
um valor.

Uma variável pode ter um nome pequeno (como x ou y) ou um nome mais descritivo do
seu propósito (idade, nomeCarro, total_volume).

Regras para variaveis Python:
- O nome de uma variavel tem de começar com uma letra ou o caracter "_" .
- O nome de uma variavel não pode começar com um numero.
- O nome de uma variavel apenas pode conter caracteres alfa numericos e underscores (A-z, 0-9, e _ ).
- Os nomes das variaveis são "case-sensitive" (idade, Idade e IDADE são três diferentes variaveis).
"""


def test_variables():
    """Testar variaveis"""

    integer_variable = 5 # Um integer é um tipo de dados que corresponde a numeros inteiros

    string_variable = 'John' # Uma String é um tipo de dados que corresponde a texto

    boolean_variable = True # Um boolean é um tipo de dados que representa o verdadeiro (True) ou falso (False)

    none_variable = None # O None é um tipo de dados que indica uma ausencia de valor

    # os comandos "assert <condição>" vão ser corridos pelo pytest que só passara caso a condição
    # sejá positiva (True) 

    assert integer_variable == 5
    assert string_variable == 'John'
    #assert boolean_variable == 0 # Altera o valor à esquerda de forma a que o teste passe. Existem duas formas diferentes de fazer consegues descobrir as duas?

    variable_with_changed_type = 4  # a variavel é do tipo int (Integer)
    variable_with_changed_type = 'Sally'  # agora a variavel é do tipo str (String)

    assert variable_with_changed_type == 'Sally'
    #assert variable_with_changed_type == none_variable # atribui um novo valor a uma das variaveis existentes de forma a passar o teste

    # uma forma de perceber o valor de uma variavel é imprimindo-a no terminal através do comando "print"
    # NOTA: corre o comando python3 test_variables.p, pois correr o pytest não imprime o print no terminal
    print("Posso imprimir variaveis inteiras ", integer_variable)

    # experimenta declarar uma variavel à escolha e imprime-a no terminal!


    
test_variables()