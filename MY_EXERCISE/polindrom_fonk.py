#Verilen herhangi bir kelimenin palindrom olup olmadığını söyleyen fonksiyonu yazınız.

def palindrom(kelime):
    if(kelime==kelime[::-1]):
        return "palindrom"
    else:
        return "palindrom değildir"

print(palindrom("beyz"))