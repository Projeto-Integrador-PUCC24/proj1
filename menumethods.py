import main, time
main.products = []
def prodAdding():
  while True:
    try:
      product_id = input("Insira o código do produto: ")
      product_id = int(product_id)
      if (product_id in main.products):
        print("\n\nProduct already exists!")
        prodAdding()
      elif(product_id < 0):
        print("\n\nInvalid ID!")
        prodAdding()
      
      product_name = input("Insira o nome do produto: ")
      product_desc = input("Insira a descrição do produto: ")
      product_cost = float(input("Insira o custo do produto: "))
      if (product_cost < 0):
        print("\n\Valor inválido!")
        continue
      product_cf = float(input("Insira o custo fixo do produto: "))
      if (product_cf < 0):
        print("\n\Valor inválido!")
        continue
      product_cv = float(input("Insira a comissão de vendas: "))
      if (product_cv < 0):
        print("\n\Valor inválido!")
        continue
      product_tax = float(input("Insira o valor dos impostos: "))
      if (product_tax < 0):
        print("\n\Valor inválido!")
        prodAdding()
      product_ml = float(input("Insira a rentabilidade/margem de lucro: "))
      if (product_ml < 0):
        print("\n\Valor inválido!")
        continue 
    

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

      main.products.append(product)

      print("\n\nProduct added successfully!")
      print("\n\nWant to add another product?")
      answer = input("[1] Yes\n[2] No\n")
      if answer == "1":
        prodAdding()
      else:
        main.menu()
      break
    except ValueError:
      print("\n\nInvalid ID!")
      prodAdding()

def prodRemoving():
  main.cls()
  while True:
    try:
      product_id = int(input("Enter the product ID: "))

      for product in main.products:
        if product["id"] == product_id:
          ans = input("Are you sure you want to remove this product? [1] Yes [2] No\n")
          if ans == "1":
            main.products.remove(product)
            print("\n\nProduct removed successfully!")
            main.menu()
          else:
            prodRemoving()
      else:
        print("\n\nProduct not found!")
        prodRemoving()
      main.menu()
    except ValueError:
      print("\n\nInvalid ID!")
      prodRemoving()

def prodUpdating():
  main.cls()
  product_id = int(input("Enter the product ID: "))
  for product in main.products:
    if product["id"] == product_id:
      product_name = input("Enter the product name: ")
      product_price = float(input("Enter the product price: "))

      product["name"] = product_name
      product["price"] = product_price

      print("\n\nProduct updated successfully!")
      main.menu()
      
  else:
    print("\n\nProduct not found!")
    prodUpdating()

def prodListing():
  main.cls()
  for product in main.products:
    if not main.products:
      print("\n\nNo products found!")
      main.menu()
    print("\n\nID:", product["id"])
    print("Name:", product["name"])
    print("Price:", product["price"])
    time.sleep(10)
  main.menu()

def prodSearching():
  main.cls()
  product_id = input("Enter the product ID: ")

  for product in main.products:
    if product["id"] == product_id:
      print("\n\nID:", product["id"])
      print("Name:", product["name"])
      print("Price:", product["price"])
      print("Type:", product["type"])
      break
  else:
    print("\n\nProduct not found!")
  main.menu()

print("\n\nWelcome to our system!")
main.menu()
  
