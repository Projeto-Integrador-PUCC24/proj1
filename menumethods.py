import time, os
from db import host, user, password, database
from main import conn, menuShow
from sys import stdout
import tabulate, mysql.connector, ctypes


def pushProduct(cod, nome, desc, cp, ip, cf, cv, ml):
  if conn != None:
      cursor = conn.cursor() #cria um 'cursor', que permite que você interaja com o banco
      sql = "INSERT INTO products (`cod`, `nome`, `desc`, `cp`, `ip`, `cf`, `cv`, `ml`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" #criação da query
      vals = (cod, nome, desc, cp, ip, cf, cv, ml) #valores da query para impedir SQL Injection
      cursor.execute(sql, vals) #executa a query utilizando os valores
      conn.commit()#'commit' necessario para fazer alterações no banco
      cursor.close()#fecha o cursor
  else:
    print("Produto não foi adicionado. Por favor, tente novamente.")


    
def prodAdding():
  while True:
    try:
      product_id = input("Insira o código do produto: ")
      product_id = int(product_id)
      if(product_id <= 0):
        print("\n\nCódigo inválido!")
        continue
      product_name = input("Insira o nome do produto: ")
      product_desc = input("Insira uma breve descrição do produto: ")
      product_cost = float(input("Insira o custo do produto: "))
      if (product_cost <= 0):
        print("\n\Valor inválido!")
        continue
      product_cf_percent = float(input("Insira o custo fixo do produto: "))
      if (product_cf_percent <= 0):
        print("\n\Valor inválido!")
        continue
      product_cv_percent = float(input("Insira a comissão de vendas: "))
      if (product_cv_percent <= 0):
        print("\n\Valor inválido!")
        continue
      product_tax_percent = float(input("Insira o valor dos impostos: "))
      if (product_tax_percent <= 0):
        print("\n\Valor inválido!")
        continue
      product_ml_percent = float(input("Insira a rentabilidade/margem de lucro: "))
      sellingPrice = product_cost / (1 - ((product_cf_percent + product_cv_percent + product_tax_percent + product_ml_percent) / 100)) 
      sellingPrice_percent = (sellingPrice / sellingPrice) * 100
      grossIncome = sellingPrice - product_cost
      grossIncome_percent = (grossIncome / sellingPrice) * 100
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
      product_cost_percent = (product_cost / sellingPrice) * 100
      productDetails = [["Descrição", "Valor", "%"],["Preço de Venda", round(sellingPrice,2), sellingPrice_percent],
            ["Custo de aquisição", round(product_cost,2), product_cost_percent ],
            ["Receita Bruta", round(grossIncome, 2), grossIncome_percent],
            ["Custo Fixo", round(product_cf,2), product_cf_percent],
            ["Comissão de Vendas", round(product_cv,2), product_cv_percent],
            ["Impostos", round(product_tax,2), product_tax_percent],
            ["Outros custos",round(others,2), others_percent], 
            ["Rentabilidade", round(product_ml,2), product_ml_percent],
            ["Descrição da Margem de Lucro", product_mlDesc, product_ml_percent]
            ]
      table1 = tabulate.tabulate(productDetails,headers = "firstrow", tablefmt = "grid")#cria uma tabela usando a biblioteca tabulate
      print(table1)
      products = [["Código", "Preço de Venda", "Margem de Lucro"],[product_id, round(sellingPrice,2), round(product_ml,2)]]
      pushProduct(product_id, product_name, product_desc, product_cost, product_tax_percent, product_cf_percent, product_cv_percent, product_ml_percent) #envia o produto para o banco de dados através da função criada
      print("\n\nProduto adicionado com sucesso!")
      print("\n\nDeseja adicionar outro produto?")
      answer = input("[1] Sim\n[2] Não\n")
      if answer == "1":
        prodAdding()
      else:
        menuShow() 
      break
    except ValueError:
      print("\n\nValor inválido! Por favor, tente novamente.")
      prodAdding()

