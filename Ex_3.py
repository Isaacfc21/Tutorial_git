import operacoes

print("\n=== Menu da Pizzaria ===")

def main():
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
            continue  

        if escolha in {"1", "2", "3", "4"}:
            quantidade = input("Quantas pizzas você deseja? ")
            if quantidade.isdigit() and int(quantidade) > 0:
                quantidade = int(quantidade)
            else:
                print("Quantidade inválida! Digite um número inteiro positivo.")
                continue  

        sabor  = ""
        
        
        if escolha == "1": 
            sabor = "Calabresa"
            preco_unitario = 35.00
            operacoes.Operacoes.escolha_calabresa(preco_unitario)
        elif escolha == "2":
            sabor = "Mussarela"
            # preco_unitario = 32.00
            operacoes.Operacoes.escolha_mussarela(preco_unitario)
        elif escolha == "3":
            # preco_unitario = 38.00
            sabor = "Portuguesa"
            operacoes.Operacoes.escolha_portuguesa(preco_unitario)
        elif escolha == "4":
            # preco_unitario = 40.00
            sabor = "Frango com Catupiry"
            
        operacoes.Operacoes.calcular_preco(preco_unitario, quantidade, sabor)

main()