import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

id_produto = int(input("ID do produto: "))
quantidade = int(input("Quantidade vendida: "))

cursor.execute("""
UPDATE produto
SET quantidade = quantidade - ?
WHERE id = ?
""", (quantidade, id_produto))

conexao.commit()
conexao.close()

print("Saída registrada!")
