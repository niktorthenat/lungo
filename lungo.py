# Progetto LUNGO versione 0.0.58
# by NiktorTheNat (20202021)
# interprete su base del linguaggio Python
# ultima revisione 16/02/2021

vl="**** PROGETTO LUNGO 0.0.58 ****\n\nPER TUTTI I SISTEMI OPERATIVI BY NIKTORTHENAT\n\nPRONTO."

import subprocess,os,sys,atexit
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter import Menu
from tkinter import ttk


def editor_salva():
    global testo
    txt=testo.get(1.0,END)
    programma=open("provola.txt","w")
    programma.write(txt)
    programma.close()
    controlla()
    

def leggi():
    #Creo una lista di nome 'riga'
    riga=[]
    #Apro il file con il programma e lo metto dentro 'codice'
    codice=open("provola.txt","r")
    #Creo variabile z come indice per determinare ogni riga letta
    z=1
    #Eseguo ciclo e metto dentro lista 'riga' tutte le righe del programma
    for x in codice.readlines():
        riga.append(x)
        z=z+1
    #Torno all'istruzione di chiamata
    return riga

def controlla():
    #Chiamo la funzione per leggere tutte le istruzioni del programma
    programma=leggi()
    l=0
    #Creo lista 'parola' per contenere tutte le parole o segni della riga
    linea=[]
    #Creo variabile 'eseguibile' che contiene 1 se devo poi creare file eseguibile
    #oppure contiene 0 se non devo creare file eseguibile
    eseguibile=0
    #Creo variabile 'debug' che contiene 1 se devo fare debug oppure 0 se eseguo normalmente
    debug=0
    #Controllo se l'utente vuole creare il file eseguibile
    if "creaeseguibile" in programma[0]:
        eseguibile=1
    else:
        eseguibile=0
    if "controllaprogramma" in programma[0]:
        debug=1
    else:
        debug=0
    #Eseguo ciclo per leggere ogni singola riga
    for riga in programma:
        #Creo variabile 'parola' che conterrà, provvisoriamente, ogni singola istruzione che sta leggendo
        parola=""
        #Creo variabile 'x' che conterrà la posizione corrente sulla linea
        x=0
        #Creo variabile 'p' che contiene 0 se la parentesi è chiusa o 1 se è aperta
        p=0
        #Creo variabile 'v' che contiene 0 se virgolette chiuse o 1 per virgolette aperte
        v=0
        #Creo ciclo per leggere ogni singolo carattere della riga
        for r in riga:
            if r=="(" and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
                if p==0:
                    p=1
                else:
                    p=0
            elif r==")" and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
                if p==0:
                    p=1
                else:
                    p=0
            elif r=="+" and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
            elif r=="-" and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
            elif r=="*" and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
            elif r=="." and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
            elif r==":" and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
            elif r=="," and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
            elif r==" " and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
            elif r=="=" and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
            elif r=='"' and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
                v=1
            elif r=='"' and v==1:
                linea.append(parola)
                parola=""
                linea.append(r)
                v=0
            elif r=="\n":
                linea.append(parola)
                parola=""
                linea.append(r)
            elif r=="\t":
                linea.append(parola)
                parola=""
                linea.append("    ")
            elif r=="//" and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
            elif r=="[" and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
            elif r=="]" and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
            elif r=="{" and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
            elif r=="}" and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
            else:
                parola=parola+r
            x=x+1



    #Creo la variabile 'listato' che conterrà tutto il programma riconvertito in linguaggio Python
    listato=[]
    #Creo variabile 'p' che contiene 0 se la parentesi è chiusa o 1 se è aperta
    p=0
    #Creo variabile 'v' che contiene 0 se virgolette singole chiuse o 1 per virgolette singole aperte
    vs=0
    #Creo variabile 'v' che contiene 0 se virgolette doppie chiuse o 1 per virgolette doppie aperte
    vd=0
    #Creo variabile 'e' che controlla se istruzione può essere corretta o possibile errore
    e=0
    #Creo variabile 'riga' che serve a segnalare in quale riga potrebbe esserci l'errore
    riga=1
    #Leggo ogni singola istruzione della linea
    #e converto le istruzioni in Python
    istruzioni={"__inizializza__":"__init__","_no_":'"no"',"_si_":'"yes"'}
    istruzionia={"aggiornadatabase":"commit","aggiungi":"append","aggiungimenu":"add_cascade","aggiungimenusecondario":"add_command","aggiungiparagrafo":"add_paragraph","alfabetico":"sort","alnumero":"to","altezza":"height","altrimenti":"else","altrimentise":"elif","anche":"and","apri":"open","apriaudio":"playsound.playsound","apricartella":"openpyxl.load_workbook","arrotondaperdifetto":"math.floor","arrotondapereccesso":"math.ceil","attendifineregistrazione":"sounddevice.wait"}
    istruzionib={"barra":"Progressbar","bordato":"GROOVE","botfine":"polling()","botinizio":"telebot.TeleBot"}
    istruzionic={"canali":"channels","casellaadiscesa":"ttk.Combobox","casellaascelta":"Radiobutton","caselladitesto":"Entry","caselladitestoscrollabile":"scrolledtext.ScrolledText","casellaselezionabile":"Checkbutton","casuale":"random.random","cella":"cell","cercatutti":"findAll","chiudi":"close","ciclico":"mainloop","ciclo":"while","classe":"class","colonna":"column","colonnafinale":"max_col","colonnainiziale":"min_col","colore":"color","coloresfondo":"background","coloretesto":"foreground","comandidibase":"commands=['help','start']","comandimessaggi":"func=lambda message: True","combinazionetasti":"pyautogui.hotkey","combinazioniestese":"itertools.permutations","combinazioniuniche":"itertools.combinations","come":"as","con":"in","configura":"config","connettidatabase":"mysql.connector.connect","considera":"for","conta":"count","contalettere":"itertools.groupby","contatore":"Spinbox","contenuto":"content","continuaparagrafo":"add_run","controllaprogramma":"","corsivo":"italic","coseno":"math.cos","creaeseguibile":""}
    istruzionid={"da":"from","dalnumero":"from_","deviazionestandard":"statistics.stdev","diagrammaabarre":"matplotlib.pyplot.bar","diagrammaalinee":"matplotlib.pyplot.plot","diagrammaetichettax":"matplotlib.pyplot.xlabel","diagrammaetichettay":"matplotlib.pyplot.ylabel","diagrammatitolo":"matplotlib.pyplot.title","diventa":"as","dividi":"split","domanda":"input"}
    istruzionie={"e":"and","elaborasito":"BeautifulSoup","elimina":"delete","eliminaspazi":"strip","eliminaspaziiniziali":"lstrip","eliminaspazifinali":"rstrip","esegui":"command","estensione":"length","etichetta":"Label","eulero":"math.e"}
    istruzionif={"faiclick":"pyautogui.click","faipausa":"interval","falso":"False","ferma":"break","fileaudio":"speech_recognition.AudioFile","FINE":"END","finestra":"Tk","finestraattenzione":"messagebox.showwarning","finestracartella":"filedialog.askdirectory","finestradomanda":"messagebox.askquestion","finestraerrore":"messagebox.showerror","finestrafile":"filedialog.askopenfilename","finestrafiles":"filedialog.askopenfilenames","finestramessaggio":"messagebox.showinfo","finestraokannulla":"messagebox.askokcancel","finestrariprovaannulla":"messagebox.askretrycancel","finestrasino":"messagebox.askyesno","finestrasinoannulla":"messagebox.askyesnocancel","finiscecon":"endswith","foglioattivo":"active","francese":"lang='fr'","frequenza":"samplerate","funzione":"def"}
    istruzionig={"gestionemessaggi":"message_handler","gestore":"cursor","giocoaggiornafinestra":"pygame.display.update","giococontrollaevento":"pygame.event.get","giocodimensionefinestra":"pygame.display.set_mode","giocodisegnarettangolo":"pygame.draw.rect","giocofine":"pygame.quit","giocofrequenza":"pygame.time.delay","giocoinizio":"pygame.init","giocoriempimentofinestra":"fill","giocotastodestro":"pygame.K_RIGHT","giocotastoinalto":"pygame.K_UP","giocotastoinbasso":"pygame.K_DOWN","giocotastopremuto":"pygame.key.get_pressed","giocotastosinistro":"pygame.K_LEFT","giocotitolofinestra":"pygame.display.set_caption","gradi":"math.degrees","grandezza":"geometry","grassetto":"bold"}
    istruzionih={"htmlclasse":"class_","htmlid":"id"}
    istruzionii={"impacchetta":"pack","importa":"import","imposta":"set","incassato":"SUNKEN","indice":"index","inglese":"lang='en'","iniziacon":"startswith","insecondi":"duration","inserisci":"insert","intero":"int","intervallo":"range","inverso":"reverse","inverti":"reversed","invia_benvenuto":"send_welcome","invia_messaggio":"echo_message","italiano":"lang='it'"}
    istruzionil={"lancia":"execute","larghezza":"width","legenda":"label","leggi":"read","lettura":"r","lineaapuntini":"'dotten'","lineaapuntinietrattini":"'dashdot'","lineaatrattini":"'dashed'","lineaatrattiniepuntini":"'dashdot'","lineacontinua":"'solid'","linguaggio":"language","lunghezza":"len","logaritmo":"math.log"}
    istruzionim={"maggiore":"max","maiuscolo":"upper","margine":"border","media":"statistics.mean","memorizza":"write","menu":"Menu","menufinestra":"menu","menuprimario":"label","menusecondario":"menu","mestesso":"self","microfono":"sounddevice.rec","minore":"min","minuscolo":"lower","mischia":"random.shuffle","mostradiagramma":"matplotlib.pyplot.show","mostrahtml":"prettify","mostralegenda":"matplotlib.pyplot.legend","muovimouse":"pyautogui.moveTo"}
    istruzionin={"nepero":"math.e","nomecarattere":"font.name","nomefogli":"sheetnames","nomemenusecondario":"label","numerocasuale":"random.randint","numeroricorrente":"statistics.mode","numerosuccessivo":"itertools.accumulate","nuovacartella":"openpyxl.Workbook","nuovodocumento":"docx.Document"}
    istruzionio={"oppure":"or","ospite":"host"}
    istruzionip={"paginahtml":"'html.parser'","paginaweb":"features='lxml'","parla":"gTTS","passa":"pass","pausasistema":"pyautogui.PAUSE","piatto":"FLAT","pigreco":"math.pi","positivo":"abs","posizione":"pop","posizionemouse":"pyautogui.position","potenza":"pow","premipulsante":"pyautogui.mouseDown","prendi":"get","primamaiuscola":"capitalize","primemaiuscole":"title","problema":"except","prova":"try","pulsante":"Button","pulsantedestro":"button='right'","pulsantedimezzo":"button='middle'","pulsantesinistro":"button='left'"}
    istruzionir={"radianti":"math.radians","radicequadrata":"math.sqrt","registrazione":"record","riconoscimentogoogle":"recognize_google","riconoscimentovocale":"speech_recognition.Recognizer","riga":"row","rigafinale":"max_row","rigainiziale":"min_row","righefoglio":"iter_rows","rilasciapulsante":"pyautogui.mouseUp","rilievo":"relief","rimuovi":"remove","risoluzioneschermo":"pyautogui.size","rispondi":"reply_to"}
    istruzionis={"salva":"save","sceltacasuale":"random.choice","scrittura":"w","scrivi":"print","scrollamouse":"pyautogui.scroll","se":"if","selezionaelemento":"current","seno":"math.sin","sito":"requests.get","solovalori":"values_only","sostituisci":"replace","sottolineato":"underline","spaziox":"padx","spazioy":"pady","spessorelinea":"linewidth","stilelinea":"linestyle"}
    istruzionit={"tangente":"math.tan","tastodestra":"'right'","tastoelimina":"'backspace'","tastoinvio":"'enter'","tastosinistra":"'left'","testo":"text","tipocarattere":"font","tipofile":"filetype","TipoErrore":"Exception","titolo":"title","trascinamouse":"pyautogui.dragTo","trova":"find"}
    istruzioniu={"unici":"set","unisci":"join","usa":"with","usalatastiera":"pyautogui.typewrite","utente":"user"}
    istruzioniv={"valore":"value","valori":"values","variabile":"var","variabilebooleana":"BooleanVar()","variabileintera":"IntVar()","VariabileNonDefinita":"NameError","vero":"True","verticelinea":"marker","volte":"clicks"}
    colori={"!rosso":"'red'","!giallo":"'yellow'","!verde":"'green'"}
    codice={**istruzioni,**istruzionia,**istruzionib,**istruzionic,**istruzionid,**istruzionie,**istruzionif,**istruzionig,**istruzionih,**istruzionii,**istruzionil,**istruzionim,**istruzionin,**istruzionio,**istruzionip,**istruzionir,**istruzionis,**istruzionit,**istruzioniu,**istruzioniv,**colori}
    punteggiatura=["'",'"',"(",")","[","]"]
    segni=[".",":",","," ","=","\n","\t",""]
    for r in linea:
        if r=="\n":
            riga=riga+1
        if r=="'":
            if vs==0:
                vs==1
            else:
                vs==0
        if r=='"':
            if vd==0:
                vd=1
            else:
                vd=0
        if r in codice.keys() and vs==0 and vd==0:
            listato.append(codice[r])
            e=0
        else:
            listato.append(r)

    #Scrivo il programma Python dentro il file "Provola-convertito.py"
    programma=open("provola-convertito.py","w",encoding="utf-8")
    #Verifico se il programma che stiamo creando è un bot per Telegram
    #Se è un bot per telegram, non scrivo le istruzioni per Tkinter
    if "telebot.TeleBot" in listato:
        pass
    else:
        programma.write("from tkinter import *\n")
        programma.write("from tkinter.ttk import *\n")
        programma.write("from tkinter import scrolledtext\n")
        programma.write("from tkinter import messagebox\n")
        programma.write("from tkinter.ttk import Progressbar\n")
        programma.write("from tkinter import filedialog\n")
        programma.write("from tkinter import Menu\n")
        programma.write("from tkinter import ttk\n")
    #Controllo necessità di importazione modulo nel programma
    if "openpyxl.Workbook" in listato or "openpyxl.load_workbook" in listato:
        programma.write("import openpyxl\n")
        if "openpyxl" in sys.modules:
            pass
        else:
            os.system("pip install openpyxl")
    if "mysql.connector.connect" in listato:
        programma.write("import mysql.connector\n")
        if "mysql.connector" in sys.modules:
            pass
        else:
            os.system("pip install mysql-connector-python")
    if "speech_recognition.Recognizer" in listato:
        programma.write("import speech_recognition\n")
        if "speech_recognition" in sys.modules:
            pass
        else:
            os.system("pip install SpeechRecognition")
    if "gTTS" in listato:
        programma.write("from gtts import *\n")
        if "gtts" in sys.modules:
            pass
        else:
            os.system("pip install gtts")
    if "playsound.playsound" in listato:
        programma.write("import playsound\n")
        if "playsound" in sys.modules:
            pass
        else:
            os.system("pip install playsound")
    if "docx.Document" in listato:
        programma.write("import docx\n")
        if "python-docx" in sys.modules:
            pass
        else:
            os.system("pip install python-docx")
    if "requests.get" in listato or "BeautifulSoup" in listato:
        programma.write("import requests\n")
        programma.write("from bs4 import BeautifulSoup\n")
        if "requests" in sys.modules and "beautifulsoup4" in sys.modules:
            pass
        else:
            os.system("pip install python-docx")
    if "matplotlib.pyplot.plot" in listato or "matplotlib.pyplot.bar" in listato:
        programma.write("import matplotlib.pyplot\n")
        if "matplotlib" in sys.modules:
            pass
        else:
            os.system("pip install matplotlib")
    if "pygame.init" in listato:
        programma.write("import pygame\n")
        if "pygame" in sys.modules:
            pass
        else:
            os.system("pip install pygame")

    for r in listato:
        if "pyautogui." in r:
            programma.write("import pyautogui\n")
            if "pyautogui" in sys.modules:
                pass
            else:
                os.system("pip install pyautogui")
                break

    if "telebot.TeleBot" in listato:
        programma.write("import telebot\n")
        if "telebot" in sys.modules:
            pass
        else:
            os.system("pip install pyTelegramBotAPI")
    if "sounddevice.rec" in listato:
        programma.write("import sounddevice\n")
        programma.write("from soundfile import write\n")
        if "sounddevice" in sys.modules:
            pass
        else:
            os.system("pip install sounddevice")
            os.system("pip install soundfile")
    if "math.ceil" in listato or "math.floor" in listato or "math.sqrt" in listato or "math.pi" in listato or "math.e" in listato or "math.radians" in listato or "math.degrees" in listato or "math.sin" in listato or "math.cos" in listato or "math.tan" in listato or "math.log" in listato:
        programma.write("import math\n")
    if "statistics.stdev" in listato or "statistics.mode" in listato or "statistics.mean" in listato:
        programma.write("import statistics\n")
    if "itertools.accumulate" in listato or "itertools.combinations" in listato or "itertools.permutations" in listato or "itertools.groupby" in listato:
        programma.write("import itertools\n")
    if "random.shuffle" in listato or "random.choice" in listato or "random.randint" in listato or "random.random" in listato:
        programma.write("import random\n")
    for r in listato:
        programma.write(r)
    #Aggiungo un'istruzione finale che non fa chiudere subito il terminale
    #ma la aggiungo solo se non sto creando un bot per Telegram
    if "telebot.TeleBot" in listato:
        print("Ho creato il file provola-convertito.py")
        print("Ora vai sul sito https://www.pythonanywhere.com/")
        print("e premi sul pulsante 'Browse Files'")
        print("Premi su 'Upload a file' e carica il file provola-convertito.py")
        print("Poi premi sul link 'Open Bash console here' che trovi sulla stessa pagina")
        print("Si aprirà un terminale dove devi scrivere la seguente istruzione:")
        print("mkvirtualenv --python=/usr/bin/python3 mysite-virtualenv")
        print("Premi il tasto INVIO per lanciare quell'istruzione")
        print("Al termine scrivi la seguente istruzione:")
        print("pip install pyTelegramBotAPI")
        print("premi il tasto INVIO sulla tastiera")
        print("Al termine della procedura, lancia il bot con la seguente istruzione:")
        print("python provola-convertito.py")
        print("Premi il tasto INVIO sulla tastiera e il bot sarà attivo")
        print("Buon divertimento...")
    else:
        programma.write('\nzzz=input("Programma terminato")')
    programma.close()
    #Converto programma Python in eseguibile
    #os.system("pyinstaller provola-convertito.py --onefile")
    #Eseguo il programma Python
    if eseguibile==0:
        if debug==1:
            subprocess.run("python.exe -m pdb provola-convertito.py")
        else:
            subprocess.run("python.exe provola-convertito.py")
    else:
        if "pyinstaller" in sys.modules:
            subprocess.run("pyinstaller --onefile provola-convertito.py")
        else:
            os.system("pip install pyinstaller")
            subprocess.run("pyinstaller --onefile provola-convertito.py")


