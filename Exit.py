import sys

class Exit():

    def __init__(self):
        self.message="Thankyou For Using Our Application !"
        Exit.exitApp(self)
    
    def exitApp(self):
        sys.exit(self.message)
