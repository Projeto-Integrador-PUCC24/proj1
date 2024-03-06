products = []
def prodAdding():
  product_id = input("Enter the product ID: ")
  if any(product["id"] == product_id for product in products):
    print("\n\nID already exists!")
    return
  if not product_id:
    print("\n\nID cannot be empty!")
    return
  if not product_id.isdigit():
    print("\n\nID must be a number!")
    return
  product_name = input("Enter the product name: ")
  if not product_name:
    print("\n\nName cannot be empty!")
    return
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

def prodRemoving():
  product_id = input("Enter the product ID: ")

  for product in products:
    if product["id"] == product_id:
      products.remove(product)
      print("\n\nProduct removed successfully!")
      break
  else:
    print("\n\nProduct not found!")

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
      break
  else:
    print("\n\nProduct not found!")
  
def prodListing():
  for product in products:
    print("\n\nID:", product["id"])
    print("Name:", product["name"])
    print("Price:", product["price"])
    print("Type:", product["type"])

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

print("\n\nWelcome to our system!")
prodAdding()
print("Do you want to add another product?")
answer = input("\n\nEnter 'yes' or 'no': ")
if answer == "yes":
  prodAdding()
else:
  menu = int(input("\n\nChoose another option!\n1. Add a product.\n2. Remove a product.\n3. Update a product\n4. List all products\n5. Search for a product\n6. Exit"))
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
