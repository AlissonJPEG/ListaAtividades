
#Calcule a tabuada do 13.

#for i in range (1,11):
 #   tabuada = 13 * i
  #  print(f"13x {i} = {tabuada}")

#Questão 2 Ler do teclado 10 números e imprima a quantidade de números entre 10 e 50.

#numeroNoIntervalo = 0
#for i in range (10):
 #   numero = float (input("Digite um numero:"))

  #  if numero >=10 and numero <=50:
   #     numeroNoIntervalo = numeroNoIntervalo + 1

#print (f"quantidade de numeros entre 10 e 50: {numeroNoIntervalo}")

#Ler do teclado uma lista com 5 inteiros e imprimir o menor valor.



#for i in range (5):
 #   numero = int(input("insira um numero inteiro: "))

#    if i == 0:
 #       menor = numero
  #  else : 
   #     if numero < menor:
    #        menor = numero
#print("O menor numero foi:", menor)

#Calcule o somatório dos números de 1 a 100 e imprima o resultado.

#soma = 0

#for i in range(1,101):
    
 #   soma = soma + i
    
#print("O somatório de 1 até 100 é: ", soma )


#Questao 5 #Receba dois números inteiros correspondentes à largura e altura. Devolva uma cadeia de
#caracteres # que representa um retângulo com as medidas fornecidas.

altura = int(input("Escreva a altura do retângulo: "))
largura = int(input("escreva a largura do retângulo: "))

linha = "" 

for i in range(largura):
    linha = linha + "#"

retangulo = ""

for i in range(altura):
    retangulo = retangulo + "\n" + linha

print(retangulo)