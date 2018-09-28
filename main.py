

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
            self.printLists()
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
    #Functional. Adds a new contact to the list.
    #Allows user to quit the process midway.
    bigLoop = True
    flag = True
    yesNo = ''
    id = 0
    name = ''
    address = ''
    while bigLoop:
        flag = True
        while flag:
            yesNo = input("\n\nDo you want to add a new contact?  Y/N or QUIT\t").upper()
            if yesNo in ['Y','YES']:
                print("\nYou want to add a contact.\n")
                flag = False
            elif yesNo in ['N','NO']:
                print("\nYou don't want to add a new contact.\n")
                flag = False
                bigLoop = False
            elif yesNo in ['Q','QUIT']:
                print("\nExiting.\n")
                flag = False
                bigLoop = False
            else:
                flag = True

        if ((yesNo in ['Y', 'YES']) and bigLoop):
            flag = True
            yesNo = ''
            print("""
            Please enter new contact info in using the following guidelines:
            ID: 123456\t**ID must be a 6-digit number, exactly. No leading zeroes allowed.
            Names should NOT include middle names. First and last names only. 
            Program will accept incorrect formatting. Please use caution.
            """)
            while flag:
                try:
                    id = int(input("\nPlease enter 6-digit ID number: "))
                    yesNo = input("\nIs this correct? Y/N or QUIT").upper()
                    if yesNo in ['Y','YES']:
                        id = str(id)
                        if len(id) != 6:
                            #Currently, this doesn't allow leading zeroes. If led with a zero, the number will be less than 6 digits
                            print("\nActually, your ID number is too short. It must be exactly 6 digits.\nTry again...")
                        else:
                            flag = False
                    elif yesNo in ['N', 'NO']:
                        print("\nTry again...\n")
                        flag = True
                    elif yesNo in ['Q', 'QUIT']:
                        print("\nExiting.\n")
                        flag = False
                        bigLoop = False
                    else:
                        flag = True
                except (ValueError):
                    print("\nOops. That input was invalid. Try again.\n")

            flag = True
            if bigLoop == False:
                flag = False
            while flag:
                try:
                    Fname = input("\nPlease enter contact's first name: ")
                    Lname = input("\nPlease enter contact's last name: ")
                    yesNo = input("\nIs this correct? Y/N or QUIT").upper()
                    if yesNo in ['Y','YES']:
                        if ((len(Fname) < 2) or (len(Lname) < 2)):
                            print("\nIsn't that too short for a full name? Try again...")
                        elif not (Fname.isalpha() and Lname.isalpha()):
                            #This statement isn't accepting ANY responses. Thinks all responses are invalid.
                            print("\nOnly alphabet characters allowed. Try again...")
                        else:
                            name = Lname + ',' + Fname
                            flag = False

                    elif yesNo in ['N', 'NO']:
                        print("\nTry again...\n")
                        flag = True
                    elif yesNo in ['Q', 'QUIT']:
                        print("\nExiting.\n")
                        flag = False
                        bigLoop = False
                    else:
                        flag = True
                except (ValueError):
                    print("\nOops. That input was invalid. Try again.\n")

            flag = True
            if bigLoop == False:
                flag = False
            while flag:
                try:
                    print("""\nPlease enter the contact's street address. Example:
                    Street number and name: 900 Westchester Rd
                    City: Grosse Pointe Park
                    State: MI
                    Zipcode: 48230 """)
                    street = input("\nStreet number and name: ")
                    city = input("\nCity: ")
                    state = input("\nState: ")
                    zip = input("\nZipcode: ")
                    yesNo = input("\nIs this all correct? Y/N or QUIT ").upper()
                    if yesNo in ['Y', 'YES']:
                        address = street + ',' + city + ',' + state + ' ' + zip
                        if len(state) != 2:
                            print("\nPlease enter the state as an abbreviation.\nExample: TX , TN, MI, FL")
                        if len(address) < 15:
                            print("\nIsn't that too short for a full address? Try again...")
                        else:
                            flag = False
                    elif yesNo in ['N', 'NO']:
                        print("\nTry again...\n")
                        flag = True
                    elif yesNo in ['Q', 'QUIT']:
                        print("\nExiting.\n")
                        flag = False
                        bigLoop = False
                    else:
                        flag = True
                except (ValueError):
                    print("\nOops. That input was invalid. Try again.\n")

            flag = True
            if bigLoop == False:
                flag = False
            while flag:
                print("""\nThis is the contact you added:
                ID: {}
                Name: {}
                Address: {}""".format(id,name,address))
                yesNo = input("\nIs this all correct? Y/N or QUIT").upper()
                if yesNo in ['Y','YES']:
                    print("\nOkay, adding contact to the list.")
                    Person.add(id,name,address,"Y")
                    flag = False
                    bigLoop = False
                elif yesNo in ['N','NO']:
                    print("\nOkay, lets try re-entering ALL of that information.\nBe careful with input this time.")
                    flag = False
                elif yesNo in ['Q','QUIT']:
                    print("\nExiting.\n")
                    flag = False
                    bigLoop = False
                else:
                    flag = True








headerText()
contactList = Person()
readData(contactList)
contactList.printLists()
new_contact(contactList)



