
#/////////////////////////////////////////////////////////////////////////////////////////////
#Escreva um programa que solicite ao usuário um número inteiro e imprima o dobro desse número.
#/////////////////////////////////////////////////////////////////////////////////////////////


#Numero = int(input("Digite um inteiro:"))

#print(Numero*2)


#////////////////////////////////////////////////////////////////////////////////////////////////
#Escreva um programa que solicite ao usuário o raio de um círculo e calcule a área desse círculo.
#////////////////////////////////////////////////////////////////////////////////////////////////


# Raio = float(input("Qual o raio do circulo:"))

# area = Raio * Raio * 3.14

# print (f" a area é: {area:.2f}")

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Escreva um programa que solicite ao usuário seu nome e idade e imprima uma mensagem personalizada com essas informações.
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# nome = str(input("Digite seu nome:"))
# idade = int(input("Digite Sua idade:"))

# print(f"Seu nome é {nome} e você tem: {idade} anos")


#//////////////////////////////////////////////////////////////////////////////////////////////////////
#Escreva um programa que leia uma lista de números inteiros e imprima o maior e o menor número da lista.
#//////////////////////////////////////////////////////////////////////////////////////////////////////

# numeros = [1,2,3,4,5,6,7,8,9,10]

# print (f"O maior numero da lista é: {max(numeros)}\nE o menor da lista é : {min(numeros)}")


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///Escreva um programa que leia uma lista de nomes e crie um dicionário onde a chave é o nome e o valor é o número de vezes que o nome aparece na lista.///
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# lista = ['alisson', 'alisson', 'rodrigo', 'daniel', 'tarik']
# contador_nome = {}
# for nome in lista:
#     if nome in contador_nome:
#         contador_nome [nome] += 1
#     else:
#         contador_nome [nome] = 1

# print (contador_nome)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///Escreva um programa que leia uma lista de números inteiros e remova todos os valores duplicados. Em seguida, imprima a lista sem os valores duplicados.///
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> metodo 1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# lista  = [ 1,1,1,2,3,4,5,5,6,7,8,8,9,10,10]

# for numero in lista:
#      if lista.count(numero) >= 2:
#           lista.remove(numero)

# print(lista)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> metodo 2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# lista  = [ 1,1,1,2,3,4,5,5,6,7,8,8,9,10,10]

# novaLista= []

# for numero in lista:
#      if numero not in novaLista:
#         novaLista.append(numero)

# print(novaLista)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Estruturas Condicionais<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#Escreva um programa que solicite ao usuário um número e imprima se ele é positivo, negativo ou zero.//
#//////////////////////////////////////////////////////////////////////////////////////////////////////

# while True:

#     try:
#         numero = int(input("Digite um numero:"))

#         if numero >0:
#             print("SEU NUMERO É POSITIVO")
#         elif numero <0:
#             print ("SEU NUMERO É NEGATIVO")
#         elif numero == 0:
#             print("SEU NUMERO É ZERO")
#         else:
#             print("ERROR")
#         break   
    
#     except:
#         print("Você digitou algo inválido,digite um número.")

#/////////////////////////////////////////////////////////////////////////////////////////////