import sqlite3

conexao = sqlite3.connect('Lista_Tarefas.db')
cursor = conexao.cursor()

print('''O que deseja fazer? \n
[1] Listar afazeres
[2] Listar categorias
[3] Sair
''')
funcao = int(input())
def lista_afazeres():
    print('''Selecione uma opção: \n
    [1] Lista completa
    [2] Lista por datas
    [3] Lista de conclusão
    [4] Sair
    ''')
    opcao = int(input())
    if opcao == 1:
        tarefas = cursor.execute("SELECT * FROM tarefas")
        for completa in tarefas:
            print(completa)
    if opcao == 2:
        data = input('Digite a data desejada: ')
        data1 = '%' + data + '%'
        lista = ("SELECT * FROM tarefas WHERE data LIKE?")
        datas = conexao.execute(lista, [data1])
        for dados in datas:
            print(dados)
    if opcao == 3:
        conclusao = cursor.execute("SELECT * FROM tarefas WHERE conclusao = concluido")
        for lista in conclusao:
            print(lista)
    if opcao == 4:
        quit()
def lista_categ():
    categorias = cursor.execute("SELECT * FROM categorias")
    for lista in categorias:
        print(lista)
if funcao == 1:
    lista_afazeres()
if funcao == 2:
    lista_categ()
if funcao == 3:
    quit()

conexao.commit()
conexao.close()