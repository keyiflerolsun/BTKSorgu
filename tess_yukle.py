# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import platform, sys, subprocess
from setuptools.command.install import install

class TesseractYukle(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sistem = platform.system()

    def tess_yuklu_mu(self):
        try:
            subprocess.check_output(["tesseract", "--version"])
            return True
        except Exception:
            return False

    def tess_yukle(self):
        if self.sistem != "Linux":
            raise OSError(f"\n\n» Bu paketi kullanabilmek için '{self.sistem}' cihazına 'tesseract-ocr' yüklemelisin!\n")

        print("\n\n» 'tesseract-ocr' yüklenmeye çalışılıyor...\n")

        try:
            import distro
        except ImportError:
            subprocess.run([sys.executable, "-m", "pip", "install", "distro"])
            try:
                import distro
            except ImportError:
                print("» 'distro' kütüphanesi yüklenemedi!\n")
                sys.exit(1)

        match distro.id():
            case "debian" | "ubuntu":
                subprocess.run(["sudo", "apt-get", "update"])
                subprocess.run(["sudo", "apt-get", "install", "-y", "libleptonica-dev"])
                subprocess.run(["sudo", "apt-get", "install", "-y", "tesseract-ocr"])
            case "fedora":
                subprocess.run(["sudo", "dnf", "install", "-y", "leptonica-devel"])
                subprocess.run(["sudo", "dnf", "install", "-y", "tesseract"])
            case "centos" | "rhel" | "rocky" | "redhat":
                subprocess.run(["sudo", "yum", "install", "-y", "leptonica-devel"])
                subprocess.run(["sudo", "yum", "install", "-y", "tesseract"])
            case "arch" | "manjaro":
                subprocess.run(["sudo", "pacman", "-Sy"])
                subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "leptonica"])
                subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "tesseract"])
            case bilinmeyen:
                print(f"\n\n» Bilinmeyen dağıtım : `{bilinmeyen}`\n\n")

        if not self.tess_yuklu_mu():
            raise RuntimeError("» 'tesseract-ocr' yüklenemedi!\n")

    def run(self):
        try:
            if not self.tess_yuklu_mu():
                self.tess_yukle()
        except Exception as hata:
            print(hata)
            sys.exit(1)

        install.run(self)