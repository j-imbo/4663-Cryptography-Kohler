import sys
import math
from collections import OrderedDict

# presupplied polybius code
class Polybius:
    def __init__(self,k=None):
        self.key = self.remove_duplicates(k)

        self.alphabet = [chr(x+97) for x in range(26)]
        self.adfgx = ['A','D','F','G','X']
        self.keylen = 0

        if self.key:
            self.keylen = len(self.key)

        self.polybius = None
        self.lookup = None

    def remove_duplicates(self,key):
        """ Removes duplicate letters from a given key, since they
            will break the encryption.
            Example: 
                key = 'helloworldhowareyou'
                returns 'helowrdayu'
        """
        newkey = []             # create a list for letters
        for i in key:           # loop through key
            if not i in newkey: # skip duplicates
                newkey.append(i)
        
        # create a string by joining the newkey list as a string
        return ''.join(str(x) for x in newkey)
       

    def build_polybius_string(self,key=None):
        """ Builds a string consisting of a keyword + the remaining
            letters of the alphabet. 
            Example:
                key = 'superbatzy'
                polybius = 'superbatzycdfghiklmnoqvwx'
        """
        # no key passed in, used one from constructor
        if key != None:
            self.key = self.remove_duplicates(key)

        # NO key!
        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # key exists ... continue
        self.keylen = len(self.key)

        # prime polybius_string variable with key
        self.polybius = self.key

        for l in self.alphabet:
            if l == 'j':        # no j needed!
                continue
            if not l in self.key:    # if letter not in key, add it
                self.polybius += l
        return self.polybius

    def build_polybius_lookup(self,key=None):
        """ Builds a lookup dictionary so we can get the two letter pairs for each
            polybius letter. 
            Example:
                key = superbatzy
                polybius = superbatzycdfghiklmnoqvwx
                lookup = 
                {'a': 'DD',
                'b': 'DA',
                'c': 'FA',
                'd': 'FD',
                'e': 'AG',
                'f': 'FF',
                'g': 'FG',
                'h': 'FX',
                'i': 'GA',
                'k': 'GD',
                'l': 'GF',
                'm': 'GG',
                'n': 'GX',
                'o': 'XA',
                'p': 'AF',
                'q': 'XD',
                'r': 'AX',
                's': 'AA',
                't': 'DF',
                'u': 'AD',
                'v': 'XF',
                'w': 'XG',
                'x': 'XX',
                'y': 'DX',
                'z': 'DG'}
        """
        if key != None:
            self.key = self.remove_duplicates(key)

        # NO key!
        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # no polybius built, make one!
        if self.polybius == None:
            self.build_polybius_string()

        # init our dictionary
        self.lookup = {}            # dict as our adfgx reverse lookup
        for l in self.polybius:     # loop through the 1D matrix we created
            self.lookup[l] = ''     # init keys in the dictionary

        row = 0 
        col = 0

        # loop through the polybius 1D string and get the 2 letter pairs
        # needed to do the initial encryption
        for row in range(5):
            for col in range(5):
                i = (5 * row) + col
                self.lookup[self.polybius[i]] = self.adfgx[row]+self.adfgx[col]

        return self.lookup


    def sanity_check(self):
        """ This method lets you look at an actual "matrix" that you built using 
            a keyword. 
            Example: 
                key = 'superbatzy'
                output = 
                      A D F G X 
                    A s u p e r 
                    D b a t z y 
                    F c d f g h 
                    G i k l m n 
                    X o q v w x 
            This is not what you would use to encrypt!! Its only a sanity check
            meaning that it visualizes the lookup table just to see proof it's correct.
        """

        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # no polybius built, make one!
        if self.polybius == None:
            self.build_polybius_string()

        row = 0
        col = 0
       
        sys.stdout.write('\n  ')
        for l in self.adfgx:
            sys.stdout.write(l+' ')
        sys.stdout.write('\n')
        for l in self.adfgx:
            sys.stdout.write(l+' ')
            for ll in self.adfgx:
                i = (5 * row) + col
                sys.stdout.write(self.polybius[i]+' ')
                col += 1
            row += 1
            col = 0
            sys.stdout.write("\n")

def makeADFGXstring(instr,poly):
    # turn input string into ADFGX format
    instr = instr.lower()
    outstring = ""
    alpha = [chr(x+97) for x in range(26)]
    for char in instr:
        if (char not in alpha):
            pass
        elif (char == "j"):
            outstring += poly['i']
        else:
            outstring += poly[char]

    return outstring    

def fractionate(poly,k):
    key = []
    for char in k:
        key.append(char)

    # form matrix
    adfgx = {k:[] for k in key}
    i = 0
    for p in poly:
        adfgx[k[i]].append(p)
        i += 1
        i = i % len(k)

    # turn matrix into fractionated string for return
    outstring = ""
    for ky in sorted(k):
        for a in adfgx[ky]:
            outstring += a

    return outstring

def defrac(adfgx,k):
    key = list(k)

    # create empty dictionary for defractionting
    ind = sorted(range(len(key)), key=lambda k: key[k])
    mat = list(ind)

    # determine short columns and column length
    shorts = len(adfgx) % len(k)
    collen = int(math.ceil(len(adfgx) / len(k)))

    # reconstruct matrix
    lf = 0
    rt = 0
    for ky, vl in enumerate(ind):
        rt = lf
        rt += collen
        if shorts > 0 and vl > shorts-1:
            rt -= 1
        mat[vl] = adfgx[lf:rt]
        lf = rt

    # turn matrix into string
    i = 0
    j = 0
    outstring = ""
    for each in range(len(adfgx)):
        outstring += mat[i][j]
        i += 1
        if i == len(k):
            i = 0
            j += 1
    
    return outstring

def depoly(poly,strng):
    # turn each letter pair into a single letter using polybius
    pollook = poly.build_polybius_lookup()
    polrev = {v:k for k,v in pollook.items()}
    outstring = ""
    i = 0
    for x in range(int(len(strng)/2)):
        adfgx = strng[i] + strng[i+1]
        letter = polrev[adfgx]
        outstring += letter
        i += 2

    return outstring

def main():
    with open(sys.argv[1],"r") as infile:
        inpt = infile.read()
        inpt = inpt.replace(" ","")
    key1 = sys.argv[2]
    key2 = sys.argv[3]

    if (sys.argv[4] == "encrypt"):
        mode = 1
    elif (sys.argv[4] == "decrypt"):
        mode = 2
    else: 
        print("Invalid mode argument.")

    poly = Polybius(key1)
    pollook = poly.build_polybius_lookup()

    if (mode==1): # encrypt
        polsq = makeADFGXstring(inpt,pollook)
        output = fractionate(polsq,key2)
    elif (mode==2): # decrypt
        depol = defrac(inpt,key2)
        output = depoly(poly,depol)

    print(output)


if __name__ == "__main__":
    main()
