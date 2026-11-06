import os

while True:

    print("\n======================")
    print(" SISTEMA DE INVENTÁRIO ")
    print("======================")
    print("1 - Cadastrar Produto")
    print("2 - Consultar Estoque")
    print("3 - Registrar Entrada")
    print("4 - Registrar Saída")
    print("5 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        os.system("python cadastrar.py")

    elif opcao == "2":
        os.system("python consultar.py")

    elif opcao == "3":
        os.system("python entrada.py")

    elif opcao == "4":
        os.system("python saida.py")

    elif opcao == "5":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")
