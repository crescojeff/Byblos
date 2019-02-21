__author__ = 'CresCoJeff'
class AnnotatedWord(object):

    mv_sWord = "";
    mv_sWordClass = "none"

    def __init__(self,word):
        self.mv_sWord = word

    def getWord(self):
        return self.mv_sWord
    def getWordClass(self):
        return self.mv_sWordClass
    def classifyWord(self,wordclass):
        self.mv_sWordClass = wordclass