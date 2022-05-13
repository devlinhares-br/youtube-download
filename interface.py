from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import downloader

class Aplication:
    
    def __init__(self, master=None):

        #Defifição de fonte
        self.fonte = ("Arial", "10")
        self.fonte_btn = ("Calibri", "10")

        #Definição dos conteiners
        self.ct_title = Frame(master)
        self.ct_title["pady"] = 10
        self.ct_title.pack()

        self.ct_url = Frame(master)
        self.ct_url["pady"] = 10
        self.ct_url.pack()

        self.ct_baixar = Frame(master)
        self.ct_baixar["pady"] = 10
        self.ct_baixar.pack()

        self.ct_salvar = Frame(master)
        self.ct_salvar["pady"] = 10
        self.ct_salvar.pack()

        self.ct_down = Frame(master)
        self.ct_down["pady"] = 10
        self.ct_down.pack()

        self.ct_statusbar = Frame(master)
        self.ct_statusbar.pack()       

        #Label do Titulo
        self.lb_titulo = Label(self.ct_title, text="YouTube Download")
        self.lb_titulo["font"] = ("Arial", "10", "bold")
        self.lb_titulo.pack()

        #Label URL
        self.lb_url = Label(self.ct_url, text="URL: ", font=self.fonte)
        self.lb_url.pack(side=LEFT)

        #Imput URL
        self.cp_url = Entry(self.ct_url)
        self.cp_url["width"] = 45
        self.cp_url["font"] = self.fonte
        self.cp_url.pack(side=LEFT)

        #Label Baixar
        self.lb_baixar = Label(self.ct_baixar, text="Baixar: ", font=self.fonte)
        self.lb_baixar.grid(column=0)
        self.lb_baixar.pack(side=LEFT)

        #Radio Button
        baixar = BooleanVar()
        self.rd_baixarMp4 = Radiobutton(self.ct_baixar, text="Video", variable=baixar, value=True)
        self.rd_baixarMp4.select()
        self.rd_baixarMp4.pack(side=LEFT)

        self.rd_baixarMp4 = Radiobutton(self.ct_baixar, text="Audio", variable=baixar, value=False)
        self.rd_baixarMp4.pack(side=LEFT)

        #Label Salvar
        self.lb_salvar = Label(self.ct_salvar, text='Salvar: ', font=self.fonte)
        self.lb_salvar.pack(side="left")

        #Imput local salvar
        self.cp_salvar = Entry(self.ct_salvar)
        self.cp_salvar["width"] = 30
        self.cp_salvar["font"] = self.fonte
        self.cp_salvar.pack(side="left")

        #Botão Local Salva
        self.btn_salvar = Button(self.ct_salvar, command= lambda: self.explorador(self.cp_salvar))
        self.btn_salvar['text'] = "Procurar"
        self.btn_salvar['width'] = 12
        self.btn_salvar['font'] = self.fonte_btn
        self.btn_salvar.pack(side='left', padx=5)

        #Botão Download
        self.btn_down = Button(self.ct_down)
        self.btn_down['text'] = "Download"
        self.btn_down['width'] = 12
        self.btn_down['font'] = self.fonte_btn
        self.btn_down['command'] = lambda: self.download(self.cp_url.get(), self.cp_salvar.get(), baixar.get())
        self.btn_down.pack(side='left', padx=5)
        
        # Barra de status
        self.statusbar = Label(master, text='Versão 1.0.1', bd=1, relief=SUNKEN, anchor=W)
        self.statusbar.pack(side=BOTTOM, fill=X)


    def download(self, url, filename, formato):
        v = downloader.Video(url)
        v.download(filename, formato)
        self.MsgBox = messagebox.showwarning("Download concluído", "Download concluído com sucesso!")
    
    def explorador(self, campo):
        campo.delete(0, 'end')
        campo.insert(0, filedialog.askdirectory())
        campo.insert("end", "/")


def init():
    root = Tk()
    Aplication(root)
    root.geometry("400x250")
    root.minsize(400, 250)
    root.maxsize(400, 250)
    root.title("YoutuDownloader")
    root.iconbitmap('ico.ico')
    root.mainloop()
    

# <a href="https://www.flaticon.com/br/icones-gratis/baixar" title="baixar ícones">Baixar ícones criados por msidiqf - Flaticon</a>