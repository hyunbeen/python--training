#sample11.py

class parent :
    def __init__(self):
        # super().__init__()
        pass

    def printparent(self):
        print("parent")
        pass

class child(parent):
    def __init__(self):
        # super().__init__()
        pass


childobj = child()
childobj.printparent()

