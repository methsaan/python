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
    alphabet = atbashlist("")
    for x in range(len(encryptAlpha)):
        decrypt.append(atbashAlpha[alphabet.index(encrypt[x])])
    return ''.join(decrypt)

kw = input("Enter keyword: ")
encrypt = input("Enter word to encrypt: ")
print(atbashDecrypt(kw, encrypt))
