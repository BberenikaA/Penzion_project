import datetime

class Host:
    def __init__(self, jmeno_prijmeni, email, telefon):
        self.jmeno_prijmeni = jmeno_prijmeni
        self.email = email
        self.telefon = telefon

class Rezervace:
    def __init__(self, host, pocet_osob, pocet_noci):
        self.host = host
        self.pocet_osob = pocet_osob
        self.pocet_noci = pocet_noci
        self.datum_vytvoreni = datetime.date.today()

    def vypocti_celkovou_cenu(self):
        cena_za_noc = self.pocet_osob * 450
        if cena_za_noc > 8000:
            cena_za_noc = 8000
        return cena_za_noc * self.pocet_noci

    def uloz_do_souboru(self):
        celkova_cena = self.vypocti_celkovou_cenu()
        zapis_hosta = (f"{self.datum_vytvoreni}: {self.host.jmeno_prijmeni} ({self.host.email}), ({self.host.telefon}) - "
                        f"{self.pocet_osob} osob, {self.pocet_noci} nocí, "
                        f"Cena: {celkova_cena} Kč\n")
        try:
            with open("rezervace.txt", "a", encoding="utf-8") as soubor:
                soubor.write(zapis_hosta)
            print("Rezervace byla úspěšně uložena do souboru rezervace.txt")
        except IOError:
            print("Chyba: Dp souboru nelze zapisovat. Zkontrolujte, zda není soubor otevřen jinde.")


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
            noci = int(input("Počet nocí (min. 2): "))
            if 12 <= osob <= 22 and noci >= 2:
                break
            else:
                print("Chyba: Nesplněny podmínky kapacity (12-22) nebo délky pobytu (min 2).")
        except ValueError:
            print("Chyba: Zadávejte prosím pouze číselné údaje u počtu osob a nocí.")

    novy_host = Host(jmeno_prijmeni, email, telefon)
    nova_rezervace = Rezervace(novy_host, osob, noci)
    celkova_cena = nova_rezervace.vypocti_celkovou_cenu()

    print(f"\nRezervace pro: {novy_host.jmeno_prijmeni}")
    print(f"Celková cena pobytu: {celkova_cena} Kč")

    nova_rezervace.uloz_do_souboru()


if __name__ == "__main__":
    spustit_system()

