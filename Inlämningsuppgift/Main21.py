import random, os, time


class Kort: #    En klass som representerar ett kort i en kortlek.

    def __init__(self, färg, nummer):
        self.färg = färg #attribut
        self.nummer = nummer #attribut

    #Skapat en funktion som skapar en kortlek, med hjälp av shuffle så sparas kortleken i listan kortlek.
    @staticmethod
    def skapa_kortlek():
        kortlek = []
        for färg in ["Hjärter", "Ruter", "Klöver", "Spader"]:
            for nummer in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dam", "Kung", "Ess"]:
                kortlek.append(Kort(färg, nummer)) #Append funktionen gör att den ligger till färg och nummer i kortlek.
        random.shuffle(kortlek)
        return kortlek

    #en funktion som räknar värdet i din hand.
    @staticmethod
    def räkna_värde(din_hand):
        value = 0
        ess = 0  # För att hålla koll på antalet ess i handen, ifall det är två så måste värdet justeras.
        for kort in din_hand:
            if kort.nummer == "Knekt":
                value += 11
            elif kort.nummer == "Dam":
                value += 12
            elif kort.nummer == "Kung":
                value += 13
            elif kort.nummer == "Ess":
                value += 14
                ess += 1
            else:
                value += int(kort.nummer)

        # Justera värdet om det finns ess och handen blir över 21
        while ess > 0 and value > 21:
            value -= 13
            ess -= 1

        return value


    @staticmethod #spelare1 funktionen, använder staticmethod, för jag kommer inte behöva ändra några attribut.
    def spelare1(din_total):#Först skapar jag en variabel kortlek och kallar på funktionn skapa_kortlek
        kortlek = Kort.skapa_kortlek()
        din_hand = [] #Sparar min hand i denna lista
        for _ in range(1):
            din_hand.append(kortlek.pop())#Startar spelet med att ge ett kort automatiskt till spelare1
        while din_total <= 21:#så länge min hand är mindre 21 så är loopen igång eller när jag väljer att avsluta den i
            # mina if satser nedan.
            print("Din hand:")
            for kort in din_hand:
                print(f"{kort.nummer} {kort.färg}")#printar ut det första kortet jag fick.
            print(f"Ditt totala värde: {Kort.räkna_värde(din_hand)}")#Använder sedan funktionen räkna värde, för att räkna värdet
            svar = input("Vill du dra ett kort eller stanna? (Dra/Stanna): ").lower()
            if svar == "dra":
                if os.name == "nt":  # Rensa terminal
                    os.system("cls")
                elif os.name == "posix":
                    os.system("clear")
                nytt_kort = kortlek.pop()
                din_hand.append(nytt_kort)
                print(f"Du drog {nytt_kort.nummer} {nytt_kort.färg}")
                din_total = Kort.räkna_värde(din_hand)
                if din_total >= 22:
                    print(f'Du förlorade, din hand är', din_total)
                    break
            elif svar == "stanna":
                break
                if os.name == "nt":
                    os.system("cls")
                elif os.name == "posix":
                    os.system("clear")
            elif svar != "dra" or "stanna":
                print('Felaktig inmatning')
                time.sleep(1)
        if din_total <= 21:
            Kort.dator(din_total)
        else:
            print('Hejdå')
    @staticmethod
    def dator(din_total):#Funktion för datorn, och hoppar hit när jag väljer att stanna.
        datorns_hand = []
        kortlek = Kort.skapa_kortlek()
        #Så länge datorns hand är mindre än 21 och är mindre än spelare1s hand så ska den dra ett kort.
        while Kort.räkna_värde(datorns_hand) < 21 and Kort.räkna_värde(datorns_hand) <= din_total:
            datorns_hand.append(kortlek.pop())

        # Visa datorns hand
        print("Datorns hand:")
        for kort in datorns_hand:
            print(f"{kort.nummer} {kort.färg}")
        print(f"Datorns totala värde: {Kort.räkna_värde(datorns_hand)}")

        datorns_total = Kort.räkna_värde(datorns_hand)

        if datorns_total > 21:
            print("Datorn förlorade!")
        elif din_total > datorns_total:
            print("Du vann!")
        elif datorns_total > din_total:
            print("Datorn vann!")
        elif din_total == datorns_total:
            print("Ni fick samma score, så datorn vann!")

    @staticmethod
    def spelet():#Själva funktionen för att spelet ska gå igång
        print('Välkommen till spelet 21')
        print('''
Regler: 
*Max 21
*Får du över 21, så förlorar du.
*Får du högre än datorn så vinner du.''')
        print()
        input('Tryck på enter för att starta igång')
        os.system("cls")
        while True:
            din_total = 0
            #Detta anropar funktionen spelare1 i din Kort-klass och skickar med din_total som ett argument med startvärde 0
            Kort.spelare1(din_total)
            svar = input("Vill du spela igen? (ja/nej): ").lower()
            while svar not in ["ja", "nej"]:
                print('Felaktig inmatning')
                time.sleep(1)
                svar = input("Vill du spela igen? (ja/nej): ").lower()
                if svar == "ja":
                    continue
                elif svar == "nej":
                    break
                os.system("cls")




if __name__ == "__main__":
    Kort.spelet()
