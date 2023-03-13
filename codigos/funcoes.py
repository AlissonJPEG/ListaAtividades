
#def hello(nome, sobrenome, idade):
 #   print("hello",nome, sobrenome, idade)

#hello("alisson","costa", "voce tem 26 anos ?")


#def calcular_pagamentos(qtd_horas, valor_hora):
    
#    horas= float(qtd_horas)
 #   taxa= float(valor_hora)

  #  if horas <= 40:
   #     salario = horas * taxa
    
    #else:
     #   h_excd = horas - 40
      
      #  salario = 40 * taxa + (h_excd*(1.5*taxa))

#    return salario

#str_horas=input("digite as horas:")
#str_taxas= input("digite a taxa:")
#total_salario=calcular_pagamentos(str_horas,str_taxas)

#print("o valor do seu salário é R$: ", total_salario)


#def calculoImc(peso, altura):
 #   print(int (peso / altura ** 2))

#calculoImc(peso=75, altura=1.68)


#Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta
#do garçom, considerando 10% do valor da conta.

total_pedido=float(input("digite o total do pedido:"))
gorjeta= total_pedido *0.1

print(f"A gorjeta do garcom é de R$ :{gorjeta:.2f}")
