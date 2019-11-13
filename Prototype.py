
class Bestelling: 
    """
   :method: Dit is een class die operaties uitvoert op bestellingen.
   :input: Geen.
   :output: Geen.
   :pre-condition: Geen.
   :post-condition: Geen.

    """

    def __init__(self, gebruikers_id, timestamp, chocolademelk_id):
        """
       :method: Dit is de constructor van de class Bestelling. Het maakt een Bestelling met de attributen gebruikers_id, timestamp, chocolademelk_id en afgehaald.
       :input: gebruikersid(int): de id van de gebruiker; timestamp(int): zoeksleutel van de Bestelling; chocolademelk_id(str): id van chocolademelk; afgehaald(bool): toont aan of de Bestelling is afgehaald;
       :output: Geen.
       :pre-condition: Geen.
       :post-condition: De aangemaakte Bestelling met gebruikers_id, timestamp, chocolademelk_id, afgehaald.

        """


class Werknemer:
    """
   :method: Dit is een class om operaties uit te voeren op werknemers.
   :input: Geen.
   :output: Geen.
   :pre-condition: Geen.
   :post-condition: Geen.

    """

    def __init__(self, id, voornaam, achternaam, workload):
        """
       :method: Dit is de constructor van de class Werknemer. Het maakt een Werkenemer met een id, voornaam, achternaam en workload.
       :input: id(int): de zoeksleutel van de Werknemer; voornaam(str): voornaam van de Werknemer; achternaam(str): achternaam van de Werknemer; workload(int): workload van de Werknemer uitgedrukt in credits;
       :output: Geen
       :pre-condition: Geen
       :post-condition: Een Werknemer met id , voornaam, achetrnaam, workload.

        """

class keyify:
    def __init__(self, value, key):
        """

        :param value: val(classobj)
        :param key:   classobj.element (het element waarop we zoeken)
        """
        self.value = value
        self.key = key



class Stack:                    #Geimplementeerd door Jason Halder
    """
   :method: Dit is een class om operaties uit te voeren op een stack.
   :input: geen
   :output:geen
   :pre-condition: geen
   :post-condition: geen
    """

    def __init__(self):
        """
       :method: De constructor voor de Stack class. Maakt een stack en stackTop aan.
       :input: Geen.
       :output: Geen.
       :pre-condition: Geen.
       :post-condition: Een stack en stackTop aangemaakt zonder elementen.
        """


    def isEmpty(self):
        """
        :method: Toont aan of de stack leeg is.
        :input: Geen input.
        :output: Geeft "True" als de stack leeg is en "False" als de stack niet leeg is.
        :pre-condition: Een lege of gevulde stack.
        :post-condition: Geen.

        """

    def pop(self):
        """
        :method: Verwijdert de laatst toegevoegde element in de stack.
        :input: Geen.
        :output: Geeft "True" als succes en "False" voor mislukking.
        :pre-condition: Stack moet minsten 1 element bezitten.
        :post-condition: Het laatste toegevoegde element in de stack is verwijderd. De stackTop is nu het volgend element in de stack als er 1 aanwezig is.

        """


    def getTop(self):
        """
        :method: Geeft de element die laatst toegevoegd is aan de stack.
        :input: Geen.
        :output: Geeft "True" voor succes en "False" voor mislukking.
        :pre-condtion: Een stack met minstens 1 element.
        :post-condition: Geen

        """


    def push(self, val):
        """
       :method: Voegt een nieuw element toe aan de stack.
       :input: val(classobj): de element die men wenst toe te voegen.
       :output: Geeft "True" voor succes en "False" voor mislukking.
       :pre-condition: Geenhttps://github.com/ilias-ahm/Ilias
       :post-condition: Aan de stack is de element val toegevoegd. stackTop is nu het reeds toegevoegde element.

        """


class Ketting:          #Geimplementeerd door Mano Lemmens
    """
   :method: Dit is een class om operaties uit te voeren op een dubbel gelinkte circulaire ketting.
   :input: Geen.
   :output: Geen.
   :pre-condition: Geen.
   :post-condition: Geen.
    """

    def __init__(self):
        """
       :method: Dit is de constructor voor de class Ketting. Het maakt een tail en een head aan die respectievelijk het begin en het einde van de ketting tonen.
       :input: Geen.
       :output: Geen.
       :pre-condition: Geen.
       :post-condition: Een lege head en lege tail.

        """

    def tableInsert(self, val):
        """https://github.com/ilias-ahm/Ilias
       :method: Voegt een element toe aan de ketting.
       :input: val(classobj): element die men wenst toe te voegen aan de ketting.
       :output: Geeft "True" voor succes en "False" voor mislukking.
       :pre-condition: Geen.
       :post-condition: Een element is toegevoegd aan het einde van de ketting. Hierdoor zal de head wijzen naar het nieuw element.

        """

    def tableDelete(self, key):
        """
       :method: Delete het gevraagde element in de ketting.
       :input: key(classobj): het element die men wilt verwijderen.
       :output: Geeft "True" voor succes en "False" voor mislukking.
       :pre-condition: Het element te verwijderen moet in de ketting aanwezig zijn.
       :post-condition: Ketting zonder het verwijderde element. De head en tail zullen wijzen naar een nieuw als verwijderde element een head of tail was.

        """



    def tableEmpty(self):
        """
       :method: Toont aan of de ketting leeg is.
       :input: Geen.
       :output: Geeft True als de ketting elementen bezit en False als de ketting leeg is.
       :pre-condition: Een lege of gevulde ketting.
       :post-condition: Geen.

        """

    def tableRetrieve(self, key):
        """
       :method: Geeft een gevraagde element terug.
       :input: key(classobj): het element die men terug wilt.
       :output: Geeft key terug voor succes en False voor mislukking.
       :pre-condition: Het gevraagde element moet in de ketting zijn.
       :post-condition: Geen.

        """


    def tableTraverse(self):
        """
       :method: Geeft een lijst met alle elementen van de ketting.
       :input: Geen.
       :output: Lijst met elementen (succes) en geeft "False" voor mislukking.
       :pre-condition: De ketting is niet leeg.
       :post-condition: Geen.

        """


    def lengthTable(self):
        """
       :method: Geef het aantal elementen in de ketting weer.
       :input: Geen.
       :output: Aantal elementen in de ketting (succes) en "False" voor mislukking.
       :pre-condition: Ketting is niet leeg.
       :post-condition: Geen.

        """

    def sortBubble(self):
        """
       :method: Sorteert de volgorde van ketting van klein naar groot.
       :input: Geen.
       :output: Geeft "True" voor succes en "False" voor mislukking.
       :pre-condition: Een ketting met minstens 2 elementen.
       :post-condition: De ketting zijn elementen zijn verplaatst van klein naar groot waarbij de tail en head wijzen naar een nieuw element als de elementen van de ongesorteerde ketting is verplaatst.

        """


