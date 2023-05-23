import sqlite3
conexao = sqlite3.connect('Lista_Tarefas.db')
cursor = conexao.cursor()

print("""O que deseja fazer? \n
[1] criar nova tarefa
[2] atualizar tarefa
[3] excluir tarefa
[4] sair
""")
funcao = int(input())

def criar_tarefa():
    nome = input('Digite o nome da tarefa: ')
    data = str(input('Digite o data da tarefa: '))
    status = input('Digite o status da tarefa: ')
    cat_id = cursor.execute("SELECT id FROM Categorias")
    for categoria in cat_id:
        print(categoria)
    categoria_id = input('Digite o id da categoria da tarefa: ')
    sql_criar = "INSERT INTO tarefas(nome, data, conclusao, categorias_id) values (?, ?, ?, ?)"
    conexao.execute(sql_criar, [nome, data, status, categoria_id])
def atualizar_tarefa():
    id = cursor.execute("SELECT id FROM tarefas")
    for tarefa in id:
        print(tarefa)
    print('Qual o id da tarefa? ')
    tarefa_id = int(input())
    print("""O que deseja atualizar? \n
    [1] nome da tarefa
    [2] data da tarefa
    [3] status da tarefa
    [4] categoria da tarefa
    [5] sair
    """)
    funcao = int(input())
    if funcao == 1:
        nome = input('Digite o nome da tarefa: ')
        sql_atualizar = "UPDATE tarefas SET nome = ? WHERE id = ?"
        cursor.execute(sql_atualizar, [nome, tarefa_id])
    if funcao == 2:
        data = int(input('Digite o data da tarefa: '))
        sql_atualizar = "UPDATE tarefas SET data = ? WHERE id = ?"
        cursor.execute(sql_atualizar, [data, tarefa_id])
    if funcao == 3:
        status = input('Digite o status da tarefa: ')
        sql_atualizar = "UPDATE tarefas SET conclusao = ? WHERE id = ?"
        cursor.execute(sql_atualizar, [status, tarefa_id])
    if funcao == 4:    
        id = cursor.execute("SELECT categorias_id FROM tarefas")
        for tarefa in id:
            print(tarefa)
        categoria = int(input('Digite o id da tarefa: '))
        sql_atualizar = "UPDATE tarefas SET categoria_id = ? WHERE id = ?"
        cursor.execute(sql_atualizar, [sql_atualizar, categoria])
    if funcao == 4:
        quit()
def excluir_tarefa():
    tarefa = cursor.execute("SELECT categorias_id FROM tarefas")
    for excluir in tarefa:
        print(excluir)
    tarefa_id = int(input('Digite o id da tarefa: '))
    sql_excluir = "DELETE FROM tarefas WHERE id = ?"
    cursor.execute(sql_excluir,[tarefa_id])


if funcao == 1:
    criar_tarefa()
if funcao == 2:
    atualizar_tarefa()
if funcao == 3:
    excluir_tarefa()
if funcao == 4:
    quit()

conexao.commit()
conexao.close()