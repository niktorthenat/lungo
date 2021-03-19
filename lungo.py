# Progetto LUNGO versione 0.1.93
# by NiktorTheNat (20202021)
# interprete su base del linguaggio Python
# ultima revisione 19/03/2021

vl="**** PROGETTO LUNGO 0.1.93 ****\n\nPER TUTTI I SISTEMI OPERATIVI BY NIKTORTHENAT\n\nPRONTO."

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
            elif r==">" and v==0:
                linea.append(parola)
                parola=""
                linea.append(r)
            elif r=="<" and v==0:
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
    istruzionia={"adesso":"datetime.datetime.now","aggiornadatabase":"commit","aggiungi":"append","aggiungimenu":"add_cascade","aggiungimenusecondario":"add_command","aggiungiparagrafo":"add_paragraph","alfabetico":"sort","alnumero":"to","altezza":"height","altrimenti":"else","altrimentise":"elif","anche":"and","anno":"year","apri":"open","apriaudio":"playsound.playsound","apricartella":"openpyxl.load_workbook","arrotondaperdifetto":"math.floor","arrotondapereccesso":"math.ceil","attendifineregistrazione":"sounddevice.wait"}
    istruzionib={"barra":"Progressbar","bordato":"GROOVE","botfine":"polling()","botinizio":"telebot.TeleBot"}
    istruzionic={"cambiacartella":"os.chdir","canali":"channels","cartellaesiste":"os.path.isdir","cartellacorrente":"os.getcwd","casellaadiscesa":"ttk.Combobox","casellaascelta":"Radiobutton","caselladitesto":"Entry","caselladitestoscrollabile":"scrolledtext.ScrolledText","casellaselezionabile":"Checkbutton","casuale":"random.random","cella":"cell","cercatutti":"findAll","chiudi":"close","ciclico":"mainloop","classe":"class","colonna":"column","colonnafinale":"max_col","colonnainiziale":"min_col","colore":"color","coloresfondo":"background","coloretesto":"foreground","comandidibase":'commands=["help","start"]',"comandimessaggi":"func=lambda message: True","combinazionetasti":"pyautogui.hotkey","combinazioniestese":"itertools.permutations","combinazioniuniche":"itertools.combinations","come":"as","con":"in","configura":"config","connettidatabase":"mysql.connector.connect","considera":"for","conta":"count","contalettere":"itertools.groupby","contatore":"Spinbox","contenuto":"content","contenutocartella":"os.listdir","continuaparagrafo":"add_run","controllaprogramma":"","copiafile":"shutil.copy","corsivo":"italic","coseno":"math.cos","creacartella":"os.mkdir","creaeseguibile":""}
    istruzionid={"da":"from","dalnumero":"from_","deviazionestandard":"statistics.stdev","diagrammaabarre":"matplotlib.pyplot.bar","diagrammaalinee":"matplotlib.pyplot.plot","diagrammaetichettax":"matplotlib.pyplot.xlabel","diagrammaetichettay":"matplotlib.pyplot.ylabel","diagrammatitolo":"matplotlib.pyplot.title","distruggi":"destroy","diventa":"as","dividi":"split","domanda":"input"}
    istruzionie={"e":"and","elaborasito":"BeautifulSoup","elimina":"delete","eliminacartella":"os.rmdir","eliminafile":"os.unlink","eliminaspazi":"strip","eliminaspaziiniziali":"lstrip","eliminaspazifinali":"rstrip","esegui":"command","estensione":"length","etichetta":"Label","eulero":"math.e","eventochiudi":"pygame.QUIT"}
    istruzionif={"faiclick":"pyautogui.click","faipausa":"interval","falso":"False","ferma":"break","fileaudio":"speech_recognition.AudioFile","fileesiste":"os.path.isfile","FINE":"END","finestra":"Tk","finestraattenzione":"messagebox.showwarning","finestracartella":"filedialog.askdirectory","finestradomanda":"messagebox.askquestion","finestraerrore":"messagebox.showerror","finestrafile":"filedialog.askopenfilename","finestrafiles":"filedialog.askopenfilenames","finestramessaggio":"messagebox.showinfo","finestraokannulla":"messagebox.askokcancel","finestrariprovaannulla":"messagebox.askretrycancel","finestrasino":"messagebox.askyesno","finestrasinoannulla":"messagebox.askyesnocancel","finiscecon":"endswith","finoache":"while","foglioattivo":"active","francese":"lang='fr'","frequenza":"samplerate","funzione":"def"}
    istruzionig={"gestionemessaggi":"message_handler","gestore":"cursor","giocoaggiornafinestra":"pygame.display.update","giococontrollaevento":"pygame.event.get","giocodimensionefinestra":"pygame.display.set_mode","giocodisegnacerchio":"pygame.draw.circle","giocodisegnalinea":"pygame.draw.line","giocodisegnapoligono":"pygame.draw.polygon","giocodisegnarettangolo":"pygame.draw.rect","giocofine":"pygame.quit","giocofrequenza":"pygame.time.delay","giocoinizio":"pygame.init","giocoriempimentofinestra":"fill","giocotastopremuto":"pygame.KEYDOWN","giocotitolofinestra":"pygame.display.set_caption","giorno":"day","giornodellasettimana":"weekday","gradi":"math.degrees","grandezza":"geometry","grassetto":"bold"}
    istruzionih={"htmlclasse":"class_","htmlid":"id"}
    istruzionii={"impacchetta":"pack","importa":"import","imposta":"set","in":"in","incassato":"SUNKEN","indice":"index","inglese":"lang='en'","iniziacon":"startswith","insecondi":"duration","inserisci":"insert","intero":"int","intervallo":"range","inverso":"reverse","inverti":"reversed","invia_benvenuto":"send_welcome","invia_messaggio":"echo_message","italiano":"lang='it'"}
    istruzionil={"lancia":"execute","larghezza":"width","legenda":"label","leggi":"read","lettura":'"r"',"lineaapuntini":"'dotten'","lineaapuntinietrattini":"'dashdot'","lineaatrattini":"'dashed'","lineaatrattiniepuntini":"'dashdot'","lineacontinua":"'solid'","linguaggio":"language","lunghezza":"len","logaritmo":"math.log"}
    istruzionim={"maggiore":"max","maiuscolo":"upper","margine":"border","media":"statistics.mean","memorizza":"write","menu":"Menu","menufinestra":"menu","menuprimario":"label","menusecondario":"menu","mese":"month","mestesso":"self","metti":"format","microfono":"sounddevice.rec","minore":"min","minuscolo":"lower","minuti":"minute","mischia":"random.shuffle","mostradiagramma":"matplotlib.pyplot.show","mostrahtml":"prettify","mostralegenda":"matplotlib.pyplot.legend","muovimouse":"pyautogui.moveTo"}
    istruzionin={"nepero":"math.e","nomecarattere":"font.name","nomefogli":"sheetnames","nomemenusecondario":"label","numerocasuale":"random.randint","numeroricorrente":"statistics.mode","numerosuccessivo":"itertools.accumulate","nuovacartella":"openpyxl.Workbook","nuovodocumento":"docx.Document"}
    istruzionio={"oppure":"or","ore":"hour","ospite":"host","ovunque":"global"}
    istruzionip={"paginahtml":"'html.parser'","paginaweb":"features='lxml'","parla":"gTTS","passa":"pass","pausasistema":"pyautogui.PAUSE","piatto":"FLAT","pigreco":"math.pi","porta":"port","positivo":"abs","posizione":"pop","posizionemouse":"pyautogui.position","potenza":"pow","premipulsante":"pyautogui.mouseDown","prendi":"get","primamaiuscola":"capitalize","primemaiuscole":"title","problema":"except","prova":"try","pulsante":"Button","pulsantedestro":"button='right'","pulsantedimezzo":"button='middle'","pulsantesinistro":"button='left'"}
    istruzionir={"radianti":"math.radians","radicequadrata":"math.sqrt","registrazione":"record","riconoscimentogoogle":"recognize_google","riconoscimentovocale":"speech_recognition.Recognizer","riga":"row","rigafinale":"max_row","rigainiziale":"min_row","righefoglio":"iter_rows","rilasciapulsante":"pyautogui.mouseUp","rilievo":"relief","rimuovi":"remove","rinominacartella":"os.rename","rinominafile":"os.rename","risoluzioneschermo":"pyautogui.size","rispondi":"reply_to"}
    istruzionis={"salva":"save","sceltacasuale":"random.choice","scrittura":'"w"',"scrivi":"print","scrollamouse":"pyautogui.scroll","se":"if","secondi":"second","selezionaelemento":"current","seno":"math.sin","sito":"requests.get","solovalori":"values_only","sostituisci":"replace","sottolineato":"underline","spaziox":"padx","spazioy":"pady","spessorelinea":"linewidth","spostafile":"shutil.move","stilelinea":"linestyle"}
    istruzionit={"tangente":"math.tan","tasto":"key","tasto_\\":"pygame.K_\\","tasto_|":"pygame.K_|","tasto_1":"pygame.K_1","tasto_!":"pygame.K_!","tasto_2":"pygame.K_2","tasto_3":"pygame.K_3","tasto_£":"pygame.K_£","tasto_4":"pygame.K_4","tasto_$":"pygame.K_$","tasto_5":"pygame.K_5","tasto_%":"pygame.K_%","tasto_6":"pygame.K_6","tasto_&":"pygame.K_&","tasto_7":"pygame.K_7","tasto_/":"pygame.K_/","tasto_8":"pygame.K_8","tasto_(":"pygame.K_(","tasto_9":"pygame.K_9","tasto_)":"pygame.K_)","tasto_0":"pygame.K_0","tasto_=":"pygame.K_=","tasto_?":"pygame.K_?","tasto_q":"pygame.K_q","tasto_Q":"pygame.K_Q","tasto_w":"pygame.K_w","tasto_W":"pygame.K_W","tasto_e":"pygame.K_e","tasto_E":"pygame.K_E","tasto_r":"pygame.K_r","tasto_R":"pygame.K_R","tasto_t":"pygame.K_t","tasto_T":"pygame.K_T","tasto_y":"pygame.K_y","tasto_Y":"pygame.K_Y","tasto_u":"pygame.K_u","tasto_U":"pygame.K_U","tasto_i":"pygame.K_i","tasto_I":"pygame.K_I","tasto_o":"pygame.K_o","tasto_O":"pygame.K_O","tasto_p":"pygame.K_p","tasto_P":"pygame.K_P","tasto_a":"pygame.K_a","tasto_A":"pygame.K_A","tasto_s":"pygame.K_s","tasto_S":"pygame.K_S","tasto_d":"pygame.K_d","tasto_D":"pygame.K_D","tasto_f":"pygame.K_f","tasto_F":"pygame.K_F","tasto_g":"pygame.K_g","tasto_G":"pygame.K_G","tasto_h":"pygame.K_h","tasto_H":"pygame.K_H","tasto_j":"pygame.K_j","tasto_J":"pygame.K_J","tasto_k":"pygame.K_k","tasto_K":"pygame.K_K","tasto_l":"pygame.K_l","tasto_L":"pygame.K_L","tasto_z":"pygame.K_z","tasto_Z":"pygame.K_Z","tasto_x":"pygame.K_x","tasto_X":"pygame.K_X","tasto_c":"pygame.K_c","tasto_C":"pygame.K_C","tasto_v":"pygame.K_v","tasto_V":"pygame.K_V","tasto_b":"pygame.K_b","tasto_B":"pygame.K_B","tasto_n":"pygame.K_n","tasto_N":"pygame.K_N","tasto_m":"pygame.K_m","tasto_M":"pygame.K_M","tasto_destro":"pygame.K_RIGHT","tasto_alto":"pygame.K_UP","tasto_basso":"pygame.K_DOWN","tasto_sinistro":"pygame.K_LEFT","tastodestra":"'right'","tastoelimina":"'backspace'","tastoinvio":"'enter'","tastosinistra":"'left'","testo":"text","tipo":"type","tipocarattere":"font","tipofile":"filetype","TipoErrore":"Exception","titolo":"title","trascinamouse":"pyautogui.dragTo","trova":"find"}
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
    #Rivedo tutte le istruzioni convertite per suddividerle
    #in base alle virgolette singole o doppie trovate
    listato_test=[]
    for r in listato:
        if '"' in r and len(r)>1:
            x=r.split('"')
            for t in x[:-1]:
                listato_test.append(t)
                listato_test.append('"')
            listato_test.append(x[-1])
        elif "'" in r and len(r)>1:
            x=r.split("'")
            for t in x[:-1]:
                listato_test.append(t)
                listato_test.append("'")
            listato_test.append(x[-1])
        else:
            listato_test.append(r)
    #Metto tutto il codice rivisitato dentro la variabile "listato"
    listato=listato_test  

    #Riesce a capire le istruzioni in modo più automatico
    #per sapere se deve importare moduli esterni sia da installare che moduli
    #già compresi con Python
    vs=0
    vd=0
    numero_moduli=0
    modulo_os,modulo_pyautogui,modulo_shutil=0,0,0
    modulo_pygame,modulo_matplotlib,modulo_beautifulsoup4=0,0,0
    modulo_docx,modulo_playsound,modulo_gtts=0,0,0
    modulo_speech,modulo_mysql,modulo_openpyxl=0,0,0
    modulo_telebot,modulo_sounddevice=0,0
    modulo_math,modulo_statistics,modulo_intertools=0,0,0
    modulo_random,modulo_datetime,modulo_requests=0,0,0
    for r in listato:
        if "'" in r:
            if vs==0:
                vs=1
            else:
                vs=0
        elif '"' in r:
            if vd==0:
                vd=1
            else:
                vd=0
    #Blocco che importa i moduli esterni NON presenti nell'installazione Python
        if "openpyxl" in r and vd==0 and vs==0:
            if modulo_openpyxl==0:
                programma.write("import openpyxl\n")
                modulo_openpyxl=1
                numero_moduli=numero_moduli+1
            if "openpyxl" in sys.modules:
                pass
            else:
                os.system("pip install openpyxl")
        if "mysql" in r and vd==0 and vs==0:
            if modulo_mysql==0:
                programma.write("import mysql-connector\n")
                modulo_mysql=1
                numero_moduli=numero_moduli+1
            if "mysql.connector" in sys.modules:
                pass
            else:
                os.system("pip install mysql-connector-python")
        print(r,vd,vs)
        if "speech_recognition" in r and vd==0 and vs==0:
            if modulo_speech==0:
                programma.write("import speech_recognition\n")
                modulo_speech=1
                numero_moduli=numero_moduli+1
            if "speech_recognition" in sys.modules:
                pass
            else:
                os.system("pip install SpeechRecognition")
        if "gTTS" in r and vd==0 and vs==0:
            if modulo_gtts==0:
                programma.write("from gtts import *\n")
                modulo_gtts=1
                numero_moduli=numero_moduli+1
            if "gtts" in sys.modules:
                pass
            else:
                os.system("pip install gtts")
        if "playsound" in r and vd==0 and vs==0:
            if modulo_playsound==0:
                programma.write("import playsound\n")
                modulo_playsound=1
                numero_moduli=numero_moduli+1
            if "playsound" in sys.module:
                pass
            else:
                os.system("pip install playsound")
        if "docx.Document" in r and vd==0 and vs==0:
            if modulo_docx==0:
                programma.write("import docx\n")
                modulo_docx=1
                numero_moduli=numero_moduli+1
            if "python-docx" in sys.modules:
                pass
            else:
                os.system("pip install python-docx")
        if "requests.get" in r and vd==0 and vs==0:
            if modulo_beautifulsoup4==0:
                programma.write("import requests\n")
                programma.write("from bs4 import BeautifulSoup\n")
                modulo_beautifulsoup4=1
                numero_moduli=numero_moduli+1
            if "requests" in sys.modules and "beautifulsoup4" in sys.modules:
                pass
            else:
                os.system("pip install beautifulsoup4")
                os.system("pip install requests")
        #if "requests.get" in r and vd==0 and vs==0:
         #   if modulo_requests==0:
          #      programma.write("import requests\n")
           #     modulo_requests=1
            #    numero_moduli=numero_moduli+1
           # if "requests" in sys.modules:
            #    pass
            #else:
             #   os.system("pip install requests")
        if "pyautogui" in r and vd==0 and vs==0:
            if modulo_pyautogui==0:
                programma.write("import pyautogui\n")
                modulo_pyautogui=1
                numero_moduli=numero_moduli+1
            if "pyautogui" in sys.modules:
                pass
            else:
                os.system("pip install pyautogui")
                break
        if "pygame" in r and vd==0 and vs==0:
            if modulo_pygame==0:
                programma.write("import pygame\n")
                modulo_pygame=1
                numero_moduli=numero_moduli+1
            if "pygame" in sys.modules:
                pass
            else:
                os.system("pip install pygame")
        if "matplotlib" in r and vd==0 and vs==0:
            if modulo_matplotlib==0:
                programma.write("import matplotlib.pyplot\n")
                modulo_matplotlib=1
                numero_moduli=numero_moduli+1
            if "matplotlib" in sys.modules:
                pass
            else:
                os.system("pip install matplotlib")
        if "telebot" in r and vd==0 and vs==0:
            if modulo_telebot==0:
                programma.write("import telebot\n")
                modulo_telebot=1
                numero_moduli=numero_moduli+1
            if "telebot" in sys.modules:
                pass
            else:
                os.system("pip install pyTelegramBotAPI")

        if "sounddevice" in r and vd==0 and vs==0:
            if modulo_sounddevice==0:
                programma.write("import sounddevice\n")
                programma.write("from soundfile import write\n")
                modulo_sounddevice=1
                numero_moduli=numero_moduli+1
            if "sounddevice" in sys.modules:
                pass
            else:
                os.system("pip install sounddevice")
                os.system("pip install soundfile")
    #Blocco che importa i moduli plugin già presenti nell'installazione Python
        if "os" in r and vd==0 and vs==0:
            if modulo_os==0:
                programma.write("import os\n")
                modulo_os=1
                numero_moduli=numero_moduli+1
        if "shutil" in r and vd==0 and vs==0:
            if modulo_shutil==0:
                programma.write("import shutil\n")
                modulo_shutil=1
                numero_moduli=numero_moduli+1
        if "math" in r and vd==0 and vs==0:
            if modulo_math==0:
                programma.write("import math\n")
                modulo_math=1
                numero_moduli=numero_moduli+1
        if "statistics" in r and vd==0 and vs==0:
            if modulo_statistics==0:
                programma.write("import statistics\n")
                modulo_statistics=1
                numero_moduli=numero_moduli+1
        if "intertools" in r and vd==0 and vs==0:
            if modulo_intertools==0:
                programma.write("import intertools\n")
                modulo_intertools=1
                numero_moduli=numero_moduli+1
        if "random" in r and vd==0 and vs==0:
            if modulo_random==0:
                programma.write("import random\n")
                modulo_random=1
                numero_moduli=numero_moduli+1
        if "datetime" in r and vd==0 and vs==0:
            if modulo_datetime==0:
                programma.write("import datetime\n")
                modulo_datetime=1
                numero_moduli=numero_moduli+1
    #fine blocco - riesce a capire le istruzioni in mod più automatico
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
        output1 = subprocess.call("python.exe provola-convertito.py")
        output = subprocess.Popen("python.exe provola-convertito.py",stderr=subprocess.PIPE)
        x1x,y1y=output.communicate()
        #print("***1111****",x1x,"\n\n***222****",y1y)
        if output1==1:
            x1x=str(y1y)
            #print(x1x)
            x2x=x1x.split("line")
            #print(x2x)
            x3x=x2x[1]
            x3x=str(x3x).strip()
            x4x=x3x.split(" ")
            x5x=(x4x[0].translate({ord(i):None for i in "()#':;-+*ABCDEFGHIJKLMNOPQRSTUVWYXZabcdefghijklmnopqrstuvwyxz/\\"}))
            #print("**\n",(x5x),"\n**")
            codice_errore={"AssertionError":"anomalia non meglio rilevata","AttributeError":"assegnazione o di riferimento di un attributo","EOFError":"fine file incorretto","FileNotFoundError":"file inesistente","FloatingPointError":"virgola mobile","GeneratorExit":"probabile chiusura flusso dati","ImportError":"importazione modulo","IndexError":"indice fuori intervallo","KeyError":"elemento o chiave dizionario non trovata","KeyboardInterrupt":"chiusura volontaria del programma da parte dell'utente","MemoryError":"memloria esaurita","NameError":"variabile inesistente o per variabile usata fuori dalla sua usabilità","NotImplementedError":"anomalia non meglio identificata","OSError":"anomalia generica non meglio identificata","OverflowError":"calcolo matematico troppo grande","ReferenceError":"Garbage Collection","RuntimeError":"anomalia non meglio identificata","StopIteration":"richiesta generica non potuta esaudire","SyntaxError":"sintassi, cioè di scrittura del codice, spesso dovuto a mancanza parentesi, virgolette, graffe, segno del duepunti e cose simili","IndentationError":"istruzione che è stata scritta con rientro dal margine (indentazione) sbagliata","TabError":"istruzione che ha un rientro dal margine (indentazione) sbagliata perchè troppo spaziata o meno","SystemError":"anomalia del linguaggio Lungo","SystemExit":"uscita dal programma","TypeError":"applicazione di funzione o operazione a oggetto errato","UnboundLocalError":"una variabile locale o di una funzione che non ha valore","UnicodeError":"codifica o decodifica unicode (esempio sono le lettere speciali o caratteri speciali)","UnicodeEncodeError":"codifica o decodifica unicode (esempio sono le lettere speciali o caratteri speciali)","UnicodeDecodeError":"codifica o decodifica unicode (esempio sono le lettere speciali o caratteri speciali)","UnicodeTranslateError":"codifica o decodifica unicode (esempio sono le lettere speciali o caratteri speciali)","ValueError":"errore di valore","ZeroDivisionError":"divisione per zero"}
            if x5x.isdigit():
                for r in codice_errore.keys():
                    if r in x1x:
                        messagebox.showerror(title="ERRORE",message="Rilevato errore alla riga "+str(int(x5x)-8-numero_moduli-1)+" di "+codice_errore[r])
                        break
            else:
                messagebox.showerror(title="PROBLEMA",message="Rilevo una anomalia nel codice che non so meglio individuare. Statisticamente è capitato questo problema quando si usa una variabile in una istruzione SE che non era stata dichiarata prima")
    else:
        if "pyinstaller" in sys.modules:
            subprocess.run("pyinstaller --onefile provola-convertito.py")
        else:
            os.system("pip install pyinstaller")
            subprocess.run("pyinstaller --onefile provola-convertito.py")

