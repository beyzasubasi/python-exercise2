"""
b)String’leri küçük harfle yazılanlar önce gelecek şekilde düzenleyen bir program kodu yazınız.

Girdi:
str1 = PyNaTive
Çıktı:
yaivePNT
"""

str1 = "PyNaTive"
lower = []
upper = []

for char in str1:
    if char.islower():
        lower.append(char)

    else:
        upper.append(char)

sorted_string = ' '.join(lower+upper)
print(sorted_string)