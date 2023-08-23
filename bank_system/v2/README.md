# Desafio de projeto

## Objetivo Geral
Aprimorar o sistema bancário criado na v1 utilizando funções e tornando o código mais "modular", além de adicionar funções de criação de usuários e contas.

## Regras
A v2 do projeto deve permitir criar um usuário e criar conta corrente que será vinculada à esse usuário, além de manter as funções da v1 de forma modularizada: devem ser criadas funções para todas as operações no sistema. O retorno e a forma como serão chamadas durante o código são de livre escolha, porém haverão algumas regras na passagem dos argumentos para as funções.

## Funções

### Depósito
v1: Devem ser armazenados em uma variável e exibidos na operação de extrato.
v2: A função deve receber os argumentos apenas por posição (positional only)
### Saque
v1: O sistema deve permitir 3 saques diários com limite de R$ 500,00 por saque. Caso o usuário não possua saldo em conta, deve ser exibida uma mensagem informando que o saldo é insuficiente para a operação. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato
v2: A função deve receber os argumentos apenas por nome (keyword only).
### Extrato
v1: Essa operação deve listar todos os depósitos e saques realizados na conta e ao fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, deve exibir a mensagem informando que não foram realizadas movimentações.
Os valores devem ser exibidos no formato R$ xxx.xx
v2: A função deve receber os argumentos por posição e por nome (positional only e keyword only)
    posicionais: saldo
    nomeados: extrato
### Criar Usuário (cliente)
O programa deve armazenar os usuários em uma lista.
Usuário é composto por:
- nome
- data de nascimento
- cpf --> armazenar somente números e não pode haver duplicados
- endereço --> logradouro - nro - bairro - cidade/UF
### Criar Conta-Corrente
Uma conta é composta por:
- agência --> 0001 (fixo)
- número da conta --> sequencial iniciando em 1
- usuário 