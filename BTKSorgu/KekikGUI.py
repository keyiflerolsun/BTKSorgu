# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import tkinter as tk
from tkinter  import ttk, messagebox
from base64   import encodebytes
from sv_ttk   import set_theme
from BTKSorgu import BTKSorgu

from BTKSorgu.ekstra import dosya_ver


class KekikGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        set_theme("dark")
        self.title("BTK Sorgu")

        logo_b64 = encodebytes(open(file=dosya_ver("logo.png", 1), mode="rb").read())
        favicon  = tk.PhotoImage(data=logo_b64)
        self.iconphoto(False, favicon)

        self.p_genislik  = max(self.winfo_width(), 400)
        self.p_yukseklik = max(self.winfo_height(), 250)
        self.minsize(width=self.p_genislik, height=self.p_yukseklik)

        self.bind("<Escape>",    lambda _: self.pencereyi_kapat())
        self.bind("<F11>",       lambda _: self.tam_ekran())
        self.bind("<Control-a>", lambda event: self.ctrl_a(event))
        self.bind("<Control-A>", lambda event: self.ctrl_a(event))
        self.protocol("WM_DELETE_WINDOW", self.pencereyi_kapat)

        # !
        SorguAlani(self)
        # !

        # * Sağ Alt Köşeye Pencere Yeniden Boyutlandırma
        __temp = ttk.Frame(self)
        __temp.pack(fill="both", expand=True)
        self.sizegrip = ttk.Sizegrip(__temp)
        self.sizegrip.place(relx=1, rely=1, anchor="se", x=-5, y=-5)

    def tam_ekran(self):
        self.attributes("-fullscreen", not self.attributes("-fullscreen"))

        if self.attributes("-fullscreen"):
            self.sizegrip.place(relx=1, rely=1, anchor="se", x=-5, y=-5)       
        else:
            self.sizegrip.place_forget()

    def ctrl_a(self, event):
        event.widget.select_range(0, "end")
        event.widget.icursor("end")

    def pencereyi_kapat(self):
        if messagebox.askokcancel("👋 Ciao..", "Programı Kapatayım Mı?"):
            self.destroy()


class SorguAlani(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill="both", expand=True)

        self.rowconfigure(index=(0, 1, 2), weight=1)
        self.columnconfigure(index=0,      weight=1)

        self.btk_ui()

    def btk_ui(self):
        self.arama_metni = ttk.Entry(self)
        self.arama_metni.insert(0, "Sorgulanacak Domain Giriniz..")
        self.arama_metni.bind("<Return>", lambda _: self.ara_buton_tiklaninca())
        self.arama_metni.grid(row=0, column=0, padx=30, pady=10, sticky="ew")
        self.arama_metni.focus()

        ara_buton = ttk.Button(self, text="Ara", command=lambda: self.ara_buton_tiklaninca())
        ara_buton.grid(row=1, column=0, padx=30, sticky="ew")

        ayrac = ttk.Separator(self, orient="horizontal")
        ayrac.grid(row=2, column=0, pady=(10, 0), padx=30, sticky="ew")

        self.cikti_alani = CiktiAlani(self.parent)

    def ara_buton_tiklaninca(self):
        sorgu = self.arama_metni.get()
        if not sorgu:
            return False

        self.arama_metni.state(["disabled"])
        self.cikti_alani.metin.configure(text="Lütfen Bekleyiniz...", foreground="#EF7F1A")
        self.update()

        btk_sorgu = str(BTKSorgu(sorgu))

        if "engellenmiştir" not in btk_sorgu:
            self.arama_metni.state(["!disabled", "!invalid"])
            self.cikti_alani.metin.configure(text=btk_sorgu, foreground="#17a2b8")            
        else:
            self.arama_metni.state(["!disabled", "invalid"])
            self.cikti_alani.metin.configure(text=btk_sorgu, foreground="#dc3545")

        self.update()
        self.arama_metni.focus()


class CiktiAlani(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill="both", expand=True)

        self.rowconfigure(index=0,    weight=1)
        self.columnconfigure(index=0, weight=1)

        self.metin = ttk.Label(self, wraplength=self.parent.p_genislik - 65)
        self.metin.configure(justify="center")
        self.metin.grid(row=0, column=0, pady=20, sticky="ns")