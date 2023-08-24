class Menu():

    def __init__(self):
        self.icecreamlist =[]
        self.dictionary = {}
        Menu.icecream(self)

    def iceCreamTable(self):
        print("**"*36)
        print("ID\t\t\tIce-Cream\t\t\tPrice/Scoop")
        print("**"*36)


    def icecream(self):
        Menu.iceCreamTable(self)
        number = 0
        file = open("icecream.csv","r")
        icecreams = file.read()
        icecreams = icecreams.split("\n")
        icecreams.pop()

        for i in range(len(icecreams)):
            number = number + 1
            self.dictionary[i+1] = icecreams[i].split(",")
        
        for key,value in self.dictionary.items():
            print(key,end="\t\t\t")
            for i in value:
                print(i,end="\t")
            print("\n")
        print("**"*36)
        print("**"*36)



