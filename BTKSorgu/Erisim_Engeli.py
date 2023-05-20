# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from rich         import pretty, traceback
from rich.console import Console
pretty.install()
traceback.install(show_locals=False)
konsol = Console(log_path=False)

from requests import Session
from parsel   import Selector

from shutil      import copyfileobj
from pytesseract import image_to_string 
from PIL         import Image
from re          import search

from os import remove

class BTKSorgu(object):
    """
    BTKSorgu : Hedef websitesinin BTK Tarafından Erişim Engeli Sorgusu

    Dönüş
    ----------
        (str):
            {domain}, {karar} Karar Bulunamadı.
    """
    def __init__(self, sorgu_url:str):
        """Karar Döndürür"""
        self.ana_sayfa      = "https://internet2.btk.gov.tr"
        self.sorgu_sayfasi  = "https://internet2.btk.gov.tr/sitesorgu/"
        self.sorgu_url      = search(r"(?:https?://)?(?:www\.)?([^/]+)", sorgu_url).group(1)
        self._gecici_gorsel = "captcha.png"

        self.oturum = Session()

    def __captcha_ver(self):
        """Captcha görselini indirip OCR ile okur"""
        ilk_bakis    = self.oturum.get(self.sorgu_sayfasi, allow_redirects=True)
        captcha_yolu = Selector(ilk_bakis.text).xpath("//div[@class='arama_captcha']/img/@src").get()

        captcha_data = self.oturum.get(f"{self.ana_sayfa}{captcha_yolu}", stream=True)
        with open(self._gecici_gorsel, "wb") as captcha_gorsel:
            copyfileobj(captcha_data.raw, captcha_gorsel)

        try:
            captcha_harfleri = image_to_string(Image.open(self._gecici_gorsel)).strip().replace(" ", "")
        except Exception as hata:
            konsol.print(f"[bold red]Hata: {hata}\n\n")
            return None

        return captcha_harfleri

    def karar_ver(self):
        """Captcha ile birlikte sorgu sitesini POST eder"""
        captcha = self.__captcha_ver()
        if not captcha:
            return "Muhtemelen Sisteminizde 'tesseract-ocr' Yüklü Değil!"

        karar_sayfasi = self.oturum.post(
            url     = self.sorgu_sayfasi,
            headers = {
                "Content-Type" : "application/x-www-form-urlencoded",
                "Host"         : "internet2.btk.gov.tr",
                "Origin"       : self.ana_sayfa,
                "Referer"      : self.sorgu_sayfasi,
            },
            data    = {
                "deger"         : self.sorgu_url,
                "ipw"           : "",
                "kat"           : "",
                "tr"            : "",
                "eg"            : "",
                "ayrintili"     : 0,
                "submit"        : "Sorgula",
                "security_code" : captcha
            }
        )

        # print(karar_sayfasi.text)
        secici     = Selector(karar_sayfasi.text)
        hatali_kod = secici.xpath("//div[@class='icerik']/ul/li/text()").get()
        erisim_var = secici.xpath("//div[@class='yazi2']/text()").get()
        erisim_yok = secici.xpath("//span[@class='yazi2_2']/text()").get()

        return hatali_kod or erisim_var or erisim_yok or ""

    def __repr__(self) -> str:
        """Kararı Döndürür"""
        hatalar = ["Lütfen güvenlik kodunu giriniz.", "Güvenlik kodunu yanlış girdiniz. Lütfen Güvenlik Kodunu resimde gördüğünüz şekilde giriniz."]
        while True:
            karar = self.karar_ver()
            if karar not in hatalar:
                remove(self._gecici_gorsel)
                return karar