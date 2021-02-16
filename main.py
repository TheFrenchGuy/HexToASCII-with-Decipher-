import string  ##Necessary for ascii to cipher

letterGoodness = dict(zip(string.ascii_uppercase,
                          [.0817, .0149, .0278, .0425, .1270, .0223, .0202,
                           .0609, .0697, .0015, .0077, .0402, .0241, .0675,
                           .0751, .0193, .0009, .0599, .0633, .0906, .0276,
                           .0098, .0236, .0015, .0197,
                           .0007]))  # https://en.wikipedia.org/wiki/Letter_frequency for how used are each letters in the dicationaries

translatedTable = [str.maketrans(string.ascii_uppercase,
                                 string.ascii_uppercase[i:] + string.ascii_uppercase[:i])
                   for i in range(26)]  # Aka there is 26 letters in the alphabet


def hex_to_ascii(hex_str):  # First translate the hex to ascii
    ascii_str = bytearray.fromhex(hex_str).decode()
    return ascii_str


def goodness(msg):  ##So that it returns the most english message (HAHAHAH so funny because its me)
    return sum(letterGoodness.get(char, 0) for char in msg)  ##Evalutate all of the char each by one


def shiftBy(msg):
    msg = msg.upper()  ##So that all the characters have been upcase
    for trans_table in translatedTable:
        txt = msg.translate(trans_table)
        yield goodness(txt), txt


hex = '47 79 20 6c 67 78 20 67 79 20 63 6b 20 71 74 75 63 20 7a 6e 6b 78 6b 20 6f 79 20 74 75 20 4d 20 6f 74 20 6e 6b 64 6f 6a 6b 69 6f 73 67 72'  # The Hex you have provided to us!

translated_ascii = hex_to_ascii(hex)
##print('ascii result is:{0}'.format(translated_ascii))

print(max(shiftBy(translated_ascii)))
