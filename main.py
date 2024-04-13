import os, menumethods, time, db
products = []
def cls():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    while True:
      try:
        print("\n\nEscolha uma opção.\n[1]Adicione um produto.\n[2]Remova um produto.\n[3]Atualize um produto.\n[4]Ver todos os produtos.\n[5]Buscar produto.\n[6]Sair.\n")
        menu = int(input("Opção: "))
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
          case 7:
            db.con()
          case _:
            print("\n\nOpção inválida.")
      except ValueError:
        print("\n\nValor inválido, tente novamente.")
        time.sleep(1)
        cls()

if __name__ == "__main__":
  cls()
  menu()