# for n in range(1,3):
#     nome = input('digite seu nome:')
#     idade = input('digite sua idade:')
#     email = input('digite seu email:')
#     print('obrigado proximo cliente')

# jogo

# chances = [4]

# for n in chances:
#     chute = int(input('digite um numero:'))
#     aleatorio = random.rendit(1,6)
#     if chute == aleatorio:
#         print("acertou", aleatorio)
#         break
#     else:
#         print('errou')

# Acesso a conta
# - Ver extrato
# - Fazer um deposito
# - Fazer um saque 
# - Sair do sistema 
# - 3  chances para acessar a conta, caso contrario, haverá um 
# bloqueio na conta.(for) 


nome = input('digite seu nome:')
senha = int(input('digite uma senha:'))
print('usuario cadastrado')
print('-digite os seus dados para acessar sua conta-')
meu_nome = input('digite o nome do usuario:')
minha_senha = int(input('digite sua senha:'))

for n in range(1,4):
    if minha_senha == senha and nome:
        print('bem-vindo', nome)

        Acesso = input('''
        escolha o que deseja
        
        1 - ver extrato
        2 - fazer deposito
        3 - fazer saque
        4 - sair do sistema
        
        ''')
  



