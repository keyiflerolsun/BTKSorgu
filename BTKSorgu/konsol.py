# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from BTKSorgu import BTKSorgu
from .Libs    import konsol
from sys      import argv

def basla():
    print()

    if len(argv) != 2:
        konsol.print("[bold yellow2][!] Lütfen Domain Girin..")
        konsol.print("\n[turquoise2]Örn.: [pale_green1]BTKSorgu redtube.com\n")
        return

    konsol.print(f"[yellow]{BTKSorgu(argv[1])}\n")

if __name__ == "__main__":
    basla()