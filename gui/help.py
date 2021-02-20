import tkinter as tk
import tkinter.ttk as ttk
from tkinterhtml import HtmlFrame
import os

DOC_PATH = os.path.join(os.getcwd(), "doc")

__author__ = "h3r0cybersec"
__version__ = "0.0.1"


class HelpApp:
    """
        App per documentazione Lungo.
    """
    def __init__(self, master=None):
        self.main_help_win = tk.Tk() if master is None else tk.Toplevel(master)

        # Contenitore di sinistra con vista ad albero su struttura directory documentazione
        self.doc_tree_view = ttk.Frame(self.main_help_win, borderwidth=0, relief="solid")
        self.treeview_struct = ttk.Treeview(self.doc_tree_view, show="tree")
        self.fileview_scroll = tk.Scrollbar(self.doc_tree_view, orient=tk.VERTICAL, command=self.treeview_struct.yview)
        self.base_doc_node = self.treeview_struct.insert('', 'end', iid="doc", text="Documentazione", open=True)
        self.treeview_struct.heading("#0", text="")
        self.treeview_struct.configure(yscroll=self.fileview_scroll.set)
        self.treeview_struct.bind("<<TreeviewSelect>>", self.__get_opened_item)
        self.__populate_tree()
        self.treeview_struct.pack(expand='true', fill='both', side='top')
        self.doc_tree_view.pack(anchor='n', expand='false', fill='both', side='left')

        # Contenitore di destra con contenuto pagina documentazione
        self.doc_text_view = ttk.Frame(self.main_help_win, borderwidth=0)
        self.doc_text_view.pack(expand='true', fill='both', side='right', padx=5)
        self.doc_page = HtmlFrame(self.doc_text_view, horizontal_scrollbar=False)
        self.doc_page.pack(expand='true', fill='both', side='right')

        # Configurazione generale su finestra
        self.main_help_win.configure(relief='flat')
        self.main_help_win.geometry('640x480')
        self.main_help_win.maxsize(800, 600)
        self.main_help_win.resizable(True, True)
        self.main_help_win.title('Lungo Help')

        # Main widget
        self.mainwindow = self.main_help_win

    def __get_opened_item(self, event):
        """
            Prende l'elemento selezionato e avvia la procedura di rendering del codice html
            nella pagina di manuale.
        """
        iid = self.treeview_struct.focus()
        parent, child = self.treeview_struct.parent(iid), iid
        path = os.path.join(parent, child)
        if os.path.isfile(path):
            self.__elaborate_data(path)
    
    def __populate_tree(self):
        """
            Popola la vista sulla documentazione.
            NOTE: Questo metodo è pensato per operato su un solo livello di directory, qualora 
                  si avesse la necessità di richiamarlo su pià livelli non basta fare altro
                  che aggiungere una chimata ricorsiva dello stesso.
        """
        for index, path in enumerate(os.listdir(DOC_PATH)):
            fullpath = os.path.join(DOC_PATH, path)
            parent_node = self.treeview_struct.insert(self.base_doc_node, "end", iid=f"{fullpath}", text=f"/{path}")
            for file in os.listdir(fullpath):
                self.treeview_struct.insert(parent_node, "end", iid=f"{file}", text=file.split(".")[0])

    def __elaborate_data(self, path):
        """
            Mostra il contenuto html del file della documentazione selezionato.
        """
        with open(path) as html_file:
            self.doc_page.set_content(html_file.read())

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    #NOTE: Appena aperta l'applicazione se si fà click sul pannello di destra nel terminale
    #      viene fuori un errore non bloccante. Penso ci sia un bug nella libreria tkinterhtml
    #      il quale non gestisce propriamente il codice. Se in qualche modo dovesse creare 
    #      problemi sarebbe meglio risolverlo.
    app = HelpApp()
    app.run()