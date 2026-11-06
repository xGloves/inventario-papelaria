import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM produto")

produtos = cursor.fetchall()

print("\n=========== ESTOQUE ===========")

for produto in produtos:
    print(produto)

conexao.close()
