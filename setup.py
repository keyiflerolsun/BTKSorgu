# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from setuptools import setup
from io         import open

setup(
    # ? Genel Bilgiler
    name         = "BTKSorgu",
    version      = "1.0.1",
    url          = "https://github.com/keyiflerolsun/E-Fatura_Sorgu",
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
        "Kekik",
        "requests",
        "parsel",
        "regex",
        "Pillow",
        "pytesseract"
    ],

    # ? Konsoldan Çalıştırılabilir
    entry_points = {
        "console_scripts": [
            "BTKSorgu = BTKSorgu.konsol:basla",
        ]
    },

    # ? PyPI Bilgileri
    long_description_content_type = "text/markdown",
    long_description              = "".join(open("README.md", encoding="utf-8").readlines()),
    include_package_data          = True
)