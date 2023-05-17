# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from contextlib import suppress
from BTKSorgu   import KekikGUI
from tkinter    import ttk
from BTKSorgu   import BTKSorgu

kekik = KekikGUI(
    pencere_adi = "BTK Sorgu",
    logo_yolu   = "logo.png",
    satir_sutun = 1,
    ortala      = False,
    cikis_onay  = False,
    p_genislik  = 400,
    p_yukseklik = 250
)

def input_alanlari():
    # İnput Alanları için bir Çerçeve oluşturun
    kekik.pencere.inputlar_frame = ttk.Frame(kekik.pencere, padding=(0, 0, 0, 10))
    kekik.pencere.inputlar_frame.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
    kekik.pencere.inputlar_frame.columnconfigure(index=0, weight=1)

    # Giriş Alanı
    kekik.pencere.arama_metni = ttk.Entry(kekik.pencere.inputlar_frame)
    kekik.pencere.arama_metni.insert(0, "Sorgulanacak Domain Giriniz..")
    kekik.pencere.arama_metni.bind("<Return>", lambda _: ara_buton_tiklaninca())
    kekik.pencere.arama_metni.state(["invalid"])
    kekik.pencere.arama_metni.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")
    kekik.pencere.arama_metni.focus()

    # Ekle Buton
    kekik.pencere.ara_buton = ttk.Button(kekik.pencere.inputlar_frame, text="Ara", command=lambda: ara_buton_tiklaninca())
    kekik.pencere.ara_buton.grid(row=1, column=0, padx=(10, 10), pady=10, sticky="ew")

    # Ayırıcı
    kekik.pencere.ayrac = ttk.Separator(kekik.pencere.inputlar_frame)
    kekik.pencere.ayrac.grid(row=2, column=0, padx=(10, 10), pady=10, sticky="ew")

def ara_buton_tiklaninca():
    arama_sorgusu = kekik.pencere.arama_metni.get()
    kekik.pencere.arama_metni.state(["!invalid"])

    kekik.pencere.cikti_frame = ttk.Frame(kekik.pencere, padding=(0, 0, 0, 10))
    kekik.pencere.cikti_frame.grid(row=1, column=0, sticky="n")
    kekik.pencere.cikti_frame.columnconfigure(index=0, weight=1)
    kekik.pencere.cikti_frame.rowconfigure(index=0, weight=1)

    with suppress(Exception):
        kekik.pencere._bekleyiniz.destroy()

    kekik.pencere._bekleyiniz = ttk.Label(kekik.pencere.inputlar_frame, text="Lütfen Bekleyiniz...", wraplength=kekik.p_genislik - 40)
    kekik.pencere._bekleyiniz.configure(foreground="#17a2b8", justify="center")
    kekik.pencere._bekleyiniz.grid(row=3, column=0, pady=(10, 0), sticky="n")

    kekik.pencere.update()

    kekik.pencere._bekleyiniz.configure(text=f"Lütfen Bekleyiniz!\n\n{arama_sorgusu} Aranıyor..")
    kekik.pencere.update()

    btk = str(BTKSorgu(arama_sorgusu))
    kekik.pencere._bekleyiniz.configure(text=btk)

    kekik.pencere.update()

    kekik.pencere.arama_metni.focus()

def basla():
    input_alanlari()
    kekik.mainloop()