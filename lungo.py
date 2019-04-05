# Lungo versione 0.2.108
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

def colora(istruzione,x,y,colore):
    xx=str(y)+"."+str(x)
    xx1=str(y)+"."+str(x-len(istruzione))
    testo.tag_add(colore,xx1,xx)

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
                colora(istruzione,x,y,"uno")
                istruzione=""

            if istruzione=="stringa" and aperta==0:
                rigacompleta=rigacompleta+"str"
                colora(istruzione,x,y,"uno")
                istruzione=""

            if istruzione=="formatoorario" and aperta==0:
                rigacompleta=rigacompleta+"strftime"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="considera" and aperta==0:
                rigacompleta=rigacompleta+"for"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="dividi" and aperta==0:
                rigacompleta=rigacompleta+"split"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="aggiungitag" and aperta==0:
                rigacompleta=rigacompleta+"tag_add"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="configuratag" and aperta==0:
                rigacompleta=rigacompleta+"tag_config"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="carattere" and aperta==0:
                rigacompleta=rigacompleta+"font"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="coloretesto" and aperta==0:
                rigacompleta=rigacompleta+"foreground"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="globale" and aperta==0:
                rigacompleta=rigacompleta+"global"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="lunghezza" and aperta==0:
                rigacompleta=rigacompleta+"len"
                colora(istruzione,x,y,"uno")
                istruzione=""

            if istruzione=="prova" and aperta==0:
                rigacompleta=rigacompleta+"try"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="eccezione" and aperta==0:
                rigacompleta=rigacompleta+"except"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="chiedistringa" and aperta==0:
                rigacompleta=rigacompleta+"askstring"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="ciclo" and aperta==0:
                rigacompleta=rigacompleta+"mainloop"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="funzione" and aperta==0:
                rigacompleta=rigacompleta+"def"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="esegui" and aperta==0:
                rigacompleta=rigacompleta+"exec"
                colora(istruzione,x,y,"uno")
                istruzione=""
                
            if istruzione=="preleva" and aperta==0:
                rigacompleta=rigacompleta+"get"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="inserisci" and aperta==0:
                rigacompleta=rigacompleta+"insert"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="scrivi" and aperta==0:
                rigacompleta=rigacompleta+"write"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="apri" and aperta==0:
                rigacompleta=rigacompleta+"open"
                colora(istruzione,x,y,"uno")
                istruzione=""

            if istruzione=="chiudi" and aperta==0:
                rigacompleta=rigacompleta+"close"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="orario" and aperta==0:
                rigacompleta=rigacompleta+"time"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="niente" and aperta==0:
                rigacompleta=rigacompleta+"None"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="dialogo" and aperta==0:
                rigacompleta=rigacompleta+"simpledialog"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="evento" and aperta==0:
                rigacompleta=rigacompleta+"event"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="leggi" and aperta==0:
                rigacompleta=rigacompleta+"read"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="finestre" and aperta==0:
                rigacompleta=rigacompleta+"tkinter"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="importa" and aperta==0:
                rigacompleta=rigacompleta+"import"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="matematica" and aperta==0:
                rigacompleta=rigacompleta+"math"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="ferma" and aperta==0:
                rigacompleta=rigacompleta+"break"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="etichetta" and aperta==0:
                rigacompleta=rigacompleta+"label"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="comando" and aperta==0:
                rigacompleta=rigacompleta+"command"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="radicequadrata" and aperta==0:
                rigacompleta=rigacompleta+"sqrt"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="passa" and aperta==0:
                rigacompleta=rigacompleta+"pass"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="Finestra" and aperta==0:
                rigacompleta=rigacompleta+"Tk"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="Testo" and aperta==0:
                rigacompleta=rigacompleta+"Text"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="titolo" and aperta==0:
                rigacompleta=rigacompleta+"title"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="aggiungicascata" and aperta==0:
                rigacompleta=rigacompleta+"add_cascade"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="aggiungicomando" and aperta==0:
                rigacompleta=rigacompleta+"add_command"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="rileva" and aperta==0:
                rigacompleta=rigacompleta+"bind"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="unisci" and aperta==0:
                rigacompleta=rigacompleta+"pack"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="se" and aperta==0:
                if linea[progressivo+1]!=" " and linea[progressivo+1]!=":" and linea[progressivo+1]!="(":
                    pass
                else:
                    rigacompleta=rigacompleta+"if"
                    colora(istruzione,x,y,"tre")
                    istruzione=""

            if istruzione=="da" and aperta==0:
                if linea[progressivo+1]!=" " and linea[progressivo+1]!=":" and linea[progressivo+1]!="(":
                    pass
                else:
                    rigacompleta=rigacompleta+"from"
                    colora(istruzione,x,y,"tre")
                    istruzione=""

            if istruzione=="domanda" and aperta==0:
                rigacompleta=rigacompleta+"input"
                colora(istruzione,x,y,"uno")
                istruzione=""

            if istruzione=="finoache" and aperta==0:
                rigacompleta=rigacompleta+"while"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="allora" and aperta==0:
                rigacompleta=rigacompleta+":"
                colora(istruzione,x,y,"tre")
                istruzione=""

            if istruzione=="ugualea" and aperta==0:
                rigacompleta=rigacompleta+"=="
                colora(istruzione,x,y,"uno")
                istruzione=""

            if istruzione=="diversoda" and aperta==0:
                rigacompleta=rigacompleta+"!="
                colora(istruzione,x,y,"uno")
                istruzione=""

            if istruzione=="maggioredi" and aperta==0:
                rigacompleta=rigacompleta+">"
                colora(istruzione,x,y,"uno")
                istruzione=""
                
            if istruzione=="minoredi" and aperta==0:
                rigacompleta=rigacompleta+"<"
                colora(istruzione,x,y,"uno")
                istruzione=""

            if istruzione=="altrimentise" and aperta==0:
                rigacompleta=rigacompleta+"elif"
                colora(istruzione,x,y,"uno")
                istruzione=""

            if istruzione=="altrimenti" and aperta==0:
                if linea[progressivo+1]!=" " and linea[progressivo+1]!=":" and linea[progressivo+1]!="(":
                    pass
                else:
                    rigacompleta=rigacompleta+"else"
                    colora(istruzione,x,y,"uno")
                    istruzione=""

            if istruzione=="e" and aperta==0:
                if linea[progressivo+1]!=" " and linea[progressivo+1]!=":" and linea[progressivo+1]!="(":
                    pass
                else:
                    rigacompleta=rigacompleta+"and"
                    colora(istruzione,x,y,"uno")
                    istruzione=""

            if istruzione=="o" and aperta==0:
                if linea[progressivo+1]!=" " and linea[progressivo+1]!=":" and linea[progressivo+1]!="(":
                    pass
                else:
                    rigacompleta=rigacompleta+"or"
                    colora(istruzione,x,y,"uno")
                    istruzione=""

            if carattere==" ":
                rigacompleta=rigacompleta+istruzione
                istruzione=""

            if carattere=="=":
                rigacompleta=rigacompleta+istruzione
                istruzione=""

            if carattere=="+":
                rigacompleta=rigacompleta+istruzione
                istruzione=""

            if carattere=="-":
                rigacompleta=rigacompleta+istruzione
                istruzione=""

            if carattere=="(":
                rigacompleta=rigacompleta+istruzione
                istruzione=""

            if carattere==")":
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
