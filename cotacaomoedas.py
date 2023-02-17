import requests
from tkinter import *
#Definindo a Função
def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    #Aqui tranformamos o json para python em um dicionario e guardamos em uma variavel
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

    texto = f'''
    Dolar: {cotacao_dolar}
    Euro:  {cotacao_euro}
    Bitcoin: {cotacao_btc}
    '''
    texto_cotacoes["text"] = texto #aqui o parametro "text" da variavel texto_cotacoes recebera a variavel "texto"

#Layout
janela = Tk()
janela.title("Cotações de Moedas")
janela.geometry("480x320")

texto_orientacao = Label(janela,
                         text="Clique no botão \n para ver a cotação atual das Moedas",
                         bg="#ffb366", font="Arial 20",
                         bd=2, relief="solid")
texto_orientacao.grid(column=1, row=1, padx=10,pady=10)

botao = Button(janela,
               text="Buscar Cotações", command=pegar_cotacoes,
               bg="#ff66cc", font="Arial 20", bd=6, relief="ridge")
botao.grid(column=1, row=2, padx=10,pady=10)

texto_cotacoes = Label(janela,
                       text="$$$",
                       bg="#00cc00", font="Arial 16 bold", bd=2, relief="solid")
texto_cotacoes.grid(column=1,row=3, padx=10,pady=10)


janela.mainloop()
