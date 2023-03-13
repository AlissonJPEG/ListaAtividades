

# def calculaGorjeta(total_pedido):

#       gorjeta= total_pedido *0.1

#       return gorjeta

# total=float(input("digite o total do pedido:"))

# valor_gorjeta = calculaGorjeta(total)

# subtotal= total + valor_gorjeta   



# print(f"Taxa de serviço R$ :{valor_gorjeta:.2f} \nSubtotal de R$:{subtotal:.2F}")


# def contaLetras (palavra,letra):   
#     contador = 0

#     for l in palavra:
#         if l.lower () == letra.lower():
#             contador += 1

#     return contador

# pal = input("Digite uma palavra:")
# let = input("Digite uma letra:")

# contagem = contaLetras(pal,let)

# print(f"A letra {let} aparece {contagem} na palavra {pal}")


# def listaCrescente (lista, limInferior, limSuperior):

#     novaLista = []

#     for n in lista:
#         if n>=limInferior and n<=limSuperior:
#             novaLista.append(n)

#     return novaLista

# listaNumero = []

# for i in range(10):
#     listaNumero.append(int(input("Digite um numero:")))


# listaNumero.sort()
# listaIntervalo=listaCrescente(listaNumero,14,25)
# print(f'''lista original: {listaNumero}   Nova lista: {listaIntervalo}''')

def imprimirData(data):
    listaData= data.split("/")


    if len(listaData) != 3:
        print("Voce escreveu no formato errado.")
    elif int (listaData[0])<=0 or int(listaData[0])>31:
        print("Insria um dia entre 1 e 31.")
    elif int(listaData[1])<=0 or int(listaData [1])>12:
        print("Insira um mês entre 1 e 12.")
    elif not listaData[2].isnumeric():
        print("O ano deve ser um numero inteiro.")
    else:
        match int(listaData[1]):
            case 1:
                mes = "janeiro"
            case 2:
                mes = "Fevereiro"
            case 3:
                mes = "março"
            case 4: 
                mes = "abril"
            case 5:
                mes = "maio"
            case 6:
                mes = "Junho"
            case 7:
                mes = "Julho"
            case 8:
                mes = "Agosto"
            case 9:
                mes = "Setembro"
            case 10:
                mes = "Outubro"
            case 11:
                mes = "Novemrbro"
            case 12:
                mes = "Dezembro"
        return f"{listaData[0]} de {mes} de {listaData[2]}"
    return None

diaMesAno = input("Digite a data no formato DD/MM/AAAA:")
print(imprimirData(diaMesAno))
    
















