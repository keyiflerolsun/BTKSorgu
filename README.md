# 🔍 BTKSorgu

[![Repo Boyutu](https://img.shields.io/github/repo-size/keyiflerolsun/BTKSorgu?logo=git&logoColor=white)](#)
[![Görüntülenme](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/keyiflerolsun/BTKSorgu&title=Görüntülenme)](#)
<a href="https://KekikAkademi.org/Kahve" target="_blank"><img src="https://img.shields.io/badge/☕️-Kahve Ismarla-ffdd00" title="☕️ Kahve Ismarla" style="padding-left:5px;"></a>

[![Python Version](https://img.shields.io/pypi/pyversions/BTKSorgu?logo=python&logoColor=white)](#)
[![License](https://img.shields.io/pypi/l/BTKSorgu?logo=gnu&logoColor=white)](#)
[![Status](https://img.shields.io/pypi/status/BTKSorgu?logo=windowsterminal&logoColor=white)](#)

[![PyPI](https://img.shields.io/pypi/v/BTKSorgu?logo=pypi&logoColor=white)](https://pypi.org/project/BTKSorgu)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/BTKSorgu?logo=pypi&logoColor=white)](https://pypi.org/project/BTKSorgu)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/BTKSorgu?logo=pypi&logoColor=white)](https://pypi.org/project/BTKSorgu)

[![PyPI Yükleyici](https://github.com/keyiflerolsun/BTKSorgu/actions/workflows/pypiYukle.yml/badge.svg)](https://github.com/keyiflerolsun/BTKSorgu/actions/workflows/pypiYukle.yml)
[![Flatpak Yükleyici](https://github.com/keyiflerolsun/BTKSorgu/actions/workflows/flatpakYukle.yml/badge.svg)](https://github.com/keyiflerolsun/BTKSorgu/actions/workflows/flatpakYukle.yml)

[![FlatHub](https://img.shields.io/flathub/v/org.KekikAkademi.BTKSorgu?logo=flathub&logoColor=white)](https://flathub.org/tr/apps/org.KekikAkademi.BTKSorgu)
[![FlatHub - Downloads](https://img.shields.io/flathub/downloads/org.KekikAkademi.BTKSorgu?logo=flathub&logoColor=white)](https://flathub.org/tr/apps/org.KekikAkademi.BTKSorgu)

*Hedef websitesinin BTK Tarafından Erişim Engeli Sorgusu..*

[![BTKSorgu](https://raw.githubusercontent.com/keyiflerolsun/BTKSorgu/main/.github/icons/SS.png)](#)

[![ForTheBadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](https://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/keyiflerolsun/)

## 🚀 Kurulum

### <a href="#"><img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/BTKSorgu/main/.github/icons/pypi.svg"></a> PyPi (Lib - CLI - UI)

```bash
# Yüklemek
pip install BTKSorgu

# Güncellemek
pip install -U BTKSorgu
```

### <a href="#"><img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/BTKSorgu/main/.github/icons/flathub.svg"></a> FlatHub (UI)

```bash
# Yüklemek
flatpak install flathub org.KekikAkademi.BTKSorgu

# Çalıştırmak
flatpak run org.KekikAkademi.BTKSorgu
```

## 📝 Kullanım

### <a href="#"><img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/BTKSorgu/main/.github/icons/python.svg"></a> Lib

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

### <a href="#"><img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/BTKSorgu/main/.github/icons/iterm2.svg"></a> CLI

```bash
BTKSorgu keyiflerolsun.dev

# > Bilgi Teknolojileri ve İletişim Kurumu tarafından uygulanan bir karar bulunamadı.
```

### <a href="#"><img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/BTKSorgu/main/.github/icons/freedesktop.svg"></a> UI

```bash
BTKSorguGUI

# veya

flatpak run org.KekikAkademi.BTKSorgu
```

---

<details>
    <summary style="font-weight: bold; font-size: 20px">
      <a href="#"><img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/BTKSorgu/main/.github/icons/buddy.svg"></a> <b>Kendiniz Paketlemek İsterseniz</b>
      <i>(genişletmek için tıklayın!)</i>
    </summary>
    <br/>

### <a href="#"><img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/BTKSorgu/main/.github/icons/python.svg"></a> Python

```bash
# Depoyu Çek
https://github.com/keyiflerolsun/BTKSorgu.git
cd BTKSorgu

# Gerekli Ortamları Kur
pip install -U pip setuptools wheel twine

# Paketi Yükle
pip install .

# Artıkları Temizle
rm -rf build *.egg-info

# Çalıştır
BTKSorgu     # CLI
BTKSorguGUI  # GUI

# Paketi Kaldır
pip uninstall BTKSorgu
```

### <a href="#"><img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/BTKSorgu/main/.github/icons/flatpak.svg"></a> FlatPak

```bash
# Depoyu Çek
git clone https://github.com/keyiflerolsun/BTKSorgu.git
cd BTKSorgu

# Gerekli Dosyaları Al
mv Shared/*.yml . && mv Shared/SRC .

# Gerekli Ortamları Kur
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak remote-add --if-not-exists flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
flatpak update && flatpak upgrade
flatpak install flathub org.freedesktop.{Platform,Sdk}//22.08

# Paketle
flatpak-builder --user --install --force-clean build-dir org.KekikAkademi.BTKSorgu.yml

# Artıkları Temizle
rm -rf .flatpak* .vscode build-dir && find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

# Çalıştır
flatpak run org.KekikAkademi.BTKSorgu

# Paketi Kaldır
flatpak uninstall org.KekikAkademi.BTKSorgu
```

</details>

---

## 🔖 Program Akış Şeması

1. *Oturum Başlat,*
2. *[https://internet2.btk.gov.tr](https://internet2.btk.gov.tr/) adresine yönlendirmeleri kabul ederek git: kurabiyeleri ye,*
3. *Dönen kaynak kodundan doğrulama resmini indir,*
4. *Doğrulama resmini OCR ile harflere dönüştür, boşlukları sil,*
5. *Sorgu adresini okuduğun doğrulama koduyla birlikte post at,*
6. *Dönen yanıtı ayrıştırıp edip geri döndür..*

> Bu programın yazılma ve açık kaynak kodlu olarak paylaşılma amacı: *Tarayıcı Otomasyonlarının sebep olduğu  **gereksiz kaynak tüketimi** ve  **zaman kaybının**  önüne geçmeye teşvik etmektir…*

> Tarayıcı Otomasyonu : *[Selenium IDE](https://www.selenium.dev/selenium-ide/)* **-** *[Katalon Automation Recorder](https://www.katalon.com/resources-center/blog/katalon-automation-recorder/)* **-** *[BrowserAutomationStudio](https://bablosoft.com/shop/BrowserAutomationStudio)*

> Karşılaştırması : **[Selenium VS Requests](https://www.r10.net/off-topic/2751612-selenium-vs-requests.html)**

## 📝 Proje İlerlemesi

- ✅ **[@raifpy](https://github.com/raifpy)** *tarafından kodlanmış projenin hantal bir bileşeni itinayla `dızz 🐍`'lanmıştır..*
- ✅ **Selenium** *bağımlılığından dolayı hantal çalışan kod yapısı tamamen ayıklanıp bütün iş* `requests`*'e yaptırılıp ciddi miktarda kaynak ve zaman tasarrufu ettirilmiştir..*
- ✅ *Kolay erişilebilir olması ve ilham yaratması için* **pypi** *depolarına yüklenmiştir..*
- ✅ **Tkinter** *ile basit bir arayüz tasarlanmıştır ve eğitim amacıyla Depolara yüklenmiştir..*

## 🌐 Telif Hakkı ve Lisans

* *Copyright (C) 2023 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/BTKSorgu/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/KekikKahve)

## 💸 Bağış Yap

**[☕️ Kahve Ismarla](https://KekikAkademi.org/Kahve)**

***

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*