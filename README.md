# Rezervační systém pro Penzion pod Špičákem (Tanvald)

Projekt pro vytvoření rezervačního systému pro reálný objekt: **Penzion pod Špičákem (Pod Špičákem 336, Tanvald)**.
Web: www.penzionpodspicakem.cz

## Funkce systému
* **Objektově orientované programování (OOP):** Využití tříd 'Host' a 'Rezervace' pro přehlednou správu dat.
* **Validace vstupů:** Automatická kontrola formátu e-mailu a telefonního čísla.
* **Kontrola kapacity:** Hlídání kapacity penzionu (12-22 osob) a minimální délky pobytu (2 noci).
* **Ošetření chyb (Try-Except):** Použití cyklu 'while' a bloku 'try-except' pro ošetření chybných uživatelských vstupů (ValueError).
  * Ošetření chyb při zápisu do souboru pomocí 'IOError' (např. při nedostatku práv k zápisu nebo uzamčení souboru jiným programem).
* **Správa dat:** Rezervace jsou automaticky ukládány do souboru 'rezervace.txt'.
## Plánované funkce
* **Správa rezervací:** Výpočet ceny na základě počtu osob (450 Kč/osoba) a délky pobytu.
* **iCal Synchronizace:** Automatické hlídání obsazenosti propojením s kalendářem na e-chalupy.cz.
* **Počasí pro hosty:** Integrace aktuální předpovědi přímo pro lokalitu **Tanvald**.

## Technické informace
* Projekt je vyvíjen v jazyce Python 3.14.0
* Externí data: Open-Meteo API (počasí), iCal (kalendář).