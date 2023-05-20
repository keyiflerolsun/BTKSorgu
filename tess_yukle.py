# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import platform, sys, subprocess
from setuptools.command.install import install

class TesseractYukle(install):
    def gereksinim_kontrol(self):
        try:
            match platform.system():
                case "Linux":
                    self.program_kontrol("tesseract")
                case "Windows":
                    self.program_kontrol("tesseract")
                case "Darwin":
                    self.program_kontrol("tesseract")
                case _:
                    raise OSError(f"\n\n» Bilinmeyen işletim sistemi : `{platform.system()}`\n\n")
        except Exception as hata:
            print(hata)
            exit()

    def run(self):
        match platform.system():
            case "Linux":
                try:
                    import distro
                except ImportError:
                    subprocess.call([sys.executable, "-m", "pip", "install", "distro"])
                    try:
                        import distro
                    except ImportError:
                        print("\n\n» 'distro' kütüphanesi yüklenemedi!\n\n")
                        exit()

                match distro.id():
                    case "debian" | "ubuntu":
                        subprocess.call(["sudo", "apt-get", "update"])
                        subprocess.call(["sudo", "apt-get", "install", "-y", "libleptonica-dev"])
                        subprocess.call(["sudo", "apt-get", "install", "-y", "tesseract-ocr"])
                    case "fedora":
                        subprocess.call(["sudo", "dnf", "install", "-y", "leptonica-devel"])
                        subprocess.call(["sudo", "dnf", "install", "-y", "tesseract"])
                    case "centos" | "rhel" | "rocky" | "redhat":
                        subprocess.call(["sudo", "yum", "install", "-y", "leptonica-devel"])
                        subprocess.call(["sudo", "yum", "install", "-y", "tesseract"])
                    case "arch" | "manjaro":
                        subprocess.call(["sudo", "pacman", "-Sy"])
                        subprocess.call(["sudo", "pacman", "-S", "--noconfirm", "leptonica"])
                        subprocess.call(["sudo", "pacman", "-S", "--noconfirm", "tesseract"])
                    case _:
                        print(distro.id())

            case "Windows":
                subprocess.call(["choco", "install", "-y", "tesseract"])

            case "Darwin":
                subprocess.call(["brew", "install", "leptonica"])
                subprocess.call(["brew", "install", "tesseract"])
            case _:
                print(platform.system())


        install.run(self)
        self.gereksinim_kontrol()


    def program_kontrol(self, program):
        try:
            subprocess.check_output([program, "--version"])
        except Exception as hata:
            raise RuntimeError(f"\n\n» '{program}' yüklü değil!\n\n") from hata