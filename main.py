import datetime
import requests


def zkontroluj_obsazenost_online():
    try:
        from config import URL_OBSAZENOST
        odpoved = requests.get(URL_OBSAZENOST, timeout=5)
        if odpoved.status_code == 200:
            return "✅ OK (Synchronizace s e-chalupy.cz je aktivní)"
        else:
            return "❌ CHYBA (Server e-chalupy neodpovídá)"
    except ImportError:
        return "⚠️ CHYBA (Chybí soubor config.py)"
    except Exception:
        return "🌐 CHYBA (Nelze se připojit k internetu)"


def ziskej_info_o_pobytu(datum_prijezdu_str):
    try:
        prijezd_dt = datetime.datetime.strptime(datum_prijezdu_str, "%d.%m.%Y")
        mesic = prijezd_dt.month

        if mesic in [12, 1, 2]:
            sezona, tipy = "ZIMA ❄️", "lyže (Špičák), brusle a běžky"
        elif mesic in [6, 7, 8]:
            sezona, tipy = "LÉTO ☀️", "kolo, koupání v bazéně, v Jizeře"
        elif mesic in [3, 4, 5]:
            sezona, tipy = "JARO 🌱", "procházky a cykloturistika"
        else:
            sezona, tipy = "PODZIM 🍂", "houbaření a podzimní výšlapy"

        url = "https://api.open-meteo.com/v1/forecast?latitude=50.7383&longitude=15.3082&current_weather=true"
        odpoved = requests.get(url).json()
        teplota = odpoved['current_weather']['temperature']

        return f"{sezona} (aktuálně v Tanvaldu {teplota}°C). Doporučujeme: {tipy}."
    except:
        return "Informace o počasí a aktivitách nejsou dostupné."


class Host:
    def __init__(self, jmeno_prijmeni, email, telefon):
        self.jmeno_prijmeni = jmeno_prijmeni
        self.email = email
        self.telefon = telefon


class Rezervace:
    def __init__(self, host, pocet_osob, pocet_noci, datum_prijezdu, datum_odjezdu):
        self.host = host
        self.pocet_osob = pocet_osob
        self.pocet_noci = pocet_noci
        self.datum_prijezdu = datum_prijezdu
        self.datum_odjezdu = datum_odjezdu
        self.datum_vytvoreni = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

    def vypocti_celkovou_cenu(self):
        cena_za_noc = self.pocet_osob * 450
        if cena_za_noc > 8000:
            cena_za_noc = 8000
        return cena_za_noc * self.pocet_noci

    def uloz_do_souboru(self):
        celkova_cena = self.vypocti_celkovou_cenu()
        zapis_hosta = (
            f"{self.datum_vytvoreni}: {self.host.jmeno_prijmeni} ({self.host.email}), ({self.host.telefon}) - "
            f"TERMÍN: {self.datum_prijezdu} až {self.datum_odjezdu} , "
            f"{self.pocet_osob} osob, {self.pocet_noci} nocí, "
            f"Cena: {celkova_cena} Kč\n")
        try:
            with open("rezervace.txt", "a", encoding="utf-8") as soubor:
                soubor.write(zapis_hosta)
            print("Rezervace byla úspěšně uložena do souboru rezervace.txt")
            return True
        except IOError:
            print("Chyba: Do souboru nelze zapisovat. Zkontrolujte, zda není soubor otevřen jinde.")
            return False


def spustit_system():
    print("=== Rezervační systém: Penzion pod Špičákem (Tanvald) ===")

    jmeno_prijmeni = input("Jméno a příjmení hosta: ")

    while True:
        email = input("Email hosta: ")
        if "@" in email and "." in email:
            break
        print("Chyba: Email musí obsahovat zavináč (@) a tečku (.)")

    while True:
        telefon = input("Telefon hosta (pouze číslice): ")
        if telefon.isdigit():
            break
        print("Chyba: Telefon nesmí obsahovat písmena ani mezery.")

    while True:
        try:
            osob = int(input("Počet osob (12-22): "))
            if 12 <= osob <= 22:
                break
            print("Chyba: Nesplněny podmínky kapacity (12-22).")
        except ValueError:
            print("Chyba: Zadávejte prosím pouze číselné údaje u počtu osob.")

    while True:
        try:
            noci = int(input("Počet nocí (min. 2): "))
            if noci >= 2:
                break
            print("Chyba: Minimální délka pobytu jsou 2 noci.")
        except ValueError:
            print("Chyba: Zadávejte prosím pouze číselné údaje u počtu nocí.")

    while True:
        try:
            prijezd_str = input("Zadejte datum příjezdu (např. 15.01.2026): ")
            prijezd_dt = datetime.datetime.strptime(prijezd_str, "%d.%m.%Y")
            break
        except ValueError:
            print("Chyba: Špatný formát data. Zadejte např. 15.01.2026")

    odjezd_dt = prijezd_dt + datetime.timedelta(days=noci)
    odjezd_str = odjezd_dt.strftime("%d.%m.%Y")

    print(f"Datum odjezdu spočítáno automaticky: {odjezd_str}")

    prijezd = prijezd_str
    odjezd = odjezd_str

    novy_host = Host(jmeno_prijmeni, email, telefon)
    nova_rezervace = Rezervace(novy_host, osob, noci, prijezd, odjezd)
    celkova_cena = nova_rezervace.vypocti_celkovou_cenu()

    print(f"\nRezervace pro: {novy_host.jmeno_prijmeni}")
    print(f"Celková cena pobytu: {celkova_cena} Kč")

    if nova_rezervace.uloz_do_souboru():
        print("✅ Rezervace byla úspěšně uložena do souboru rezervace.txt")
    else:
        print("❌ Chyba: Do souboru nelze zapisovat. Zkontrolujte, zda není soubor otevřen jinde.")

    print("\n" + "=" * 40)
    print(f"REZERVAČNÍ SYSTÉM PRO: {novy_host.jmeno_prijmeni}")
    print(f"TERMÍN: {prijezd} - {odjezd}")
    print(f"CELKOVÁ CENA: {celkova_cena} Kč")
    print("-" * 40)
    print(f"STAV OBSAZENOSTI: {zkontroluj_obsazenost_online()}")
    print(f"Roční období V TANVALDĚ v termínu rezervace: {ziskej_info_o_pobytu(prijezd)}")
    print("=" * 40 + "\n")
    print("Rezervace byla úspěšně zpracována. Děkujeme!")


if __name__ == "__main__":
    spustit_system()
