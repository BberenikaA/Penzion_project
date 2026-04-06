# Rezervační systém pro Penzion pod Špičákem (Tanvald)

Projekt pro vytvoření rezervačního systému pro reálný objekt: **Penzion pod Špičákem (Pod Špičákem 336, Tanvald)**.
Web: www.penzionpodspicakem.cz

## Funkce systému
* **Využití externích a interních knihoven:** 
  * Knihovna `requests` pro komunikaci s internetovými servery (stahování počasí a kontrola kalendáře).
  * Knihovna `datetime` pro práci s daty, časem a výpočty termínů.
* **Objektově orientované programování (OOP):** Využití tříd `Host` a `Rezervace` pro přehlednou správu dat.
* **Validace vstupů:** Automatická kontrola formátu e-mailu a telefonního čísla.
* **Kontrola kapacity:** Hlídání kapacity penzionu (12-22 osob) a minimální délky pobytu (2 noci).
* **Chytrý výpočet termínu:** Po zadání data příjezdu a počtu nocí systém sám automaticky dopočítá přesné datum odjezdu.
* **Ošetření chyb (Try-Except):** Použití cyklu `while` a bloku `try-except` pro ošetření chybných uživatelských vstupů (ValueError).
  * Ošetření chyb při zápisu do souboru pomocí `IOError` (např. při nedostatku práv k zápisu nebo uzamčení souboru jiným programem).
* **Správa dat:** Rezervace jsou automaticky ukládány do souboru `rezervace.txt`.

## Implementované (původně plánované) funkce
* **Správa rezervací:** Výpočet ceny na základě počtu osob (450 Kč/osoba) a délky pobytu (se stropem 8000 Kč za noc za celý penzion).
* **iCal Synchronizace:** Automatické hlídání obsazenosti propojením s utajenou adresou kalendáře z e-chalupy.cz. Tato adresa je z důvodu bezpečnosti uložena v souboru `config.py` a kód je ošetřen pro případ výpadku sítě.
* **Počasí pro hosty:** Integrace aktuální předpovědi (Open-Meteo API) přímo pro lokalitu **Tanvald** a automatické doporučení aktivit podle měsíce příjezdu.

## Ignorované soubory (.gitignore)
Projekt využívá soubor `.gitignore` pro vyloučení systémových a osobních souborů z verzování na GitHubu:
* `.idea/` – lokální konfigurační složka vývojového prostředí PyCharm.
* `__pycache__/` – automaticky generované mezipaměti Pythonu pro rychlejší běh.
* `.venv/` – složka virtuálního prostředí se staženými knihovnami.
* `config.py` – soubor s citlivou URL adresou kalendáře z důvodu bezpečnosti.
* `rezervace.txt` – lokální databáze rezervací (aby se na GitHub v budoucnu nepřenášela reálná data hostů, pro současnou potřebu jsou data fiktivní).

## Technické informace
* Projekt je vyvíjen v jazyce Python 3.14.0
* Použití knihoven `datetime` (interní) a `requests` (externí).
* Kódování souborů:** `UTF-8` (pro správné zobrazení českých znaků v souboru `rezervace.txt`)

