


#nome = input("Insira seu nome:")



#print(nome[0])


#palavra = input("insira uma palavra:")

#print(palavra[::-1])

#palavraInvertida = ""

#for i in range(len(palavra)):
 #   palavraInvertida = palavraInvertida + palavra[len(palavra)-1-i]
  #  print(palavraInvertida)

#questão

palavra = input("digite uma palavra:")

for i in range(len(palavra)):
    if i % 2 == 0:

        print(f"{i+1} {palavra[i]}")