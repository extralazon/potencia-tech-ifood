import bank_functions as bf
import time

# Definir variáveis
LIMITE_SAQUE_VALOR = 500
LIMITE_SAQUE_QUANTIDADE = 3
quantidade_saques = 0
base_clientes = []
numero_conta_inicial = 0


# iniciar a base de clientes com algumas contas para teste
base_teste_clientes = bf.criar_base_teste()
for cliente in base_teste_clientes:
    base_clientes.append(cliente)
for cliente in base_clientes:
    for i in range(3):
        cliente.adicionar_conta(bf.criar_contas_teste(numero_conta_inicial))
        numero_conta_inicial+=1

# Estrutura do código
while True:
    # registra opção do usuário
    option = bf.menu_inicial()    
    # Lógica de cadastro de novo cliente
    if option == '1':
        base_clientes.append(bf.criar_usuario(base_clientes))
    
    # Lógica de cadastro de conta corrente
    elif option == '2':
        numero_conta_inicial = bf.criar_conta_corrente(numero_inicial_conta_corrente=numero_conta_inicial, base_clientes=base_clientes)

    # Listar clientes cadastrados
    elif option == '3':
        bf.listar_clientes(base_clientes)
        
    
    # Operações de conta    
    elif option == '4':
        
        existe_cliente, cliente = bf.buscar_cliente(base_clientes=base_clientes)
        
        if existe_cliente:
            while True:
                second_option = bf.sub_menu(base_clientes[cliente])
            
                if second_option == 'D':
                    bf.depositar(cliente,base_clientes)
                elif second_option == 'S':
                    print('')
                elif second_option == 'E':
                    bf.extrato(cliente=base_clientes[cliente])
                elif second_option == 'V':
                    print('- retornando ao menu inicial')
                    time.sleep(1)
                    break
                else:
                    print('ERRO: opção inválida')
                    time.sleep(1)
        else:
            print('ERROR: cliente não identificado')
        

    
    # Opção de encerrar a aplicação
    elif option == '0':
        print('aplicação encerrada')
        time.sleep(0.5)
        break
    # Mensagem de opção errada
    else:
        print('ERROR - opção inválida, escolha uma das opções disponíveis -')
        time.sleep(0.5)