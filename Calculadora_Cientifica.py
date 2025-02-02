import math

print("Bem-vindo à calculadora científica!\n")

while True:
    # exibe as opções do menu
    print("Escolha uma opção:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz quadrada")
    print("7. Seno")
    print("8. Cosseno")
    print("9. Tangente")
    print("10. Logaritmo")
    print("0. Sair")

    # pede ao usuário para escolher uma opção
    opcao = input("\nOpção escolhida: ")

    # verifica a opção escolhida pelo usuário
    if opcao == "1":
        num1 = float(input("\nDigite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("\nResultado: ", num1 + num2)

    elif opcao == "2":
        num1 = float(input("\nDigite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("\nResultado: ", num1 - num2)

    elif opcao == "3":
        num1 = float(input("\nDigite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("\nResultado: ", num1 * num2)

    elif opcao == "4":
        num1 = float(input("\nDigite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 != 0:
            print("\nResultado: ", num1 / num2)
        else:
            print("\nErro: Divisão por zero!")

    elif opcao == "5":
        num1 = float(input("\nDigite a base: "))
        num2 = float(input("Digite o expoente: "))
        print("\nResultado: ", num1 ** num2)

    elif opcao == "6":
        num1 = float(input("\nDigite um número: "))
        print("\nResultado: ", math.sqrt(num1))

    elif opcao == "7":
        num1 = float(input("\nDigite um ângulo em graus: "))
        print("\nResultado: ", math.sin(math.radians(num1)))

    elif opcao == "8":
        num1 = float(input("\nDigite um ângulo em graus: "))
        print("\nResultado: ", math.cos(math.radians(num1)))

    elif opcao == "9":
        num1 = float(input("\nDigite um ângulo em graus: "))
        print("\nResultado: ", math.tan(math.radians(num1)))

    elif opcao == "10":
        num1 = float(input("\nDigite um número: "))
        print("\nResultado: ", math.log10(num1))

    elif opcao == "0":
        print("\nObrigado por usar a calculadora científica!")
        break

    else:
        print("\nOpção inválida. Tente novamente.")