class Queue:        #Geimplementeerd door Ilias Ahmindach
    """
   :method: Dit is de class die operaties uitvoer op een Queue.
   :input: Geen.
   :output: Geen.
   :pre-condition: Geen.
   :post-condition: Geen.

    """
    def __init__(self):
        """
       :method: Dit is de constructor voor class Queue en maakt een lege queue, frontP en backP. De laatste twee kijken respectievelijk naar het eerste en laatste element van Queue.
       :input: Geen.
       :output:Geen.
       :pre-condition: Geen.
       :post-condition: Een lege queue, frontP en backP.

        """

    def isEmpty(self):
        """
       :method: Toont aan of de queue leeg is of niet.
       :input: Geen.
       :output: Geeft True als het leeg is en False als het niet leeg is.
       :pre-condition: Geen.
       :post-condition: Geen.

        """


    def enqueue(self, val):
        """
       :method: Voegt een element toe aan het einde van de queue.
       :input: val(classobj): het element die men wenst toe te voegen.
       :output: Geeft "True" voor succes en "False" voor mislukking.
       :pre-condition: Een lege of gevulde queue.
       :post-condition: Het gewenste element is toegevoegd aan het einde van de queue. Hierdoor kijkt de backP naar het nieuw element.

        """


    def dequeue(self):
        """
       :method: Verwijdert het eerste element van de queue.
       :input: Geen.
       :output: Geen.
       :pre-condition: Een queue met minstens 1 element.
       :post-condition: Het eerste element is verijderd waardoor frontP wijst naar de opvolger van het verwijderde element.

        """


    def getFront(self):
        """
       :method: Geeft het eerste element van de queue.
       :input: Geen.
       :output: Het eerste element van de queue.
       :pre-condition: Queue bevat minstens 1 element.
       :post-condition: Geen.

         """
class BST:          #Geimplementeerd door Giorgi Guledani
    """
   :method: Dit is een class die operaties uitvoer op de binaire zoekboom.
   :input: Geen.
   :output: Geen.
   :pre-condition: Geen.
   :post-condition: Geen.

    """
    def __init__(self):
        """
       :method: Dit is de constructor voor de class BST en maakt de root, linkerdeelboom en rechterdeelboom.
       :input: Geen.
       :output: Geen.
       :pre-condition: Geen.
       :post-condition: Een lege root, linkerdeelboom  en rechterdeelboom.

        """


    def insert(self, val):
        """
       :method: Voegt een nieuw element aan de boom.
       :input: val(classobject): Het element die men wenst toe te voegen.
       :output: Geeft "True" voor succes en "False" voor mislukking.
       :pre-condition: Een lege of gevulde binaire zoekboom.
       :post-condition: Het nieuw element is toegevoegd en is geplaatst op de plek volgens de methode van een binaire zoekboom.

        """
    def retrieve(self):
        """
        :method: Zoekt een opgegeven element en returnt deze.
        :input: key(int): 
        :pre-condition:een lege of gevulde binaire zoekboom
        :post-condition: Als het element is gevonden word deze gereturnd, zo niet word er False gereturnd.
        """

    def inorderTraversal(self):
        """
       :method: Geeft de elementen van de boom van klein naar groot weer.
       :input: Geen.
       :output: Geeft de elementen weer van klein naar groot, geeft "True" als succes en "False" voor mislukking.
       :pre-condition: Een boom met elementen.
       :post-condition: Geen.

        """
    def isEmpty(self):
        """
       :method: Toont aan of de BST leeg is of niet.
       :input: Geen.
       :output: Geeft True als het leeg is en False als het niet leeg is.
       :pre-condition: Geen.
       :post-condition: Geen.

        """

    def delete(self):
        """
        :method: Verwijdert een element uit de zoekboom.
        :input: key(int)
        :output: Geeft True als het het gelukt is en False als het niet gelukt is.
        :pre-condition: Een lege of gevulde boom.
        :post-condition: Het element is verwijdert als de operatie is gelukt.
