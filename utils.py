import sqlite3
from time import sleep


def conectar():
    """
    Função para conectar ao servidor
    """
    conn = sqlite3.connect('psqlite3.caio')

    conn.execute("""CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTERGER NOT NULL);""")
    return conn


def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    conn.close()


def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM PRODUTOS')
    produtos = cursor.fetchall()

    if len(produtos) != 0:
        print('Listando produtos...')
        print('====================')
        for produto in produtos:
            print(f'ID: {produto[0]}')
            print(f'Nome: {produto[1]}')
            print(f'Preco: {produto[2]}')
            print(f'Estoque: {produto[3]}')
    else:
        print('Nao existem produtos para serem listados...')
    desconectar(conn)


def inserir():
    """
    Função para inserir um produto
    """  
    conn = conectar()
    cursor = conn.cursor()

    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: '))
    estoque = int(input('Digite a quantidade em estoque: '))

    cursor.execute(f'INSERT INTO produtos (nome, preco, estoque) VALUES ("{nome}", {preco}, {estoque})')
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi inserido com sucesso')
    else:
        print(f'Nao foi possivel inserir o produto!')


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    id = int(input('Informe o ID do produto: '))
    nome = input('Informe o novo nome do produto: ')
    preco = float(input('Informe o novo preco do produto: '))
    estoque = int(input('Informe a nova quantidade em estoque: '))

    cursor.execute(f'UPDATE produtos SET nome = "{nome}", preco = {preco}, estoque = {estoque} WHERE id = {id}')
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi atualizado com sucesso')
    else:
        print('Nao foi possivel deletar o produto.')

    desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """  
    conn = conectar()
    cursor = conn.cursor()

    _id = int(input('Digite o codigo do produto a ser deletad: '))
    cursor.execute(f'SELECT nome FROM produtos WHERE id={_id}')

    cursor.execute(f'DELETE FROM produtos WHERE id={_id}')
    conn.commit()

    if cursor.rowcount == 1:
        print(f'Produto foi deletado com sucesso!')
    else:
        print(f'Nao foi possivel deletar o produto...')
    desconectar(conn)


def procura():
    conn = conectar()
    cursor = conn.cursor()

    produto = input('Digite o nome do produto: ')
    produto.capitalize()
    cursor.execute(f"SELECT id, nome, preco FROM produtos WHERE nome LIKE '{produto}%';")
    produtos = cursor.fetchall()
    for produto in produtos:
        print(f'ID: {produto[0]}')
        print(f'NOME: {produto[1]}')
        print(f'PRECO: {produto[2]}')


def menu():
    """
    Função para gerar o menu inicial
    """
    while True:
        print('=========Gerenciamento de Produtos==============')
        print('Selecione uma opção: ')
        print('1 - Listar produtos.')
        print('2 - Inserir produtos.')
        print('3 - Atualizar produto.')
        print('4 - Deletar produto.')
        print('5 - Procurar Produto.')
        print('6 - Sair do Menu.')
        opcao = int(input('Escolha uma opcao: '))
        if opcao in [1, 2, 3, 4, 5, 6]:
            if opcao == 1:
                listar()
            elif opcao == 2:
                inserir()
            elif opcao == 3:
                atualizar()
            elif opcao == 4:
                deletar()
            elif opcao == 5:
                procura()
            elif opcao == 6:
                print('Programa Encerrado')
            else:
                print('Opção inválida')
        else:
            print('Opção inválida')
        sleep(1)
