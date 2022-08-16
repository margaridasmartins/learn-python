"""
Parabens! Já tens conhecimentos de Python suficientes que te premitam resolver problemas simples.
Os problemas estão por ordem de dificuldade. Boa sorte!
"""

import math

def horas_para_segundos(horas):
    """
        Dado uma quantidade de tempo em horas (pode ser decimal), retorna o tempo em segundos
    """

    # A variavel horas contem o valor da quantidade de tempo (vamos falar sobre funções mais à frente)

    # Faz os teus calculos aqui


    return None # Deves retornar aqui a variavel com a quantidade de tempo em segundos, return <nome_variavel>


def imc(peso, altura):
    """
        Dado um peso e uma altura retorna uma string de acordo com o IMC
        menor que 18,5 - Magro
        maior ou igual a 18,5 e menor que 25 - Normal
        maior ou igual a 25 e menor que 30 - Excesso de Peso
        maior ou igual a 30 - Obeso

        O IMC é o peso a dividir pela altura ao quadrado
    """

    imc =  None # calcular imc

    # Retornar de acordo com o imc calculado
    if None: 
        return "Magro"
    elif None:
        return "Normal"
    elif None:
        return "Excesso de Peso"
    else:
        return "Obeso"

def perimetro_area_circulo(funcao, raio):
    """
        Dada uma função e um raio retorna o calculo pretendido:
            - perimetro se a variavel funcao for igual a P
            - area se a variavel funcao for igual a A
        Deves retornar o numero arredondado com duas casas decimais
    """

    # pi = math.pi, pi é o pi com 15 casas decimais

    # x = round(y, 2),  a x é atribuido o valor de y arredondado com duas casas decimais


    return None

def fibonacci(posicao):
    """
        Dada uma posição da sequencia de fibonacci retorna o numero correspondente
        Nota: A posição é sempre menor ou igual a 10, mas não vale fazer batota assume que apenas conheces as posições 1 e 2 
        deves calcular as restantes a partir dai.
        Mais à frente vamos voltar a esta função e resolve-la de uma forma mais "inteligente" com o uso de ciclos

        Posição 1 = 1
        Posição 2 = 1 
        Posicção n = Posição n-1 + Posição n-2
    """

    return None

def chess_pieces(x,y,xfinal, yfinal):
    """
        Dada uma posição num tabuleiro de xadrez, onde x representa as linhas e y as colunas (com 0<= x,y <= 7) e uma posicação final
        (xfinal, yfinal).
        Retorna:
         - 'Q' se uma rainha conseguiria chegar à posição final a partir da inicial (usando apenas um movimento).
         - 'QT' se uma rainha e uma torre conseguiriam
         - 'QK' se uma rainha e uma rei conseguiriam
         - 'QTK' se uma rainha, uma torre e um rei conseguiriam
         - 'N' se nenhuma das peças conseguiria chegar à posição final

        A rainha movimenta-se na horizontal, vertical e diagonal (a distancia que quiser)
        A torre movimenta-se na horizontal e na vertical (a distancia que quiser)
        O rei movimenta-se para uma casa adjacente na horizontal, vertical e diagonal 
        
        Para este problema pode ajudar desenhar o tabuleiro e os movientos das peças num papel 
    """
    return None

def test_problems():
    # Problema 1
    assert horas_para_segundos(1) == 3600
    assert horas_para_segundos(2.5) == 9000

    # Problema 2
    assert imc(70, 1.6) == "Excesso de Peso"
    assert imc(123, 1.78) == "Obeso"
    assert imc(48, 1.65) == "Magro"
    assert imc(75, 1.80) == "Normal"

    # Problema 3 
    assert perimetro_area_circulo("P", 1) == 6.28
    assert perimetro_area_circulo("A", 1) == 3.14
    assert perimetro_area_circulo("A", 2.13) == 14.25

    # Problema 4
    assert fibonacci(3)==2
    assert fibonacci(5)==5
    assert fibonacci(7)==13
    assert fibonacci(9)==34

    # Problema 5
    assert chess_pieces(0,0,1,1) == "QTK"
    assert chess_pieces(2,3,1,2) == "QK"
    assert chess_pieces(7,4,3,4) == "QT"
    assert chess_pieces(5,3,3,5) == "Q"
    assert chess_pieces(1,4, 2,6) == "N"
