# Ocak 2020 ayını baz alarak ayın kaçında hangi günde olduğumuzu söyleyen fonksiyonu yazınız



def ocak(veri):
        ay={1:"Cuma",2:"Cumartesi",3:"Pazar",4:"Pazartesi",5:"Salı",6:"Çarşamba",7:"Perşembe"}
        print(ay[veri%7])

ocak(9)