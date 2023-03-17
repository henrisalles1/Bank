# Bank
Simulador simples de transações, depositos, saques, e criação de contas bancarias.
Ações:
  conta = Conta(#numero_da_conta, #titular, #saldo, #limite)
  conta.extrato 
  conta.saldo
  conta.numero
  conta.titular
  conta.limite
  conta.limite(#novo_limite)
  conta.codigo_banco
  conta.saque(#valor_do_saque)
  conta.deposito(#valor_do_deposito)
  conta.transfere(#valor_da_transferencia , #conta_destino)