def carattere_piccolo():
    testo.configure(font=('Courier new', 11))

def carattere_medio():
    testo.configure(font=('Courier', 13))

def carattere_grande():
    testo.configure(font=('Courier', 16))

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

def istruzioni1(event):
    y=event.widget.get()
    x=aiuto.get(0,"end").index(y)
    aiuto_testo.focus_set()
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
    #faccio scomparire i vari componenti di testo e pulsanti
    presentazione.pack_forget()
    testo.pack_forget()
    pulsante_reset.pack(fill=BOTH, expand = YES)
    aiuto.pack(fill=BOTH,expand=YES)
    aiuto_cerca.pack(fill=BOTH,expand=YES)
    #copia delle istruzioni riconosciute dal programma
    istruzioni={"__inizializza__":"__init__","_no_":'"no"',"_si_":'"yes"'}
    istruzionia={"adesso":"datetime.datetime.now","aggiornadatabase":"commit","aggiungi":"append","aggiungimenu":"add_cascade","aggiungimenusecondario":"add_command","aggiungiparagrafo":"add_paragraph","alfabetico":"sort","alnumero":"to","altezza":"height","altrimenti":"else","altrimentise":"elif","anche":"and","anno":"year","apri":"open","apriaudio":"playsound.playsound","apricartella":"openpyxl.load_workbook","arrotondaperdifetto":"math.floor","arrotondapereccesso":"math.ceil","attendifineregistrazione":"sounddevice.wait"}
    istruzionib={"barra":"Progressbar","bordato":"GROOVE","botfine":"polling()","botinizio":"telebot.TeleBot"}
    istruzionic={"cambiacartella":"os.chdir","canali":"channels","cartellaesiste":"os.path.isdir","cartellacorrente":"os.getcwd","casellaadiscesa":"ttk.Combobox","casellaascelta":"Radiobutton","caselladitesto":"Entry","caselladitestoscrollabile":"scrolledtext.ScrolledText","casellaselezionabile":"Checkbutton","casuale":"random.random","cella":"cell","cercatutti":"findAll","chiudi":"close","ciclico":"mainloop","classe":"class","colonna":"column","colonnafinale":"max_col","colonnainiziale":"min_col","colore":"color","coloresfondo":"background","coloretesto":"foreground","comandidibase":'commands=["help","start"]',"comandimessaggi":"func=lambda message: True","combinazionetasti":"pyautogui.hotkey","combinazioniestese":"itertools.permutations","combinazioniuniche":"itertools.combinations","come":"as","con":"in","configura":"config","connettidatabase":"mysql.connector.connect","considera":"for","conta":"count","contalettere":"itertools.groupby","contatore":"Spinbox","contenuto":"content","contenutocartella":"os.listdir","continuaparagrafo":"add_run","controllaprogramma":"","copiafile":"shutil.copy","corsivo":"italic","coseno":"math.cos","creacartella":"os.mkdir","creaeseguibile":""}
    istruzionid={"da":"from","dalnumero":"from_","deviazionestandard":"statistics.stdev","diagrammaabarre":"matplotlib.pyplot.bar","diagrammaalinee":"matplotlib.pyplot.plot","diagrammaetichettax":"matplotlib.pyplot.xlabel","diagrammaetichettay":"matplotlib.pyplot.ylabel","diagrammatitolo":"matplotlib.pyplot.title","distruggi":"destroy","diventa":"as","dividi":"split","domanda":"input"}
    istruzionie={"e":"and","elaborasito":"BeautifulSoup","elimina":"delete","eliminacartella":"os.rmdir","eliminafile":"os.unlink","eliminaspazi":"strip","eliminaspaziiniziali":"lstrip","eliminaspazifinali":"rstrip","esegui":"command","estensione":"length","etichetta":"Label","eulero":"math.e","eventochiudi":"pygame.QUIT"}
    istruzionif={"faiclick":"pyautogui.click","faipausa":"interval","falso":"False","ferma":"break","fileaudio":"speech_recognition.AudioFile","fileesiste":"os.path.isfile","FINE":"END","finestra":"Tk","finestraattenzione":"messagebox.showwarning","finestracartella":"filedialog.askdirectory","finestradomanda":"messagebox.askquestion","finestraerrore":"messagebox.showerror","finestrafile":"filedialog.askopenfilename","finestrafiles":"filedialog.askopenfilenames","finestramessaggio":"messagebox.showinfo","finestraokannulla":"messagebox.askokcancel","finestrariprovaannulla":"messagebox.askretrycancel","finestrasino":"messagebox.askyesno","finestrasinoannulla":"messagebox.askyesnocancel","finiscecon":"endswith","finoache":"while","foglioattivo":"active","francese":"lang='fr'","frequenza":"samplerate","funzione":"def"}
    istruzionig={"gestionemessaggi":"message_handler","gestore":"cursor","giocoaggiornafinestra":"pygame.display.update","giococontrollaevento":"pygame.event.get","giocodimensionefinestra":"pygame.display.set_mode","giocodisegnacerchio":"pygame.draw.circle","giocodisegnalinea":"pygame.draw.line","giocodisegnapoligono":"pygame.draw.polygon","giocodisegnarettangolo":"pygame.draw.rect","giocofine":"pygame.quit","giocofrequenza":"pygame.time.delay","giocoinizio":"pygame.init","giocoriempimentofinestra":"fill","giocotastopremuto":"pygame.KEYDOWN","giocotitolofinestra":"pygame.display.set_caption","giorno":"day","giornodellasettimana":"weekday","gradi":"math.degrees","grandezza":"geometry","grassetto":"bold"}
    istruzionih={"htmlclasse":"class_","htmlid":"id"}
    istruzionii={"impacchetta":"pack","importa":"import","imposta":"set","in":"in","incassato":"SUNKEN","indice":"index","inglese":"lang='en'","iniziacon":"startswith","insecondi":"duration","inserisci":"insert","intero":"int","intervallo":"range","inverso":"reverse","inverti":"reversed","invia_benvenuto":"send_welcome","invia_messaggio":"echo_message","italiano":"lang='it'"}
    istruzionil={"lancia":"execute","larghezza":"width","legenda":"label","leggi":"read","lettura":'"r"',"lineaapuntini":"'dotten'","lineaapuntinietrattini":"'dashdot'","lineaatrattini":"'dashed'","lineaatrattiniepuntini":"'dashdot'","lineacontinua":"'solid'","linguaggio":"language","lunghezza":"len","logaritmo":"math.log"}
    istruzionim={"maggiore":"max","maiuscolo":"upper","margine":"border","media":"statistics.mean","memorizza":"write","menu":"Menu","menufinestra":"menu","menuprimario":"label","menusecondario":"menu","mese":"month","mestesso":"self","metti":"format","microfono":"sounddevice.rec","minore":"min","minuscolo":"lower","minuti":"minute","mischia":"random.shuffle","mostradiagramma":"matplotlib.pyplot.show","mostrahtml":"prettify","mostralegenda":"matplotlib.pyplot.legend","muovimouse":"pyautogui.moveTo"}
    istruzionin={"nepero":"math.e","nomecarattere":"font.name","nomefogli":"sheetnames","nomemenusecondario":"label","numerocasuale":"random.randint","numeroricorrente":"statistics.mode","numerosuccessivo":"itertools.accumulate","nuovacartella":"openpyxl.Workbook","nuovodocumento":"docx.Document"}
    istruzionio={"oppure":"or","ore":"hour","ospite":"host","ovunque":"global"}
    istruzionip={"paginahtml":"'html.parser'","paginaweb":"features='lxml'","parla":"gTTS","passa":"pass","pausasistema":"pyautogui.PAUSE","piatto":"FLAT","pigreco":"math.pi","porta":"port","positivo":"abs","posizione":"pop","posizionemouse":"pyautogui.position","potenza":"pow","premipulsante":"pyautogui.mouseDown","prendi":"get","primamaiuscola":"capitalize","primemaiuscole":"title","problema":"except","prova":"try","pulsante":"Button","pulsantedestro":"button='right'","pulsantedimezzo":"button='middle'","pulsantesinistro":"button='left'"}
    istruzionir={"radianti":"math.radians","radicequadrata":"math.sqrt","registrazione":"record","riconoscimentogoogle":"recognize_google","riconoscimentovocale":"speech_recognition.Recognizer","riga":"row","rigafinale":"max_row","rigainiziale":"min_row","righefoglio":"iter_rows","rilasciapulsante":"pyautogui.mouseUp","rilievo":"relief","rimuovi":"remove","rinominacartella":"os.rename","rinominafile":"os.rename","risoluzioneschermo":"pyautogui.size","rispondi":"reply_to"}
    istruzionis={"salva":"save","sceltacasuale":"random.choice","scrittura":'"w"',"scrivi":"print","scrollamouse":"pyautogui.scroll","se":"if","secondi":"second","selezionaelemento":"current","seno":"math.sin","sito":"requests.get","solovalori":"values_only","sostituisci":"replace","sottolineato":"underline","spaziox":"padx","spazioy":"pady","spessorelinea":"linewidth","spostafile":"shutil.move","stilelinea":"linestyle"}
    istruzionit={"tangente":"math.tan","tasto":"key","tasto_\\":"pygame.K_\\","tasto_|":"pygame.K_|","tasto_1":"pygame.K_1","tasto_!":"pygame.K_!","tasto_2":"pygame.K_2","tasto_3":"pygame.K_3","tasto_£":"pygame.K_£","tasto_4":"pygame.K_4","tasto_$":"pygame.K_$","tasto_5":"pygame.K_5","tasto_%":"pygame.K_%","tasto_6":"pygame.K_6","tasto_&":"pygame.K_&","tasto_7":"pygame.K_7","tasto_/":"pygame.K_/","tasto_8":"pygame.K_8","tasto_(":"pygame.K_(","tasto_9":"pygame.K_9","tasto_)":"pygame.K_)","tasto_0":"pygame.K_0","tasto_=":"pygame.K_=","tasto_?":"pygame.K_?","tasto_q":"pygame.K_q","tasto_Q":"pygame.K_Q","tasto_w":"pygame.K_w","tasto_W":"pygame.K_W","tasto_e":"pygame.K_e","tasto_E":"pygame.K_E","tasto_r":"pygame.K_r","tasto_R":"pygame.K_R","tasto_t":"pygame.K_t","tasto_T":"pygame.K_T","tasto_y":"pygame.K_y","tasto_Y":"pygame.K_Y","tasto_u":"pygame.K_u","tasto_U":"pygame.K_U","tasto_i":"pygame.K_i","tasto_I":"pygame.K_I","tasto_o":"pygame.K_o","tasto_O":"pygame.K_O","tasto_p":"pygame.K_p","tasto_P":"pygame.K_P","tasto_a":"pygame.K_a","tasto_A":"pygame.K_A","tasto_s":"pygame.K_s","tasto_S":"pygame.K_S","tasto_d":"pygame.K_d","tasto_D":"pygame.K_D","tasto_f":"pygame.K_f","tasto_F":"pygame.K_F","tasto_g":"pygame.K_g","tasto_G":"pygame.K_G","tasto_h":"pygame.K_h","tasto_H":"pygame.K_H","tasto_j":"pygame.K_j","tasto_J":"pygame.K_J","tasto_k":"pygame.K_k","tasto_K":"pygame.K_K","tasto_l":"pygame.K_l","tasto_L":"pygame.K_L","tasto_z":"pygame.K_z","tasto_Z":"pygame.K_Z","tasto_x":"pygame.K_x","tasto_X":"pygame.K_X","tasto_c":"pygame.K_c","tasto_C":"pygame.K_C","tasto_v":"pygame.K_v","tasto_V":"pygame.K_V","tasto_b":"pygame.K_b","tasto_B":"pygame.K_B","tasto_n":"pygame.K_n","tasto_N":"pygame.K_N","tasto_m":"pygame.K_m","tasto_M":"pygame.K_M","tasto_destro":"pygame.K_RIGHT","tasto_alto":"pygame.K_UP","tasto_basso":"pygame.K_DOWN","tasto_sinistro":"pygame.K_LEFT","tastodestra":"'right'","tastoelimina":"'backspace'","tastoinvio":"'enter'","tastosinistra":"'left'","testo":"text","tipo":"type","tipocarattere":"font","tipofile":"filetype","TipoErrore":"Exception","titolo":"title","trascinamouse":"pyautogui.dragTo","trova":"find"}
    istruzioniu={"unici":"set","unisci":"join","usa":"with","usalatastiera":"pyautogui.typewrite","utente":"user"}
    istruzioniv={"valore":"value","valori":"values","variabile":"var","variabilebooleana":"BooleanVar()","variabileintera":"IntVar()","VariabileNonDefinita":"NameError","vero":"True","verticelinea":"marker","volte":"clicks"}
    colori={"!rosso":"'red'","!giallo":"'yellow'","!verde":"'green'"}
    codice={**istruzioni,**istruzionia,**istruzionib,**istruzionic,**istruzionid,**istruzionie,**istruzionif,**istruzionig,**istruzionih,**istruzionii,**istruzionil,**istruzionim,**istruzionin,**istruzionio,**istruzionip,**istruzionir,**istruzionis,**istruzionit,**istruzioniu,**istruzioniv,**colori}
    tt=1
    #inserisce nella lista a discesa "aiuto" tutte le istruzioni del dizionario qui sopra
    for xx in codice:    
        aiuto.insert(tt,xx)
        tt=tt+1
    aiuto_testo.pack(fill=BOTH,expand=YES)

