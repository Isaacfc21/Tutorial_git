class Operacoes:
    def escolha_calabresa(preco_unitario, sabor):
        preco_unitario = 35.00
        sabor = "isaac"

    def escolha_mussarela(preco_unitario):
        preco_unitario = 32.00

    def escolha_portuguesa(preco_unitario):
        preco_unitario = 38.00

    def escolha_frango(preco_unitario):
        preco_unitario = 40.00
        
    def calcular_preco(preco_unitario, quantidade, sabor):
        total = preco_unitario * quantidade
        print(f"\nVocê pediu {quantidade} pizza(s) de {sabor}.")
        print(f"Total a pagar: R$ {total:2f}")