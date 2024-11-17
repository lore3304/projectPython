#DA LEGGERE 
"""
    Dovreste cercare di modificare le vostre funzioni in modo tale che siano simili  (ovviamente conb le opportune modifiche derivanti dalle vostre funzioni) a quella "modifica_o_inserisci_quantita"
    ho modificato la funzione in modo tale che prendesse un dizionario (riga 17) che gli viene passato  (riga 93) quando viene essa viene chiamata.
    il dizionario gli viene passato come argomento frazie alla funzione "ricercaProdotto", che verifichera l esistenza del prodotto e se presente ritornera il dizionario contenente le sue specifiche.
    Una volta che il dizionario viene passato si possono modificare i suoi elementi usando i modi che abbiamo visto sulle lezioni relative alle collezioni
    Importante le funzioni devono prevedere un caso in cui o la stringa è vuota ("") o uguale a 0, ciò sopratutto serve a far funzionare la funzione 1 correttamente (almeno in teoria)
    vi consiglio di lasciare la lista di dizionari di partenza giacenzeMagazzino gia con degli elementi presenti cosi che possiate testare la vostra funzione
    Ho commentato il codice in piu fasi quindi ci po


"""








#richiede come parametro il dizionario del prodotto, il dizionario viene ritornato dalla funzione di ricerca del prodotto
def modifica_o_inserisci_quantita(prodotto):
    if prodotto["quantita"] == 0:# se il prodotto = 0 dare possibilità di modificarlo -> metodo sopratutto utile quando si mette un nuovo prodotto (vedere codice relativo a input 1)
        # Chiediamo all'utente di inserire la quantità
        nuova_quantita = int(input(f"Inserisci la quantità per il prodotto '{prodotto['nome']}': "))
        prodotto['quantita'] = nuova_quantita # modificata la quantita
        print(f"Quantità per '{prodotto['nome']}' inserita: {prodotto['quantita']}")
    else:
        # Mostriamo la quantità attuale e chiediamo se vogliono modificarla
        print(f"Quantità attuale di '{prodotto['nome']}': {prodotto["quantita"]}")
        modifica = input("Vuoi modificare la quantità? (s/n): ")
        if modifica.lower() == 's': # sulla base dell input utente modifichiamo la quantita 
            nuova_quantita = int(input(f"Inserisci la nuova quantità per il prodotto '{prodotto['nome']}': "))
            prodotto['quantita'] = nuova_quantita
            print(f"Quantità per '{prodotto['nome']}' aggiornata a: {prodotto['quantita']}")
        else:
            print("Nessuna modifica effettuata.")
            # Funzione per modificare o inserire il prezzo di un prodotto
            
def modifica_o_inserisci_prezzo(prodotto):
    # Se il prezzo è 0, chiediamo all'utente di inserirlo per un nuovo prodotto
    if prodotto["prezzo"] == 0:
        while True:  # Ciclo per assicurarsi che l'input sia valido
            nuovo_prezzo = input(f"Inserisci il prezzo per il prodotto '{prodotto['nome']}': ")
            try:
                # Controlliamo che l'input sia un numero valido
                nuovo_prezzo_float = float(nuovo_prezzo)
                if nuovo_prezzo_float >= 0:
                    prodotto['prezzo'] = nuovo_prezzo_float
                    print(f"Prezzo per '{prodotto['nome']}' inserito: {prodotto['prezzo']:.2f}")
                    break
                else:
                    print("Il prezzo non può essere negativo.")
            except ValueError:
                print("Prezzo non valido. Inserisci solo numeri (es. 12 o 12.99).")
    else:
        # Mostriamo il prezzo attuale e chiediamo se vogliono modificarlo
        print(f"Prezzo attuale di '{prodotto['nome']}': {prodotto['prezzo']:.2f}")
        modifica = input("Vuoi modificare il prezzo? (s/n): ")
        if modifica.lower() == 's':
            while True:
                nuovo_prezzo = input(f"Inserisci il nuovo prezzo per il prodotto '{prodotto['nome']}': ")
                try:
                    nuovo_prezzo_float = float(nuovo_prezzo)
                    if nuovo_prezzo_float >= 0:
                        prodotto['prezzo'] = nuovo_prezzo_float
                        print(f"Prezzo per '{prodotto['nome']}' aggiornato a: {prodotto['prezzo']:.2f}")
                        break
                    else:
                        print("Il prezzo non può essere negativo.")
                except ValueError:
                    print("Prezzo non valido. Inserisci solo numeri (es. 12 o 12.99).")
        else:
            print("Nessuna modifica effettuata.")

