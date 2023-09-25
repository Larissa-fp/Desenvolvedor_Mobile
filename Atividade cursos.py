# Importar a biblioteca sqlite
import sqlite3

# Criando conexão e o banco de dados
banco = sqlite3.connect('primeiro_banco.db')

# Criando o objeto cursor
cursor = banco.cursor()

# Criar nova tabela no banco
#cursor.execute("CREATE TABLE Cursos (id integer, nome text, instituição text)")

# Inserir valores
#cursor.execute("INSERT INTO Cursos VALUES(1, 'Pedagogia', 'UPF')")
#cursor.execute("INSERT INTO Cursos VALUES(2, 'Medicina', 'ATITUS')")
#cursor.execute("INSERT INTO Cursos VALUES(3, 'Psicologia', 'Anhaguera')")
#cursor.execute("INSERT INTO Cursos VALUES(4, 'Desenvolvedor Mobile', 'SENAI')")
#cursor.execute("INSERT INTO Cursos VALUES(5, 'Análise e Desenvolvimento de Sistemas', 'IFSUL')")

# Commit para enviar as informações para o banco de dados
banco.commit()


# Verificar o que foi adicionado
cursor.execute("SELECT * FROM Cursos")
print(cursor.fetchall())