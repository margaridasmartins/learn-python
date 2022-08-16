""" Comando If

@see: https://docs.python.org/3/tutorial/controlflow.html

Os blocos if else premitem executar código só se se verificar determinada condição
Podem existir zero or mais partes elif, e a parte else é opcional. A palavra ‘elif’ é uma abreviação
de ‘else if’ (ou se).

"""


def test_if_statement():
    """Comando If"""

    numero = 15
    conclusao = ''

    if numero < 0: 
        conclusao = 'Number is less than zero' # este codigo so será executado se o numero for menor que 0
    elif numero == 0:
        conclusao = 'Number equals to zero' # este codigo so será executado se o numero for igual a 0
    elif numero < 1:
        conclusao = 'Number is greater than zero but less than one' # este codigo so será executado se o numero for menor que 1 e maior que 0
    else:
        conclusao = 'Number bigger than or equal to one' # este codigo so será executado se nenhuma das condições acima se verificou (ou seja numero >= 1)

    assert conclusao == 'Number bigger than or equal to one'
