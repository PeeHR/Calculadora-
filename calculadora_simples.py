print("Vamos realizar um calculo:\n")
print("Favor escolha uma das opções a seguir:\n")
print(" 1 - Somar\n 2 - Subitrair\n 3 - Multiplicar\n 4 - Dividir\n")

painel = int(input("escolha uma operação: "))

if painel == 1:
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite outro valor: ")) 
    soma = n1 + n2
    print("Soma dos resultados informados é %i" %soma)

elif painel == 2:
    s1 = int(input("Digite um valor: "))
    s2 = int(input("Digite outro valor: "))
    sub = s1 - s2
    print("O valor da subtração é %i" %sub)

elif painel == 3:
    m1 = int(input("Digite um valor: "))
    m2 = int(input("Digite a quantidade de vezes: "))
    multi = m1 * m2
    print("O valor da multiplicação é %i" %multi)

elif painel == 4:
    d1 = int(input("Digite um valor: "))
    d2 = int(input("Digite a quantidade de divisões: "))
    divi = d1/d2
    print("o valor da divisão é %i" %divi)

