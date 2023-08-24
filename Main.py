#importing necessary files to access their functions
import Exit


#display welcome message
def welcome():
    ''' This function Prints the Welcome message of the console application'''
    print("--"*36)
    print("--"*10,end="")
    print("Welcome To The Ice Cream Parlour",end="")
    print("--"*10)
    print("--"*36)
    print("\n\n")


#display options 
def options():
    welcome()
    while True:
        print("--"*36)
        print("Please Select Your Desired Option: ")
        print("--"*36)
        print(""" 1] Purchase An Ice-Cream\n 2] Exit Application """)
        print("--"*36)

        select = input("Enter the desired option: ")

        if select =="1":
            pass
        elif select == "2":
            print("--"*36)
            Exit.exit()
        else:
            print("Please enter a Valid Input")
            print("--"*36)

        
options()

    
