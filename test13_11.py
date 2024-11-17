
import random
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod

# Classe astratta per un personaggio
class Personaggio(ABC):
    def __init__(self, nome, salute, attacco_base, attacco_speciale):
        self.nome = nome  # Nome del personaggio
        self.salute = salute  # Salute del personaggio
        self.attacco_base = attacco_base  # Funzione per l'attacco base
        self.attacco_speciale = attacco_speciale  # Funzione per l'attacco speciale
        self.turni_attacco_speciale = 3  # Numero di turni che deve passare prima di poter usare di nuovo l'attacco speciale

    # Metodo astratto per l'attacco base (ogni personaggio lo implementa in modo diverso)
    @abstractmethod
    def usa_attacco_base(self):
        pass

    # Metodo per usare l'attacco speciale (da implementare per ogni personaggio)
    def usa_attacco_speciale(self):
        pass

    # Metodo per subire danni e ridurre la salute
    def subisci_danno(self, danno):
        self.salute -= danno
        if self.salute < 0:
            self.salute = 0

    # Verifica se il personaggio è ancora vivo
    def is_alive(self):
        return self.salute > 0

# Classe Guerriero, derivata dalla classe Personaggio
class Guerriero(Personaggio):
    def __init__(self):
        super().__init__("Baltar", 200, self.crea_attacco_base(), self.crea_attacco_speciale())

    # Crea l'attacco base per il Guerriero
    def crea_attacco_base(self):
        def attacco():
            danno = random.randint(15, 25)  # Danno casuale tra 15 e 25
            print(f"{self.nome} usa Colpo di Spada causando {danno} danni!")
            return danno
        return attacco

    # Crea l'attacco speciale per il Guerriero
    def crea_attacco_speciale(self):
        def attacco():
            danno = random.randint(30, 50)  # Danno casuale tra 30 e 50
            print(f"{self.nome} usa Urlo di Guerra causando {danno} danni!")
            return danno
        return attacco

    # Metodo per eseguire l'attacco base
    def usa_attacco_base(self):
        return self.attacco_base()

    # Metodo per eseguire l'attacco speciale
    def usa_attacco_speciale(self):
        if self.turni_attacco_speciale == 0:  # Se il Guerriero può usare l'attacco speciale
            self.turni_attacco_speciale = 3  # Resetta il conteggio dei turni
            return self.attacco_speciale()
        else:
            print(f"{self.nome} non può ancora usare l'attacco speciale!")
            return 0

# Classe Mago, derivata dalla classe Personaggio
class Mago(Personaggio):
    def __init__(self):
        self.mana = 100  # Il Mago ha una quantità di mana
        super().__init__("Aharad", 140, self.crea_attacco_base(), self.crea_attacco_speciale())

    # Crea l'attacco base per il Mago (danno e consumo di mana)
    def crea_attacco_base(self):
        def attacco():
            if self.mana >= 10:  # Verifica che il Mago abbia abbastanza mana
                danno = random.randint(10, 20)  # Danno casuale tra 10 e 20
                self.mana -= 10  # Consuma mana
                print(f"{self.nome} usa Dardo di Fuoco causando {danno} danni. Mana rimanente: {self.mana}")
                return danno
            else:
                print(f"{self.nome} non ha abbastanza mana per usare Dardo di Fuoco!")
                return 0
        return attacco

    # Crea l'attacco speciale per il Mago
    def crea_attacco_speciale(self):
        def attacco():
            if self.mana >= 20:  # Verifica che il Mago abbia abbastanza mana
                danno = random.randint(25, 45)  # Danno casuale tra 25 e 45
                self.mana -= 20  # Consuma mana
                print(f"{self.nome} usa Tempesta Magica causando {danno} danni. Mana rimanente: {self.mana}")
                return danno
            else:
                print(f"{self.nome} non ha abbastanza mana per usare Tempesta Magica!")
                return 0
        return attacco

    # Metodo per eseguire l'attacco base
    def usa_attacco_base(self):
        return self.attacco_base()

    # Metodo per eseguire l'attacco speciale
    def usa_attacco_speciale(self):
        if self.turni_attacco_speciale == 0:  # Se il Mago può usare l'attacco speciale
            self.turni_attacco_speciale = 3  # Resetta il conteggio dei turni
            return self.attacco_speciale()
        else:
            print(f"{self.nome} non può ancora usare l'attacco speciale!")
            return 0

    # Metodo per recuperare mana (se usato in futuro)
    def recupera_mana(self):
        recupero = np.random.randint(10, 20)
        self.mana += recupero
        print(f"{self.nome} recupera {recupero} punti mana. Mana attuale: {self.mana}")

