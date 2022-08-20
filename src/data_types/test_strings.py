"""Strings.

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_strings.asp
@see: https://www.w3schools.com/python/python_ref_string.asp

O Python premite manipular strings (texto), que pode ser expressos em diferentes 
formas. As strings podem ser delimitadas em aspas simples ('<texto>') ou 
aspas duplas ("<texto>"), o resultado é o mesmo.
"""

import pytest


def test_string_type():
    """Tipo String"""

    # String com aspas duplas.
    name_1 = "John"
    # String com aspas simples.
    name_2 = 'John'

    # Strings creadas com aspas diferentes são tratadas da mesma forma.
    assert name_1 == name_2
    assert isinstance(name_1, str)
    assert isinstance(name_2, str)

    # O caracter \ pode ser usado para se escrever aspas dentro de strings.
    # Com o mesmo efeito, tambem se pode usar aspas simples dentro de aspas duplas e vice-versa
    single_quote_string = 'doesn\'t'
    double_quote_string = "doesn't"

    assert single_quote_string == double_quote_string

    # O caractere \n  significa "new line" ou seja mudar de linha.
    multiline_string = 'First line.\nSecond line.'

    # Experiementa ver a mudança de linha no python interativo correndo o comando
    print(multiline_string)

    assert multiline_string == 'First line.\nSecond line.'

    # As Strings podem ser indexadas, ou seja é possivel obter um caracter de uma string
    # sabendo a sua posição, o primeiro caracter tem sempre index(posição) 0, o segundo index 1, etc.
    # Também existem indexs negativos que começam no fim da palavra, ou seja o index -1 corresponde ao ultimo caracter da string.
    # a sintaxe para aceder um caracter é: nome_variavel[index]
    word = 'Python'
    assert word[0] == 'P'  # O primeiro character (index 0)
    assert word[5] == 'n'  # O sexto character (index 5).
    assert word[-1] == 'n'  # O ultimo caracter (index -1).
    assert word[-2] == 'o'  # O penultimo caracter (index -2).
    assert word[-6] == 'P'  # O sexto caracter a contar do fim que corresponde ao primeiro caracter.


    # Para além de poderem ser indexadas, as strings podem ser cortadas (slicing). Enquanto que o indexamento
    # é usado para obter caracteres individuais o slicing é usado para obter substrings (uma parte da string):
    assert word[0:2] == 'Py'  # Caracteres a partir da posição 0 (incluida) até 2 (excluido).
    assert word[2:5] == 'tho'  # Caracteres a partir da posição 2 (incluido) até 5 (excluido).

    # O index do inicio é sempre incluido e o fim é sempre excluido
    # Os indexs têm valores por defeito, se omitirmos o index inicial o default é 0,
    # ou seja, começa do inicio, se omitirmos o index final o default é o tamanho da string, 
    # ou seja, o ultimo caracter
    assert word[:2] + word[2:] == 'Python'
    assert word[:4] + word[4:] == 'Python'

    assert word[:2] == 'Py'  # Substring a partir do caracter inicial até à posição 2 (exclusivamente).
    assert word[4:] == 'on'  # Substring  a partir do caracter com index 4 (o quinto) até ao fim da palavra.
    assert word[-2:] == 'on'  # Substring a partir do penultimo caracter (inclusivamente) até ao fim.

    # Uma forma de relembrar como é que o slicing funciona é pensar nos indexs como
    # pontos entre caracteres, sendo 0 a posição à esquerda do primeiro caracter 
    # Assim, a posição à direita do ultimo caracter de uma string com n caracteres
    # tem index n, por exemplo:
    #
    # +---+---+---+---+---+---+
    #  | P | y | t | h | o | n |
    #  +---+---+---+---+---+---+
    #  0   1   2   3   4   5   6
    # -6  -5  -4  -3  -2  -1

    # Atenção! Tentar usar um index que é muito grande (maior que o numero de caracteres da palavra) resulta num erro.
    with pytest.raises(Exception):
        not_existing_character = word[42]
        assert not not_existing_character

    # Porém, o Python consegue lidar bem (não levanta erro) com indexes fora de alcance quando usados em slicing:
    assert word[4:42] == 'on'
    assert word[42:] == '' # como não existe caraceters a partir do index 42, o slice resulta numa string vazia

    # As strings no Python são imutavie, ou seja não podem ser mudadas. Assim,
    # atribuir um valor a uma posição de uma string resulta num erro:
    with pytest.raises(Exception):
        word[0] = 'J' # operação impossivel

    # Caso seja necessário uma string diferente deve-se criar uma nova:
    assert 'J' + word[1:] == 'Jython'
    assert word[:2] + 'py' == 'Pypy'

    # O Python possui uma função chamada len() que premite saber o tamanho de uma string:
    characters = 'supercalifragilisticexpialidocious'
    assert len(characters) == 34

    # As strings podem ocupar multiplas linhas. Uma maneira é usar aspas triplas: """..."""
    # ou '''...'''. O \n é automaticamente incluido na string, mas é possivel
    # prevenir isto adicionando uma \ no final da linha. 
    multi_line_string = '''\
        First line
        Second line
    '''

    assert multi_line_string == '''\
        First line
        Second line
    '''

    # Existe um terceiro parametro no slicing que premite saltar caracteres, 1 significa não saltar nenhum, 2 saltar 1 caracter, etc
    assert word[::2] == "Pto" # começa no primeiro caracter P salta 1 caracter t, salta outro o e chega ao fim da palavra
    assert word[1:-1:2] =="yh" # comaça no segundo caracter salta 1 caracter e não salta mais pois acaba no penultimo caracter


    # Mensagem escondida, consegues decifrar?

    mensagem = "D" 


