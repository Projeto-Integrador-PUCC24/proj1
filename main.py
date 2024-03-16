import mysql.connector, db

mydb = mysql.connector.connect(
  host=db.host)
products = []
def menu():
    menu = int(input("\n\nChoose another option!\n[1]Add a product.\n[2]Remove a product.\n[3]Update a product\n[4]List all products\n[5]Search for a product\n[6]Exit.\n"))
    match menu:
      case 1:
        prodAdding()
      case 2:
        prodRemoving()
      case 3:
        prodUpdating()
      case 4:
        prodListing()
      case 5:
        prodSearching()
      case 6:
        print("\n\nGoodbye!")
      case _:
        print("\n\nInvalid option!")
def prodAdding():
  product_id = input("Insira o código do produto: ")
  product_id = int(product_id)
  if (product_id in products):
    print("\n\nProduct already exists!")
    prodAdding()
  product_name = input("Insira o nome do produto: ")
  product_desc = input("Insira a descrição do produto: ")
  product_cost = input("Insira o custo do produto: ")
  product_cf = input("Insira o custo fixo do produto: ")
  product_cv = input("Insira a comissão de vendas: ")
  product_tax = input("Insira o valor dos impostos: ")
  product_ml = input("Insira a rentabilidade/margem de lucro: ")

  product = {
    "id": product_id, 
    "name": product_name,
    "description": product_desc,
    "price": product_cost,
    "custo fixo": product_cf,
    "commission": product_cv,
    "tax": product_tax,
    "margin": product_ml
  }

  products.append(product)

  print("\n\nProduct added successfully!")
  print("\n\nWant to add another product?")
  answer = input("[1] Yes\n[2] No\n")
  if answer == "1":
    prodAdding()
  else:
    menu()

def prodRemoving():
  product_id = input("Enter the product ID: ")

  for product in products:
    if product["id"] == product_id:
      ans = input("Are you sure you want to remove this product? [1] Yes [2] No\n")
      if ans == "1":
        products.remove(product)
      else:
        prodRemoving()
      print("\n\nProduct removed successfully!")
      break
  else:
    print("\n\nProduct not found!")
    prodRemoving()
  menu()

def prodUpdating():
  product_id = input("Enter the product ID: ")
  for product in products:
    if product["id"] == product_id:
      product_name = input("Enter the product name: ")
      product_price = float(input("Enter the product price: "))
      product_type = input("Enter the product type: ")

      product["name"] = product_name
      product["price"] = product_price
      product["type"] = product_type

      print("\n\nProduct updated successfully!")
      menu()
      
  else:
    print("\n\nProduct not found!")
    prodUpdating()
  
def prodListing():
  for product in products:
    if not products:
      print("\n\nNo products found!")
      menu()
    print("\n\nID:", product["id"])
    print("Name:", product["name"])
    print("Price:", product["price"])
    print("Type:", product["type"])
  menu()

def prodSearching():
  product_id = input("Enter the product ID: ")

  for product in products:
    if product["id"] == product_id:
      print("\n\nID:", product["id"])
      print("Name:", product["name"])
      print("Price:", product["price"])
      print("Type:", product["type"])
      break
  else:
    print("\n\nProduct not found!")
  menu()

print("\n\nWelcome to our system!")
menu()