# Funzione per scegliere il personaggio
def scegli_personaggio():
    scelta = input("Scegli il tuo personaggio (1 per Guerriero, 2 per Mago): ")
    if scelta == "1":
        return Guerriero()
    elif scelta == "2":
        return Mago()
    else:
        print("Scelta non valida! Verrà scelto un Guerriero di default.")
        return Guerriero()

# Funzione per la battaglia
def battaglia(giocatore, nemico):
    turno = 1
    statistiche = {
        "giocatore_attacchi": [],
        "nemico_attacchi": [],
        "mana_usato": [],
        "giocatore_salute": [],
        "nemico_salute": []
    }

    print(f"Inizia la battaglia tra {giocatore.nome} e {nemico.nome}!\n")

    while giocatore.is_alive() and nemico.is_alive():  # La battaglia continua finché entrambi sono vivi
        print(f"--- Turno {turno} ---")
        print(f"Salute {giocatore.nome}: {giocatore.salute}, Salute {nemico.nome}: {nemico.salute}")

        # Turno del giocatore
        print(f"\nTocca a {giocatore.nome}!")
        if isinstance(giocatore, Mago):
            print(f"Mana disponibile: {giocatore.mana}")

        scelta = int(input("1. Attacco Base | 2. Attacco Speciale: "))
        if scelta == 1:
            danno = giocatore.usa_attacco_base()  # Usa l'attacco base
            statistiche["mana_usato"].append(10 if isinstance(giocatore, Mago) else 0)
            print(f"{giocatore.nome} infligge {danno} danni con l'Attacco Base!")
        elif scelta == 2:
            if turno % 3 == 0:
                danno = giocatore.usa_attacco_speciale()  # Usa l'attacco speciale
                statistiche["mana_usato"].append(20 if isinstance(giocatore, Mago) else 0)
                print(f"{giocatore.nome} infligge {danno} danni con l'Attacco Speciale!")
            else:
                print(f"{giocatore.nome} non può ancora usare l'Attacco Speciale!")
                danno = 0
        else:
            print("Scelta non valida, perdi il turno!")
            danno = 0

        # Il nemico attacca
        danno_nemico = random.randint(10, 20)  # Il nemico infligge danni casuali
        nemico.subisci_danno(danno_nemico)
        statistiche["nemico_attacchi"].append(danno_nemico)
        print(f"{nemico.nome} infligge {danno_nemico} danni!")

        # Aggiungi le statistiche
        statistiche["giocatore_attacchi"].append(danno)
        statistiche["giocatore_salute"].append(giocatore.salute)
        statistiche["nemico_salute"].append(nemico.salute)

        turno += 1  # Aumenta il turno

    return statistiche  # Ritorna le statistiche

# Funzione per il resoconto
def resoconto(statistiche):
    import matplotlib.pyplot as plt

    # Calcola la media danni e totale mana
    media_danni_giocatore = np.mean(statistiche["giocatore_attacchi"])
    media_danni_nemico = np.mean(statistiche["nemico_attacchi"])
    totale_mana_usato = np.sum(statistiche["mana_usato"])

    # Mostra il resoconto della battaglia
    print("\nResoconto della battaglia:")
    print(f"Media danni giocatore: {media_danni_giocatore:.2f}")
    print(f"Media danni nemico: {media_danni_nemico:.2f}")
    print(f"Totale mana usato: {totale_mana_usato}")

# Scegli il personaggio
giocatore = scegli_personaggio()

# Crea un nemico (esempio Guerriero)
nemico = Guerriero()

# Avvia la battaglia
statistiche = battaglia(giocatore, nemico)

# Mostra il resoconto finale
resoconto(statistiche)


#arion@cefi.it
