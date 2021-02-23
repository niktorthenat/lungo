import tkinter as tk
import tkinter.ttk as ttk
import os
from platform import system
from glob import glob

if system() != "Windows":
    from tkinterhtml import HtmlFrame

DOC_PATH = os.path.join(os.getcwd(), "doc")

__author__ = "h3r0cybersec"
__version__ = "0.0.1"


class HelpApp:
    """
        App per documentazione Lungo.
    """
    def __init__(self, master=None):
        self.main_help_win = tk.Toplevel(master)
        self.main_paned_container = tk.PanedWindow(self.main_help_win)
        self.main_paned_container.pack(expand=1, fill=tk.BOTH)

        # Pannello di sinistra
        self.doc_tree_view = tk.PanedWindow(self.main_paned_container, orient=tk.VERTICAL)
        self.treeview_struct = ttk.Treeview(self.doc_tree_view, show="tree")
        self.base_doc_node = self.treeview_struct.insert('', 'end', iid="doc", text="Documentazione", open=True)
        self.treeview_struct.heading("#0", text="")
        self.treeview_struct.bind("<<TreeviewSelect>>", self.__get_opened_item)
        self.__populate_tree()
        self.treeview_struct.pack(expand='true', fill='both', side='top')
        self.doc_tree_view.pack(anchor='n', expand='false', fill='both', side='left')

        # Pannello di destra
        self.doc_text_view = tk.PanedWindow(self.main_paned_container, orient=tk.VERTICAL)
        if system() == "Windows":
            self.doc_page = tk.Text(self.doc_text_view, font=("Helvetica", 10), borderwidth=0)
        else:
            self.doc_page = HtmlFrame(self.doc_text_view, horizontal_scrollbar=False)
        self.doc_page.pack(expand='true', fill='both', side='right')

        # Aggiungo i pannelli 
        self.main_paned_container.add(self.doc_tree_view)
        self.main_paned_container.add(self.doc_text_view)
        self.doc_tree_view.add(self.treeview_struct)
        self.doc_text_view.add(self.doc_page)

        # Configurazione generale su finestra
        self.main_help_win.configure(relief='flat')
        self.main_help_win.geometry('640x480')
        self.main_help_win.maxsize(800, 600)
        self.main_help_win.resizable(True, True)
        self.main_help_win.title('Lungo Help')

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

    def __get_right_file_type(self, node, base_path, regex) -> list:
        """
            In base al tipo di sistema operativo sceglie quali pagine 
            della documentazione recuperare.
        """
        file_match = f"{os.path.join(base_path, regex)}"
        for file in glob(file_match):
            filename, ext = os.path.splitext(os.path.basename(file))
            self.treeview_struct.insert(node, "end", iid=f"{file}", text=filename)
    
    def __populate_tree(self):
        """
            Popola la vista sulla documentazione.
        """
        for index, path in enumerate(os.listdir(DOC_PATH)):
            fullpath = os.path.join(DOC_PATH, path)
            parent_node = self.treeview_struct.insert(self.base_doc_node, "end", iid=f"{fullpath}", text=f"/{path}")
            if system() == "Windows":
                self.__get_right_file_type(parent_node, fullpath, "*.txt")
            else:
                self.__get_right_file_type(parent_node, fullpath, "*.html")

    def __elaborate_data(self, path):
        """
            Mostra il contenuto html del file della documentazione selezionato.
        """
        with open(path, encoding="utf-8") as documentation:
            data = documentation.read()
            if system() == "Windows":
                self.doc_page.configure(state="normal")
                self.doc_page.delete(1.0, tk.END)
                self.doc_page.insert(tk.INSERT, data)
                self.doc_page.configure(state="disabled")
            else:
                self.doc_page.set_content(documentation.read())

    def run(self):
        self.main_help_win.mainloop()
