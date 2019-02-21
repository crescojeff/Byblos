__author__ = 'CresCoJeff'
'''
This fellow analyzes the individual phonemes of a word and
maps them based on training data to associated sentiment;
ex. the suffix -or in the word dominator gives a feeling of
intense finality.
Obviously this is subjective, but that's sort of the point -- it is
subjective in its details, but tends to be a shared subjectivity amongst
sophonts with similar cultural experience sets.  It would be good
to build a means by which a Galatea instance could have similar
experiential data and memories to draw upon in forming opinions,
processing feelings, and making decisions which relates back to
words and subsets of words.

Also notable, this system could be used for a badass magic system
similar to Treasure of the Rudra's Mantra system, but with
a less arbitrary and potentially more flexible system for determining
effects etc. of various individual phoneme or
prefix+base+suffix combinations.
'''
class Sentimentalist(object):

    '''
    fields
    '''
    '''
    The suffix, mid, and prefix dicts define mappings between English
    phoneme macros (ex. the sound 'or') and related sentimental connotations
    '''
    rSentimentSuffixDict = {"or":["savage","domination","conquest"],"rix":["wily","femme fatale","domination","female sexuality"]}
    rSentimentMidDict = {"ag":["force","savage","violent","final"]}

    def __init__(self):
        pass

