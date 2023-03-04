'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''
entrada=int(input())

primeiro=1
anterior =0
auxiliar=1
proximo = 1
cont=3

while cont <= entrada:
    if (entrada == primeiro) or (entrada == anterior) or (entrada == proximo):
        print("O numero faz parte da sequencia de Fibonacci.")
    proximo = primeiro + anterior
    primeiro = anterior+1
    anterior = auxiliar
    auxiliar = proximo
    cont+=1
    print(primeiro)