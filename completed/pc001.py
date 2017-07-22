import string

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def decrypt(text):
    length = len(text)
    counter = 0
    result = ""

    while counter < length:
        c = text[counter]

        if not str.isalpha(c):
            result += c
        else:
            result += str(chr(ord(c) + 2))

        counter = counter + 1

    print(result)

decrypt(text)
decrypt("map")