def test_string_methods():
    """String methods"""

    hello_world_string = "Hello, World!"

    # The strip() method removes any whitespace from the beginning or the end.
    string_with_whitespaces = " Hello, World! "
    assert string_with_whitespaces.strip() == "Hello, World!"

    # The len() method returns the length of a string.
    assert len(hello_world_string) == 13

    # The lower() method returns the string in lower case.
    assert hello_world_string.lower() == 'hello, world!'

    # The upper() method returns the string in upper case.
    assert hello_world_string.upper() == 'HELLO, WORLD!'

    # The replace() method replaces a string with another string.
    assert hello_world_string.replace('H', 'J') == 'Jello, World!'

    # The split() method splits the string into substrings if it finds instances of the separator.
    assert hello_world_string.split(',') == ['Hello', ' World!']

    # Converts the first character to upper case
    assert 'low letter at the beginning'.capitalize() == 'Low letter at the beginning'

    # Returns the number of times a specified value occurs in a string.
    assert 'low letter at the beginning'.count('t') == 4

    # Searches the string for a specified value and returns the position of where it was found.
    assert 'Hello, welcome to my world'.find('welcome') == 7

    # Converts the first character of each word to upper case
    assert 'Welcome to my world'.title() == 'Welcome To My World'

    # Returns a string where a specified value is replaced with a specified value.
    assert 'I like bananas'.replace('bananas', 'apples') == 'I like apples'

    # Joins the elements of an iterable to the end of the string.
    my_tuple = ('John', 'Peter', 'Vicky')
    assert ', '.join(my_tuple) == 'John, Peter, Vicky'

    # Returns True if all characters in the string are upper case.
    assert 'ABC'.isupper()
    assert not 'AbC'.isupper()

    # Check if all the characters in the text are letters.
    assert 'CompanyX'.isalpha()
    assert not 'Company 23'.isalpha()

    # Returns True if all characters in the string are decimals.
    assert '1234'.isdecimal()
    assert not 'a21453'.isdecimal()


