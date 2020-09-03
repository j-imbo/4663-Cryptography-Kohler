import sys
import os
import string
from decimal import Decimal, getcontext

def freqs():
    
    getcontext().prec = 7
    freq = [Decimal('0')] * 26  # letter frequency
    counter = 0                 # total letter counter
    occur = [0] * 26            # letter occurences
    
    # standard frequency of each letter in English text:
    distrib = ['0.0651738', '0.0124248', '0.0217339', '0.0349835', '0.1041442', '0.0197881', '0.0158610', '0.0492888', '0.0558094', '0.0009033', '0.0050529', '0.0331490', '0.0202124', '0.0564513', '0.0596302', '0.0137645', '0.0008606', '0.0497563', '0.0515760', '0.0729357', '0.0225134', '0.0082903', '0.0171272', '0.0013692', '0.0145984', '0.0007836']
    
    args = input("Enter name of file to analyze frequency:\n")

    # read through input
    with open(args,"r") as infile:
        cypher = infile.readline()
    cypher.lower() # ensure all characters are lowercase

    # count letters
    for char in cypher:
        if (ord(char) > 96 and ord(char) < 123):
            occur[(ord(char)-97)] += 1
            counter += 1

    # turn occurences into frequence
    for i in range(26):
        freq[i] = occur[i] / counter
        freq[i] = round(freq[i],7)
    getcontext().prec = 7

    # output frequency data
    temp = os.path.splitext(args)
    outname = temp[0] + "_freq.txt"
    with open(outname,"w+") as outfile:
        print("Letters  |Std Dstrb|CyphDstrb|Std %|Cyph %",file=outfile)
        for i in range(26):
            print("    " + string.ascii_lowercase[i] + "    |" + str(distrib[i]) + "|"
                + "{0:.7f}".format(freq[i]) + "|" + "{0:>5.2f}".format(Decimal(distrib[i])*100) + "|"
                + "{0:>5.2f}".format(freq[i]*100), file=outfile)

freqs()
