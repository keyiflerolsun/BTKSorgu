# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import platform, sys, subprocess
from setuptools.command.install import install

class TesseractYukle(install):
    def gereksinimler(self):
        match platform.system():
            case "Linux":
                self.program_kontrol("tesseract")
            case "Windows":
                self.program_kontrol("tesseract")
            case "Darwin":
                self.program_kontrol("tesseract")

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
                        subprocess.call(["apt-get", "update"])
                        subprocess.call(["apt-get", "install", "-y", "libleptonica-dev"])
                        subprocess.call(["apt-get", "install", "-y", "tesseract-ocr"])
                    case "fedora":
                        subprocess.call(["dnf", "install", "-y", "leptonica-devel"])
                        subprocess.call(["dnf", "install", "-y", "tesseract"])
                    case "centos" | "rhel" | "rocky" | "redhat":
                        subprocess.call(["yum", "install", "-y", "leptonica-devel"])
                        subprocess.call(["yum", "install", "-y", "tesseract"])
                    case "arch" | "manjaro":
                        subprocess.call(["pacman", "-Sy"])
                        subprocess.call(["pacman", "-S", "--noconfirm", "leptonica"])
                        subprocess.call(["pacman", "-S", "--noconfirm", "tesseract"])

            case "Windows":
                subprocess.call(["choco", "install", "-y", "tesseract"])

            case "Darwin":
                subprocess.call(["brew", "install", "leptonica"])
                subprocess.call(["brew", "install", "tesseract"])


        install.run(self)


        try:
            self.gereksinimler()
        except RuntimeError as hata:
            print(hata)
            exit()

    def program_kontrol(self, program):
        try:
            subprocess.check_output([program, "--version"])
        except (OSError, subprocess.CalledProcessError) as hata:
            raise RuntimeError(f"\n\n» '{program}' yüklü değil!\n\n") from hata