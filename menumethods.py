import main, time
import tabulate
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
      product_cv = product_cv * product_cost / 100
      product_tax = product_tax * product_cost / 100
      product_ml = product_ml * product_cost / 100
      sellingPrice = product_cost / ( 1 - (product_cf + product_cv + product_tax + product_ml/100))
      
      if (product_ml > 20):
        product_mlDesc = "High"
      elif (product_ml > 10 and product_ml < 20):
        product_mlDesc = "Medium"
      elif (product_ml > 0 and product_ml < 10):
        product_mlDesc = "Low"
      elif (product_ml == 0):
        product_mlDesc = "None"
      if (product_ml < 0):
        product_mlDesc = "Negative profit."

      product = [product_id, product_name, product_desc, product_cost, product_cf, product_cv, product_tax, product_ml]
      products = [["Nome", "Preço", "Margem de Lucro"],[product_name, sellingPrice, product_ml]]
      print("=============================================")
      print("\n\nProduct overview: ")
      table1 = tabulate.tabulate(products,headers = "firstrow", tablefmt = "fancy_grid")
      print(table1)
      print("=============================================")
      print("\n\nMore details: ")
      productDetails = [["ID", "Nome", "Descrição", "Custo", "Custo Fixo", "Comissão de Vendas", "Impostos", "Margem de Lucro", "Descrição do Lucro"],[product_id, product_name, product_desc, product_cost, product_cf, product_cv, product_tax, product_ml, product_mlDesc]]
      table2 = tabulate.tabulate(productDetails,headers = "firstrow", tablefmt = "fancy_grid")
      print(table2)
      print("=============================================")
      print("\n\nProduct added successfully!")
      print("\n\nWant to add another product?")
      answer = input("[1] Yes\n[2] No\n")
      if answer == "1":
        prodAdding()
      else:
        main.menu() 
      break
    except ValueError:
      print("\n\nInvalid value! Please try again.")
      prodAdding()

def prodListing():
  print("Not implemented.")
  
def prodRemoving():
  print("Not implemented.")

def prodUpdating():
  print("Not implemented.")

def prodSearching():
  print("Not implemented.")
