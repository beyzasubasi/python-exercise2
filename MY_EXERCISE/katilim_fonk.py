# Eğitimlerde genellikle hafta hafta katılım sayılarında düşüşler yaşanmaktadır,
# 4 haftalık bir eğitim süresince her hafta için verilen katılım sayılarına göre
# (bu katılım sayıları tuple cinsinden verilecektir.) bir haftada ortalama kaç öğrencinin
# derse katıldığını ekrana yazdıran kodu yazınız. örnek katılım sayıları(53,47,44,36)

def katilim(veri):
    ort = 0
    veri = list(veri)
    for i in range(len(veri)):
        ort = ort + veri[i]
    print(ort / len(veri))

katilim((55,12,87))