def prodListing():
  try:
    os.system('cls')
    cursor = conn.cursor()#cria um 'cursor', que permite que você interaja com o banco
    cursor.execute("SELECT * FROM products")#define a query
    result = cursor.fetchall()#executa o metodo 'fetchall', que retorna todos os resultados da query
    for row in result: #itera o resultado
      if (row[7] > 20):
        ml_desc = "Lucro alto"
      elif (row[7] > 10 and row[7] <= 20):
        ml_desc = "Lucro médio"
      elif (row[7] > 0 and row[7] < 10):
        ml_desc = "Lucro baixo"
      elif (row[7] == 0):
        ml_desc = "Equilíbrio"
      elif (row[7] < 0):
        ml_desc = "Prejuízo"  
      sellingPrice = row[3] / (1 - ((row[5] + row[6] + row[4] + row[7]) / 100))
      grossIncome = sellingPrice - row[3]
      others = row[5] + row[6] + row[4]
      netIncome = grossIncome - others
      product_cost = row[3]
      product_tax = row[4]
      product_cf = row[5]
      product_cv = row[6]
      product_ml = row[7]
      sellingPrice_percent = (sellingPrice / sellingPrice) * 100
      product_cost_percent = (product_cost / sellingPrice) * 100
      grossIncome_percent = (grossIncome / sellingPrice) * 100
      product_tax_percent = (product_tax * sellingPrice) / 100
      product_cf_percent = (product_cf * sellingPrice) / 100
      product_cv_percent = (product_cv * sellingPrice) / 100
      others_percent = (others * sellingPrice) / 100
      product_ml_percent = (sellingPrice * product_ml) /100
      
      prodDetails = [["Código", row[0], ],
                ["Nome", row[1], ],
                ["Descrição", row[2], ],
                ["Preço de Venda", round(sellingPrice,2), sellingPrice_percent],
                ["Custo", round(product_cost,2), product_cost_percent],
                ["Receita Bruta", round(grossIncome,2), grossIncome_percent],
                ["Custo Fixo", round(product_cf_percent,2), product_cf],
                ["Comissão de Vendas", round(product_cv_percent,2), product_cv],
                ["Impostos", round(product_tax_percent,2), product_tax],
                ["Outros custos", round(others_percent,2), others],
                ["Margem de Lucro", round(product_ml_percent,2), product_ml],
                ["Descrição da Margem de Lucro",ml_desc]]
      table = tabulate.tabulate(prodDetails, headers = ["Descrição", "Valor", "%"], tablefmt = "grid")
      print(table)
    cursor.close()
    print("\n\nDeseja conferir os produtos novamente?")
    answer = input("[1] Sim\n[2] Não\n")
    if answer == "1":
      os.system('cls')
      prodListing()
    else:
      menuShow()
  except ValueError:
    print("\n\nValor inválido. Por favor, tente novamente.")
    os.system("cls")  
    prodListing()
  
def prodRemoving():
  cursor = conn.cursor()
  searchCode = (input("Insira o código do produto que deseja excluir(0 para retornar ao menu): "))
  if (searchCode == "0"):
    menuShow()
  else:
    sql = "SELECT * FROM `products` WHERE cod = %s"#cria query
    val = (searchCode, )#valores da query
    cursor.execute(sql, val)#executa query com os valores
    result = cursor.fetchall()
    if not result:
      print("\n\nProduto não encontrado.")
      prodRemoving()
    for row in result: #itera resultado
        if (row[7] > 20):
          ml_desc = "Lucro alto"
        elif (row[7] > 10 and row[7] <= 20):
          ml_desc = "Lucro médio"
        elif (row[7] > 0 and row[7] < 10):
          ml_desc = "Lucro baixo"
        elif (row[7] == 0):
          ml_desc = "Equilíbrio"
        elif (row[7] < 0):
          ml_desc = "Prejuízo"  
        sellingPrice = row[3] / (1 - ((row[5] + row[6] + row[4] + row[7]) / 100))
        grossIncome = sellingPrice - row[3]
        others = row[5] + row[6] + row[4]
        product_cost = row[3]
        product_tax = row[4]
        product_cf = row[5]
        product_cv = row[6]
        product_ml = row[7]
        sellingPrice_percent = (sellingPrice / sellingPrice) * 100
        product_cost_percent = (product_cost / sellingPrice) * 100
        grossIncome_percent = (grossIncome / sellingPrice) * 100
        product_tax_percent = (product_tax * sellingPrice) / 100
        product_cf_percent = (product_cf * sellingPrice) / 100
        product_cv_percent = (product_cv * sellingPrice) / 100
        others_percent = (others * sellingPrice) / 100
        product_ml_percent = (sellingPrice * product_ml) /100
        prodDetails = [["Código", row[0], ],
                  ["Nome", row[1], ],
                  ["Descrição", row[2], ],
                  ["Preço de Venda", round(sellingPrice,2), sellingPrice_percent],
                  ["Custo", round(product_cost,2), product_cost_percent],
                  ["Receita Bruta", round(grossIncome,2), grossIncome_percent],
                  ["Custo Fixo", round(product_cf_percent,2), product_cf],
                  ["Comissão de Vendas", round(product_cv_percent,2), product_cv],
                  ["Impostos", round(product_tax_percent,2), product_tax],
                  ["Outros custos", round(others_percent,2), others],
                  ["Margem de Lucro", round(product_ml_percent,2), product_ml],
                  ["Descrição da Margem de Lucro",ml_desc]] #cria lista com valores de produto
        table = tabulate.tabulate(prodDetails, headers = ["Descrição", "Valor", "%"], tablefmt = "grid") #cria uma tabela usando a biblioteca 'tabulate' e a lista 'prodDetails'
        print(table)
    ans = input("\n\nEsse é o produto que você deseja remover? [1] Sim [2] Não\n")
    match ans:
      case "1":
        sql = "DELETE FROM `products` WHERE cod = %s"#cria query
        val = (searchCode, )#valores da query
        cursor.execute(sql, val)#executa query com valores
        conn.commit()
        print("\n\n" + str(cursor.rowcount) + " produto removido com sucesso.")
        cursor.close()
        menuShow()
      case "2":
        prodRemoving()
      
