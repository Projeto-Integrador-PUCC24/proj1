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
  product_id = input("Enter the product ID: ")
  if any(product["id"] == product_id for product in products):
    print("\n\nID already exists!")
    prodAdding()
  if not product_id:
    print("\n\nID cannot be empty!")
    prodAdding()
  if not product_id.isdigit():
    print("\n\nID must be a number!")
    prodAdding()
  product_name = input("Enter the product name: ")
  if not product_name:
    print("\n\nName cannot be empty!")
    prodAdding()
  product_price = float(input("Enter the product price: "))
  if product_price <= 0:
    print("\n\nPrice must be greater than zero!")
    return
  if not product_price:
    print("\n\nPrice cannot be empty!")
    return
  product_type = input("Enter the product type: ")
  if not product_type:
    print("\n\nType cannot be empty!")
    return

  product = {
    "id": product_id,
    "name": product_name,
    "price": product_price,
    "type": product_type
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

