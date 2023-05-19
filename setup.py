# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from setuptools import setup
from io         import open

setup(
    # ? Genel Bilgiler
    name         = "BTKSorgu",
    version      = "1.1.9",
    url          = "https://github.com/keyiflerolsun/BTKSorgu",
    description  = "Hedef websitesinin BTK Tarafından Erişim Engeli Sorgusu",
    keywords     = ["BTKSorgu", "KekikAkademi", "keyiflerolsun"],

    author       = "keyiflerolsun",
    author_email = "keyiflerolsun@gmail.com",

    license      = "GPLv3+",
    classifiers  = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3"
    ],

    # ? Paket Bilgileri
    packages         = ["BTKSorgu"],
    python_requires  = ">=3.10",
    install_requires = [
        "setuptools",
        "wheel",
        "install_freedesktop",
        "rich",
        "requests",
        "parsel",
        "cssselect",
        "regex",
        "Pillow",
        "pytesseract",
        "sv_ttk"
    ],

    # ? Konsoldan Çalıştırılabilir
    entry_points = {
        "console_scripts": [
            "BTKSorgu    = BTKSorgu.konsol:basla",
            "BTKSorguGUI = BTKSorgu.arayuz:basla"
        ]
    },

    # ? Masaüstü Paketi
    setup_requires = ["install_freedesktop"],
    data_files     = [
        ("share/applications",                ["Shared/org.KekikAkademi.BTKSorgu.desktop"]),
        ("share/appdata",                     ["Shared/org.KekikAkademi.BTKSorgu.appdata.xml"]),
        ("share/icons/hicolor/scalable/apps", ["Shared/org.KekikAkademi.BTKSorgu.svg"])
    ],

    # ? PyPI Bilgileri
    long_description_content_type = "text/markdown",
    long_description              = "".join(open("README.md", encoding="utf-8").readlines()),
    include_package_data          = True
)