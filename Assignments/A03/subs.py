
def subs():

    # list of letters
    alphabet = [chr(x+97) for x in range(26)]
    
    inf = input("Enter name of file to decrypt:\n")
    keyf = input("Enter name of file with key:\n")
    n = input("Enter number for file postfix:\n")
    
    # list of letters to substitute
    with open(keyf,"r") as key:
        subs = key.readline()

    # input text
    with open(inf,"r") as infile:
        text = infile.readline()
    text.lower()

    # output file
    f = open("decrypted_" + n + ".txt","w")

    # performs the substitution
    for p in text:
        i = ord(p)-97
        if p in alphabet:
            i = ord(p)-97
            f.write(subs[i])
        else:
            f.write(p)

subs()