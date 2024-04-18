import main, time
import tabulate
main.products = []
def prodAdding():
  while True:
    try:
      product_id = input("Insira o código do produto: ")
      product_id = int(product_id)
      if(product_id < 0):
        print("\n\nCódigo inválido!")
        prodAdding()
      product_name = "Coca-Cola"
      product_desc = "Refrigerante de cola"
      product_cost = 36.00
      product_cf_percent = 15
      product_cv_percent = 5
      product_tax_percent = 12
      product_ml_percent = 20
      product_name = input("Insira o nome do produto: ")
      product_desc = input("Insira a descrição do produto: ")
      product_cost = float(input("Insira o custo do produto: "))
      if (product_cost < 0):
        print("\n\Valor inválido!")
        continue
      product_cf_percent = float(input("Insira o custo fixo do produto: "))
      if (product_cf_percent < 0):
        print("\n\Valor inválido!")
        continue
      product_cv_percent = float(input("Insira a comissão de vendas: "))
      if (product_cv_percent < 0):
        print("\n\Valor inválido!")
        continue
      product_tax_percent = float(input("Insira o valor dos impostos: "))
      if (product_tax_percent < 0):
        print("\n\Valor inválido!")
        prodAdding()
      product_ml_percent = float(input("Insira a rentabilidade/margem de lucro: "))
      if (product_ml_percent < 0):
        print("\n\Valor inválido!")
        continue 
      grossIncome_percent = product_cf_percent + product_cv_percent + product_tax_percent + product_ml_percent
      grossIncome_percentCalc = (grossIncome_percent / 100) * product_cost
      division = 1 - (grossIncome_percentCalc / product_cost)
      print("Receita Bruta: ", grossIncome_percent)
      sellingPrice = product_cost / division

      sellingPrice_percent = (product_cost / sellingPrice) * 100

      grossIncome = (grossIncome_percent * sellingPrice) / 100
      product_cf = (product_cf_percent * sellingPrice) / 100
      product_cv = (product_cv_percent * sellingPrice) / 100
      product_tax = (product_tax_percent * sellingPrice) / 100
      product_ml = (product_ml_percent * sellingPrice) / 100

      if (product_ml_percent >= 20):
          product_mlDesc = "Lucro alto"   
      elif (product_ml_percent > 10 and product_ml_percent < 20):
          product_mlDesc = "Lucro Médio"
      elif (product_ml_percent > 0 and product_ml_percent < 10):
          product_mlDesc = "Lucro baixo"
      elif (product_ml_percent == 0):
          product_mlDesc = "Lucro nulo"
      elif (product_ml_percent < 0):
          product_mlDesc = "Prejuízo"   
      others = product_cf + product_cv + product_tax
      others_percent = (others / sellingPrice) * 100
      print("=============================================")
      print("\n\nVisão detalhada: ")
      productDetails = [["Descrição", "Valor", "%"],["Preço de Venda", f"R${sellingPrice}", 100],
            ["Custo de aquisição", f"R${product_cost}", sellingPrice_percent ],
            ["Receita Bruta", f"R${grossIncome}", grossIncome_percent],
            ["Custo Fixo", f"R${product_cf}", product_cf_percent],
            ["Comissão de Vendas", f"R${product_cv}", product_cv_percent],
            ["Impostos", f"R${product_tax}", product_tax_percent],
            ["Outros custos", f"R${others}", others_percent], 
            ["Rentabilidade", f"R${product_ml}", product_ml_percent],
            ["Descrição da Margem de Lucro", product_mlDesc, product_ml_percent]
            ]
      table2 = tabulate.tabulate(productDetails,headers = "firstrow", tablefmt = "github")
      print(table2)
      print("=============================================")
      products = [["Nome", "Preço de Venda", "Margem de Lucro"],[product_name, sellingPrice, product_ml]]

      print("\n\nVisão geral: ")
      table1 = tabulate.tabulate(products,headers = "firstrow", tablefmt = "github")
      print(table1)
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
