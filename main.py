import os
import banco
import funcoes_clientes as fc

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\n Pressione ENTER para continuar...")

def iniciar_sistema():
    banco.criar_tabela()

    while True:
        limpar_tela()
        print("="*10)
        print("  SISTEMA DE GESTÃO 1.0  ")
        print("[1] Novo cliente")
        print("[2] listar_cliente")
        print("[3] Atualiza cliente")
        print("[4] Excluir cliente")     
        print("[5] Sair")  

        opcao = input("\n Escolha uma opcao") 

        limpar_tela()

        match opcao:
            case "1":

            case "2":

            case "3": 

            case "4": 

            case "5":                           

                   