class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor inválido para depósito.')

    def sacar(self, valor):
        if self.saldo >= valor and valor <= 500 and len(self.saques) < 3:
            self.saldo -= valor
            self.saques.append(valor)
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        elif self.saldo < valor:
            print('Saldo insuficiente para realizar o saque.')
        elif valor > 500:
            print('Valor máximo de saque é de R$ 500.00.')
        elif len(self.saques) >= 3:
            print('Limite de saques diários excedido.')

    def extrato(self):
        if not self.depositos and not self.saques:
            print('Não foram realizadas movimentações.')
        else:
            print('Extrato:')
            for deposito in self.depositos:
                print(f'Depósito: R$ {deposito:.2f}')
            for saque in self.saques:
                print(f'Saque: R$ {saque:.2f}')
            print(f'Saldo atual: R$ {self.saldo:.2f}')


# Função para interagir com o usuário
def menu():
    banco = Banco()
    while True:
        print("\n=== MENU ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Visualizar Extrato")
        print("4. Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            valor_deposito = float(input("Digite o valor a depositar: "))
            banco.depositar(valor_deposito)
        elif opcao == "2":
            valor_saque = float(input("Digite o valor a sacar: "))
            banco.sacar(valor_saque)
        elif opcao == "3":
            banco.extrato()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opcao inválida. Por favor, escolha uma opcao válida.")


# Execução do programa
menu()