#richiede come parametro il dizionario del prodotto, il dizionario viene ritornato dalla funzione di ricerca del prodotto
def modificare_o_inserire_nome(prodotto):
    if prodotto["nome"]=="":# se il prodotto = "" dare possibilità di modificarlo -> metodo sopratutto utile quando si mette un nuovo prodotto (vedere codice relativo a input 1)
        # Chiediamo all'utente di inserire la quantità
        nuovo_nome = input(f"Inserisci il nome del prodotto: ")
        prodotto["nome"] = nuovo_nome # modificato il nome
        print(f"Nome inserito: {prodotto["nome"]}")
    else:
        # mostriamo il nome attuale e chiediamo se vogliono modificarla
        print(f"Nome del prodotto {prodotto["nome"]}")
        modifica = input("Vuoi modificare il nome? (s/n):") # sulla base dell input utente modifichiamo la quantita 
        if modifica.lower() =="s":
            nuovo_nome = input(f"Inserisci il nuovo nome del prodotto '{prodotto["nome"]}: ")
            prodotto["nome"]= nuovo_nome
            print(f"Nome del prodotto: '{prodotto['nome']}' aggiornato a: '{prodotto["nome"]}")
            input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 
            
        else:
            print("Nessuna modifica effettuata")
            
#   ricercaProdotto
"""
# funzione per verificare la presenza di un prodotto all interno della lista tramite il suo nome
# se - presente stampera tutte le chiavi e valori associate a quell oggetto
quando chiama una funzione diversa da 1, 7, 6 la funzione controlli la presenza o meno del prodotto 
e una volta fatto ritorni il dizionario contenenti gli elementi che l utente vuole modificare, che verrà poi modificato dalle vostre funzioni
# altro - stamperà prodotto non esistente, ritorna false
"""
def ricercaProdotto(listaDizionari, inputUtente):
    nomeProdottoDesiderato = input("Inserisci il nome del prodotto da ricercare: ").lower() 
    for dizionario in listaDizionari:
        if dizionario["nome"] == nomeProdottoDesiderato: # controlla se il valore per la chiave nome di ogni elemento della lista sia uguale a quello selezionato dall utente
            print("Prodotto esistente ")
            for chiave, valore in dizionario.items():#for che andra a stampare tutte le info del prodoyyo
                print(f"{chiave}: {valore}")
                input("Premi invio per continuare")#input che ha lo scopo di rallentare lo scorrimento di testo nel terminale e che consente di leggere all utente con calma le info 
            if(inputUtente in "2345"):#se l utente ha digitato 2 o 3 o 4 o 5 ritorna il dizionario cercato/che vuole modificare l utente
                
                return dizionario
                
            return True #prodotto esistente
    print("Prodotto non esistente")
    return False #prodotto non presente

def isListaVuota(listaDizionari): #controlla se la lista è vuota
    if len(listaDizionari) == 0:
        print("Magazzino vuoto")
        print("Devi inserire degli elementi dentro al gestionale magazzino se vuoi modificarli o vederli")
        return True #true se vuota
    else:
        return False#false se presente almeno un elemento

