
class Person():
    def __init__(self):
        self.idList = []
        self.nameList = []
        self.addressList = []

    def __str__(self):
        return "ID: {}\nName: {}\nAddress: {}\n".format(self.idList,self.nameList,self.addressList)

    def printLists(self):
        #functional member
        i = 0
        print("\n\nPrinting the full contacts list:\n")
        print("{:10} {:20} {:20}".format("ID #:","Name:","Address"))
        print("-"*46)
        while i < len(self.idList):
            print("{:10} {:20} {:20}".format(self.idList[i],self.nameList[i],self.addressList[i]))
            i +=1

    def add(self,id,name,address,show="N"):
        #functional member
        self.idList.append(id.strip())
        self.nameList.append(name.strip())
        self.addressList.append(address.strip())

        if show.upper() == "Y":
            print("\n\nContact Added:\nID #: {}\nName: {}\n Address: {}\n".format(self.idList,self.nameList,self.addressList))
        else:
            pass


def headerText():
    #functional
    print("""
    Answer all Y/N questions with a single letter Y or N.
    The program will first read the current addresses from a file.
    When the user inputs an address, the street name must be one word with no spaces.
    """)

def readData(Person):
    #functional
    file = open("ContactList.txt","r")
    print("\n\nLoading external contacts list....\n")
    id = ''
    name = ''
    address = ''
    for line in file:
        if line != ' ':
            id = line
            name = file.readline()
            address = file.readline()
            file.readline() #read the expected blank space

            Person.add(id,name,address)
        else:
            continue
    print("Contacts List loaded.\n")
    file.close()

def new_contact(Person):
    #Currently not functional
    flag = True
    yesNo = ''
    while flag:
        yesNo = input("\n\nDo you want to add a new contact?  Y/N\t").upper()
    
		if yesNo in ['Y','YES']:
			print("\nYou want to add a contact.\n")
			flag = False
		elif yesNo in ['N','NO']:
			print("\nYou don't want to add a new contact.\n")
			flag = False
		elif yesNo in ['Q','QUIT']:
		print("\nExiting.\n")
			flag = False
		else:
			flag = True




headerText()
contactList = Person()
readData(contactList)
contactList.printLists()
new_contact(contactList)