def prodUpdating():
    try:
      cursor = conn.cursor()
      searchCode = int(input("Insira o código do produto que deseja atualizar(Insira 0 para retornar ao menu): "))
      if (searchCode <= 0):
        menuShow()
      else:
        sql = "SELECT * FROM `products` WHERE cod = %s"
        val = (searchCode, )
        cursor.execute(sql, val)
        result = cursor.fetchall()
        for row in result:
          if (row[7] > 20):
            ml_desc = "Lucro alto"
          elif (row[7] > 10 and row[7] <= 20):
            ml_desc = "Lucro médio"
          elif (row[7] > 0 and row[7] < 10):
            ml_desc = "Lucro baixo"
          elif (row[7] == 0):
            ml_desc = "Equilíbrio"
          elif (row[7] < 0):
            ml_desc = "Prejuízo"  
        sellingPrice = row[3] / (1 - ((row[5] + row[6] + row[4] + row[7]) / 100))
        grossIncome = sellingPrice - row[3]
        others = row[5] + row[6] + row[4]
        product_cost = row[3]
        product_tax = row[4]
        product_cf = row[5]
        product_cv = row[6]
        product_ml = row[7]
        sellingPrice_percent = (sellingPrice / sellingPrice) * 100
        product_cost_percent = (product_cost / sellingPrice) * 100
        grossIncome_percent = (grossIncome / sellingPrice) * 100
        product_tax_percent = (product_tax * sellingPrice) / 100
        product_cf_percent = (product_cf * sellingPrice) / 100
        product_cv_percent = (product_cv * sellingPrice) / 100
        others_percent = (others * sellingPrice) / 100
        product_ml_percent = (sellingPrice * product_ml) /100
        prodDetails = [["Código", row[0], ],
                  ["Nome", row[1], ],
                  ["Descrição", row[2], ],
                  ["Preço de Venda", round(sellingPrice,2), sellingPrice_percent],
                  ["Custo", round(product_cost,2), product_cost_percent],
                  ["Receita Bruta", round(grossIncome,2), grossIncome_percent],
                  ["Custo Fixo", round(product_cf_percent,2), product_cf],
                  ["Comissão de Vendas", round(product_cv_percent,2), product_cv],
                  ["Impostos", round(product_tax_percent,2), product_tax],
                  ["Outros custos", round(others_percent,2), others],
                  ["Margem de Lucro", round(product_ml_percent,2), product_ml],
                  ["Descrição da Margem de Lucro",ml_desc]]
        table = tabulate.tabulate(prodDetails, headers = ["Descrição", "Valor", "%"], tablefmt = "grid")
        print(table)
        ans = input("\n\nEsse é o produto que você deseja atualizar? [1] Sim [2] Não\n")
        match ans:
          case "2":
            prodUpdating()
          case "1":
              while True:
                desired = int(input("O que você deseja atualizar?\n[1] Nome\n[2] Descrição\n[3] Custo\n[4] Impostos\n[5] Custo Fixo\n[6] Comissão de Vendas\n[7] Margem de Lucro\n[8] Cancelar\n"))
                match desired:
                  case 1:
                    cursor = conn.cursor()
                    newName = input("Insira o novo nome do produto: ")
                    sql = "UPDATE `products` SET nome = %s WHERE cod = %s"
                    val = (newName, searchCode)
                    cursor.execute(sql, val)
                    conn.commit()
                    print("\n\n" + str(cursor.rowcount) + " produto atualizado com sucesso.")
                    cursor.close()
                  case 2:
                    cursor = conn.cursor()
                    newDesc = input("Insira a nova descrição do produto: ")
                    sql = "UPDATE `products` SET `desc` = %s WHERE cod = %s"
                    val = (newDesc, searchCode)
                    cursor.execute(sql, val)
                    conn.commit()
                    print("\n\n" + str(cursor.rowcount) + " produto atualizado com sucesso.")
                    cursor.close()
                  case 3:
                    cursor = conn.cursor()
                    newCost = float(input("Insira o novo custo do produto: "))
                    sql = "UPDATE `products` SET cp = %s WHERE cod = %s"
                    val = (newCost, searchCode)
                    cursor.execute(sql, val)
                    conn.commit()
                    print("\n\n" + str(cursor.rowcount) + " produto atualizado com sucesso.")
                    cursor.close()
                  case 4:
                    cursor = conn.cursor()
                    newTax = float(input("Insira o novo valor dos impostos: "))
                    sql = "UPDATE `products` SET ip = %s WHERE cod = %s"
                    val = (newTax, searchCode)
                    cursor.execute(sql, val)
                    conn.commit()
                    print("\n\n" + str(cursor.rowcount) + " produto atualizado com sucesso.")
                    cursor.close()
                  case 5:
                    cursor = conn.cursor()
                    newCF = float(input("Insira o novo custo fixo do produto: "))
                    sql = "UPDATE `products` SET cf = %s WHERE cod = %s"
                    val = (newCF, searchCode)
                    cursor.execute(sql, val)
                    conn.commit()
                    print("\n\n" + str(cursor.rowcount) + " produto atualizado com sucesso.")
                    cursor.close()
                  case 6:
                    cursor = conn.cursor()
                    newCV = float(input("Insira a nova comissão de vendas: "))
                    sql = "UPDATE `products` SET cv = %s WHERE cod = %s"
                    val = (newCV, searchCode)
                    cursor.execute(sql, val)
                    conn.commit()
                    print("\n\n" + str(cursor.rowcount) + " produto atualizado com sucesso.")
                    cursor.close()
                  case 7:
                    cursor = conn.cursor()
                    newML = float(input("Insira a nova margem de lucro: "))
                    sql = "UPDATE `products` SET ml = %s WHERE cod = %s"
                    val = (newML, searchCode)
                    cursor.execute(sql, val)
                    conn.commit()
                    print("\n\n" + str(cursor.rowcount) + " produto atualizado com sucesso.")
                    cursor.close()
                  case 8:
                    menuShow()
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
          menuShow()
      for row in result:
        if (row[7] > 20):
          ml_desc = "Lucro alto"
        elif (row[7] > 10 and row[7] <= 20):
          ml_desc = "Lucro médio"
        elif (row[7] > 0 and row[7] < 10):
          ml_desc = "Lucro baixo"
        elif (row[7] == 0):
          ml_desc = "Equilíbrio"
        elif (row[7] < 0):
          ml_desc = "Prejuízo"  
      sellingPrice = row[3] / (1 - ((row[5] + row[6] + row[4] + row[7]) / 100))
      grossIncome = sellingPrice - row[3]
      others = row[5] + row[6] + row[4]
      product_cost = row[3]
      product_tax = row[4]
      product_cf = row[5]
      product_cv = row[6]
      product_ml = row[7]
      sellingPrice_percent = (sellingPrice / sellingPrice) * 100
      product_cost_percent = (product_cost / sellingPrice) * 100
      grossIncome_percent = (grossIncome / sellingPrice) * 100
      product_tax_percent = (product_tax * sellingPrice) / 100
      product_cf_percent = (product_cf * sellingPrice) / 100
      product_cv_percent = (product_cv * sellingPrice) / 100
      others_percent = (others * sellingPrice) / 100
      product_ml_percent = (sellingPrice * product_ml) /100
      prodDetails = [["Código", row[0], ],
                ["Nome", row[1], ],
                ["Descrição", row[2], ],
                ["Preço de Venda", round(sellingPrice,2), sellingPrice_percent],
                ["Custo", round(product_cost,2), product_cost_percent],
                ["Receita Bruta", round(grossIncome,2), grossIncome_percent],
                ["Custo Fixo", round(product_cf_percent,2), product_cf],
                ["Comissão de Vendas", round(product_cv_percent,2), product_cv],
                ["Impostos", round(product_tax_percent,2), product_tax],
                ["Outros custos", round(others_percent,2), others],
                ["Margem de Lucro", round(product_ml_percent,2), product_ml],
                ["Descrição da Margem de Lucro",ml_desc]]
      table = tabulate.tabulate(prodDetails, headers = ["Descrição", "Valor", "%"], tablefmt = "grid")
      print(table)
      print("\n\nDeseja buscar por outro produto?")
      answer = input("[1] Sim\n[2] Não\n")
      if answer == "1":
        prodSearching()
      elif answer == "2":
        menuShow()
      else:
        print("\n\nOpção inválida. Por favor, tente novamente.")
    except ValueError:
      print("\n\nValor inválido. Por favor, tente novamente.")