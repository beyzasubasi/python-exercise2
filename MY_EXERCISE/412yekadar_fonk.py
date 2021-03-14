#Klavyeden 412 sayısı girilene kadar veri alıp alınan bu verileri tek bir satırda arasına boşluk koyarak yazdırınız.

def surekli():
    st=""
    while True:
        if input()=="412":
            break
        else:
            st=st+" "+input()
    print(st)

surekli()