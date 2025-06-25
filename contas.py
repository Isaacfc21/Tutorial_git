class Contas:
    
    def operacao_adicao(num1,num2):
        resultado = num1 + num2
        print(f"Resultado: {resultado}")
                
    def operacao_subtracao(num1,num2):
        resultado = num1 - num2
        print(f"Resultado: {resultado}")
                
    def operacao_multiplicacao(num1,num2):
        resultado = num1 * num2
        print(f"Resultado: {resultado}")
            
    def operacao_divisao(num1,num2):
        if num2 == 0:
            print("Erro: divisão por zero!")
        else:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")