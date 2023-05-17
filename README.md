# 🔍 BTKSorgu

![Repo Boyutu](https://img.shields.io/github/repo-size/keyiflerolsun/BTKSorgu?logo=git&logoColor=white)
![Görüntülenme](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/keyiflerolsun/BTKSorgu&title=Görüntülenme)
<a href="https://KekikAkademi.org/Kahve" target="_blank"><img src="https://img.shields.io/badge/☕️-Kahve Ismarla-ffdd00" title="☕️ Kahve Ismarla" style="padding-left:5px;"></a>

![Python Version](https://img.shields.io/pypi/pyversions/BTKSorgu?logo=python&logoColor=white)
![License](https://img.shields.io/pypi/l/BTKSorgu?logo=gnu&logoColor=white)
![Status](https://img.shields.io/pypi/status/BTKSorgu?logo=windowsterminal&logoColor=white)

![PyPI](https://img.shields.io/pypi/v/BTKSorgu?logo=pypi&logoColor=white)
![PyPI - Downloads](https://img.shields.io/pypi/dm/BTKSorgu?logo=pypi&logoColor=white)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/BTKSorgu?logo=pypi&logoColor=white)

[![PyPI Yükle](https://github.com/keyiflerolsun/BTKSorgu/actions/workflows/KekikFlow.yml/badge.svg)](https://github.com/keyiflerolsun/BTKSorgu/actions/workflows/KekikFlow.yml)

*Hedef websitesinin BTK Tarafından Erişim Engeli Sorgusu..*

![BTKSorgu](https://raw.githubusercontent.com/keyiflerolsun/BTKSorgu/Shared/SS.png)

[![ForTheBadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](https://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/keyiflerolsun/)

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
print(BTKSorgu("redtube.com"))
    # » redtube.com, 30/01/2008 tarihli ve 410.01.02.2008-028105 sayılı Telekomünikasyon İletişim Başkanlığı kararıyla erişime engellenmiştir.
print(BTKSorgu("kekikakademi.org"))
    # » Bilgi Teknolojileri ve İletişim Kurumu tarafından uygulanan bir karar bulunamadı.
print(BTKSorgu("xnxx.com"))
    # » xnxx.com, 23/02/2008 tarihli ve 410.01.02.2008-054003 sayılı Telekomünikasyon İletişim Başkanlığı kararıyla erişime engellenmiştir.
bitir = time()

print(bitir-basla)
    # » 8.352766513824463
```

```bash
BTKSorgu keyiflerolsun.dev

# > Bilgi Teknolojileri ve İletişim Kurumu tarafından uygulanan bir karar bulunamadı.
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

* *Copyright (C) 2023 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/BTKSorgu/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/KekikKahve)

## 💸 Bağış Yap

**[☕️ Kahve Ismarla](https://KekikAkademi.org/Kahve)**

##

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*
