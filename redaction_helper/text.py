# coding: utf8

import re

"""
    A text object
"""
class Text(object):

    chars_to_remove = ",.;1234567890'\"&$€£%*!?:/\\-+<>\n«»”“()•"
    words_to_remove = ['the', 'of', 'for', 'a', 'by', '', 'that']
    

    """ contructor
        filename: the name of the file
    """
    def __init__(self, filename):
        self.filename = filename
        self.read_file()


    """ returns a string representation of the Text object
    """
    def __str__(self):
        return "{} :\n{}".format(self.filename, ''.join(self.body))


    """ reads and saves the text contained by the file into self.text  
    """
    def read_file(self):
        with open(self.filename, "r") as file:
            self.body = file.read()
        self.clean()


    """ cleans the text
        removes the characters contained in chars_to_remove vars
        removes everything in braces [*] (not sure if it's a good idea)
    """
    def clean(self):
        for char in self.chars_to_remove:
            self.body = self.body.replace(char, " ")
        self.body = re.sub(r'\[(.*)\]', r'', self.body.rstrip())
        
        self.body = self.body.split(" ")
        for i, word in enumerate(self.body):
            if len(word) <= 2:
                self.body.pop(i)
                
        for i, word in enumerate(self.body):
            if word.lower() in self.words_to_remove:
                self.body.pop(i)