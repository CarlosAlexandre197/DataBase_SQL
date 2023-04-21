# Comandos básicos de SQL: Linguagem de definição de dados (DDL)

# O comando CREATE serve para criar uma nova tabela. 

'''CREATE TABLE fornecedor (
 id INT,
 nome VARCHAR(100),
     endereco VARCHAR(250) 
 );'''

# O comando de exemplo acima mostra a criação da tabela “fornecedor” , com os campos “id” (identificação do fornecedor), 
# “nome” (nome do fornecedor) e “endereço” (rua e bairro do fornecedor).

# O comando “ALTER” faz alterações estruturais na tabela. Ainda no exemplo da tabela anterior, 
# vamos supor que precisamos diminuir o tamanho do campo “nome” de 100 para 70 caracteres.

'''ALTER TABLE fornecedor MODIFY COLUMN nome VARCHAR(70);'''

# o comando “ALTER” também pode ser usado para adicionar ou remover colunas. Esse comando existe para que não seja necessário recriar 
# as tabelas, caso modificações e ajustes precisem ser realizados.

'''DROP TABLE fornecedor;'''

# O último comando dentre os mais importantes da categoria DDL é o DROP. 
# Esse comando destrói toda estrutura da tabela e os seus dados. 

'''Os comandos DDL são normalmente utilizados quando as tabelas e índices do banco de dados estão sendo estruturados. 
Uma vez que a estrutura esteja pronta, os comandos mais utilizados são realmente os que pertencem à categoria de manipulação de dados (DML), 
pois apenas ocorrerão alterações nos dados.'''
