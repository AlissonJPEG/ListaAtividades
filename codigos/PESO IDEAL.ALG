Algoritmo "Peso Ideal"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/02/2023
Var
a ,p :Real
s :caractere
inicio
escreval ("Digite o seu Sexo Feminino ou Masculino:")
leia (s)
Escreval ("Digite a Sua Altura:")
leia(a)
se (( s= "Feminino") ou (s=  "feminino")) entao
P <- (62.1 *a) - 44.7
escreval ("Seu peso ideal �:" ,P)
escreval ()
escreval ("Bom treino :)")
senao
Se (( s= "Masculino") ou ( s= "masculino")) entao
P <- (72.7 *a) - 58
escreval ("Seu peso ideal �?")
escreval ()
escreval ("Bom treino :)")
senao
escreval("Digite um Sexo V�lido")
fimse
fimse
fimalgoritmo
