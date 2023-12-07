import sqlite3
#conectando um banco de dados
banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('file.db')

#criando um curso para operar comandos SQL
cursor = banco.cursor()

# 1 criando tabela nomes
cursor.execute("""CREATE TABLE Nomes (
  Nomes TEXT NOT NULL
)""");
banco.commit()

# cadastrando tabela nomes
cursor.execute("""INSERT INTO Nomes (Nome)
VALUES
('victor machado'),
('carlos antonio'),
('pedro alves'),
('fabio santos'),
('patricia ferreira')""");

#consultando dados da tabela nomes
cursor.execute("SELECT * FROM Nomes ")
print(cursor.fetchall())

# criando tabela cidades
cursor.execute("""CREATE TABLE Cidades (
  Cidades TEXT NOT NULL
)""");
banco.commit()

# cadastrando tabela cidades
cursor.execute("""INSERT INTO Cidades (Cidades)
VALUES
('sao paulo'),
('rio de janeira'),
('belo horizonte'),
('vitoria es'),
('santa catarina')""");

#consultado dados da tabela cidades
cursor.execute("SELECT * FROM Cidades")
print(cursor.fetchall())

# criando tabela salarios
cursor.execute("""CREATE TABLE Salarios (
  Salarios INTERGER NOT NULL)""");
banco.commit()

# cadastrando tabela salarios
cursor.execute("""INSERT INTO Salarios (Salarios)
VALUES
(1000,),
(1500,),
(1200,),
(1600,),
(1800,)""");

#consultando dados da tabela salario
cursor.execute("SELECT * FROM Salarios")
print(cursor.fetchall())

# criando tabela data de nascimento
cursor.execute("""CREATE TABLE Datanascimento (
  Datanascimento INTEGER NOT NULL,
)""");

# cadastrando dados na tabela
cursor.execute("""INSERT INTO Datanascimentos (Datanascimentos)
VALUES
(29/04/1998),
(11/11/1997),
(05/03/1996),
(03/12/2004),
(05/09/2003) """);
banco.commit()

#consultando dados da tabel
cursor.execute("SELECT * FROM Datanascimentos")
print(cursor.fatchall())

# criando tabela folha de pagamento
cursor.execute(""" CREATE TABLE folhadepagamento (
  folha de pagamento INTEGER NOT NULL
)""");

# adicionando valor a tabela fohadepagamento
cursor.execute("""INSERT INTO folhadepagamento (folhadepagamento)
VALUES
(1000),
(1500),
(1200),
(1600),
(1800)""");

#consultado dados da tabela folhade pagamentos
cursor.execute("SELECT * FRO folhadepagamento")
print(cursor.fatchall())

# criando  tabela nome do departamento
cursor.execite ("""CREATE TABLE departamento (
  departamento TEXT NOT NULL
)""");

#adicionando dados da tabela departamento
cursor.execute("""INSERT INTO departamento ( departamento)
VALUES
('vendas'),
('RH'),
('financeiro').
('gerente'),
('assistente')""");

#consultado dado da tabela
cursor.execute ("SELECT * FROM departamento")
print(cursor.fetchall())

# criando tabela lista de fucionarios
cursor.execute("""CREATE TABLE lista (
  lista INTEGER NOT NULL
)""");
#adicionando dados na tabela
cursor.execute(""" INSERT INTO lista (lista)
VALUES
(1),
(2),
(3),
(4),
(5),""");
banco.commit()

#consultando dados da tabela
cursor.execute("SELECT * FROM lista")
print(cursor.fetchall())

# lista nomes do departamentos ordenado por fucionarios
cursor.execute("""CREATE TABLE  nomesdepartamento(
  nomes TEXT NOT NULL
)""");

#adicionando dados na tabela
cursor.execute("""INSERT INTO nomesdepartamento (nomesdepartamento)
VALUES
('victor vendas'),
('carlos RH'),
('pedro financeiro'),
('fabio gerente'),
('patricia assistente')""");

#consultado dados da tabela
cursor.execute("SELECT * FROM nomesdepartamento")
print(cursor.fetchall())
# fim
