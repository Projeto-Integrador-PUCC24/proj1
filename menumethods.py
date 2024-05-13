import time
from db import host, user, password, database
from main import conn, menu,  cls
import tabulate, mysql.connector, ctypes


def pushProduct(cod, nome, desc, cp, ip, cf, cv, ml):
  if conn != None:
      '''cursor = conn.cursor()
      sql = "SHOW TABLES LIKE `products`"
      cursor.execute(sql)
      result = cursor.fetchone()
      if result:'''
      cursor = conn.cursor()
      sql = "INSERT INTO products (`cod`, `nome`, `desc`, `cp`, `ip`, `cf`, `cv`, `ml`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
      vals = (cod, nome, desc, cp, ip, cf, cv, ml)
      cursor.execute(sql, vals)
      conn.commit()
      cursor.close()
  else:
    print("Produto não foi adicionado. Por favor, tente novamente.")


    
def prodAdding():
  while True:
    try:
      product_id = input("Insira o código do produto: ")
      product_id = int(product_id)
      if(product_id < 0):
        print("\n\nCódigo inválido!")
        prodAdding()
      product_name = input("Insira o nome do produto: ")
      product_desc = input("Insira uma breve descrição do produto: ")
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
      productDetails = [["Descrição", "Valor", "%"],["Preço de Venda", round(sellingPrice,2), 100],
            ["Custo de aquisição", round(product_cost,2), sellingPrice_percent ],
            ["Receita Bruta", round(grossIncome, 2), grossIncome_percent],
            ["Custo Fixo", round(product_cf,2), product_cf_percent],
            ["Comissão de Vendas", round(product_cv,2), product_cv_percent],
            ["Impostos", round(product_tax,2), product_tax_percent],
            ["Outros custos",round(others,2), others_percent], 
            ["Rentabilidade", round(product_ml,2), product_ml_percent],
            ["Descrição da Margem de Lucro", product_mlDesc, product_ml_percent]
            ]
      table2 = tabulate.tabulate(productDetails,headers = "firstrow", tablefmt = "github")
      print(table2)
      products = [["Código", "Preço de Venda", "Margem de Lucro"],[product_id, round(sellingPrice,2), round(product_ml,2)]]

      print("\n\nVisão geral: ")
      table1 = tabulate.tabulate(products,headers = "firstrow", tablefmt = "github")
      print(table1)
      pushProduct(product_id, product_name, product_desc, product_cost, product_tax_percent, product_cf_percent, product_cv_percent, product_ml_percent)
      print("\n\nProduto adicionado com sucesso!")
      print("\n\nDeseja adicionar outro produto?")
      answer = input("[1] Sim\n[2] Não\n")
      if answer == "1":
        prodAdding()
      else:
        menu() 
      break
    except ValueError:
      print("\n\nValor inválido! Por favor, tente novamente.")
      prodAdding()

def prodListing():
  while True:
    try:
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM products")
      result = cursor.fetchall()     
      prodDetails = [["Código", "Nome", "Descrição", "Custo", "Impostos", "Custo Fixo", "Comissão de Vendas", "Margem de Lucro"]]
      for row in result:
        prodDetails.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])
        table = tabulate.tabulate(prodDetails, headers = "firstrow", tablefmt = "grid")
      print(table)
      cursor.close()
      print("\n\nDeseja conferir os produtos novamente?")
      answer = input("[1] Sim\n[2] Não\n")
      if answer == "1":
        prodListing()
      else:
        menu()
      break
    except ValueError:
      print("\n\nValor inválido. Por favor, tente novamente.")
      prodListing()
  
def prodRemoving():
  cursor = conn.cursor()
  searchCode = (input("Insira o código do produto que deseja excluir: "))
  sql = "SELECT * FROM `products` WHERE cod = %s"
  val = (searchCode, )
  cursor.execute(sql, val)
  result = cursor.fetchall()
  prodDetails = [["Código", "Nome", "Descrição", "Custo", "Impostos", "Custo Fixo", "Comissão de Vendas", "Margem de Lucro"]]
  if not result:
    print("\n\nProduto não encontrado.")
    prodRemoving()
  for row in result:
    prodDetails.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])
    table = tabulate.tabulate(prodDetails, headers = "firstrow", tablefmt = "grid")
  print(table)
  ans = input("\n\nEsse é o produto que você deseja remover? [1] Sim [2] Não\n")
  match ans:
    case "1":
      sql = "DELETE FROM `products` WHERE cod = %s"
      val = (searchCode, )
      cursor.execute(sql, val)
      conn.commit()
      print("\n\n" + str(cursor.rowcount) + " produto removido com sucesso.")
      cursor.close()
      
