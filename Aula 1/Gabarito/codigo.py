import pyautogui 
import time

# pyautogui -> fazer automações com python
# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar uma tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas (ex. "ctrl", "c")

pyautogui.PAUSE = 1 # quero fazer uma pausa entre cada comando de meio segundo

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")  
pyautogui.press("enter")


# digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# esperar 3 segundos
time.sleep(3)

# Passo 2: Fazer login
# preencher emaik
pyautogui.click(x=409, y=407)
pyautogui.write("rafael@gmail.com")

# preencher a senha
pyautogui.press("tab")
pyautogui.write("12345678")

# botão logar
pyautogui.press("enter")

# esperando 3 segundos por segurança e fechando o verificador de senha
time.sleep(2)
pyautogui.click(x=861, y=375)
pyautogui.press("enter")
5.0   
# Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv(r"d:\ProjetosGit\Python Power Up\Gabarito\produtos.csv")

# Passo 4: Cadastrar 1 produto
for linha in tabela.index: # para cada linha da minha tabela fazer tudo o que está abaixo
   pyautogui.click(x=394, y=292)

   codigo = tabela.loc[linha, "codigo"]
   pyautogui.write(codigo)

   pyautogui.press("tab") # passar para o próximo campo
   marca = tabela.loc[linha, "marca"]
   pyautogui.write(marca)

   pyautogui.press("tab") # passar para o próximo campo
   tipo = tabela.loc[linha, "tipo"]
   pyautogui.write(tipo)

   pyautogui.press("tab") # passar para o próximo campo
   categoria = str(tabela.loc[linha, "categoria"]) #transformar o numero para texto
   pyautogui.write(categoria)

   pyautogui.press("tab") # passar para o próximo campo
   preco_unitario = str(tabela.loc[linha, "preco_unitario"])
   pyautogui.write(preco_unitario)

   pyautogui.press("tab") # passar para o próximo campo
   custo = str(tabela.loc[linha, "custo"])
   pyautogui.write(custo)

   pyautogui.press("tab") # passar para o próximo campo
   obs = tabela.loc[linha, "obs"]

   if not pandas.isna(obs):
      pyautogui.write(str(obs))


   pyautogui.press("tab") # passou para o botao enviar
   pyautogui.press("enter")

   pyautogui.scroll(10000)

# Passo 5: Repetir para todos os produtos


