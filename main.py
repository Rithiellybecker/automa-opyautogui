#programar um codigo para mandar o abc inteiro 6 vezes para a luana 

import pyautogui
import time

pyautogui.PAUSE= 0.8

pyautogui.press('win')
pyautogui.write('crhome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=534, y=377)
pyautogui.write('teste@gmai.com')
pyautogui.press('tab')
pyautogui.write('aaaaaaaaa')
pyautogui.press('tab')
pyautogui.press('enter')

import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:

    pyautogui.click(x=547, y=255)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press('tab')
    
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')
    
    
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press('tab')
    
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press('tab')
    
    pyautogui.click(x=591, y=565)
    pyautogui.scroll(1000)

