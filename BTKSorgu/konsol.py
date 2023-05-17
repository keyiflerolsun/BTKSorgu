# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from rich         import pretty, traceback
from rich.console import Console
pretty.install()
traceback.install(show_locals=False)
konsol = Console(log_path=False)

from BTKSorgu  import BTKSorgu
from sys       import argv

def basla():
    print()

    if len(argv) != 2:
        konsol.print("[bold yellow2][!] Lütfen Domain Girin..")
        konsol.print("\n[turquoise2]Örn.: [pale_green1]BTKSorgu redtube.com\n")
        return

    konsol.print(f"[yellow]{BTKSorgu(argv[1])}\n")

if __name__ == "__main__":
    basla()