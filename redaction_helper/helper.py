# coding: utf8

import sys
import glob
import operator

from text import Text
from significiance_array import SignificianceArray

def main():
    texts = []
    sa = SignificianceArray()
    for filename in glob.glob('{dir}/*.txt'.format(dir=sys.argv[2])):
        texts.append(Text(filename))
        
    for text in texts:
        sa.generate_ngrams(text, sys.argv[1])
        
    print("Ngrams les plus présents :\n")
    s = sorted(sa.ngrams.items(), key=operator.itemgetter(1), reverse=True)
    for n in s:
        if n[1] > 2:
            print(n[0])
        
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("""
            Invalid args:
            N: The size of the ngrams
            TEXTS: The folder containing the .txt files

            python helper.py N TEXTS
        """)
        exit(1)
    main()