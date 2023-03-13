
codigos = ("100","101","102", "103", "104", "105")
codigo = input ("Insira o código do produto escolhido:")

if codigo in codigos:

    quantidade =int(input("Quantos você deseja comprar: "))
    if codigo =="100":
        nome = "Cachorro Quente"
        preço = 1.10
    elif codigo == "101":
        nome= "Bauru Simples"
        preço = 1.30
    elif codigo == "102":
        nome = "Bauru c/Ovo"
        preço = 1.50
    elif codigo == "103":
        nome ="Hamburger"
        preço=1.10
    elif codigo == "104":
        nome = "Chesseburger"
        preço=1.30
    elif codigo == "105":
        nome = "Refrigeante"
        preço= 1.00

else:
    print("nenhum item escolhido")

valorTotal = preço*quantidade
print(f"Voce comprou {quantidade} {nome} por R$ {valorTotal}")

