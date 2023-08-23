import time
from structures import Cliente, ContaCorrente

def criar_conta_corrente(numero_inicial_conta_corrente, base_clientes):
    cliente_existe, cliente = buscar_cliente(base_clientes=base_clientes)
    if cliente_existe:
        base_clientes[cliente].adicionar_conta(ContaCorrente(numero_conta_corrente=numero_inicial_conta_corrente))
        print('- conta criada com sucesso')
        time.sleep(1)
        return numero_inicial_conta_corrente + 1
    else:
        return None

def verificar_cpf_cadastrado(cpf,base_clientes):
    for cliente in base_clientes:
        if cliente.get_cpf() == cpf:
            print('ERROR: CPF já cadastrado')
            time.sleep(1)
            return False
        return True
    
def criar_usuario(base_clientes):
    print('-- cadastrar novo cliente --')
    # dados pessoais
    print('_ dados pessoais')
    #try para validar que foram digitados apenas números
    try:
        cpf = int(input('informe o CPF (apenas números) -> '))
    except ValueError:
        print('ERROR - você não informou um valor válido para o CPF')
        time.sleep(1)  
        return None
    #verificar se o cpf não está duplicado na base
    if verificar_cpf_cadastrado(cpf,base_clientes):
        nome = input('informe o nome completo -> ')
        data_nascimento = input('informe a data de nascimento -> ')
        # dados de endereço
        print('_ dados de endereço')
        logradouro = input('informe o nome do logradouro -> ')
        numero_moradia = input('informe o numero -> ')
        bairro = input('informe o bairro -> ')
        cidade = input('informe a cidade -> ')
        estado = input('informe a UF (apenas sigla) -> ').upper()
        endereço = f'{logradouro} " - "{numero_moradia}" - "{bairro}" - "{cidade}"/"{estado}'
        
        # criar o cliente
        cliente = Cliente(nome=nome, cpf=cpf, data_nascimento=data_nascimento,endereço=endereço)
        # retorno
        print('--- cadastro de cliente realizado')
        time.sleep(1)
        return cliente
    else:
        return None

def listar_clientes(base_clientes):
    print('-- clientes cadastrados\n')
    for cliente in base_clientes:
        print(f'{cliente.get_nome()} - CPF -> {cliente.get_cpf()}')
        if len(cliente.get_contas())>0:
            contas = cliente.get_contas()
            for conta in contas:
                print(f'   [Agência: {conta.get_agencia()} - CC: {conta.get_numero_conta_corrente()} ]')
    time.sleep(1)

#função para buscar um cliente na base de dados pesquisando pelo cpf
def buscar_cliente(base_clientes):
    try:
        cpf_cliente = int(input('informe o CPF (apenas números) -> '))
        for index, cliente in enumerate(base_clientes):
            if cliente.get_cpf() == cpf_cliente:
                return True, index
    except ValueError:
        print('ERROR: infome apenas números')
        return False, False
    # caso não encontre o cpf
    print('ERROR: o cpf informado não está cadastrado')
    return False, False

#função para listar as contas correntes do cliente
def listar_contas_correntes(Cliente):
    if len(Cliente.contas)> 0:
        print(f'-- contas ativas de {Cliente.get_nome()}')
        for conta in Cliente.contas:
            print(f'CC:[{conta.numero_conta_corrente}] - Saldo [R$ {conta.saldo:.2f}]')
        return True
    else:
        print(f'ERROR: nenhuma conta ativa para {Cliente.nome}')
        return False

#função para retornar o indice da conta selecionada para operar            
def buscar_conta_corrente(Cliente):
    try:
        conta_selecionada = int(input('informe qual conta deseja utilizar -> '))
        for index,conta in enumerate(Cliente.contas):
            if conta.get_numero_conta_corrente() == conta_selecionada:
                return True,index
    except ValueError:
        print('ERROR: conta inválida')
        return None
    print('ERROR: conta informada não existe')
    return False, False

def depositar(cliente,base_clientes):
    #buscar cliente e conta corrente na base de dados
    if cliente == None:
        return
    if listar_contas_correntes(base_clientes[cliente]):
        existe_conta, conta_corrente_selecionada = buscar_conta_corrente(base_clientes[cliente])
    else:
        return
    #operar o depósito se a conta selecionada existir
    if existe_conta:
        deposito = input('depósito: informe valor a ser creditado (0 para voltar) -> ')
        # Validação que não foi digitada uma letra
        try:
            deposito = float(deposito)
            if deposito > 0:
                base_clientes[cliente].contas[conta_corrente_selecionada].saldo += deposito
                base_clientes[cliente].contas[conta_corrente_selecionada].extrato.append(f"deposito: +R$ {deposito:.2f}")
                print('operação realizada com sucesso')
                time.sleep(1)
            else:
                print('retornando ao menu inicial')
                time.sleep(1)
        except ValueError:
            print('ERROR - você informou um valor inválido para depósito, tente novamente -')
#função extrato de todos os clientes
def extrato_geral(base_clientes):
    for cliente in base_clientes:
        print(f'- cliente: {cliente.get_nome()} - CPF: {cliente.get_cpf()}')
        if len(cliente.get_contas())>0:
            for conta in cliente.get_contas():
                print(f'-- Agencia: {conta.get_agencia()} - CC: {conta.get_numero_conta_corrente()}')
                for operacao in conta.get_extrato():
                    print(f'--- {operacao}')
                print(f'------- saldo atual: R$ {conta.saldo:.2f}')
                
#função extrato de um cliente
def extrato(cliente):
    saldo_total = 0
    print(f'- cliente: {cliente.get_nome()} - CPF: {cliente.get_cpf()}')
    if len(cliente.get_contas())>0:
        for conta in cliente.get_contas():
            print(f'-- Agencia: {conta.get_agencia()} - CC: {conta.get_numero_conta_corrente()}')
            saldo_total += conta.get_saldo()
            for operacao in conta.get_extrato():
                print(f'--- {operacao}')
            print(f'---- saldo atual: R$ {conta.get_saldo():.2f}')
        print(f'::: saldo total do cliente: R$ {saldo_total:.2f}')
# menu inicial        
def menu_inicial():
    date = time.strftime("%d/%m/%Y")

    menu = f"""

    :: el bank ::

    [1] CADASTRAR NOVO CLIENTE
    [2] CADASTRAR NOVA CONTA CORRENTE
    [3] LISTAR CLIENTES CADASTRADOS
    [4] OPERAÇÕES DE CONTA
    [0] SAIR

    {date}
    -> """
    return input(menu)
    
def sub_menu(Cliente):
    
    menu = f"""
    
    olá {Cliente.get_nome()}, escolha a opção desejada:
    
    [D] DEPOSITAR
    [S] SACAR
    [E] EXTRATO
    [V] VOLTAR
    
    -> """
    return input(menu).upper()

def criar_base_teste():
    cliente1 = Cliente('Dimitrius Extralazon','02/05/1983',111,'rua teste - 111 - bairro teste - cidade teste/RS')
    cliente2 = Cliente('Kalineusa Gerundina','02/05/1998',222,'rua teste - 222 - bairro teste - cidade teste/RS')
    cliente3 = Cliente('Camila Xubileivs','09/11/1992',333,'rua teste - 333 - bairro teste - cidade teste/RS')
    return [cliente1,cliente2,cliente3]

def criar_contas_teste(numero_inicial_conta):
    return ContaCorrente(numero_inicial_conta)
    