import time
# Menu de interface
date = time.strftime("%d/%m/%Y")

menu = f"""

:: el bank ::

[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[0] SAIR

{date}
-> """
# Definir variáveis
LIMITE_SAQUE_VALOR = 500
LIMITE_SAQUE_QUANTIDADE = 3
quantidade_saques = 0
saldo = 0.0
extrato = []
# Estrutura do código
while True:
    # registra opção do usuário
    option = input(menu)
    # Lógica do deposito
    if option == '1':
        while True:
            deposito = input('depósito: informe valor a ser creditado (0 para voltar) -> ')
            # Validação que não foi digitada uma letra
            try:
                deposito = float(deposito)
                if deposito > 0:
                    saldo += deposito
                    extrato.append(f"deposito: +R$ {deposito:.2f}")
                    print('operação realizada com sucesso')
                    time.sleep(1)
                    break
                else:
                    print('retornando ao menu inicial')
                    time.sleep(1)
                    break
            except ValueError:
                print('ERROR - você informou um valor inválido para depósito, tente novamente -')
    # Lógica do saque
    elif option == '2':
        while True:
            saque = input('saque: informe valor a ser retirado (0 para voltar) -> ')
            # Validação que não foi digitada uma letra
            try:
                saque = float(saque)
                if quantidade_saques < 3 and saque <= 500 and saque > 0:
                        if saque <= saldo:
                            saldo -= saque
                            extrato.append(f"   saque: -R$ {saque:.2f}")
                            quantidade_saques += 1
                            print('operação realizada com sucesso')
                            time.sleep(1)
                            break
                        else:
                            print('ERROR - saldo insuficiente, tente novamente')
                elif quantidade_saques >=3:
                        print('ERROR - quantidade de saques diários excedido, retornando ao menu -')
                        time.sleep(1)
                        break
                elif saque > 500:
                    print('ERROR - valor acima do limite de operação, tente novamente -')
                else:
                    print('retornando ao menu inicial')
                    time.sleep(1)
                    break
            except ValueError:
                print('ERROR - você informou um valor inválido para saque, tente novamente -')
    # Lógica do Extrato
    elif option == '3':
        if len(extrato)>0:
            print('='.center(45,"="))
            for i in range(len(extrato)):
                print(extrato[i])
            print('='.center(45,"="))
            print(f'saldo atual: R$ {saldo:.2f}')
            time.sleep(5)
            print('retornando ao menu')
            time.sleep(0.5)
        else:
            print('não foram realizadas movimentações')
            time.sleep(1)
    # Opção de encerrar a aplicação
    elif option == '0':
        print('aplicação encerrada')
        time.sleep(0.5)
        break
    # Mensagem de opção errada
    else:
        print('ERROR - opção inválida, escolha uma das opções disponíveis -')
        time.sleep(0.5)