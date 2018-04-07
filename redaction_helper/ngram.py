# coding: utf8

"""
    A ngram object which represents two words
"""
class Ngram(object):

    """ contructor
        n: the length of the ngram
        text: the text from where the words come
        words: a list containing the words
    """
    def __init__(self, n, text, words):
        self.n = n
        self.text = text
        self.words = words

    """ returns a string representation of the ngram
    """
    def __str__(self):
        return "{}".format(self.words)
        
    # """ returns a tuple with the two words
    # """
    # def get(self):
    #     return (self.w1, self.w2)