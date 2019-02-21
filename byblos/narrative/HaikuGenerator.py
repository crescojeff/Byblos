__author__ = 'CresCoJeff'
'''
This fellow uses NarrativeCorpus and the various Galatea.Personality
modules to generate expressive Haiku

Seed strings and emotions can be optionally passed in to influence the output

NOTE: since we're more about AI than NLP, these Haiku will likely
be aproximate, e.g. syllables will be counted by counting vowels rather than
vowel sounds.  Shut up.
'''

class HaikuGenerator(object):

    sSeedWords = [""]
    rSeedSentiment = -1 #this will be re-typed to an emotion later if specified by caller

    def __init__(self):
        pass

    def setSeedWords(self,words):
        sSeedWords = words
    def setSeedSentiment(self,sentiment):
        rSeedSentiment = sentiment


