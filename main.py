import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os

# Inicia Serviço do Chrome
chromeService = ChromeService("/Applications/Google/Chrome.app")
driver = webdriver.Chrome()

# Cria a estrutura do DB e adiciona o cabeçalho
questionDB = [
  [
  "index",
  "Subspecialty",
  "Question Number",
  "Question Text",
  "Question Images",
  "Alternatives",
  "Correct Alternative",
  "Explanation",
  "Reference",
  "Question Link"
  ]
]

# Uso uma estrutura de try/finally para garantir que o driver será fechado ao final da execução
try:

  # Verifica se o arquivo já existe para deletá-lo no começo da execução, caso não o façá, o arquivo não é criado ao final do script
  if os.path.exists('pathologyDB.csv'):
    os.remove('pathologyDB.csv')
  

  # Loop para percorrer todas as páginas de questões
  for i in range(1, 6):
    # Abre a página de questões colocando o número da página no final da URL
    url = "https://www.pathologyoutlines.com/review-questions?sid="+str(i)
    driver.get(url)

    # Espera até que alguns elementos estejam presentes na página para garantir que a página foi carregada antes de tentar extrair os dados
    wait = WebDriverWait(driver, 2)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "f12b")))
    wait.until(EC.presence_of_element_located((By.ID, "po_banner_bottom")))


    # Extrai o elemento select que contém a subespecialidade selecionada
    selectElement = driver.find_element(By.ID, "sid")
    selectObject = Select(selectElement)
    selectedSubspetiality = selectObject.first_selected_option.text.split(" (")[0] # Remove o número de questões da subespecialidade


    # Busca todos os elementos HTML dos blocos de questões, cria um array com esses elementos
    questionBlocks = driver.find_elements(By.CLASS_NAME, "block_content")

    # Imprime no terminal algumas informações no início de cada página
    print( "QUESTÕES DA PÁGINA " + str(i) + "!!!")
    print(driver.title)
    print("SUBSPECIALTY: " + selectedSubspetiality)

    # Espera alguns segundos para que o usuário possa ver as informações no terminal
    time.sleep(5)

    # Loop para percorrer todas as questões da página atual
    for question in range(0, 10):
    # for question in range(0, len(questionBlocks)):

      # Cria uma variável para armazenar o bloco de questão atual e um array vazio para armazenar as informações da questão que iremos coletar
      currentQuestion = questionBlocks[question]
      questionArray = []

      # Adiciona o index da questão no array
      index = len(questionDB)
      questionArray.append(index)

      # Adiciona a subespecialidade da questão no array
      questionArray.append(selectedSubspetiality)

      # Busca o título da questão para extrair dele o número da questão e adiciona ao array
      questionTitleElement = currentQuestion.find_element(By.CLASS_NAME, "f12b")
      questionNumber = questionTitleElement.text.split(" ")[1]
      questionArray.append(questionNumber)

      # Extrai e trata o texto da questão e adiciona ao array (pode apresentar diferentes resultados pois a página não segue um padrão para a formatação do texto) 
      blockBody = currentQuestion.find_element(By.CLASS_NAME, "block_body")
      full_text_before_list = blockBody.get_attribute("innerText")
      splitedText = full_text_before_list.split("\n")
      rejoinedText = " ".join(splitedText)
      questionArray.append(rejoinedText)

      # Extrai a URL das imagens e cria um array de URLs para as imagens da questão
      questionImages = currentQuestion.find_elements(By.TAG_NAME, "img")
      imageArray = []
      for image in questionImages:
        imageArray.append(image.get_attribute('src'))
      questionArray.append(imageArray)

      # Extrai e trata as alternativas da questão e adiciona ao array
      alternatives = currentQuestion.find_element(By.CLASS_NAME, "liststyle2").find_elements(By.TAG_NAME, "li")
      alternativesArray = []

      # Atribui uma letra à alternativa e adiciona ao array
      for alternative in range(0, len(alternatives)):
        aleternativeLetter = ""
        match alternative:
          case 0:
            aleternativeLetter = "A"
          case 1:
            aleternativeLetter = "B"
          case 2:
            aleternativeLetter = "C"
          case 3:
            aleternativeLetter = "D"
          case 4:
            aleternativeLetter = "E"
          case 5:
            aleternativeLetter = "F"
          case 6:
            aleternativeLetter = "G"
          case 7:
            aleternativeLetter = "H"
          case 8:
            aleternativeLetter = "I"
          case 9:
            aleternativeLetter = "J"

        alternativesArray.append(aleternativeLetter + ") " + alternatives[alternative].text)
      questionArray.append(alternativesArray)

      # Busca o bloco de resposta para extrair dele a resposta correta, a explicação e a referência
      answerBlockHTML = currentQuestion.find_element(By.CLASS_NAME, "answer_block").get_attribute("innerHTML")

      # Extrair a letra entre as tags <b> para determinar a alternativa correta e adiciona ao array
      start_b_tag = answerBlockHTML.find('<b>') + 3
      end_b_tag = answerBlockHTML.find('</b>')
      letra_alternativa = answerBlockHTML[start_b_tag:end_b_tag].strip('.')
      questionArray.append(letra_alternativa)


      # Extrair o texto após a primeira tag </b> até o próximo <br> para extrair a explicação e adiciona ao array
      resto_resposta_start = end_b_tag + 4
      resto_resposta_end = answerBlockHTML.find('<br>', resto_resposta_start)
      resto_resposta = answerBlockHTML[resto_resposta_start:resto_resposta_end].strip().replace("\n", " ").replace(";", "|")
      questionArray.append(resto_resposta)

      # Extrair o link da referência e adiciona ao array
      href_index = answerBlockHTML.find('Reference: <a href="') + 20
      link_end_index = answerBlockHTML.find('"', href_index)
      link_referencia = answerBlockHTML[href_index:link_end_index]
      questionArray.append(link_referencia)

      # Adiciona a URL da questão ao array
      questionArray.append(url)
      
      # Espera um tempo para as questões não rolarem tão rapidamente no terminal
      time.sleep(0.0005)

      # Adiciona o array da questão ao DB de questões
      questionDB.append(questionArray)

      # Imprime no terminal as informações da questão
      print(questionNumber)
      pprint.pprint(questionArray)
      print("")
      print("")
      time.sleep(0.005)
      #FIM DO LOOP DE QUESTÕES DE UMA PÁGINA

    # Imprime no terminal que a página foi finalizada
    print('''
          

          PRÓXIMA PÁGINA!!!


          ''')
    time.sleep(5)
    #FIM DO LOOP DE PÁGINAS
    
    # Ao final do loop de todas as páginas, escreve o DB de questões em um arquivo CSV
    with open('pathologyDB.csv', mode= 'w') as file:
      writer = csv.writer(file)
      writer.writerows(questionDB)


finally:
  # Fecha o driver ao final da execução
  driver.quit()