def gestioneMagazzino():
    giacenzeDiMagazzino =[{"nome": "spada", "prezzo": 15,"quantita": 10,"codice":"xxx"},{"nome": "scudo", "prezzo": 10,"quantita":0, "codice":"xyz"}]#la lista dovrebbe essere vuota [], pero l ho riempita per fare delle prove e la funzione 3,7,8 funzionano (in linea purament teorica)
    sceltaUtente = input("""
Invia 1 se vuoi inserire un nuovo prodotto
Invia 2 se vuoi modificare il prezzo di un prodotto
Invia 3 se vuoi modificare la quantita di un prodotto
Invia 4 se vuoi modificare il nome di un  prodotto
Invia 5 se vuoi modificare il codice di un prodotto
Invia 6 se vuoi vedere tutto l inventario
Invia 7 se vuoi verificare se un prodotto è presente o meno nel magazzino e vedere le sue caratteristiche
Invia 8 se vuoi uscire dal programma (attenzione perderai i dati del magazzino)
>>> """)
    while sceltaUtente != "8":
        if isListaVuota(giacenzeDiMagazzino):
            sceltaUtente ="1" # se lista vuota utente forzato a inserire un nuovo prodotto
        
        #7-8-1
        if (sceltaUtente == "1"):
            print("Inserire un nuovo prodotto")
            giacenzeDiMagazzino.append({"nome":"","codice":"","prezzo":0,"quantita":0})
    
            #call funzione 4 nome, se valore nomeProdotto "" allora non stampare vecchio nome ma fare mettere direttamente all utente quello nuovo 
            #call funzione 5 codice se valore codice "" allora non stampare vecchio nome ma fare mettere direttamente all utente quello nuovo 
            #call funzione 2 prezzo se valore prezzo 0 allora non stampare vecchio nome ma fare mettere direttamente all utente quello nuovo 
            #call funzione 3 quantita se valore quantita 0  allora non stampare vecchio nome ma fare mettere direttamente all utente quello nuovo 
        elif(sceltaUtente=="2"):
            modifica_o_inserisci_prezzo(ricercaProdotto(giacenzeDiMagazzino, sceltaUtente))
    
        elif(sceltaUtente =="3"):
            modifica_o_inserisci_quantita(ricercaProdotto(giacenzeDiMagazzino, sceltaUtente))# si chiama la funzione modifica_o bla bla che xhiama la funzione ricercaprodotto che ritornera un dizionario
        elif(sceltaUtente =="4"):
            modificare_o_inserire_nome(ricercaProdotto(giacenzeDiMagazzino, sceltaUtente))
            
        
        
        
        elif(sceltaUtente == "7"):
            ricercaProdotto(giacenzeDiMagazzino, sceltaUtente)
                
        elif(sceltaUtente == "8"):
            #si chiude il programma
            print("Programma in chiusura")
            break
    
        sceltaUtente = input("""
Invia 1 se vuoi inserire un nuovo prodotto
Invia 2 se vuoi modificare il prezzo di un prodotto
Invia 3 se vuoi modificare la quantita di un prodotto
Invia 4 se vuoi modificare il nome di un  prodotto
Invia 5 se vuoi modificare il codice di un prodotto
Invia 6 se vuoi vedere tutto l inventario
Invia 7 se vuoi verificare se un prodotto è presente o meno nel magazzino e vedere le sue caratteristiche
Invia 8 se vuoi uscire dal programma (attenzione perderai i dati del magazzino)
>>> """) # richiediamo l input prima dell inizio del nuovo ciclo 




gestioneMagazzino()



