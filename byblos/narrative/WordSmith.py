__author__ = 'CresCoJeff'
'''
NLP and computation affect class that generates computational verse.
'''

import AnnotatedWord

class WordSmith(object):
    def __init__(self):
        pass

    '''
    blend returns a set of words consisting of all
    possible character permutations of the given word
    that respect the original sequence of chars.  Basically it
    varies which char starts the word and wraps the sliced
    subset onto the end
    number of perms in this manner is x where x is the char count
    Blend: length of results is char count
    ate, tea, eat
    '''
    def blend(self,word):
        saBlendedWords = []
        iWordLen = len(word)
        print "in blend word length is "+str(iWordLen)
        #for each char
        for x in range(0,iWordLen):
            newWord = word[x:]+word[:x]
            saBlendedWords.append(newWord)
            print "added blended word "+newWord
            '''
            #for each position
            for y in range(0,iWordLen):
                newWord = word[y:]+word[:y]
                saBlendedWords.append(newWord)
                print "added blended word "+newWord
            '''

        return saBlendedWords
    '''
    same as blend, except the original order is not taken
    into account; this means the permutations are actually
    x*x-1 where x is the char count.  The character uniqueness is
    still respected (e.g. no repeats)
    BlendNoOrder:
    ate,aet,eta,eat,tae,tea
    '''
    def blendNoOrder(self,word):
        saBlendedWords = []
        iWordLen = len(word)
        print "in blendNoOrder word length is "+str(iWordLen)
        #for each char
        for x in range(0,iWordLen):
            #for each position
            for y in range(0,iWordLen-1):
                newWord = word[y:]+word[:y]
                saBlendedWords.append(newWord)
                print "added blended word "+newWord


        return saBlendedWords
    '''
    blendAll returns a set of words consisting of all possible
    character permutations of all the given words concatenated into
    a single char string.
    '''
    def blendAll(self,words):
        sBlendedWord = ""

    def randPass(self,iPassLength):
        pass
    def interpretAnnotatedWord(self,anWord):
        if anWord.getWordClass == "none":
            print "class none, so nothing special"

# tests
# todo: actual unit tests w/in framework
smithy = WordSmith()
smithy.blend("ate")
smithy.blendNoOrder("ate")
