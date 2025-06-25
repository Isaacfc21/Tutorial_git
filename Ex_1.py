import contas

print("\n=== Calculadora Monolítica ===")

def main():
    while True:
        print("\nMenu:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair") 
            
        escolha = input("Escolha uma opção (1-5): ")
        
        if escolha == "5":
            print("Encerrando o programa.")
            break
        
        if escolha not in {"1", "2", "3", "4", "5"}:
            print("Opção inválida! Tente novamente.")
        
        num1_input = input("Digite o primeiro número inteiro: ")
        num2_input = input("Digite o segundo número inteiro: ")
                    
        if num1_input.lstrip('-').isdigit() and num2_input.lstrip('-').isdigit():
            num1 = int(num1_input)
            num2 = int(num2_input)
            
        if escolha == "1":
            contas.Contas.operacao_adicao(num1,num2)
        elif escolha == "2":
            contas.Contas.operacao_subtracao(num1,num2)
        elif escolha == "3":
            contas.Contas.operacao_multiplicacao(num1,num2)
        elif escolha == "4":
            contas.Contas.operacao_divisao(num1,num2)
        else:
            print("Entrada inválida! Use apenas números inteiros.")
            continue
main()
            