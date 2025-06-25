class UserService:
    def validate_user(self, user_id):
        return user_id is not None # Simula validação de usuário
    
class OrderService:
    def confirm_order(self, user_id, product_id):
        if not user_service.validate_user(user_id):
            return "Usuário inválido!"
        print(f"Pedido do produto {product_id} para o usuário {user_id} confirmado.")
        return "Pedido confirmado com sucesso!"
    
# Instanciando serviços
user_service = UserService()
order_service = OrderService()
# Exemplo de execução
resultado = order_service.confirm_order(1, 101)
print(resultado)



# def process_order(user_id, product_id, payment_info):
#     if not (user_id and product_id and payment_info):
#         return "Dados inválidos!"
#     print(f"Pedido do produto {product_id} para o usuário {user_id} confirmado.")
#     return "Pedido confirmado com sucesso!"
# # Exemplo de execução
# resultado = process_order(1,101, "cartao_credito")
# print(resultado)