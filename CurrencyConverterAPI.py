import tkinter as tk
from bs4 import BeautifulSoup
from Scrapper import Currencyscrapper
import requests

#Variáveis

screen = tk.Tk() #Instancia a classe Tk como a variável 'screen'
screen.title('CurrencyConverter') #Seta o title da janela
screen.geometry('350x200') #Seta o tamanho da janela
screen.resizable(False,False) #Torna a API não redimensionável
screen.tk.call('wm', 'iconphoto', screen._w, tk.PhotoImage(file='/home/smokedy/PythonProjects/CurrencyConverter/Images/Coin.png')) #Seta o Ícone da janela
moedas = []
with open('Currencies.txt','r') as Currencies_file:
    for line in Currencies_file:
        moedas.append(line.strip())
moedas.sort()
moedainicial_type = tk.StringVar(screen)
moedafinal_type = tk.StringVar(screen)
resultado = tk.StringVar(screen)
resultado.set(0)
quantity= tk.StringVar(screen)


#Widgets
    #Botões
botao_calcular = tk.Button(screen, 
    text='Calculate',
    command=lambda: Currencyscrapper(quantity.get(),moedainicial_type.get(),moedafinal_type.get(),resultado)
    ).place(
        x=180,
        y=160
    )
    #Labels
label_moeda_inicial = tk.Label(screen, 
    text='Initial Currency:',
    font='times 14',
    ).place(
        x=11,
        y=50
    )
label_moeda_final = tk.Label(screen,
    text='Final Currency:',
    font='times 14',
    ).place(
        x=16.5,
        y=125
    )
label_resultado = tk.Label(screen,
    textvariable=resultado,
    font='arial 12',
    ).place(
        x=140,
        y=123
    )
    #Text_Inputs
input_quantidade = tk.Entry(screen,
    width=15,
    textvariable=quantity,
).place(
    y=47,
    x=135
)
    #Option_menus
optionmenu_moeda_inicial = tk.OptionMenu(screen,moedainicial_type,*moedas).place(
    x=265,
    y=40
)
optionmenu_moeda_final = tk.OptionMenu(screen,moedafinal_type,*moedas).place(
    x=265,
    y=115,
)
screen.mainloop()



