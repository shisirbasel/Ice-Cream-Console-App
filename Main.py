#importing necessary files to access their functions
from Exit import ExitApp
from Purchase import IceCreamMenu


class Welcome():
    def __init__(self):
        Welcome.options(self)


    #display welcome message
    def welcome(self):
        ''' This function Prints the Welcome message of the console application'''
        print("**"*36)
        print("**"*10,end="")
        print("Welcome To The Ice Cream Parlour",end="")
        print("**"*10)
        print("**"*36,"\n")


    #display options 
    def options(self):
        Welcome.welcome(self)
        while True:
            print("\n\n\n")
            print("**"*36)
            print("Please Select Your Desired Option ")
            print("**"*36)
            print(""" 1] Purchase An Ice-Cream\n 2] Exit Application """)
            print("**"*36,"\n")

            
            select = input("Enter the desired option: ")
            print("**"*36,"\n")

            if select =="1":
                obj = IceCreamMenu()
            elif select == "2":
                print("**"*36)
                obj = ExitApp()
            else:
                print("Please enter a Valid Input")
                print("**"*36)
                print("\n\n\n\n")

        
object = Welcome()


    
