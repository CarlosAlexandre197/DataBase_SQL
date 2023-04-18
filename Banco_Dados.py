import sqlite3

banco = sqlite3.connect('banco.github')
cursor = banco.cursor()

sql = '''
    CREATE TABLE Pessoas (
        id INT,
        Nome VARCHAR(50)
    );
'''
cursor.execute(sql)

banco.commit
banco.close