"""
#file con l'unico scopo di inserirci dentro codice per capire dov'è il problema e debuggarlo
def modifica_o_inserisci_quantita(prodotto):
    if prodotto["quantita"] == 0:
        nuova_quantita = int(input(f"Inserisci la quantità per il prodotto '{prodotto['nome']}': "))
        prodotto['quantita'] = nuova_quantita
        print(f"Quantità per '{prodotto['nome']}' inserita: {prodotto['quantita']}")
    else:
        print(f"Quantità attuale di '{prodotto['nome']}': {prodotto['quantita']}")
        modifica = input("Vuoi modificare la quantità? (s/n): ")
        if modifica.lower() == 's':
            nuova_quantita = int(input(f"Inserisci la nuova quantità per il prodotto '{prodotto['nome']}': "))
            prodotto['quantita'] = nuova_quantita
            print(f"Quantità per '{prodotto['nome']}' aggiornata a: {prodotto['quantita']}")
        else:
            print("Nessuna modifica effettuata.")


def modifica_o_inserisci_prezzo(prodotto):
    if prodotto["prezzo"] == 0:
        while True:
            nuovo_prezzo = input(f"Inserisci il prezzo per il prodotto '{prodotto['nome']}': ")
            try:
                nuovo_prezzo_float = float(nuovo_prezzo)
                if nuovo_prezzo_float >= 0:
                    prodotto['prezzo'] = nuovo_prezzo_float
                    print(f"Prezzo per '{prodotto['nome']}' inserito: {prodotto['prezzo']:.2f}")
                    break
                else:
                    print("Il prezzo non può essere negativo.")
            except ValueError:
                print("Prezzo non valido. Inserisci solo numeri (es. 12 o 12.99).")
    else:
        print(f"Prezzo attuale di '{prodotto['nome']}': {prodotto['prezzo']:.2f}")
        modifica = input("Vuoi modificare il prezzo? (s/n): ")
        if modifica.lower() == 's':
            while True:
                nuovo_prezzo = input(f"Inserisci il nuovo prezzo per il prodotto '{prodotto['nome']}': ")
                try:
                    nuovo_prezzo_float = float(nuovo_prezzo)
                    if nuovo_prezzo_float >= 0:
                        prodotto['prezzo'] = nuovo_prezzo_float
                        print(f"Prezzo per '{prodotto['nome']}' aggiornato a: {prodotto['prezzo']:.2f}")
                        break
                    else:
                        print("Il prezzo non può essere negativo.")
                except ValueError:
                    print("Prezzo non valido. Inserisci solo numeri (es. 12 o 12.99).")
        else:
            print("Nessuna modifica effettuata.")


def modificare_o_inserire_nome(prodotto):
    if prodotto["nome"] == "":
        nuovo_nome = input(f"Inserisci il nome del prodotto: ")
        prodotto["nome"] = nuovo_nome
        print(f"Nome inserito: {prodotto['nome']}")
    else:
        print(f"Nome del prodotto: {prodotto['nome']}")
        modifica = input("Vuoi modificare il nome? (s/n): ")
        if modifica.lower() == "s":
            nuovo_nome = input(f"Inserisci il nuovo nome del prodotto '{prodotto['nome']}': ")
            prodotto["nome"] = nuovo_nome
            print(f"Nome del prodotto aggiornato a: '{prodotto['nome']}'")
        else:
            print("Nessuna modifica effettuata.")


def ricercaProdotto(listaDizionari, inputUtente):
    nomeProdottoDesiderato = input("Inserisci il nome del prodotto da ricercare: ").lower() 
    for dizionario in listaDizionari:
        if dizionario["nome"] == nomeProdottoDesiderato:
            print("Prodotto esistente ")
            for chiave, valore in dizionario.items():
                print(f"{chiave}: {valore}")
            input("Premi invio per continuare")
            if inputUtente in "2345":
                return dizionario
            return True
    print("Prodotto non esistente")
    return False


def isListaVuota(listaDizionari):
    if len(listaDizionari) == 0:
        print("Magazzino vuoto")
        print("Devi inserire degli elementi dentro al gestionale magazzino se vuoi modificarli o vederli")
        return True
    else:
        return False


def gestioneMagazzino():
    giacenzeDiMagazzino = [
        {"nome": "spada", "prezzo": 15, "quantita": 10, "codice": "xxx"},
        {"nome": "scudo", "prezzo": 10, "quantita": 0, "codice": "xyz"}
    ]
    
    sceltaUtente = input(
Invia 1 se vuoi inserire un nuovo prodotto
Invia 2 se vuoi modificare il prezzo di un prodotto
Invia 3 se vuoi modificare la quantita di un prodotto
Invia 4 se vuoi modificare il nome di un  prodotto
Invia 5 se vuoi modificare il codice di un prodotto
Invia 6 se vuoi vedere tutto l'inventario
Invia 7 se vuoi verificare se un prodotto è presente o meno nel magazzino e vedere le sue caratteristiche
Invia 8 se vuoi uscire dal programma (attenzione perderai i dati del magazzino)
>>> )
    
    while sceltaUtente != "8":
        if isListaVuota(giacenzeDiMagazzino):
            sceltaUtente = "1"
        
        if sceltaUtente == "1":
            print("Inserire un nuovo prodotto")
            giacenzeDiMagazzino.append({"nome": "", "codice": "", "prezzo": 0, "quantita": 0})
        
        elif sceltaUtente == "2":
            modifica_o_inserisci_prezzo(ricercaProdotto(giacenzeDiMagazzino, sceltaUtente))
    
        elif sceltaUtente == "3":
            modifica_o_inserisci_quantita(ricercaProdotto(giacenzeDiMagazzino, sceltaUtente))
        
        elif sceltaUtente == "4":
            modificare_o_inserire_nome(ricercaProdotto(giacenzeDiMagazzino, sceltaUtente))
        
        elif sceltaUtente == "7":
            ricercaProdotto(giacenzeDiMagazzino, sceltaUtente)
                
        elif sceltaUtente == "8":
            print("Programma in chiusura")
            break
    
        sceltaUtente = input(
Invia 1 se vuoi inserire un nuovo prodotto
Invia 2 se vuoi modificare il prezzo di un prodotto
Invia 3 se vuoi modificare la quantita di un prodotto
Invia 4 se vuoi modificare il nome di un  prodotto
Invia 5 se vuoi modificare il codice di un prodotto
Invia 6 se vuoi vedere tutto l'inventario
Invia 7 se vuoi verificare se un prodotto è presente o meno nel magazzino e vedere le sue caratteristiche
Invia 8 se vuoi uscire dal programma (attenzione perderai i dati del magazzino)
>>> )


gestioneMagazzino()
"""