def istruzioni(event):
    x=event.widget.curselection()
    aiuto_testo.delete("1.0",END)
    ff=aiuto.get(x)
    #aiuto_testo.insert(INSERT,ff)
    #Creo una lista di nome 'manuale'
    manuale=[]
    #Apro il file con il programma e lo metto dentro 'testo_istruzioni'
    testo_istruzioni=open(u"aiuto.txt","r",encoding="utf-8")
    #Creo variabile zz come indice per determinare ogni riga letta
    zz=1
    #Eseguo ciclo e metto dentro lista 'manuale' tutte le righe del manuale
    for x in testo_istruzioni.readlines():
        manuale.append(x)
        zz=zz+1
    #Torno all'istruzione di chiamata
    testo_istruzioni.close()
    istruzione_da_cercare="***"+ff+"***"
    trovato=0
    for x in manuale:
        if trovato==1 and x.strip()!=istruzione_da_cercare.strip():
            aiuto_testo.insert(INSERT,x)
        if x.strip()==istruzione_da_cercare.strip():
            trovato=trovato+1
            #aiuto_testo.insert(INSERT,x)
            if trovato==2:
                break
    if trovato==0:
        aiuto_testo.insert(INSERT,"nessuna istruzione trovata")
    else:
        trovato=0


def aiuto():
    presentazione.pack_forget()
    testo.pack_forget()
    pulsante.pack_forget()
    pulsante1.pack_forget()
    pulsante_reset.pack(fill=BOTH, expand = YES)
    aiuto.pack(fill=BOTH,expand=YES)
    istruzioni={"__inizializza__":"__init__","_no_":'"no"',"_si_":'"yes"'}
    istruzionia={"aggiornadatabase":"commit","aggiungi":"append","aggiungimenu":"add_cascade","aggiungimenusecondario":"add_command","aggiungiparagrafo":"add_paragraph","alfabetico":"sort","alnumero":"to","altezza":"height","altrimenti":"else","altrimentise":"elif","anche":"and","apri":"open","apriaudio":"playsound.playsound","apricartella":"openpyxl.load_workbook","arrotondaperdifetto":"math.floor","arrotondapereccesso":"math.ceil","attendifineregistrazione":"sounddevice.wait"}
    istruzionib={"barra":"Progressbar","bordato":"GROOVE","botfine":"polling()","botinizio":"telebot.TeleBot"}
    istruzionic={"canali":"channels","casellaadiscesa":"ttk.Combobox","casellaascelta":"Radiobutton","caselladitesto":"Entry","caselladitestoscrollabile":"scrolledtext.ScrolledText","casellaselezionabile":"Checkbutton","casuale":"random.random","cella":"cell","cercatutti":"findAll","chiudi":"close","ciclico":"mainloop","ciclo":"while","classe":"class","colonna":"column","colonnafinale":"max_col","colonnainiziale":"min_col","colore":"color","coloresfondo":"background","coloretesto":"foreground","comandidibase":"commands=['help','start']","comandimessaggi":"func=lambda message: True","combinazionetasti":"pyautogui.hotkey","combinazioniestese":"itertools.permutations","combinazioniuniche":"itertools.combinations","come":"as","con":"in","configura":"config","connettidatabase":"mysql.connector.connect","considera":"for","conta":"count","contalettere":"itertools.groupby","contatore":"Spinbox","contenuto":"content","continuaparagrafo":"add_run","controllaprogramma":"","corsivo":"italic","coseno":"math.cos","creaeseguibile":""}
    istruzionid={"da":"from","dalnumero":"from_","deviazionestandard":"statistics.stdev","diagrammaabarre":"matplotlib.pyplot.bar","diagrammaalinee":"matplotlib.pyplot.plot","diagrammaetichettax":"matplotlib.pyplot.xlabel","diagrammaetichettay":"matplotlib.pyplot.ylabel","diagrammatitolo":"matplotlib.pyplot.title","diventa":"as","dividi":"split","domanda":"input"}
    istruzionie={"e":"and","elaborasito":"BeautifulSoup","elimina":"delete","eliminaspazi":"strip","eliminaspaziiniziali":"lstrip","eliminaspazifinali":"rstrip","esegui":"command","estensione":"length","etichetta":"Label","eulero":"math.e"}
    istruzionif={"faiclick":"pyautogui.click","faipausa":"interval","falso":"False","ferma":"break","fileaudio":"speech_recognition.AudioFile","FINE":"END","finestra":"Tk","finestraattenzione":"messagebox.showwarning","finestracartella":"filedialog.askdirectory","finestradomanda":"messagebox.askquestion","finestraerrore":"messagebox.showerror","finestrafile":"filedialog.askopenfilename","finestrafiles":"filedialog.askopenfilenames","finestramessaggio":"messagebox.showinfo","finestraokannulla":"messagebox.askokcancel","finestrariprovaannulla":"messagebox.askretrycancel","finestrasino":"messagebox.askyesno","finestrasinoannulla":"messagebox.askyesnocancel","finiscecon":"endswith","foglioattivo":"active","francese":"lang='fr'","frequenza":"samplerate","funzione":"def"}
    istruzionig={"gestionemessaggi":"message_handler","gestore":"cursor","giocoaggiornafinestra":"pygame.display.update","giococontrollaevento":"pygame.event.get","giocodimensionefinestra":"pygame.display.set_mode","giocodisegnarettangolo":"pygame.draw.rect","giocofine":"pygame.quit","giocofrequenza":"pygame.time.delay","giocoinizio":"pygame.init","giocoriempimentofinestra":"fill","giocotastodestro":"pygame.K_RIGHT","giocotastoinalto":"pygame.K_UP","giocotastoinbasso":"pygame.K_DOWN","giocotastopremuto":"pygame.key.get_pressed","giocotastosinistro":"pygame.K_LEFT","giocotitolofinestra":"pygame.display.set_caption","gradi":"math.degrees","grandezza":"geometry","grassetto":"bold"}
    istruzionih={"htmlclasse":"class_","htmlid":"id"}
    istruzionii={"impacchetta":"pack","importa":"import","imposta":"set","incassato":"SUNKEN","indice":"index","inglese":"lang='en'","iniziacon":"startswith","insecondi":"duration","inserisci":"insert","intero":"int","intervallo":"range","inverso":"reverse","inverti":"reversed","invia_benvenuto":"send_welcome","invia_messaggio":"echo_message","italiano":"lang='it'"}
    istruzionil={"lancia":"execute","larghezza":"width","legenda":"label","leggi":"read","lettura":"r","lineaapuntini":"'dotten'","lineaapuntinietrattini":"'dashdot'","lineaatrattini":"'dashed'","lineaatrattiniepuntini":"'dashdot'","lineacontinua":"'solid'","linguaggio":"language","lunghezza":"len","logaritmo":"math.log"}
    istruzionim={"maggiore":"max","maiuscolo":"upper","margine":"border","media":"statistics.mean","memorizza":"write","menu":"Menu","menufinestra":"menu","menuprimario":"label","menusecondario":"menu","mestesso":"self","microfono":"sounddevice.rec","minore":"min","minuscolo":"lower","mischia":"random.shuffle","mostradiagramma":"matplotlib.pyplot.show","mostrahtml":"prettify","mostralegenda":"matplotlib.pyplot.legend","muovimouse":"pyautogui.moveTo"}
    istruzionin={"nepero":"math.e","nomecarattere":"font.name","nomefogli":"sheetnames","nomemenusecondario":"label","numerocasuale":"random.randint","numeroricorrente":"statistics.mode","numerosuccessivo":"itertools.accumulate","nuovacartella":"openpyxl.Workbook","nuovodocumento":"docx.Document"}
    istruzionio={"oppure":"or","ospite":"host"}
    istruzionip={"paginahtml":"'html.parser'","paginaweb":"features='lxml'","parla":"gTTS","passa":"pass","pausasistema":"pyautogui.PAUSE","piatto":"FLAT","pigreco":"math.pi","positivo":"abs","posizione":"pop","posizionemouse":"pyautogui.position","potenza":"pow","premipulsante":"pyautogui.mouseDown","prendi":"get","primamaiuscola":"capitalize","primemaiuscole":"title","problema":"except","prova":"try","pulsante":"Button","pulsantedestro":"button='right'","pulsantedimezzo":"button='middle'","pulsantesinistro":"button='left'"}
    istruzionir={"radianti":"math.radians","radicequadrata":"math.sqrt","registrazione":"record","riconoscimentogoogle":"recognize_google","riconoscimentovocale":"speech_recognition.Recognizer","riga":"row","rigafinale":"max_row","rigainiziale":"min_row","righefoglio":"iter_rows","rilasciapulsante":"pyautogui.mouseUp","rilievo":"relief","rimuovi":"remove","risoluzioneschermo":"pyautogui.size","rispondi":"reply_to"}
    istruzionis={"salva":"save","sceltacasuale":"random.choice","scrittura":"w","scrivi":"print","scrollamouse":"pyautogui.scroll","se":"if","selezionaelemento":"current","seno":"math.sin","sito":"requests.get","solovalori":"values_only","sostituisci":"replace","sottolineato":"underline","spaziox":"padx","spazioy":"pady","spessorelinea":"linewidth","stilelinea":"linestyle"}
    istruzionit={"tangente":"math.tan","tastodestra":"'right'","tastoelimina":"'backspace'","tastoinvio":"'enter'","tastosinistra":"'left'","testo":"text","tipocarattere":"font","tipofile":"filetype","TipoErrore":"Exception","titolo":"title","trascinamouse":"pyautogui.dragTo","trova":"find"}
    istruzioniu={"unici":"set","unisci":"join","usa":"with","usalatastiera":"pyautogui.typewrite","utente":"user"}
    istruzioniv={"valore":"value","valori":"values","variabile":"var","variabilebooleana":"BooleanVar()","variabileintera":"IntVar()","VariabileNonDefinita":"NameError","vero":"True","verticelinea":"marker","volte":"clicks"}
    colori={"!rosso":"'red'","!giallo":"'yellow'","!verde":"'green'"}
    codice={**istruzioni,**istruzionia,**istruzionib,**istruzionic,**istruzionid,**istruzionie,**istruzionif,**istruzionig,**istruzionih,**istruzionii,**istruzionil,**istruzionim,**istruzionin,**istruzionio,**istruzionip,**istruzionir,**istruzionis,**istruzionit,**istruzioniu,**istruzioniv,**colori}
    tt=1
    for xx in codice:    
        aiuto.insert(tt,xx)
        tt=tt+1

    aiuto_testo.pack(fill=BOTH,expand=YES)

