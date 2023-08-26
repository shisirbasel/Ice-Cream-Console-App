import sys

class ExitApp():

    def __init__(self):
        self.message="Thankyou For Using Our Application !"
        ExitApp.exitApp(self)
    
    def exitApp(self):
        sys.exit(self.message)
