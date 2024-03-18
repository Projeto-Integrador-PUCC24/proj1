import os, menumethods, time
products = []
def cls():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    menu = int(input("\n\nChoose an option!\n[1]Add a product.\n[2]Remove a product.\n[3]Update a product\n[4]List all products\n[5]Search for a product\n[6]Exit.\n"))
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
        print("\n\nGoodbye!")
      case _:
        print("\n\nInvalid option!")

if __name__ == "__main__":
  cls()
  menu()