from banco import conectar
import sqlite3

def cadastra_cliente():
    try:    
        print("---NOVO CLIENTE---")
        nome = input("Digite o nome: ").strip()
        email = input("Digite o e-mail:").strip()

        if not nome or not email:
            print("❌ERRO: o nome e o e-mail não podem ficar em braco.")
            return
        conexao = conectar()
        cursor = conexao.cursor()

        cmd_sql = "INSERT INTO clientes (nome, e-mail) VALUES (?, ?)"

        cursor.execute(cmd_sql, (nome, email))
        conexao.commit()

        if cursor.rowcount == 0:
            print("Cliente não inserido no banco.")
        else:
            print("Cliente cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro:{erro}")

    finally:
        if conexao:
            conexao.close()

def listar_cliente():
    try:    
        print("LISTA DE CLIENTE")

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM clientes")
        resultados = cursor.fetchall()

        if len(resultados) == 0:
            print("Nenhum cliente cadastrado ainda.")
        else:
            for cliente in resultados:
                print(f"ID {cliente[0]} | Nome: {cliente[1]} | E-mail {cliente[2]}")    

    except sqlite3.Error as erro:
        print(f"Error: {erro}")
    finally:
        if conexao:
            conexao.close()

def atualizar_email():
    try:
        print("---ATUALIZAR E-MAIL---")
        id_cliente = int(input("Digite o id do cliente: "))
        novo_email = input("Digite o novo e-meil:").split()

        if not novo_email:
            print("❌ Erro: O E-mail não pode ficar em branco! ")
            return
        
        conexao = conectar()
        cursor = conexao.cursor()

        cmd_sql = "UPDATE clientes SET email = ? WHERE id = ?"
        cursor.execute(cmd_sql, (novo_email, id_cliente))

        if cursor.rowcount == 0:
            print("Cliente não encontrado.")
        else:
            print("E-mail atualizado com sucesso")

    except sqlite3.Error as erro:
        print(f"❌Erro:{erro}")
    except ValueError:
        print("O id precisa ser um numero inteiro. ")    

    finally:
        if conexao:
            conexao.close()

def escluir_cliente():
    try:
        print("---ESCLUIR CLIENTE---")
        conexao = conectar()
        cursor = conexao.cursor()

        id_cliente = int(input("Digite o ID do cliente."))

        cmd_sql = ("DELETE cliente FROM  WHERE id")


if __name__ == "__main__":
    cadastra_cliente()           
        