def resetta():
    aiuto.delete(0,END)
    pulsante_reset.pack_forget()
    aiuto.pack_forget()
    aiuto_testo.pack_forget()
    aiuto_cerca.forget()
    presentazione.pack(fill=BOTH, expand = YES)
    testo.pack(fill=BOTH, expand = YES)


#colora nell'editor le istruzioni riconosciute
def colora(istruzione,x,y,colore):
    xx=str(y)+"."+str(x)
    xx1=str(y)+"."+str(x-len(istruzione))
    testo.tag_add(colore,xx1,xx)

def correggi(event=None):
    global programma
    programma=""
    apertav=0 #aperte/chiuse virgolette
    apertadv=0 #aperte/chiuse doppie virgolette
    linea=""
    riga=""
    istruzione=""
    rigacompleta=""
    controllore=0
    progressivo=0
    x=0
    y=0
    #mette in "codice" tutto il programma scritto fino ad ora
    codice=testo.get(0.0,END)
    #mette nella lista "riga" ogni singola riga del programma
    riga=codice.split("\n")
    #definisce i colori utilizzabili
    testo.tag_config("uno",foreground="violet")
    testo.tag_config("due",foreground="blue")
    testo.tag_config("tre",foreground="plum2")
    #print (time.strftime("Modifiche aggiornate il: %d/%m/%Y alle ore %H:%M:%S"))
    for linea in riga:
        y=y+1
        x=0
        #costruisce le singole parole esaminando carattere per carattere
        for carattere in linea:
            x=x+1
            istruzione=istruzione+carattere
            #print(istruzione)
            #verifica ed eventualmente colora le singole istruzioni
            istruzioni={"__inizializza__":"__init__","_no_":'"no"',"_si_":'"yes"'}
            istruzionia={"adesso":"datetime.datetime.now","aggiornadatabase":"commit","aggiungi":"append","aggiungimenu":"add_cascade","aggiungimenusecondario":"add_command","aggiungiparagrafo":"add_paragraph","alfabetico":"sort","alnumero":"to","altezza":"height","altrimenti":"else","altrimentise":"elif","anche":"and","anno":"year","apri":"open","apriaudio":"playsound.playsound","apricartella":"openpyxl.load_workbook","arrotondaperdifetto":"math.floor","arrotondapereccesso":"math.ceil","attendifineregistrazione":"sounddevice.wait"}
            istruzionib={"barra":"Progressbar","bordato":"GROOVE","botfine":"polling()","botinizio":"telebot.TeleBot"}
            istruzionic={"cambiacartella":"os.chdir","canali":"channels","cartellaesiste":"os.path.isdir","cartellacorrente":"os.getcwd","casellaadiscesa":"ttk.Combobox","casellaascelta":"Radiobutton","caselladitesto":"Entry","caselladitestoscrollabile":"scrolledtext.ScrolledText","casellaselezionabile":"Checkbutton","casuale":"random.random","cella":"cell","cercatutti":"findAll","chiudi":"close","ciclico":"mainloop","classe":"class","colonna":"column","colonnafinale":"max_col","colonnainiziale":"min_col","colore":"color","coloresfondo":"background","coloretesto":"foreground","comandidibase":'commands=["help","start"]',"comandimessaggi":"func=lambda message: True","combinazionetasti":"pyautogui.hotkey","combinazioniestese":"itertools.permutations","combinazioniuniche":"itertools.combinations","come":"as","con":"in","configura":"config","connettidatabase":"mysql.connector.connect","considera":"for","conta":"count","contalettere":"itertools.groupby","contatore":"Spinbox","contenuto":"content","contenutocartella":"os.listdir","continuaparagrafo":"add_run","controllaprogramma":"","copiafile":"shutil.copy","corsivo":"italic","coseno":"math.cos","creacartella":"os.mkdir","creaeseguibile":""}
            istruzionid={"da":"from","dalnumero":"from_","deviazionestandard":"statistics.stdev","diagrammaabarre":"matplotlib.pyplot.bar","diagrammaalinee":"matplotlib.pyplot.plot","diagrammaetichettax":"matplotlib.pyplot.xlabel","diagrammaetichettay":"matplotlib.pyplot.ylabel","diagrammatitolo":"matplotlib.pyplot.title","distruggi":"destroy","diventa":"as","dividi":"split","domanda":"input"}
            istruzionie={"e":"and","elaborasito":"BeautifulSoup","elimina":"delete","eliminacartella":"os.rmdir","eliminafile":"os.unlink","eliminaspazi":"strip","eliminaspaziiniziali":"lstrip","eliminaspazifinali":"rstrip","esegui":"command","estensione":"length","etichetta":"Label","eulero":"math.e","eventochiudi":"pygame.QUIT"}
            istruzionif={"faiclick":"pyautogui.click","faipausa":"interval","falso":"False","ferma":"break","fileaudio":"speech_recognition.AudioFile","fileesiste":"os.path.isfile","FINE":"END","finestra":"Tk","finestraattenzione":"messagebox.showwarning","finestracartella":"filedialog.askdirectory","finestradomanda":"messagebox.askquestion","finestraerrore":"messagebox.showerror","finestrafile":"filedialog.askopenfilename","finestrafiles":"filedialog.askopenfilenames","finestramessaggio":"messagebox.showinfo","finestraokannulla":"messagebox.askokcancel","finestrariprovaannulla":"messagebox.askretrycancel","finestrasino":"messagebox.askyesno","finestrasinoannulla":"messagebox.askyesnocancel","finiscecon":"endswith","finoache":"while","foglioattivo":"active","francese":"lang='fr'","frequenza":"samplerate","funzione":"def"}
            istruzionig={"gestionemessaggi":"message_handler","gestore":"cursor","giocoaggiornafinestra":"pygame.display.update","giococontrollaevento":"pygame.event.get","giocodimensionefinestra":"pygame.display.set_mode","giocodisegnacerchio":"pygame.draw.circle","giocodisegnalinea":"pygame.draw.line","giocodisegnapoligono":"pygame.draw.polygon","giocodisegnarettangolo":"pygame.draw.rect","giocofine":"pygame.quit","giocofrequenza":"pygame.time.delay","giocoinizio":"pygame.init","giocoriempimentofinestra":"fill","giocotastopremuto":"pygame.KEYDOWN","giocotitolofinestra":"pygame.display.set_caption","giorno":"day","giornodellasettimana":"weekday","gradi":"math.degrees","grandezza":"geometry","grassetto":"bold"}
            istruzionih={"htmlclasse":"class_","htmlid":"id"}
            istruzionii={"impacchetta":"pack","importa":"import","imposta":"set","in":"in","incassato":"SUNKEN","indice":"index","inglese":"lang='en'","iniziacon":"startswith","insecondi":"duration","inserisci":"insert","intero":"int","intervallo":"range","inverso":"reverse","inverti":"reversed","invia_benvenuto":"send_welcome","invia_messaggio":"echo_message","italiano":"lang='it'"}
            istruzionil={"lancia":"execute","larghezza":"width","legenda":"label","leggi":"read","lettura":'"r"',"lineaapuntini":"'dotten'","lineaapuntinietrattini":"'dashdot'","lineaatrattini":"'dashed'","lineaatrattiniepuntini":"'dashdot'","lineacontinua":"'solid'","linguaggio":"language","lunghezza":"len","logaritmo":"math.log"}
            istruzionim={"maggiore":"max","maiuscolo":"upper","margine":"border","media":"statistics.mean","memorizza":"write","menu":"Menu","menufinestra":"menu","menuprimario":"label","menusecondario":"menu","mese":"month","mestesso":"self","metti":"format","microfono":"sounddevice.rec","minore":"min","minuscolo":"lower","minuti":"minute","mischia":"random.shuffle","mostradiagramma":"matplotlib.pyplot.show","mostrahtml":"prettify","mostralegenda":"matplotlib.pyplot.legend","muovimouse":"pyautogui.moveTo"}
            istruzionin={"nepero":"math.e","nomecarattere":"font.name","nomefogli":"sheetnames","nomemenusecondario":"label","numerocasuale":"random.randint","numeroricorrente":"statistics.mode","numerosuccessivo":"itertools.accumulate","nuovacartella":"openpyxl.Workbook","nuovodocumento":"docx.Document"}
            istruzionio={"oppure":"or","ore":"hour","ospite":"host","ovunque":"global"}
            istruzionip={"paginahtml":"'html.parser'","paginaweb":"features='lxml'","parla":"gTTS","passa":"pass","pausasistema":"pyautogui.PAUSE","piatto":"FLAT","pigreco":"math.pi","porta":"port","positivo":"abs","posizione":"pop","posizionemouse":"pyautogui.position","potenza":"pow","premipulsante":"pyautogui.mouseDown","prendi":"get","primamaiuscola":"capitalize","primemaiuscole":"title","problema":"except","prova":"try","pulsante":"Button","pulsantedestro":"button='right'","pulsantedimezzo":"button='middle'","pulsantesinistro":"button='left'"}
            istruzionir={"radianti":"math.radians","radicequadrata":"math.sqrt","registrazione":"record","riconoscimentogoogle":"recognize_google","riconoscimentovocale":"speech_recognition.Recognizer","riga":"row","rigafinale":"max_row","rigainiziale":"min_row","righefoglio":"iter_rows","rilasciapulsante":"pyautogui.mouseUp","rilievo":"relief","rimuovi":"remove","rinominacartella":"os.rename","rinominafile":"os.rename","risoluzioneschermo":"pyautogui.size","rispondi":"reply_to"}
            istruzionis={"salva":"save","sceltacasuale":"random.choice","scrittura":'"w"',"scrivi":"print","scrollamouse":"pyautogui.scroll","se":"if","secondi":"second","selezionaelemento":"current","seno":"math.sin","sito":"requests.get","solovalori":"values_only","sostituisci":"replace","sottolineato":"underline","spaziox":"padx","spazioy":"pady","spessorelinea":"linewidth","spostafile":"shutil.move","stilelinea":"linestyle"}
            istruzionit={"tangente":"math.tan","tasto":"key","tasto_\\":"pygame.K_\\","tasto_|":"pygame.K_|","tasto_1":"pygame.K_1","tasto_!":"pygame.K_!","tasto_2":"pygame.K_2","tasto_3":"pygame.K_3","tasto_£":"pygame.K_£","tasto_4":"pygame.K_4","tasto_$":"pygame.K_$","tasto_5":"pygame.K_5","tasto_%":"pygame.K_%","tasto_6":"pygame.K_6","tasto_&":"pygame.K_&","tasto_7":"pygame.K_7","tasto_/":"pygame.K_/","tasto_8":"pygame.K_8","tasto_(":"pygame.K_(","tasto_9":"pygame.K_9","tasto_)":"pygame.K_)","tasto_0":"pygame.K_0","tasto_=":"pygame.K_=","tasto_?":"pygame.K_?","tasto_q":"pygame.K_q","tasto_Q":"pygame.K_Q","tasto_w":"pygame.K_w","tasto_W":"pygame.K_W","tasto_e":"pygame.K_e","tasto_E":"pygame.K_E","tasto_r":"pygame.K_r","tasto_R":"pygame.K_R","tasto_t":"pygame.K_t","tasto_T":"pygame.K_T","tasto_y":"pygame.K_y","tasto_Y":"pygame.K_Y","tasto_u":"pygame.K_u","tasto_U":"pygame.K_U","tasto_i":"pygame.K_i","tasto_I":"pygame.K_I","tasto_o":"pygame.K_o","tasto_O":"pygame.K_O","tasto_p":"pygame.K_p","tasto_P":"pygame.K_P","tasto_a":"pygame.K_a","tasto_A":"pygame.K_A","tasto_s":"pygame.K_s","tasto_S":"pygame.K_S","tasto_d":"pygame.K_d","tasto_D":"pygame.K_D","tasto_f":"pygame.K_f","tasto_F":"pygame.K_F","tasto_g":"pygame.K_g","tasto_G":"pygame.K_G","tasto_h":"pygame.K_h","tasto_H":"pygame.K_H","tasto_j":"pygame.K_j","tasto_J":"pygame.K_J","tasto_k":"pygame.K_k","tasto_K":"pygame.K_K","tasto_l":"pygame.K_l","tasto_L":"pygame.K_L","tasto_z":"pygame.K_z","tasto_Z":"pygame.K_Z","tasto_x":"pygame.K_x","tasto_X":"pygame.K_X","tasto_c":"pygame.K_c","tasto_C":"pygame.K_C","tasto_v":"pygame.K_v","tasto_V":"pygame.K_V","tasto_b":"pygame.K_b","tasto_B":"pygame.K_B","tasto_n":"pygame.K_n","tasto_N":"pygame.K_N","tasto_m":"pygame.K_m","tasto_M":"pygame.K_M","tasto_destro":"pygame.K_RIGHT","tasto_alto":"pygame.K_UP","tasto_basso":"pygame.K_DOWN","tasto_sinistro":"pygame.K_LEFT","tastodestra":"'right'","tastoelimina":"'backspace'","tastoinvio":"'enter'","tastosinistra":"'left'","testo":"text","tipo":"type","tipocarattere":"font","tipofile":"filetype","TipoErrore":"Exception","titolo":"title","trascinamouse":"pyautogui.dragTo","trova":"find"}
            istruzioniu={"unici":"set","unisci":"join","usa":"with","usalatastiera":"pyautogui.typewrite","utente":"user"}
            istruzioniv={"valore":"value","valori":"values","variabile":"var","variabilebooleana":"BooleanVar()","variabileintera":"IntVar()","VariabileNonDefinita":"NameError","vero":"True","verticelinea":"marker","volte":"clicks"}
            colori={"!rosso":"'red'","!giallo":"'yellow'","!verde":"'green'"}
            codiceprogrammazione={**istruzioni,**istruzionia,**istruzionib,**istruzionic,**istruzionid,**istruzionie,**istruzionif,**istruzionig,**istruzionih,**istruzionii,**istruzionil,**istruzionim,**istruzionin,**istruzionio,**istruzionip,**istruzionir,**istruzionis,**istruzionit,**istruzioniu,**istruzioniv,**colori}
            punteggiatura2=["(",")","[","]"]
            segni=[".",":",","," ","=","\n","\t",""]
            #se riconosce l'istruzione, la colora
            if istruzione in codiceprogrammazione and apertav==0 and apertadv==0 and ((linea[x] in segni) or (linea[x] in punteggiatura2)):
                rigacompleta=rigacompleta+codiceprogrammazione[istruzione]
                colora(istruzione,x,y,"tre")
                istruzione=""
            #se riconosce un segno di punteggiatura, lo scrive, ma azzera la variabile "istruzione" per ricostruire la prossima istruzione
            if carattere in segni and apertav==0 and apertadv==0:
                rigacompleta=rigacompleta+istruzione
                istruzione=""
            #se riconosce le doppie virgolette (") allora mette la variabile "apertadv" a 1, altrimenti a 0
            if carattere == '"' and apertav==0 and apertadv==0:
                rigacompleta=rigacompleta+istruzione
                apertadv=1
                istruzione=""
            elif carattere=='"' and apertadv==1 and apertav==0:
                rigacompleta=rigacompleta+istruzione
                apertadv=0
                istruzione=""
            #se riconosce la virgoletta (') allora mette la variabile "apertav" a 1, altrimenti a 0    
            if carattere == "'" and apertav==0 and apertadv==0:
                rigacompleta=rigacompleta+istruzione
                apertav=1
                istruzione=""
            elif carattere=="'" and apertadv==0 and apertav==1:
                rigacompleta=rigacompleta+istruzione
                apertav=0
                istruzione=""
        #se alla fine di elaborazione di una singola riga del programma, trova la variabile "apertadv" o "apertav" con valore 1
        #significa che c'è qualche virgoletta aperta e non chiusa, quindi segnala l'errore e termina l'esame

        rigacompleta=rigacompleta+istruzione
        programma=programma+rigacompleta+"\n"
        istruzione=""
        rigacompleta=""
        progressivo=0

