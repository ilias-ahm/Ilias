
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
class Node:          #Geimplementeerd door Giorgi Guledani
    """
   :method: Dit is een class die operaties uitvoer op de binaire zoekboom.
   :input: Geen.
   :output: Geen.
   :pre-condition: Geen.
   :post-condition: Geen.
    """
    def __init__(self, match):
    self.match = match



class BST:
    def __init__(self):
        self.root = None
        self.parent = None
        self.leftTree = None
        self.rightTree = None

    def isEmpty(self):
        if self.root is None:
            return True
        return False

    def retrieve(self, match):
        if self.root:
            if self.root.match == match:
                return self
            if self.root.match > match:
                if self.leftTree:
                    return self.leftTree.retrieve(match)
            if self.root.match < match:
                if self.rightTree:
                    return self.rightTree.retrieve(match)
            return print("Geen titel gevonden!")
        else:
            return "Lege boom"

    def insert(self, node):
        if self.root is None:
            self.root = node
            self.parent = None
            return
        if self.root.match == node.match:
            if self.rightTree is None:
                self.rightTree = BST()
                self.rightTree.root = node
                self.rightTree.parent = self
                return
            return self.rightTree.insert(node)

        if self.root.match > node.match:
            if self.leftTree is None:
                self.leftTree = BST() #We geven een object BST samen met het node mee aan de deelboom
                self.leftTree.root = node
                self.leftTree.parent = self #We geven hier een parent omdat we niet meer terugkeren naar de functie maar gewoon "returnen"
                return
            return self.leftTree.insert(node)

        if self.root.match < node.match:
            if self.rightTree is None:
                self.rightTree = BST()
                self.rightTree.root = node
                self.rightTree.parent = self
                return
            return self.rightTree.insert(node)

    def findBestMatch(self):
        if self.rightTree: # Als er een rechterkind is
            return self.rightTree.findBestMatch() # Dan gaan we naar het rechterkind
        return self.root # Anders zijn we klaar met zoeken

    def delete(self,match):
        toDelete = self.retrieve(match)

        if toDelete is None: # Te verwijderen node bestaat niet
            return
        if toDelete.leftTree and toDelete.rightTree:
            successor = toDelete.GetInorderSuccessor(match)
            temp = toDelete.root # We wisselen de positie van de successor en de te verwijderen node om
            toDelete.root = successor.root
            successor.root = temp
            return successor.delete(successor.root.match)

        if toDelete.rightTree: # Als er enkel een rechter deelboom is
            toDelete.root = toDelete.rightTree.root # Switchen we de node in de rechter deelboom met de te verwijderen node
            toDelete.leftTree = toDelete.rightTree.leftTree # De linker deelboom van de van rechter
            toDelete.rightTree = toDelete.rightTree.rightTree
            return

        if toDelete.leftTree: # Als er enkel een linker deelboom is
            toDelete.root = toDelete.leftTree.root
            toDelete.rightTree = toDelete.leftTree.rightTree
            toDelete.leftTree = toDelete.leftTree.leftTree
            return

        if toDelete.parent:
            if toDelete.parent.leftTree == toDelete:
                toDelete.parent.leftTree = None
            else:
                toDelete.parent.rightTree = None
            return
        self.root = None

    def GetInorderSuccessor(self, match):
        node = self.retrieve(match)
        successor = node.rightTree
        while successor.leftTree is not None:
            successor = successor.leftTree
        return successor

    def printDot(self):
        dot = "Graph G { "
        dot += "\n"
        dot += self.generateDot()
        dot += "\n"
        dot += "}"
        return dot

    def generateDot(self, count=0):
        dot = ""
        link = "--"
        newline = "\n"

        #basisgeval (eerst root)
        if not self.leftTree:
            filler = 'a' + str(randint(1,1000))
            dot += filler + ' [style ="invisible"]'
            dot += newline
            dot += str(self.root.match) + link + filler + ' [style=invis]'
            count += 1
        else:
            dot += str(self.root.match) + link
            dot += str(self.leftTree.root.match)
        dot += newline

        if not self.rightTree:
            filler = 'a' + str(randint(1,1000))
            dot += filler + ' [style ="invisible"]'
            dot += newline
            dot += str(self.root.match) + link + filler + ' [style=invis]'
            count += 1
        else:
            dot += str(self.root.match) + link + str(self.rightTree.root.match)
        dot += newline

        #recursieve stap (preorder traversal)
        if self.leftTree:
            dot += self.leftTree.generateDot()
        if self.rightTree:
            dot += self.rightTree.generateDot()

        return dot

    def inorderTraverse(self):

            res = []
            if self.leftTree is None and self.rightTree is None: # Als de node een blad is
                res.append(self.root.match)
                return res
            else:
                if self.leftTree:
                    res += self.leftTree.inorderTraverse()
                res.append(self.root.match)
                if self.rightTree:
                    res += self.rightTree.inorderTraverse()
                return res

    
#--------------------------- onderstaande code om BST te testen ---------------------------
    

def printTree(tree, curr_index, index=False, delimiter='-'):

    if tree == None or tree.root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    if index:
        node_repr = '{}{}{}'.format(curr_index, delimiter, tree.root.match)
    else:
        node_repr = str(tree.root.match)

    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = \
        printTree(tree.leftTree, 2 * curr_index + 1, index, delimiter)
    r_box, r_box_width, r_root_start, r_root_end = \
        printTree(tree.rightTree, 2 * curr_index + 2, index, delimiter)

    # Draw the branch connecting the current root node to the left sub-box
    # Pad the line with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(' ' * (l_root + 1))
        line1.append('_' * (l_box_width - l_root))
        line2.append(' ' * l_root + '/')
        line2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root node
    line1.append(node_repr)
    line2.append(' ' * new_root_width)

    # Draw the branch connecting the current root node to the right sub-box
    # Pad the line with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append('_' * r_root)
        line1.append(' ' * (r_box_width - r_root + 1))
        line2.append(' ' * r_root + '\\')
        line2.append(' ' * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = ' ' * gap_size
    new_box = [''.join(line1), ''.join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
        r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root repr positions
    return new_box, len(new_box[0]), new_root_start, new_root_end


BST = BST()

BST.insert(Node(0.8))  
BST.insert(Node(0.5))
BST.insert(Node(0.2))
BST.insert(Node(0.3))
BST.insert(Node(0.99))
BST.insert(Node(1))

BST.insert(Node(0.1))

print(BST)
BST.delete(0.8)
print(BST)
BST.delete(0.99)
BST.delete(1)
BST.delete(0.2)
BST.delete(0.1)
BST.delete(0.5)
print(BST)
BST.delete(0.3)
print(BST)
BST.insert(Node(0.5))
BST.insert(Node(0.8))
BST.insert(Node(0.3))
BST.insert(Node(0.4))
print(BST)
BST.delete(0.3)
print(BST)
