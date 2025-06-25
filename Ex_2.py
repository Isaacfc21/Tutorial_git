print("\n=== Menu da Pizzaria ===")

while True:
    print("\nCardápio:")
    print("1. Pizza de Calabresa - R$ 35,00")
    print("2. Pizza de Mussarela - R$ 32,00")
    print("3. Pizza Portuguesa - R$ 38,00")
    print("4. Pizza de Frango com Catupiry - R$ 40,00")
    print("5. Finalizar Pedido")

    escolha = input("Escolha uma opção (1-5): ")

    if escolha == "5":
        print("Pedido finalizado. Obrigado por comprar na nossa pizzaria!")
        break

    if escolha not in {"1", "2", "3", "4"}:
        print("Opção inválida! Tente novamente.")
    else:
        quantidade = input("Quantas pizzas você deseja? ")

        if quantidade.isdigit() and int(quantidade) > 0:
            quantidade = int(quantidade)

            if escolha == "1":
                preco_unitario = 35.00
                sabor = "Calabresa"
            elif escolha == "2":
                preco_unitario = 32.00
                sabor = "Mussarela"
            elif escolha == "3":
                preco_unitario = 38.00
                sabor = "Portuguesa"
            elif escolha == "4":
                preco_unitario = 40.00
                sabor = "Frango com Catupiry"

            total = preco_unitario * quantidade
            print(f"\nVocê pediu {quantidade} pizza(s) de {sabor}.")
            print(f"Total a pagar: R$ {total:.2f}")
        else:
            print("Quantidade inválida! Digite um número inteiro positivo.")