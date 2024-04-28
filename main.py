import os, menumethods, time, db, ctypes
import mysql.connector
products = []
def cls():
    os.system("cls" if os.name == "nt" else "clear")
conn = mysql.connector.connect(host = db.host, user = db.user, password = db.password, database = db.database)
def menu():
    while True:
      try:
        if (menumethods.conn != None):
          print("Connected succesfully.")
          ctypes.windll.user32.MessageBoxW(0, "Connection successful.", "Success", 1)
        else:
          print("Connection failed.")
          time.sleep(1)
          ctypes.windll.user32.MessageBoxW(0, "Connection failed.", "Error", 1)

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
            menumethods.prodListing()
          case 5:
            menumethods.prodSearching()
          case 6:
            print("\n\nFinalizando execução.")
          case _:
            print("\n\nOpção inválida.")
      except ValueError:
        print("\n\nValor inválido, favor tentar novamente.")
        time.sleep(1)
        cls()
if __name__ == "__main__":
  cls()
  menu()