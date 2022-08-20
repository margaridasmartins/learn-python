# Playground e Cheatsheet Para Aprender Python

[![Build Status](https://travis-ci.org/trekhleb/learn-python.svg?branch=master)](https://travis-ci.org/trekhleb/learn-python)

> Essa é uma coleção de scripts Python dividida em [tópicos](#índice) que contém 
exemplos de código com explicações, diferentes usos e links para outras leituras.


É um **playground** porque podes fazer alterações no código para ver como ele se comporta,
além de [testá-lo](#testando-o-código) usando asserções. Também é possível 
[revisar o código](#revisando-o-código) que você escreveu automaticamente e verificar se ele se encaixa
no guia de estilo de código Python.
Isso tudo pode tornar seu processo de aprendizagem mais interativo e ajudar a manter a qualidade
do código bastante alta desde o início.

É um **cheatsheet** porque você pode voltar a esses exemplos de código quando quiser recapitular a sintaxe das 
[estruturas padrão do Python](#índice). O código está cheio de asserções, então você poderá ver o retorno das funções sem precisar executá-las.

> _Você pode se interessar também por 🤖 [Interactive Machine Learning Experiments](https://github.com/trekhleb/machine-learning-experiments)_

## Como Usar Esse Repositório

Nesse repositório, cada script Python possui a seguinte estrutura:

```python
"""Lists  <--- Nome do tópico

# @see: https://www.learnpython.org/en/Lists  <-- Link para outras leituras.

A seguir, uma explicação mais detalhada do tópico atual (ex, informações gerais sobre listas (Lists)).
"""


def test_list_type():
    """Explicação do subtópico.
    
    Cada arquivo contém funções de teste que ilustram subtópicos (ou seja, tipo de lista, métodos de lista).
    """
    
    # Here is an example of how to build a list.  <-- Comentários em inglês explicam a ação.
    squares = [1, 4, 9, 16, 25]
    
    # Lists can be indexed and sliced. 
    # Indexing returns the item.
    assert squares[0] == 1  # <-- As asserções ilustram o resultado.
    # Slicing returns a new list.
    assert squares[-3:] == [9, 16, 25]  # <-- As asserções ilustram o resultado.
```

Então você pode querer fazer o seguinte:

- [Encontrar o tópico](#índice) que deseja aprender ou recapitular.
- Ler os comentários e/ou a documentação vinculada em cada script (como no exemplo acima).
- Analisar os exemplos e asserções para ver exemplos de uso e saída esperada das funções.
- Alterar o código ou adicionar novas asserções para ver o que acontece.
- [Executar testes](#testando-o-código) e [revisar o código](#revisando-o-código) para ver se ele
funciona e para saber se está escrito corretamente. 

## Índice

1. **Começando**
    - [O que é Python](src/getting_started/what_is_python.md)
    - [Sintaxe Python](src/getting_started/python_syntax.md)
    - [Variáveis](src/getting_started/test_variables.py)
2. **Operadores**
    - [Operadores Aritméticos](src/operators/test_arithmetic.py) (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
    - [Operadores Bitwise](src/operators/test_bitwise.py) (`&`, `|`, `^`, `>>`, `<<`, `~`)
    - [Operadores de Atribuição](src/operators/test_assigment.py) (`=`, `+=`, `-=`, `/=`, `//=` etc.)
    - [Operadores de Comparação](src/operators/test_comparison.py) (`==`, `!=`, `>`, `<`, `>=`, `<=`)
    - [Operadores Lógicos](src/operators/test_logical.py) (`and`, `or`, `not`)
    - [Operadores de Indentidade](src/operators/test_identity.py) (`is`, `is not`)
    - [Operadores de Associação](src/operators/test_membership.py) (`in`, `not in`)
3. **Tipos de Dados**
    - [Números](src/data_types/test_numbers.py) (incluindo boleanos)
    - [Strings](src/data_types/test_strings.py) e seus métodos
    - [Listas](src/data_types/test_lists.py) e seus métodos (incluindo lista de compreensões)
    - [Tuplas](src/data_types/test_tuples.py)
    - [Conjuntos](src/data_types/test_sets.py) e seus métodos
    - [Dicionários](src/data_types/test_dictionaries.py)
    - [Casting de Tipo](src/data_types/test_type_casting.py)
4. **Controles de Fluxo**
    - [A declaração `if`](src/control_flow/test_if.py)
    - [A declaração `for`](src/control_flow/test_for.py) (e a função `range()`)
    - [A declaração `while`](src/control_flow/test_while.py)
    - [A declaração `try`](src/control_flow/test_try.py)
    - [A declaração `break`](src/control_flow/test_break.py)
    - [A declaração `continue`](src/control_flow/test_continue.py)
5. **Funções**
    - [Definição de Função](src/functions/test_function_definition.py) (declaração `def` e `return`)
    - [Variáveis Dentro das Funções](src/functions/test_function_scopes.py) (declaração `global` e `nonlocal`)
    - [Valores Padrão de Argumentos](src/functions/test_function_default_arguments.py)
    - [Argumentos de palavras-chave](src/functions/test_function_keyword_arguments.py)
    - [Listas de Argumento Arbitrárias](src/functions/test_function_arbitrary_arguments.py)
    - [Desfazendo Lista de Argumentos](src/functions/test_function_unpacking_arguments.py) (declaração `*` e `**`)
    - [Expressões Lambda](src/functions/test_lambda_expressions.py) (declaração `lambda`)
    - [Documentação das Strings](src/functions/test_function_documentation_string.py)
    - [Função de Anotações](src/functions/test_function_annotations.py)
    - [Função de Decoradores](src/functions/test_function_decorators.py)
6. **Classes**
    - [Definição de Classe](src/classes/test_class_definition.py) (declaração `class`)
    - [Classes dos Objetos](src/classes/test_class_objects.py)
    - [Instância dos Objetos](src/classes/test_instance_objects.py)
    - [Métodos de Objetos](src/classes/test_method_objects.py)
    - [Variável de Classe e Instância](src/classes/test_class_and_instance_variables.py)
    - [Herança](src/classes/test_inheritance.py)
    - [Herança Múltipla](src/classes/test_multiple_inheritance.py)
7. **Módulos**
    - [Módulos](src/modules/test_modules.py) (declaração `import`)
    - [Pacotes](src/modules/test_packages.py)
8. **Erros e Exceções**
    - [Tratando Exceções](src/exceptions/test_handle_exceptions.py) (declaração `try`)
    - [Levantando Exceções](src/exceptions/test_raise_exceptions.py) (declaração `raise`) 
9. **Arquivos**
    - [Lendo e Escrevendo](src/files/test_file_reading.py) (declaração `with`)
    - [Métodos de Objetos de Arquivos](src/files/test_file_methods.py)
10. **Adicional**
    - [A declaração `pass`](src/additions/test_pass.py)
    - [Geradores](src/additions/test_generators.py) (declaração `yield`)
11. **Algumas Bibliotecas Padrão**
    - [Serialization](src/standard_libraries/test_json.py) (biblioteca `json`)
    - [File Wildcards](src/standard_libraries/test_glob.py) (biblioteca `glob`)
    - [String Pattern Matching](src/standard_libraries/test_re.py) (biblioteca `re`)
    - [Matemática](src/standard_libraries/test_math.py) (bibliotecas `math`, `random` e `statistics`)
    - [Tempo e Datas](src/standard_libraries/test_datetime.py) (biblioteca `datetime`)
    - [Comprimindo Dados](src/standard_libraries/test_zlib.py) (biblioteca `zlib`)

## Pré-requisitos

**Instalando o Python**

Certifique-se de ter o [Python3 instalado](https://realpython.com/installing-python/) em sua máquina.

Você pode usar a biblioteca padrão do Python [venv](https://docs.python.org/3/library/venv.html)
para criar ambientes virtuais e ter o Python, pip e todos os outros pacotes a serem instalados
 a partir do diretório local do projeto para evitar mexer com pacotes externos ou do sistema.

Dependendo da sua instalação, você pode ter acesso ao interpretador Python3 executando `python` ou `python3`. O mesmo vale para o gerenciador de pacotes pip, você pode acessá-lo executando `pip` ou `pip3`.

Você pode ver a versão do seu Python executando:

```bash
python --version
```

Observe que neste repositório sempre que você vê o `python`, será assumido que é o Python **3**.

**Instalando dependências**

Instale todas as dependências necessárias para o projeto executando:

```bash
pip install -r requirements.txt
```

## Testando o Código

Testes são feitos usando o framework [pytest](https://docs.pytest.org/en/latest/).

Você pode adicionar novos testes criando arquivos e funções com o prefixo `test_` 
(ex. `test_topic.py` com a função `def test_sub_topic()` dentro).

Para executar todos os testes, execute o seguinte comando na pasta raiz do projeto:

```bash
pytest
```

Para executar testes específicos, execute:

```bash
pytest ./path/to/the/test_file.py
```

## Revisando o Código

A revisão é feita usando as bibliotecas [pylint](http://pylint.pycqa.org/) e [flake8](http://flake8.pycqa.org/en/latest/).

### PyLint

Para verificar se o código está escrito de acordo com o guia de estilo 
do [PEP 8](https://www.python.org/dev/peps/pep-0008/), execute:

```bash
pylint ./src/
```

Caso o pylint detecte um erro (ex. `missing-docstring`), convém ler mais sobre erros específicos executando:

```bash
pylint --help-msg=missing-docstring
```

[Saber mais sobre PyLint](http://pylint.pycqa.org/)

### Flake8

Para verificar se o código está escrito de acordo com o guia de estilo 
do [PEP 8](https://www.python.org/dev/peps/pep-0008/), execute:

```bash
flake8 ./src
```

Ou, se você quiser uma saída mais detalhada, execute:

```bash
flake8 ./src --statistics --show-source --count
```

[Saber mais sobre Flake8](http://flake8.pycqa.org/en/latest/)

---

Traduzido por [vilmacio22](https://github.com/vilmacio22).

## Importante!

- Garantir antes de qualquer aleteração que estão no branch certo

```
    git checkout <nome_do_vosso_branch>
```

- Garantir que estão a utilizar a versão mais atualizada

```
    git checkout master
    git pull
    git checkout <nome_do_vosso_branch>
    git merge master
```

- No final de programar atualizar o branch remoto

(na pasta raiz)

```
    git add * 
    git commit -m "<resumo do que fizeram>"
    git push
```

## Ordem de aprendizagem

1. Começando (getting_started)
2. Operadores (operators) 
    1. test_arithmetic
    2. test_biwise
    3. test_comparison
    4. test_assignment
    5. test_logical
3. Contolos de fluxo (control_flow)
    1. test_if
4. **problemas_I**
5. Tipos de Dados (data_types)
    1. test_numbers
    2. test_strings (NÃO COMPLETO)