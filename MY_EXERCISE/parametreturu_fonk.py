# Klavyeden bir veri alınız ve girilen veriyi hangiTur adında bir fonksiyona parametre olarak yollayın.
# Bu fonksiyonda verinin türünü tespit edip ekrana verinin türünü basınız.

def hangiTur(veri):

    if type(veri) is str:
        print("string")
    elif type(veri) is int:
        print("integer")
    elif type(veri) is float:
        print("float")
    elif type(veri) is complex:
        print("karmaşık sayı")


hangiTur(4.2)