from BancoDan import Conta

conta1 = Conta('12345-6', 'Daniel', 2000, 4000)
conta2 = Conta('65432-1', 'Monteiro', 4000, 8000)
conta1.extrato()
conta2.extrato()
conta1.transferencia(conta2, 100)
conta1.extrato()
conta2.extrato()
conta1.saque(100)
conta1.extrato()
conta2.deposito(1000)
conta2.extrato()