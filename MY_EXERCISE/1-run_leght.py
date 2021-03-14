"""
input_text= 'aaaaaaaabbbbbbcc'
a8 b6 c2 şeklinde harf sayılarını çıktı versin
"""
input_text= 'aaaaaaaabbbbbbcc'
text_list=list(input_text)
lenght=len(text_list)

#harflerin neler olduğunu bilmiyorsam
karakter_sayisi=1
i=0
while i<lenght-1:
    once=input_text[i]
    i+=1
    sonra=input_text[i]

    if(once==sonra):
        karakter_sayisi+=1
        if(i==lenght-1):
            print(once,karakter_sayisi)
    else:
        print(once,karakter_sayisi)
        karakter_sayisi=1
        if(i==lenght-1):
            print(sonra,karakter_sayisi)















#x=input_text.find('a') kaçıncı indexte bulunduğunu söyler
#print(x)

""" eğer harflerin neler olduğunu biliyorsam bu şekilde bulurum
text_list=list(input_text)
print(text_list)
counta=0
countb=0
countc=0

for i in(text_list):
    if(i=='a'):
        counta+=1
    elif(i=='b'):
        countb+=1
    elif(i=='c'):
        countc+=1

print("a:", counta, "b:", countb, "c:", countc)
"""



