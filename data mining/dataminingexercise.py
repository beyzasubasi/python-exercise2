#Belge başına toplam kelimeyi saymak için TF hesaplamalıyız
#Her kelimenin ne kadar nadir olduğunu tanımlamak için IDF hesaplamalıyız

#import pandas as pd
import math

text=["duran duran sang wild boys in 1984","wild boys don't remain forever wild","who brought wild flowers","it was john krakauer who wrote in to the wild"]

""" 
#önce cümlelerimi ayırmak istedim
textSplit=[word for line in text for word in line.split(",")]
print(textSplit)

#ÇIKTISI:
#['duran duran sang wild boys in 1984', "wild boys don't remain forever wild", 'who brought wild flowers','it was john krakauer who wrote in to the wild']


text0="duran duran sang wild boys in 1984"
text1="wild boys don't remain forever wild"
text2="who brought wild flowers"
text3="it was john krakauer who wrote in to the wild"


#liste görünümünde çıktı almak istediğim için ayırdığım cümlelerdeki kelimeleri birleştirip listeye atıyorum

textlist=[]
total= set(text0).union(set(text1)).union(set(text2)).union(set(text3))
for i in total:
    textlist.append(i)
    
print(textlist)

#ÇIKTISI:
#['to', 'john', 'krakauer', 'the', 'remain', 'wrote', 'forever', 'flowers', 'boys', 'wild', 
#'in', 'it', 'brought', 'sang', '1984', 'who', 'was', 'duran', "don't"]

"""

#listemi yukarıdaki şekilde bastırıyorum fakat terimler karışık geldiği için sıralamada sorun çıkmaması için cümleleri ayırmadan sırayla yazdıracağım
textlist= [word for line in text for word in line.split()]
print(textlist)


"""

#hangi cümlede kaçar tane geçtiğini gösteriyorum en başta cümlelerimi bu yüzden ayırmıştım
wordDictText0 = dict.fromkeys(total, 0)
wordDictText1 = dict.fromkeys(total, 0)
wordDictText2 = dict.fromkeys(total, 0)
wordDictText3 = dict.fromkeys(total, 0)

#tablolayarak kaçar tane olduklarını gösterdim
pd.DataFrame([wordDictText0, wordDictText1, wordDictText2, wordDictText3])

in	the	was	wild	1984	duran	who	sang	boys	krakauer	john	forever	it	wrote	to	don't	flowers	remain	brought

0.cümle	1	0	0	1	1	2	0	1	1	0	0	0	0	0	0	0	0	0	0
1.cümle	0	0	0	2	0	0	0	0	1	0	0	1	0	0	0	1	0	1	0
2.cümle	0	0	0	1	0	0	1	0	0	0	0	0	0	0	0	0	1	0	1
3.cümle	1	1	1	1	0	0	1	0	0	1	1	0	1	1	1	0	0	0	0



"""
#kelimelerin tekrar sayısını buluyorum
def frequencyValue(list):
    frequencyValueDict={}
    for f in list:
        if(f in frequencyValueDict):
            frequencyValueDict[f]+=1
        else:
            frequencyValueDict[f]=1
    return frequencyValueDict

frequency=frequencyValue(textlist)
print(frequency)

"""

for word in text0:
      wordDictText0[word] += 1

for word in text1:
      wordDictText1[word] += 1

for word in text2:
      wordDictText2[word] += 1

for word in text3:
      wordDictText3[word] += 1

pd.DataFrame([wordDictA, wordDictB, wordDictC, wordDictD])




def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict
    
    
    
    
    
#cümleleri tek tek alabilseydim TF lerini hesaplayıp bu şekilde tablolu olarak bastırabiliyorum fakat cümleleri ayrı ayrı almadım tek bir text dizisinden çektiğim için yorum satırı bırakıyorum

tftext0 = computeTF(wordDictText0, text0)
tftext1 = computeTF(wordDictText1, text1)
tftext2 = computeTF(wordDictText2, text2)
tftext3 = computeTF(wordDictText3, text3)

tf_df= pd.DataFrame([tftext0, tftext1, tftext2, tftext3])

tf_df

        in	the	was	wild	1984	duran	who	sang	boys	krakauer	john	forever	it	wrote	to	don't	flowers	remain	brought 
0   0.142857	0.0	0.0	0.142857	0.142857	0.285714	0.00	0.142857	0.142857	0.0	0.0	0.000000	0.0	0.0	0.0	0.000000	0.00	0.000000	0.00
1	0.000000	0.0	0.0	0.333333	0.000000	0.000000	0.00	0.000000	0.166667	0.0	0.0	0.166667	0.0	0.0	0.0	0.166667	0.00	0.166667	0.00
2	0.000000	0.0	0.0	0.250000	0.000000	0.000000	0.25	0.000000	0.000000	0.0	0.0	0.000000	0.0	0.0	0.0	0.000000	0.25	0.000000	0.25
3	0.100000	0.1	0.1	0.100000	0.000000	0.000000	0.10	0.000000	0.000000	0.1	0.1	0.000000	0.1	0.1	0.1	0.000000	0.00	0.000000	0.00



"""

# IDFT yi buluyorum her bir cümlenin her bir kelimesi için ve log formülümü uyguluyorum
IDFTdoc = list(frequency.keys())
computeIDFT = []
computeCountList = []

for fword in range(len(IDFTdoc)):
    computeCount = 0

    if (IDFTdoc[fword] in text[0]):
        computeCount += 1

    if (IDFTdoc[fword] in text[1]):
        computeCount += 1

    if (IDFTdoc[fword] in text[2]):
        computeCount += 1

    if (IDFTdoc[fword] in text[3]):
        computeCount += 1

    computeIDFT.append(math.log(len(text) / computeCount, 10))

# virgülden sonra 3 basamak olmasını sağladım
for n in range(len(computeIDFT)):
    computeIDFT[n] = round(computeIDFT[n], 3)



# son olarak TF*IDF çarpımını hesaplayım bastırıyorum
TFIDFsentence0 = []
TFIDFsentence1 = []
TFIDFsentence2 = []
TFIDFsentence3 = []

for fword in range(len(IDFTdoc)):
    word = IDFTdoc[fword]

    computeTFTD = text[0].count(word)
    TFIDFsentence0.append(computeTFTD * computeIDFT[fword])

    computeTFTD = text[1].count(word)
    TFIDFsentence1.append(computeTFTD * computeIDFT[fword])

    computeTFTD = text[2].count(word)
    TFIDFsentence2.append(computeTFTD * computeIDFT[fword])

    computeTFTD = text[3].count(word)
    TFIDFsentence3.append(computeTFTD * computeIDFT[fword])


print(TFIDFsentence0)
print(TFIDFsentence1)
print(TFIDFsentence2)
print(TFIDFsentence3)

