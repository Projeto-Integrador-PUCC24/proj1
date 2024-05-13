import os, menumethods, time, db, ctypes
import mysql.connector
products = []
def cls():
    os.system("cls" if os.name == "nt" else "clear")
conn = mysql.connector.connect(host = db.host, user = db.user, password = db.password, database = db.database)
if (conn != None):
          print("Connection successful.")
else:
          print("Connection failed.")
def menu():
    while True:
      try:
        print("\n\nEscolha uma opção.\n[1]Cadastrar produto.\n[2]Remover um produto.\n[3]Atualizar um produto.\n[4]Listar todos os produtos.\n[5]Buscar por um produto.\n[6]Sair.\n")
        menu = int(input("Digite o número da opção desejada: "))
        match menu:
          case 1:
            menumethods.prodAdding()
          case 2:
            menumethods.prodRemoving()
          case 3:
            menumethods.prodUpdating()
          case 4:
            cls()
            menumethods.prodListing()
          case 5:
            menumethods.prodSearching()
          case 6:
            conn.close()
            print("\n\nFinalizando execução.")
            exit()
          case _:
            print("\n\nOpção inválida.")
      except ValueError:
        print("\n\nValor inválido, favor tentar novamente.")
        time.sleep(1)
        cls()
if __name__ == "__main__":
  time.sleep(1)
  cls()
  menu()