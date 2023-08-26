class PurchaseCone:
    
    def validateCone(self,num):
        loop = True
        while loop == True:
            try:
                id = int(input("Enter the ID of the Cone that you want to purchase: "))
                print("**" * 36, "\n")

                if 0 < id <= num:
                    Y = True
                    while Y == True:
                        print("**" * 36)
                        try:
                            cone = int(input("How many Cones do you want? "))
                            print("**" * 36, "\n")
                            if cone > 0:
                                Y = False
                                loop = False
                                cone_list.append([id,cone]) # Corrected the list to tuple append
                            else:
                                print("Invalid Input! Please try Again")
                        except:
                            print("Invalid Input! Please try Again")
                else:
                    print("Invalid Input! Please try Again")
            except:
                print('Invalid Input! Please try Again') 


class ConeMenu(PurchaseCone):

    def __init__(self):
        ConeMenu.coneShow(self)
    
    def coneTable(self):
        print("**"*36)
        print("ID\t\t\tCone\t\t\t\tPrice")
        print("**"*36)

    def coneShow(self):
        ConeMenu.coneTable(self)
        number = 0
        file = open("cones.csv", "r")
        cones = file.read()
        cones = cones.split("\n")
        cones.pop()

        for i in range(len(cones)):
            number = number + 1
            cone_data = cones[i].split(",")
            cone_dictionary[number] = cone_data

        for key, value in cone_dictionary.items():
            print(key, end="\t\t\t")
            for i in value:
                print(i, end="\t\t\t")
            print("\n")
        print("**" * 36)
        print("**" * 36, "\n")
        ConeMenu.validateCone(self,number)
        loop = True
        while loop == True:
            question = input("Do you want to buy more cone?(y/n): ").lower()
            print("**"*36,"\n")
            if question == "y":
                ConeMenu.validateCone(self,number)
            elif question == "n":
                    loop = False
                    Bills.bill(self)
            else:
                print('Invalid Input!! Please Try Again! ')

class PurchaseIceCream:
    global icecream_list 
    icecream_list=[]
    global icecream_dictionary
    icecream_dictionary= {}
    global cone_list 
    cone_list= []
    global cone_dictionary
    cone_dictionary={} 
    def validateIcecream(self, num):
        loop = True
        while loop == True:
            try:
                id = int(input("Enter the ID of the Ice Cream that you want to purchase: "))
                print("**" * 36, "\n")

                if 0 < id <= num:
                    Y = True
                    while Y == True:
                        print("**" * 36)
                        try:
                            scoop = int(input("How many Scoops do you want? "))
                            print("**" * 36, "\n")
                            if scoop > 0:
                                Y = False
                                loop = False
                                icecream_list.append([id,scoop]) # Corrected the list to tuple append
                            else:
                                print("Invalid Input! Please try Again")
                        except:
                            print("Invalid Input! Please try Again")
                else:
                    print("Invalid Input! Please try Again")
            except:
                print('Invalid Input! Please try Again')
                
class IceCreamMenu(PurchaseIceCream,ConeMenu):
    def __init__(self):
        IceCreamMenu.icecreamShow(self)
    

    def iceCreamTable(self):
        print("**"*36)
        print("ID\t\t\tIce-Cream\t\tPrice/Scoop")
        print("**"*36)

    def icecreamShow(self):
        IceCreamMenu.iceCreamTable(self)
        number = 0
        file = open("icecream.csv","r")
        icecreams = file.read()
        icecreams = icecreams.split("\n")
        icecreams.pop()

        for i in range(len(icecreams)):
            number = number + 1
            icecream_dictionary[i+1] = icecreams[i].split(",")
        
        for key,value in icecream_dictionary.items():
            print(key,end="\t\t\t")
            for i in value:
                print(i,end="\t")
            print("\n")
        print("**"*36)
        print("**"*36,"\n")
        IceCreamMenu.validateIcecream(self, number)
        loop = True
        while loop == True:
            
            question = input("Do you want to buy more ice cream?(y/n): ").lower()
            print("**" * 36, "\n")

            if question == "y":
                IceCreamMenu.validateIcecream(self, number)
            elif question == "n":
                loop = False
            else:
                print("Please Enter a valid Input")

        loop1 = True
        while loop1 == True:
            question = input("Do you want to buy cone?(y/n): ").lower()
            if question == "y":
                IceCreamMenu.coneShow(self)
                loop1 = False
            elif question == "n":
                Bills.bill(self)
                loop1 = False
            else:
                print("Please Enter a valid Input")


class Bills:

    def bill(self):
        import datetime
        icecreamtotal = 0
        contestotal = 0
         # Initialize the total
        date = datetime.datetime.now()
        print("**" * 36)
        name = input("Enter your name: ")
        while True:
            try:
                print("**" * 36)
                contact = int(input("Enter your contact number: "))
                break
            except:
                print("Phone number must be numeric! ")
            
        
        print("\n\n")
        print("**" * 36)
        print("**" * 12, end="")
        print("Ice-cream Parlour Bill", end="")
        print("**" * 13)
        print("**" * 36, "\n")
        print("Date: ", date)
        print("Name: ", name)
        print("Contact: ", contact)

        print("**" * 36)
        print("ID\tItem\t\t\t\tPrice\t\tquantity")
        print("**" * 36)

        counter = 0
        for i in range(len(icecream_list)):
            id = int(icecream_list[i][0])
            icecreamscoop = int(icecream_list[i][1])
            name = icecream_dictionary[id][0]
            price = float(icecream_dictionary[id][1])
            icecreamtotal += price * icecreamscoop
            counter += 1

            print()
            print(counter, "\t", name,"\t",price, "\t\t", icecreamscoop)
        

        for i in range(len(cone_list)):
            counter+=1
            id = int(cone_list[i][0])
            cone= int(cone_list[i][1])
            name = cone_dictionary[id][0]
            price = float(cone_dictionary[id][1])
            contestotal += price * cone

            print()

            print(counter, "\t", name, "\t\t\t",price, "\t\t", cone)

        icecream_list.clear()
        cone_list.clear()

        print("**" * 36)
        grandtotal = icecreamtotal + contestotal
        print("\t\t\t\t\tGrand Total= Rs",grandtotal)
        print("**" * 36)

        
        





        











