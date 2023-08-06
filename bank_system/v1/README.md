# Desafio de projeto

## Objetivo Geral
Criar um sistema bancário em Python com as operações: sacar, depoistar e visualizar extrato.

## Regras
A v1 do projeto trabalha apenas com 1 usuário, não sendo necessário identificar dados bancários como agência e conta bancária.

## Funções

### Depósito
Devem ser armazenados em uma variável e exibidos na operação de extrato.
### Saque
O sistema deve permitir 3 saques diários com limite de R$ 500,00 por saque. Caso o usuário não possua saldo em conta, deve ser exibida uma mensagem informando que o saldo é insuficiente para a operação. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato
### Extrato
Essa operação deve listar todos os depósitos e saques realizados na conta e ao fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, deve exibir a mensagem informando que não foram realizadas movimentações.
Os valores devem ser exibidos no formato R$ xxx.xx
