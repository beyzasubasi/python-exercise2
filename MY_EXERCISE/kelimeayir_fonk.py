#Verilen herhangi bir metni verilen parametreye göre cümlelere veya kelimelere ayıran fonksiyonu yazınız.

def ayirici(metin,hangisi=False):
    if hangisi==False:
        return metin.split(" ")
    elif hangisi==True:
        return metin.split(".")
    else:
        return "Lütfen kelime ise False, cümle ise True parametresi veriniz."

print(ayirici("Ben iyiyim. Merak etme. Git.", True)) #cümle ayırdım
print(ayirici("Ben iyiyim. Merak etme. Git.", False)) #kelime ayırdım