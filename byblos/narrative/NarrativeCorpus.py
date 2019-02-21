__author__ = 'CresCoJeff'
'''
The set of words the AI has associated with knowledge
representation, specifically related to sentiment data,
indexed by part of speech.

Ex. You wish to find what Verbs are associated with Anger?
Simply look it up via
getSentimentPOSStringVectorMapsMap()[Anger][Verb] which will
return a set of words as strings that are verbs and associated with
the sentiment anger.
todo: less cringey API
'''

from PartOfSpeech import PartOfSpeech

class NarrativeCorpus(object):

    #establish our mapping of POS objects to string vectors
    #and our mapping of Sentiment objects to the aforementioned
    #POS:strings map
    mv_POSStringVectorMap = {'default':{'default'}}
    mv_rSentimentPOSStringVectorMapsMap = {'default':{'default':'default'}}

    def getSentimentPOSStringVectorMapsMap(self):
        return self.mv_rSentimentPOSStringVectorMapsMap
    def getPOSStringVectorMap(self):
        return self.mv_POSStringVectorMap
    def associateStringVectorWithPOS(self,pos,stringVector):
        self.mv_POSStringVectorMap[pos] = stringVector
    def associatePOSStringVectorMapWithSentiment(self,sentiment,posStringVectorMap):
        self.mv_rSentimentPOSStringVectorMapsMap[sentiment] = posStringVectorMap
