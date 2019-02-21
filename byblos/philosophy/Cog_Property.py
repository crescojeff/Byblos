class Cog_Property:

    mv_sName = ""


    def __init__(self):
        print("CogProp initialized")

    def setName(self,sName):
        self.mv_sName = sName

    def getName(self):
        return self.mv_sName