import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

nome = input("Nome do produto: ")
categoria = input("Categoria: ")
quantidade = int(input("Quantidade: "))
preco = float(input("Preço: "))

cursor.execute("""
INSERT INTO produto
(nome, categoria, quantidade, preco)
VALUES (?, ?, ?, ?)
""", (nome, categoria, quantidade, preco))

conexao.commit()
conexao.close()

print("Produto cadastrado com sucesso!")
