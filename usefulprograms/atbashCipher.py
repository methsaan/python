#! /usr/bin/python3

def strToList(string):
    return [string[i:i+1] for i in range(0, len(string), 1)]

def atbashlist(keyword):
    keywordAlpha = strToList(keyword)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for x in range(26-len(keyword)):
        if alphabet[x] in keywordAlpha:
            del alphabet[x]
    alphabetCipher = keywordAlpha + alphabet
    return alphabetCipher

def atbashDecrypt(keyword, encrypt):
    encryptAlpha = strToList(encrypt)
    decrypt = []
    atbashAlpha = atbashlist(keyword)
    for x in range(len(encryptAlpha)):
        decrypt.append(atbashAlpha[encryptAlpha.index(encrypt[x])])
    return decrypt

print(atbashlist(""))
print(atbashlist("hello"))
print(atbashDecrypt("hello", "the boat and the by you float right by you"))
