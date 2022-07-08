# Importação dos módulos usados na aplicação
from email import header
import os
import inquirer
from tabulate import tabulate
from time import sleep
from datetime import date

'''
To-Do list:
    [X] Verificar se o usuário digitou um login já existente
    [X] Função de gerar relatório de clientes
    [ ] Resolver caracteres bugados no relatório
    [ ] Testar como o programa executaria no Linux
    [ ] Adicionar segurança para senha (opcional)
'''

# Variável global para armazenar as 'chaves' das informações
datas = ['Nome', 'Login', 'Senha', 'E-mail', 'Data de nascimento', 'Número de celular', 'Endereço']

# Variável global para armazenar as opções de escolha do menu principal
menu = ["Cadastrar cliente", "Mostrar dados do cliente", "Mostrar clientes cadastrados", "Gerar relatório dos clientes", "Sair"]

# Função para limpar o terminal
def clear():
    sleep(2)
    os.system('cls' or 'clear')

# Função para criação dos arquivos essenciais para o funcionamento do programa
def create_archives():
    if os.name == 'nt':
        if not os.path.isfile('src\\clientes_db.txt'):
            db_client = open('src\\clientes_db.txt', 'w')
            db_client.close()
        if not os.path.isfile('src\\relatorio_clientes.txt'):
            report_client = open('src\\relatorio_clientes.txt', 'w')
            report_client.close()
    else:
        if not os.path.isfile('src/clientes_db.txt'):
            db_client = open('src/clientes_db.txt', 'w')
            db_client.close()
        if not os.path.isfile('src/relatorio_clientes.txt'):
            report_client = open('src/relatorio_clientes.txt', 'w')
            report_client.close()

# Função para cadastrar um cliente
def register():
    name = str(input("Digite o NOME COMPLETO do cliente: "))
    login = str(input("Digite o LOGIN do cliente: "))
    
    # Verifica se o login já existe
    clients = read_db()
    for client in clients:
        client = eval(client)
        if client['login'] == login:
            print("Login já existe! Tente novamente.")
            return
    
    password = str(input("Digite a SENHA do cliente: "))
    email = str(input("Digite o E-MAIL do cliente: "))
    dateOfBirth = str(input("Digite a DATA DE NASCIMENTO do cliente (__/__/____): "))
    phone = str(input("Digite o NÚMERO DE CELULAR do cliente (__ _____-____): "))
    address = str(input("Digite o ENDEREÇO COMPLETO do cliente: "))

    # Armazenando os dados do cliente em um dicionário
    client_model = {
        "name": name,
        "login": login,
        "password": password,
        "email": email,
        "dateOfBirth": dateOfBirth,
        "phone": phone,
        "address": address
    }

    # Armazenando os dados do cliente em um arquivo
    db_client = open('src\clientes_db.txt', 'a')
    db_client.write(str(client_model) + '\n')
    db_client.close()

    # Mostrando a mensagem de sucesso
    print("\nCliente cadastrado com sucesso! 🎉")

# Função para ler o arquivo de clientes
def read_db():
    db_client = open('src\clientes_db.txt', 'r')
    clients = db_client.readlines()
    db_client.close()
    return clients

# Função para mostrar os dados de um cliente específico
def index(login):
    clients = read_db()
    for client in clients:
        client = eval(client)
        index = 0
        if client['login'] == login:
            print('********************************************************************************************************************')
            for key in client:    
                print(f"{datas[index]}: {client[key]}")
                index += 1
                sleep(0.2)
            print('********************************************************************************************************************')
            return
    print("Cliente não encontrado! Verifique o LOGIN digitado e tente novamente. 😢")

# Função para mostrar os dados de todos os clientes
def show():
    clients = read_db()
    nomes = []
    for client in clients:
        client = eval(client)
        nomes.append([client['name'], client['login']])
    print(tabulate([nomes[i] for i in range(len(nomes))], headers=['Nome', 'Login'], tablefmt="rst"))
    sleep(0.2)

# Função para gerar o relatório dos clientes
def report():
    index = 0
    fullDate = date.today()
    day = fullDate.day
    month = fullDate.month
    year = fullDate.year
    clients = read_db()
    
    report_client = open('src\\relatorio_clientes.txt', 'w')
    report_client.write(f'Relatório de clientes\n\nA loja Randinho Market possui {len(clients)} clientes que estão listados abaixo:\n\n')
    
    for client in clients:
        client = eval(client)
        report_client.write(f'{index+1}. {client["name"]}\n')
        index += 1
    
    report_client.write(f'\nRussas, {day:02d} de {month:02d} de {year}')

    print('Relatório gerado com sucesso! 🎉')

# Loop infinito para mostrar o menu principal
while True:
    # Criação dos arquivos essenciais para o funcionamento do programa
    create_archives()

    # Mostrando o menu principal
    print('************************************************* Randinho Market **************************************************')
    option = inquirer.list_input("Escolha uma opção: ", choices=menu)

    # Verificando a opção escolhida pelo usuário
    if option == "Cadastrar cliente":
        register()
        sleep(1)
        input("\nPressione ENTER para continuar...")
        clear()
    elif option == "Mostrar dados do cliente":
        clients = read_db()
        if clients == []:
            print("Não há clientes cadastrados! 😢")
        else:
            login = str(input("Digite o LOGIN do cliente que deseja ver os dados: "))
            index(login)
        sleep(1)
        input("\nPressione ENTER para continuar...")
        clear()
    elif option == "Mostrar clientes cadastrados":
        clients = read_db()
        if clients == []:
            print("Não há clientes cadastrados! 😢")
        else:
            show()
        sleep(1)
        input("\nPressione ENTER para continuar...")
        clear()
    elif option == "Gerar relatório dos clientes":
        clients = read_db()
        if clients == []:
            print("Não há clientes cadastrados! 😢")
        else:
            report()
        sleep(1)
        input("\nPressione ENTER para continuar...")
        clear()
    elif option == "Sair":
        print('Saindo do programa... 🚀')
        print('Até mais! 👋')
        clear()
        break