def togli_intestazione():
    presentazione.pack_forget()
    finestra.config(pady=7,padx=7)

#Scrive la posizione del cursore nell'editor
def movimento(event):
    posizione_completa=testo.index("insert")
    posizione_listata=posizione_completa.split(".")
    posizione_y=posizione_listata[0]
    posizione_x=posizione_listata[1]
    menu.entryconfigure(3,label="- Riga: "+posizione_y+" - Posizione: "+posizione_x)

#taglia testo
def taglia_testo():
    global selezione
    if testo.selection_get():
        selezione=testo.selection_get()
        testo.delete("sel.first","sel.last")

#incolla testo
def incolla_testo():
    if selezione:
        posizione=testo.index(INSERT)
        testo.insert(posizione,selezione)

#copia testo
def copia_testo():
    global selezione
    if testo.selection_get():
        selezione=testo.selection_get()
   
#Editor di testo
finestra=Tk()
finestra.title("Editor per Lungo - by NiktorTheNat")
finestra.geometry("900x800")
finestra.config(bg="#ccccff",pady=70,padx=70)
menu=Menu(finestra)
finestra.config(menu=menu)
filemenu=Menu(menu)
filemenu1=Menu(menu)
#testo=scrolledtext.ScrolledText(finestra,width=80,height=35)
presentazione=Text(finestra,width=80,height=5,bg="#8080ff",fg="#ccccff",font=('Courier', 14))
presentazione.pack(fill=BOTH, expand = YES)
presentazione.insert(INSERT,vl)
presentazione.config(state=DISABLED)
#imposta tipo carattere, colori, dimensione carattere e colore cursore dell'editor
testo=Text(finestra,width=80,height=25,bg="#8080ff",fg="#ccccff",font=('Courier', 16),insertbackground="red")
testo.pack(fill=BOTH, expand = YES)
#cambia tipo di cursore
#testo.config(cursor="circle")
if os.path.isfile('provola.txt'):
    ff=open("provola.txt","r")
    ff1=ff.read()
    testo.insert("1.0",ff1)
    ff.close()
