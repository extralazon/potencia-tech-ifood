class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereço):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereço = endereço
        self.contas = []
    
    def get_nome(self):
        return self.nome
    
    def get_cpf(self):
        return self.cpf
    
    def adicionar_conta(self, ContaCorrente):
        self.contas.append(ContaCorrente)
        
    def get_contas(self):
        return self.contas

class ContaCorrente:
    def __init__(self, numero_conta_corrente):
        self.numero_conta_corrente = numero_conta_corrente + 1
        self.agencia = '0001'
        self.saldo = 0
        self.extrato = []
        self.saques = 0
    
    def get_agencia(self):
        return self.agencia
    
    def get_numero_conta_corrente(self):
        return self.numero_conta_corrente
    
    def get_extrato(self):
        return self.extrato
    
    def get_saldo(self):
        return self.saldo
    
    def get_saques(self):
        return self.saques
    
    def set_saques(self):
        self.saques+=1