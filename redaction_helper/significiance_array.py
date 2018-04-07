# coding: utf8

from ngram import Ngram

"""
    A significiance array that contains the ngrams and their tf-idf value
"""
class SignificianceArray(object):

    """ contructor
    """
    def __init__(self):
        self.ngrams = {}
        self.counted_ngrams = []

    """ returns a string representation of the SignificianceArray object
    """
    def __str__(self):
        return self.ngrams

    """ generates the ngrams
    """
    def generate_ngrams(self, text, ngramslen):
        for i in range(0, len(text.body), int(ngramslen)):
            ngram = ",".join(text.body[i:i+int(ngramslen)]).lower()
            value = self.ngrams.get(ngram)
            if not value:
                self.ngrams[ngram] = 1 
            else:
                self.ngrams[ngram] = value + 1 
            # self.ngrams.append(Ngram(ngramslen, text, text.body[i:i+int(ngramslen)]))
        # self.remove_singles()

    """
    """
    def count_ngrams(self):
        pass        

    # def remove_singles(self):
    #     new_ngrams = []
    #     for ngram in self.ngrams:
    #         v = self.ngrams.pop(0)
    #         if v in self.ngrams:
    #             new_ngrams.append(v)
    #     self.ngrams = new_ngrams