def test_string_formatting():
    """String formatting.

    Often you’ll want more control over the formatting of your output than simply printing
    space-separated values. There are several ways to format output
    """

    # To use formatted string literals, begin a string with f or F before the opening quotation
    # mark or triple quotation mark. Inside this string, you can write a Python expression
    # between { and } characters that can refer to variables or literal values.
    year = 2018
    event = 'conference'

    assert f'Results of the {year} {event}' == 'Results of the 2018 conference'

    # The str.format() method of strings requires more manual effort. You’ll still use { and } to
    # mark where a variable will be substituted and can provide detailed formatting directives,
    # but you’ll also need to provide the information to be formatted.
    yes_votes = 42_572_654  # equivalent of 42572654
    no_votes = 43_132_495   # equivalent of 43132495
    percentage = yes_votes / (yes_votes + no_votes)

    assert '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage) == ' 42572654 YES votes  49.67%'

    # When you don’t need fancy output but just want a quick display of some variables for debugging
    # purposes, you can convert any value to a string with the repr() or str() functions. The str()
    # function is meant to return representations of values which are fairly human-readable, while
    # repr() is meant to generate representations which can be read by the interpreter (or will
    # force a SyntaxError if there is no equivalent syntax). For objects which don’t have a
    # particular representation for human consumption, str() will return the same value as repr().
    # Many values, such as numbers or structures like lists and dictionaries, have the same
    # representation using either function. Strings, in particular, have two distinct
    # representations.

    greeting = 'Hello, world.'
    first_num = 10 * 3.25
    second_num = 200 * 200

    assert str(greeting) == 'Hello, world.'
    assert repr(greeting) == "'Hello, world.'"
    assert str(1/7) == '0.14285714285714285'

    # The argument to repr() may be any Python object:
    assert repr((first_num, second_num, ('spam', 'eggs'))) == "(32.5, 40000, ('spam', 'eggs'))"

    # Formatted String Literals

    # Formatted string literals (also called f-strings for short) let you include the value of
    # Python expressions inside a string by prefixing the string with f or F and writing
    # expressions as {expression}.

    # An optional format specifier can follow the expression. This allows greater control over how
    # the value is formatted. The following example rounds pi to three places after the decimal.
    pi_value = 3.14159
    assert f'The value of pi is {pi_value:.3f}.' == 'The value of pi is 3.142.'

    # Passing an integer after the ':' will cause that field to be a minimum number of characters
    # wide. This is useful for making columns line up:
    table_data = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    table_string = ''
    for name, phone in table_data.items():
        table_string += f'{name:7}==>{phone:7d}'

    assert table_string == ('Sjoerd ==>   4127'
                            'Jack   ==>   4098'
                            'Dcab   ==>   7678')

    # The String format() Method

    # Basic usage of the str.format() method looks like this:
    assert 'We are {} who say "{}!"'.format('knights', 'Ni') == 'We are knights who say "Ni!"'

    # The brackets and characters within them (called format fields) are replaced with the objects
    # passed into the str.format() method. A number in the brackets can be used to refer to the
    # position of the object passed into the str.format() method
    assert '{0} and {1}'.format('spam', 'eggs') == 'spam and eggs'
    assert '{1} and {0}'.format('spam', 'eggs') == 'eggs and spam'

    # If keyword arguments are used in the str.format() method, their values are referred to by
    # using the name of the argument.
    formatted_string = 'This {food} is {adjective}.'.format(
        food='spam',
        adjective='absolutely horrible'
    )

    assert formatted_string == 'This spam is absolutely horrible.'

    # Positional and keyword arguments can be arbitrarily combined
    formatted_string = 'The story of {0}, {1}, and {other}.'.format(
        'Bill',
        'Manfred',
        other='Georg'
    )

    assert formatted_string == 'The story of Bill, Manfred, and Georg.'

    # If you have a really long format string that you don’t want to split up, it would be nice if
    # you could reference the variables to be formatted by name instead of by position. This can be
    # done by simply passing the dict and using square brackets '[]' to access the keys

    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    formatted_string = 'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table)

    assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'

    # This could also be done by passing the table as keyword arguments with the ‘**’ notation.
    formatted_string = 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)

    assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'
