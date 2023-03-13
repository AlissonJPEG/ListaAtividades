#1 Escreva um programa em Python para somar todos os itens de uma lista.

#lista = [1,2,3,4,5,6]

#soma  = 0

#for i in lista:
 #   soma += i
  #  print(soma)


#2 Escreva um programa em Python para multiplicar todos os itens de uma lista

#numero = [10,20,31,55,46]

#multiplicacao = 1 

#for i in numero:
 #   multiplicacao *= i
  #  print(multiplicacao)

#3 Escreva um programa em Python para obter o maior número de uma lista


 #lista = [1,2,3,4,5,6,7,8,9,10]

#print("O maior numero da lista é:", max(lista))


#4 Escreva um programa em Python para obter o maior número de uma lista

#lista = [1,2,3,4,5,6,7,8,9,10]

#print("O maior numero da lista é:", min(lista))

#6. Escreva um programa Python para obter uma lista, classificada em ordem crescente pelo último elemento em cada tupla
#de uma determinada lista de tuplas não vazias. [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

novaLista = []

for tupla in lista:
    novaLista.append(tupla[::-1])
novaLista.sort ()

lista.clear()

for tupla in novaLista:
    lista.append(tupla[::-1])

print(lista)
