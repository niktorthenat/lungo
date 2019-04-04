# Lungo versione 0.2.106
from tkinter import *
from tkinter.simpledialog import askstring
import time

def aprifilenome(event=None):
    nome=askstring("Apri file","Nome del file?")
    f=open(nome+".txt","r")
    codice=f.read()
    f.close()
    testo.insert("1.0",codice)

def salvafilenome(event=None):
    codice=testo.get(0.0,END)
    nome=askstring("Salva file","Nome del file?")
    f=open(nome+".txt","w")
    f.write(codice)
    f.close()
    f=open(nome+".py","w")
    f.write(programma)
    f.close

def esegui(event=None):
    print
    print ("=============ESEGUO PROGRAMMA=================")
    print
    nome=askstring("Esegui programma","Nome del file?")
    try:
        exec(open(nome+".py").read())
    except:
        print ("Attenzione, errore nel programma, controlla")

def correggi(event=None):
    global programma
    programma=""
    aperta=0
    linea=""
    riga=""
    istruzione=""
    rigacompleta=""
    controllore=0
    progressivo=0
    x=0
    y=0
    codice=testo.get(0.0,END)
    riga=codice.split("\n")
    testo.tag_config("uno",foreground="violet")
    testo.tag_config("due",foreground="blue")
    testo.tag_config("tre",foreground="orange")
    print
    print ("============================================")
    print (time.strftime("Modifiche aggiornate il: %d/%m/%Y alle ore %H:%M:%S"))
    print
    for linea in riga:
        y=y+1
        x=0
        for carattere in linea:
            x=x+1
            istruzione=istruzione+carattere
            
            if istruzione=="stampa" and aperta==0:
                rigacompleta=rigacompleta+"print"
                xx=str(y)+"."+str(x)
                xx1=str(y)+"."+str(x-len(istruzione))
                testo.tag_add("tre",xx1,xx)
                istruzione=""

            if istruzione=="importa" and aperta==0:
                rigacompleta=rigacompleta+"import"
                xx=str(y)+"."+str(x)
                xx1=str(y)+"."+str(x-len(istruzione))
                testo.tag_add("tre",xx1,xx)
                istruzione=""

            if istruzione=="matematica" and aperta==0:
                rigacompleta=rigacompleta+"math"
                istruzione=""

            if istruzione=="radicequadrata" and aperta==0:
                rigacompleta=rigacompleta+"sqrt"
                istruzione=""

            if istruzione=="se" and aperta==0:
                if linea[progressivo+1]!=" " and linea[progressivo+1]!=":" and linea[progressivo+1]!="(":
                    pass
                else:
                    rigacompleta=rigacompleta+"if"
                    xx=str(y)+"."+str(x)
                    xx1=str(y)+"."+str(x-len(istruzione))
                    testo.tag_add("tre",xx1,xx)
                    istruzione=""

            if istruzione=="domanda" and aperta==0:
                rigacompleta=rigacompleta+"input"
                xx=str(y)+"."+str(x)
                xx1=str(y)+"."+str(x-len(istruzione))
                testo.tag_add("uno",xx1,xx)
                istruzione=""

            if istruzione=="finoache" and aperta==0:
                rigacompleta=rigacompleta+"while"
                xx=str(y)+"."+str(x)
                xx1=str(y)+"."+str(x-len(istruzione))
                testo.tag_add("tre",xx1,xx)
                istruzione=""

            if istruzione=="allora" and aperta==0:
                rigacompleta=rigacompleta+":"
                xx=str(y)+"."+str(x)
                xx1=str(y)+"."+str(x-len(istruzione))
                testo.tag_add("tre",xx1,xx)
                istruzione=""

            if istruzione=="ugualea" and aperta==0:
                rigacompleta=rigacompleta+"=="
                xx=str(y)+"."+str(x)
                xx1=str(y)+"."+str(x-len(istruzione))
                testo.tag_add("uno",xx1,xx)
                istruzione=""

            if istruzione=="diversoda" and aperta==0:
                rigacompleta=rigacompleta+"!="
                xx=str(y)+"."+str(x)
                xx1=str(y)+"."+str(x-len(istruzione))
                testo.tag_add("uno",xx1,xx)
                istruzione=""

            if istruzione=="maggioredi" and aperta==0:
                rigacompleta=rigacompleta+">"
                xx=str(y)+"."+str(x)
                xx1=str(y)+"."+str(x-len(istruzione))
                testo.tag_add("uno",xx1,xx)
                istruzione=""
                
            if istruzione=="minoredi" and aperta==0:
                rigacompleta=rigacompleta+"<"
                xx=str(y)+"."+str(x)
                xx1=str(y)+"."+str(x-len(istruzione))
                testo.tag_add("uno",xx1,xx)
                istruzione=""

            if istruzione=="altrimentise" and aperta==0:
                rigacompleta=rigacompleta+"elif"
                xx=str(y)+"."+str(x)
                xx1=str(y)+"."+str(x-len(istruzione))
                testo.tag_add("uno",xx1,xx)
                istruzione=""

            if istruzione=="altrimenti" and aperta==0:
                if linea[progressivo+1]!=" " and linea[progressivo+1]!=":" and linea[progressivo+1]!="(":
                    pass
                else:
                    rigacompleta=rigacompleta+"else"
                    xx=str(y)+"."+str(x)
                    xx1=str(y)+"."+str(x-len(istruzione))
                    testo.tag_add("uno",xx1,xx)
                    istruzione=""

            if istruzione=="e" and aperta==0:
                if linea[progressivo+1]!=" " and linea[progressivo+1]!=":" and linea[progressivo+1]!="(":
                    pass
                else:
                    rigacompleta=rigacompleta+"and"
                    xx=str(y)+"."+str(x)
                    xx1=str(y)+"."+str(x-len(istruzione))
                    testo.tag_add("uno",xx1,xx)
                    istruzione=""

            if istruzione=="o" and aperta==0:
                if linea[progressivo+1]!=" " and linea[progressivo+1]!=":" and linea[progressivo+1]!="(":
                    pass
                else:
                    rigacompleta=rigacompleta+"or"
                    xx=str(y)+"."+str(x)
                    xx1=str(y)+"."+str(x-len(istruzione))
                    testo.tag_add("uno",xx1,xx)
                    istruzione=""

            if carattere==" ":
                rigacompleta=rigacompleta+istruzione
                istruzione=""

            if carattere=="=":
                rigacompleta=rigacompleta+istruzione
                istruzione=""

            if carattere==".":
                rigacompleta=rigacompleta+istruzione
                istruzione=""

            if istruzione=="\t":
                rigacompleta=rigacompleta+istruzione
                istruzione=""

            if carattere=='"' and aperta==0:
                aperta=1
            elif carattere=='"' and aperta==1:
                aperta=0

            if carattere=="'" and aperta==0:
                aperta=1
            elif carattere=="'" and aperta==1:
                aperta=0

            progressivo=progressivo+1

        if aperta==1:
            print ("Errore alla riga: ",linea)
            break
        rigacompleta=rigacompleta+istruzione
        print (rigacompleta)
        programma=programma+rigacompleta+"\n"
        istruzione=""
        rigacompleta=""
        progressivo=0
                


padre=Tk()
padre.title("Lungo")
testo=Text(padre,font="Courier")
menu=Menu(padre)
padre.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Apri con nome...",command=aprifilenome)
filemenu.add_command(label="Salva con nome...",command=salvafilenome)
filemenu.add_command(label="Esegui",command=esegui)
testo.pack()
padre.bind("<Return>",correggi)
testo["bg"]="#eaffe8"
padre.mainloop()
