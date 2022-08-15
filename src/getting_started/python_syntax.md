# Python Syntax

**Sintaxe do Python comparado com outras linguagens de programação**
> A Sintaxe de uma linguagem de programação é o conjunto das regras que definem a estrutura da linguagem

- O Python foi desenhado para ser legivel, sendo que possui algumas semelhanças com a lingua inglesa e influencia da matemática.
- O Python usa novas linhas para completar um comando, outras linguagens usam ponto e virgulas ou parenteses.
- O Python usa a identação, através de espaços em branco, para definir alcance, alcance the iterações, funções ou classes, outras linguagens usam frequentemente chavetas curvas.

## Identação no Python 

Noutras linguagens de programação a identação é usada apenas por questoẽs de legibilidade, no entanto em Python a identação é muito importante resultando em erros caso não seja bem utilizada.

Python usa a indentação para indicar um bloco de código.

```python
if 5 > 2:
  print("Five is greater than two!")
```

Python irá dar um erro se não se der identação no comando print, pois este está dentro do if.

## Comentários

De forma a documentar o código (para que este seja percetivel mais facilmente) o Python permite fazer comentários.

Os comentários começão com um `#`, e tudo o que estiver para a frente na mesma linha será visto pelo Python como um comentário (não é executado)

```python
# This is a comment.
print("Hello, World!")
```

## Docstrings

Python também possui  *docstrings* que também podem ser utilizadas para documentar código

Docstrings podem ser de apenas uma linha, ou ocupar várias linhas. Docstrings são também comentários:

Python usa aspas triplas no inicio e no final para delimitar uma docstring:

```python
""" 
This 
is 
a 
multiline 
docstring. 
"""
print("Hello, World!")
```

## References

- [w3schools.com](https://www.w3schools.com/python/python_syntax.asp)
