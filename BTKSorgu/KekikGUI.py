# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from base64  import encodebytes
from sv_ttk  import set_theme

class KekikGUI(tk.Tk):
    def __init__(self, pencere_adi:str="keyiflerolsun GUI", logo_yolu:str="logo.png", satir_sutun:int=1, ortala:bool=True, cikis_onay:bool=True, p_genislik=400, p_yukseklik=300):
        super().__init__()
        set_theme("dark")
        self.title(pencere_adi)
        self.cikis_onay = cikis_onay

        # ? Pencere Kapanmadan Önce Fonksiyon Tetiklemek
        self.protocol("WM_DELETE_WINDOW", self.pencereyi_kapat)

        # ? Pencere Özellikleri
        self.bind("<Escape>",    lambda event: self.pencereyi_kapat()) # * ESC ile çıkış
        self.bind("<F11>",       lambda event: self.tam_ekran())       # * Tam Ekran
        self.bind("<Control-a>", lambda event: self.ctrl_a(event))
        self.bind("<Control-A>", lambda event: self.ctrl_a(event))

        # ? Pencere İkonu
        logo_b64 = encodebytes(open(logo_yolu, "rb").read())
        favicon  = tk.PhotoImage(data=logo_b64)
        self.iconphoto(False, favicon)

        # ? Pencere için bir minimum boyut ayarlayın ve ortasına yerleştirin
        self.update()
        self.p_genislik  = max(self.winfo_width(), p_genislik)
        self.p_yukseklik = max(self.winfo_height(), p_yukseklik)
        self.minsize(self.p_genislik, self.p_yukseklik)
        if ortala:
            x_kordinat = int((self.winfo_screenwidth()  / 2) - (self.p_genislik  / 2))
            y_kordinat = int((self.winfo_screenheight() / 2) - (self.p_yukseklik / 2))
            self.geometry(f"+{x_kordinat}+{y_kordinat - 20}")

        self.pencere = ttk.Frame(self)
        self.pencere.pack(fill="both", expand=True)

        # ? Uygulamayı Responsive Hale Getirin
        for index in range(satir_sutun):  # * 1 Satır 1 Sütun
            self.pencere.columnconfigure(index=index, weight=1)
            self.pencere.rowconfigure(index=index, weight=1)

        # ? Sağ Alt Köşeye Yeniden Boyutlandırma
        self.sizegrip = ttk.Sizegrip(self.pencere)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))
        self.update()

    def tam_ekran(self):
        self.attributes("-fullscreen", not self.attributes("-fullscreen"))

        if self.attributes("-fullscreen"):
            self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))        
        else:
            self.sizegrip.grid_forget()

    def ctrl_a(self, event):
        event.widget.select_range(0, "end")
        event.widget.icursor("end")

    def pencereyi_kapat(self):
        if (
            self.cikis_onay and messagebox.askokcancel("Program Kapanıyor", "Bunu Yapmak İstediğine Emin Misin?")
            or not self.cikis_onay
        ):
            self.destroy()