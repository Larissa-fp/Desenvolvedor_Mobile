# Mudar coisas na atividade
import sqlite3

try:
    banco = sqlite3.connect('primeiro_banco.db')
    
    cursor = banco.cursor()
    
    cursor.execute("UPDATE Cursos SET nome = 'Auxiliar Administrativo' WHERE id = 4")
    
    cursor.execute("DELETE FROM Cursos WHERE id = 5")
    
    banco.commit()
    
    banco.close()
    
    print("Os dados foram atualizados com sucesso!!")
    
except sqlite3.Error as erro:
    print("Erro ao atualizar:", erro) 
