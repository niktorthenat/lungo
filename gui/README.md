GUI
===
Questa cartella contiene tutti i componenti di interfaccia che fanno parte progetto Lungo. 

Oltre alle classi che implementano il codice applicativo all'interno della cartella **interface** vengono presentati tutti i file **.ui** che implementano il codice *xml* dei vari componenti, realizzati con lo strumento **pygubu-designer**.

Attualmente il codice delle classi non fà uso dei file ui generati da questo strumento ma si potrebbe pensare in futuro di caricare il codice che definisce la GUI direttamente da quei file e collegare nelle classi solo la logica che risponde agli eventi degli utenti.

NOTE GENERALI
=============
Pultroppo la libreria Tkinter è poco funzionale di conseguenza sarebbe meglio iniziare a pensare a qualche libreria pià recente tipo Gtk+3, PyQt5, PySide6.