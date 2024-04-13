import main, time
import tabulate
main.products = []
def prodAdding():
  while True:
    try:
      product_id = input("Insira o código do produto: ")
      product_id = int(product_id)
      if(product_id < 0):
        print("\n\nInvalid ID!")
        continue
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

      if (product_ml_percent > 20):
          product_mlDesc = "Lucro alto"   
      elif (product_ml_percent > 10 and product_ml_percent <= 20):
          product_mlDesc = "Lucro Médio"
      elif (product_ml_percent > 0 and product_ml_percent < 10):
          product_mlDesc = "Lucro baixo"
      elif (product_ml_percent == 0):
          product_mlDesc = "Equilíbrio"
      elif (product_ml_percent < 0):
          product_mlDesc = "Prejuízo"   
      others = product_cf + product_cv + product_tax
      others_percent = (others / sellingPrice) * 100
      print("=============================================")
      print("\n\nVisão detalhada: ")
      productDetails = [["Descrição", "Valor", "%"],["Preço de    Venda", round(sellingPrice,2), 100],
            ["Custo de aquisição", round(product_cost,2), sellingPrice_percent ],
            ["Receita Bruta", round(grossIncome, 2), grossIncome_percent],
            ["Custo Fixo", round(product_cf,2), product_cf_percent],
            ["Comissão de Vendas", round(product_cv,2), product_cv_percent],
            ["Impostos", round(product_tax,2), product_tax_percent],
            ["Outros custos",round(others,2), others_percent], 
            ["Rentabilidade", round(product_ml,2), product_ml_percent],
            ["Descrição da Margem de Lucro", product_mlDesc, product_ml_percent]
            ]
      table2 = tabulate.tabulate(productDetails,headers = "firstrow", tablefmt = "grid")
      print(table2)
      products = [["Código", "Preço de Venda", "Margem de Lucro"],[product_id, round(sellingPrice,2), round(product_ml,2)]]

      print("\n\nVisão geral: ")
      table1 = tabulate.tabulate(products,headers = "firstrow", tablefmt = "grid")
      print(table1)
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
  print("Não implementado.")
  
def prodRemoving():
  print("Não implementado.")

def prodUpdating():
  print("Não implementado.")

def prodSearching():
  print("Não implementado.")
