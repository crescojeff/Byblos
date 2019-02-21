__author__ = 'CresCoJeff'

class Cog:
    mv_sName = ""

    def __init__(self):
        print("Cog initialized")

    def setName(self,sName):
        self.mv_sName = sName

    def getName(self):
        return self.mv_sName