def prodUpdating():
  while True:
    try:
      cursor = conn.cursor()
      searchCode = (input("Insira o código do produto que deseja atualizar: "))
      sql = "SELECT * FROM `products` WHERE cod = %s"
      val = (searchCode, )
      cursor.execute(sql, val)
      result = cursor.fetchall()
      prodDetails = [["Código", "Nome", "Descrição", "Custo", "Impostos", "Custo Fixo", "Comissão de Vendas", "Margem de Lucro"]]
      for row in result:
        prodDetails.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])
        table = tabulate.tabulate(prodDetails, headers = "firstrow", tablefmt = "grid")
      print(table)
      ans = input("\n\nEsse é o produto que você deseja atualizar? [1] Sim [2] Não\n")
      match ans:
        case "2":
          prodUpdating()
        case "1":
          desired = int(input("O que você deseja atualizar?\n[1] Nome\n[2] Descrição\n[3] Custo\n[4] Impostos\n[5] Custo Fixo\n[6] Comissão de Vendas\n[7] Margem de Lucro\n[8] Cancelar\n"))
          match desired:
            case 1:
              newName = input("Insira o novo nome do produto: ")
              sql = "UPDATE `products` SET nome = %s WHERE cod = %s"
              val = (newName, searchCode)
              cursor.execute(sql, val)
              conn.commit()
              print("\n\n" + str(cursor.rowcount) + " produto atualizado com sucesso.")
              cursor.close()
              break
            case 2:
              newDesc = input("Insira a nova descrição do produto: ")
              sql = "UPDATE `products` SET `desc` = %s WHERE cod = %s"
              val = (newDesc, searchCode)
              cursor.execute(sql, val)
              conn.commit()
              print("\n\n" + str(cursor.rowcount) + " produto atualizado com sucesso.")
              cursor.close()
              break
            case 3:
              newCost = float(input("Insira o novo custo do produto: "))
              sql = "UPDATE `products` SET cost = %s WHERE cod = %s"
              val = (newCost, searchCode)
              cursor.execute(sql, val)
              conn.commit()
              print("\n\n" + str(cursor.rowcount) + " produto atualizado com sucesso.")
              cursor.close()
              break
            case 4:
              newTax = float(input("Insira o novo valor dos impostos: "))
              sql = "UPDATE `products` SET tax = %s WHERE cod = %s"
              val = (newTax, searchCode)
              cursor.execute(sql, val)
              conn.commit()
              print("\n\n" + str(cursor.rowcount) + " produto atualizado com sucesso.")
              cursor.close()
              break
            case 5:
              newCF = float(input("Insira o novo custo fixo do produto: "))
              sql = "UPDATE `products` SET cf = %s WHERE cod = %s"
              val = (newCF, searchCode)
              cursor.execute(sql, val)
              conn.commit()
              print("\n\n" + str(cursor.rowcount) + " produto atualizado com sucesso.")
              cursor.close()
              break
            case 6:
              newCV = float(input("Insira a nova comissão de vendas: "))
              sql = "UPDATE `products` SET cv = %s WHERE cod = %s"
              val = (newCV, searchCode)
              cursor.execute(sql, val)
              conn.commit()
              print("\n\n" + str(cursor.rowcount) + " produto atualizado com sucesso.")
              cursor.close()
              break
            case 7:
              newML = float(input("Insira a nova margem de lucro: "))
              sql = "UPDATE `products` SET ml = %s WHERE cod = %s"
              val = (newML, searchCode)
              cursor.execute(sql, val)
              conn.commit()
              print("\n\n" + str(cursor.rowcount) + " produto atualizado com sucesso.")
              cursor.close()
              break
          cursor.close()
        case _:
          print("\n\nOpção inválida. Por favor, tente novamente.")
    except ValueError:
      print("\n\nValor inválido. Por favor, tente novamente.")
      prodUpdating()

def prodSearching():
   while True:
    try:
      cursor = conn.cursor()
      searchCode = (input("Insira o código do produto que deseja ver: "))
      sql = "SELECT * FROM `products` WHERE cod = %s"
      val = (searchCode, )
      cursor.execute(sql, val)
      result = cursor.fetchall()
      prodDetails = [["Código", "Nome", "Descrição", "Custo", "Impostos", "Custo Fixo", "Comissão de Vendas", "Margem de Lucro"]]
      if not result:
        print("\n\nProduto não encontrado.")
        print("\n\nDeseja buscar por outro produto?")
        answer = input("[1] Sim\n[2] Não\n")
        if answer == "1":
          prodSearching()
        else:
          menu()
      for row in result:
        prodDetails.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])
        table = tabulate.tabulate(prodDetails, headers = "firstrow", tablefmt = "grid")
      print(table)
      ans = input("\n\nEsse é o produto que você deseja ver? [1] Sim [2] Não\n")
      if ans == "2":
        print("\n\nDeseja buscar por outro produto?")
        answer = input("[1] Sim\n[2] Não\n")
        if answer == "1":
          prodSearching()
        else:
          menu()
      elif ans == "1":
        cursor.close()
        print("\n\nDeseja buscar por outro produto?")
        answer = input("[1] Sim\n[2] Não\n")
        if answer == "1":
          prodSearching()
        else:
          menu()
      else:
        print("\n\nOpção inválida. Por favor, tente novamente.")
    except ValueError:
      print("\n\nValor inválido. Por favor, tente novamente.")