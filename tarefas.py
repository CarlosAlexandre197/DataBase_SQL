'''Neste programa, criamos duas tabelas: categorias e tarefas. A tabela categorias possui um campo id (chave primária) e um campo nome. 
A tabela tarefas possui um campo id (chave primária), um campo nome, um campo data, um campo status (que indica se a tarefa foi realizada ou não)
e um campo id_categoria (chave estrangeira que referencia a tabela categorias).'''

'''O relacionamento entre as tabelas é One-to-Many (Um-para-Muitos), já que uma categoria pode ter várias tarefas, mas cada tarefa pertence a apenas uma categoria.
Este programa criará um arquivo chamado tarefas.db, onde as tabelas serão armazenadas. Se o arquivo já existir, ele apenas se conectará a ele. 
O código utiliza a biblioteca sqlite3 do Python para interagir com o banco de dados SQLite.'''

# Biblioteca responsavel por interagir com o banco de dados

import sqlite3

# Conectar (ou criar) o banco de dados 

conexao = sqlite3.connect('tarefas.db')

# Criar um objeto cursor para executar comandos SQL

banco = conexao.cursor()

# Criar a tabela de categorias

banco.execute('''
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);
''')

# Criar a tabela de tarefas

banco.execute('''
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    data TEXT,
    status INTEGER CHECK (status IN (0, 1)),
    id_categoria INTEGER,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id)
);
''')

banco.execute("INSERT INTO categorias VALUES (1, 'Organizar Evento')")

banco.execute("INSERT INTO tarefas VALUES (1, 'Casamento', '08/07/2023', 1, 1)")

# Salvar as alterações e fechar a conexão

conexao.commit()
conexao.close()

