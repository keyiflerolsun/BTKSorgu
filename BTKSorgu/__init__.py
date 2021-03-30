r'''
# 🔍 BTKSorgu

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/bc0a52a9b57f4c29930cbd6c796f9a8b)](https://www.codacy.com/gh/keyiflerolsun/BTKSorgu/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=keyiflerolsun/BTKSorgu&amp;utm_campaign=Badge_Grade) ![Repo Boyutu](https://img.shields.io/github/repo-size/keyiflerolsun/BTKSorgu) ![Views](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/keyiflerolsun/BTKSorgu&title=Profile%20Views) [![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/keyiflerolsun/BTKSorgu)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/BTKSorgu)
![PyPI - Status](https://img.shields.io/pypi/status/BTKSorgu)
![PyPI](https://img.shields.io/pypi/v/BTKSorgu)
![PyPI - Downloads](https://img.shields.io/pypi/dm/BTKSorgu)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/BTKSorgu)
![PyPI - License](https://img.shields.io/pypi/l/BTKSorgu)

*Hedef websitesinin BTK Tarafından Erişim Engeli Sorgusu..*

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/keyiflerolsun/)

## 🚀 Kurulum

```bash
# Yüklemek
pip install BTKSorgu

# Güncellemek
pip install -U BTKSorgu
```

## 📝 Kullanım

```python
from BTKSorgu import BTKSorgu
from time     import time

basla = time()
print(BTKSorgu('redtube.com'))
    # » redtube.com, 30/01/2008 tarihli ve 410.01.02.2008-028105 sayılı Telekomünikasyon İletişim Başkanlığı kararıyla erişime engellenmiştir.
print(BTKSorgu('kekikakademi.org'))
    # » Bilgi Teknolojileri ve İletişim Kurumu tarafından uygulanan bir karar bulunamadı.
print(BTKSorgu('xnxx.com'))
    # » xnxx.com, 23/02/2008 tarihli ve 410.01.02.2008-054003 sayılı Telekomünikasyon İletişim Başkanlığı kararıyla erişime engellenmiştir.
bitir = time()

print(bitir-basla)
    # » 8.352766513824463
```

## 🔖 Program Akış Şeması

1. *Oturum Başlat,*
2. *[https://internet2.btk.gov.tr](https://internet2.btk.gov.tr/) adresine yönlendirmeleri kabul ederek git: kurabiyeleri ye,*
3. *Dönen kaynak kodundan doğrulama resmini indir,*
4. *Doğrulama resmini OCR ile harflere dönüştür, boşlukları sil,*
5. *Sorgu adresini okuduğun doğrulama koduyla birlikte post at,*
6. *Dönen yanıtı ayrıştırıp edip geri döndür..*

> Bu programın yazılma ve açık kaynak kodlu olarak paylaşılma amacı: *Tarayıcı Otomasyonlarının sebep olduğu  **gereksiz kaynak tüketimi** ve  **zaman kaybının**  önüne geçmeye teşvik etmektir…*

> Tarayıcı Otomasyonu : *[Selenium IDE](https://www.selenium.dev/selenium-ide/)* **-** *[Katalon Automation Recorder](https://www.katalon.com/resources-center/blog/katalon-automation-recorder/)* **-** *[BrowserAutomationStudio](https://bablosoft.com/shop/BrowserAutomationStudio)*

> Karşılaştırması : **[Selenium VS Requests](https://www.r10.net/off-topic/2751412-selenium-vs-requests.html)**

## 📝 Proje İlerlemesi

- ✅ **[@raifpy](https://github.com/raifpy)** *tarafından kodlanmış projenin hantal bir bileşeni itinayla `dızz 🐍`'lanmıştır..*
- ✅ **Selenium** *bağımlılığından dolayı hantal çalışan kod yapısı tamamen ayıklanıp bütün iş* `requests`*'e yaptırılıp ciddi miktarda kaynak ve zaman tasarrufu ettirilmiştir..*
- ✅ *Kolay erişilebilir olması ve ilham yaratması için* **pypi** *depolarına yüklenmiştir..*

## 🌐 Telif Hakkı ve Lisans

* *Copyright (C) 2021 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/keyifUserBot/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/keyiflerolsun)

## 💸 Bağış Yap

**[☕️ Kahve Ismarla](https://KekikAkademi.org/Kahve)**

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*
'''

YAZAR       = 'keyiflerolsun'
YAZAR_POSTA = 'keyiflerolsun@gmail.com'

PAKET       = 'BTKSorgu'
VERSIYON    = '0.1.4'

REPO        = 'https://github.com/keyiflerolsun/BTKSorgu'
ACIKLAMA    = 'Hedef websitesinin BTK Tarafından Erişim Engeli Sorgusu'
ANAHTAR_KLM = [PAKET, 'KekikAkademi', 'keyiflerolsun']

####
from BTKSorgu.Erisim_Engeli import BTKSorgu
####