def resetta():
    aiuto.delete(0,END)
    pulsante_reset.pack_forget()
    aiuto.pack_forget()
    aiuto_testo.pack_forget()
    presentazione.pack(fill=BOTH, expand = YES)
    testo.pack(fill=BOTH, expand = YES)
    pulsante.pack(fill=BOTH, expand = YES)
    pulsante1.pack(fill=BOTH, expand = YES)
    
#Editor di testo
finestra=Tk()
finestra.title("Editor per Lungo - by NiktorTheNat")
finestra.geometry("900x800")
finestra.config(bg="#ccccff",pady=70,padx=70)
#testo=scrolledtext.ScrolledText(finestra,width=80,height=35)
presentazione=Text(finestra,width=80,height=5,bg="#8080ff",fg="#ccccff",font=('Courier', 16))
presentazione.pack(fill=BOTH, expand = YES)
presentazione.insert(INSERT,vl)
presentazione.config(state=DISABLED)
testo=Text(finestra,width=80,height=25,bg="#8080ff",fg="#ccccff",font=('Courier', 16))
testo.pack(fill=BOTH, expand = YES)
if os.path.isfile('provola.txt'):
    ff=open("provola.txt","r")
    ff1=ff.read()
    testo.insert("1.0",ff1)
    ff.close()
pulsante=Button(finestra,text="ESEGUI",command=editor_salva)
pulsante1=Button(finestra,text="AIUTO",command=aiuto)
pulsante_reset=Button(finestra,text="CHIUDI",command=resetta)
aiuto_testo=Text(finestra,width=80,height=25,bg="#8080ff",fg="#ccccff",font=('Courier', 16))
aiuto=Listbox(finestra,width=80,height=5,bg="#8080ff",fg="#ccccff",font=('Courier', 16))
#aiuto.pack(fill=BOTH, expand = YES)
aiuto.bind("<<ListboxSelect>>",istruzioni)
pulsante.pack(fill=BOTH, expand = YES)
pulsante1.pack(fill=BOTH, expand = YES)
#finestra.bind('<Space>', tasto_premuto)
finestra.mainloop()
