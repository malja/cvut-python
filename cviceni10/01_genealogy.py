import sys

def loadFile( filename ):

    people = []

    with open( filename ) as file:
        for line in file:
            line = line.replace("\n", "").split(" ")

            print(line)

            if len( line ) != 5:
                return False
            people.append( line )

    return people

class Person:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex   
        self.children = []  
        self.parents = []   #parents of this node
        self.partner = None   #partner (=husbad/wife of this node)
 
    def addChild(self, node):
        self.children.append(node)
 
    def addParent(self, node):
        self.parents.append(node)
    def addPartner(self, node):
        self.partner = node
 
    def __repr__(self):
        s = "Male"
        if (self.sex == 'F'):
            s = "Female"
        return self.name + " " + s
 
    def isChildren(self):
        return len(parents) > 0

class Tree:
    def __init__( self ):
        self.people = []
        self.root = None

    def getPersonByName( self, name ):
        for person in self.people:
            if person.name == name:
                return person
        
        return None

    def add( self, name, sex ):
        person = self.getPersonByName( name )

        if person == None:
            self.people.append( Person( name, sex ) )
            return self.people[-1]

        return person

    def setRelationship( self, name1, name2 ):
        person1 = self.getPersonByName( name1 )
        person2 = self.getPersonByName( name2 )

        if person1 == None or person2 == None:
            return None

        # Trochu slušnosti, lidi!
        if person1.sex == person2.sex:
            return False

        person1.addPartner( person2 )
        person2.addPartner( person1 )
        return True

    def getAllGrandsons( self, name ):
        grandsons = []
        person = self.getPersonByName( name )

        if person != None:
            for child in person.children:
                for grandchild in child.children:
                    if grandchild.sex == "M":
                        grandsons.append( grandchild )
        else:
            return None

        return grandsons


data = loadFile( sys.argv[1] )

tree = Tree()

for record in data:
    # Pokud jde o záznam manželů
    if record[0] == "M":
        tree.add( record[1], record[3] )
        tree.add( record[2], record[4] )

        state = tree.setRelationship( record[1], record[2] )
        if state == None:
            print("Osoby neexistují, nejdřív je vložte")
            exit()
        elif state == False:
            print("Trochu slušnosti, lidi!")
            exit()

    # Pokud jde o záznam rodičovství
    elif record[0] == "P":

        # Rodič
        parent = tree.add( record[1], record[3] )
        # Potomek
        child = tree.add( record[2], record[4] )

        # Pridání rodičovství
        parent.addChild( child )
        child.parents.append( parent )
    
    else:
        print("ERROR")
        exit()

print( tree.getAllGrandsons("Jana") )






    

    
    