menu.add_cascade(label="File",menu=filemenu)
menu.add_cascade(label="Modifica",menu=filemenu1)
menu.add_cascade(label="posizione")
filemenu.add_command(label="Esegui   F5",command=editor_salva)
filemenu.add_command(label="Aiuto",command=aiuto)
filemenu.add_command(label="Nascondi intestazione    F6",command=togli_intestazione)
filemenu.add_command(label="Carattere piccolo    F2",command=carattere_piccolo)
filemenu.add_command(label="Carattere medio      F3",command=carattere_medio)
filemenu.add_command(label="Carattere grande     F4",command=carattere_grande)
filemenu1.add_command(label="Taglia",command=taglia_testo)
filemenu1.add_command(label="Copia",command=copia_testo)
filemenu1.add_command(label="Incolla",command=incolla_testo)

pulsante_reset=Button(finestra,text="CHIUDI",command=resetta)
aiuto_testo=Text(finestra,width=80,height=25,bg="#8080ff",fg="#ccccff",font=('Courier', 16))
aiuto=Listbox(finestra,width=80,height=5,bg="#8080ff",fg="#ccccff",font=('Courier', 16))
aiuto_cerca=Entry(finestra)
aiuto_cerca.bind("<Return>",istruzioni1)
#aiuto.pack(fill=BOTH, expand = YES)
aiuto.bind("<<ListboxSelect>>",istruzioni)
#pulsante.pack(fill=BOTH, expand = YES)
#pulsante1.pack(fill=BOTH, expand = YES)
#finestra.bind('<Space>', tasto_premuto)
finestra.bind("<Return>",correggi)
finestra.bind("<space>",correggi)
finestra.bind("(",correggi)
finestra.bind(")",correggi)
finestra.bind("=",correggi)
finestra.bind(".",correggi)
finestra.bind("'",correggi)
finestra.bind('"',correggi)
finestra.bind("<Down>",correggi)
finestra.bind("<Up>",correggi)
finestra.bind("<Left>",correggi)
finestra.bind("<Right>",correggi)
finestra.bind("<F5>",lambda x: editor_salva())
finestra.bind("<F2>",lambda x: carattere_piccolo())
finestra.bind("<F3>",lambda x: carattere_medio())
finestra.bind("<F4>",lambda x: carattere_grande())
finestra.bind("<F6>",lambda x: togli_intestazione())
finestra.bind("<KeyPress>",movimento)
finestra.bind("<KeyRelease>",movimento)
finestra.bind("<Key>",movimento)
finestra.bind("<Control-c>",lambda x: copia_testo())
finestra.bind("<Control-v>",lambda x: incolla_testo)
finestra.mainloop()
