print("hello")

9+9
type(9)

"a" + "b"
" a  "*5
#string-metodu
mvk="geleceği_yazanlar"

a=9
b=10
a*b

len(mvk) #stringin uzunlugunu integer tipinde bize verir


# upper() lower() isupper() islower() metodları
mvk.upper() #stringin hepsini büyük harfe dönüştürür
mvk.lower() #stringin hepsini küçük harfe dönüştürür
B=mvk.upper() #B atama işlemei yaptık

mvk.islower() #stringler küçük harfmi sorgular küçük ise True döndürür
B.isupper() # B büyük harfmi sorguladık True döndü




# replace() metodu stringin içerisindeki a harfi e harfi yapmak gibi

mvk.replace("e","a") #çıktısı 'galacaği_yazanlar' oldu ancak orjinal çıktıyı etkilemedi sadece geçici e harfini a harfi yaptı
mvk # yazdığımızda orjinal metnin değişmediğini görcez


# strip() metodu kısaca istenmeyen karakteri kırpma
# ornegin '   galacaği_yazanlar      ' sağdasolda bir sürüboşluk var bu boşlukları yok etmek için bu fonk kullanılabilir

dvk=' galacaği_yazanlar    '
dvk.strip() # ön tanımlı olarak yalın halde boşlukları yok eder

dvk='*** 3 galacaği_yazanlar***'
dvk.strip("* 3 gal") #yıldızıda 3 de çıkarmış oldu 

#DİR KULLANIMI
dir(str) #kullana bileceğimiz metodları bize listeler

dvk.split()#çıktısı Out[39]: ['***', '3', 'galacaği_yazanlar***'] 



#SUPSTİNG alt bileşen demek ve erişmek indekse erişme gibi

mvk[0:4] #str 0 1 2 3 al yaz 4 e kadarkı kısmı yaz demek






#DEĞİŞKENLER
type(100)
type(100.2)
type(2+4j) 

#tiip dönüşümleri



toplama_bir=input()
toplama_iki=input()

c=int(toplama_bir)+ int(toplama_iki)

c=c*5
c

print("geleceği yazanlar","durma" ,sep="_")
print("uzaya", "git", sep = "**")

type(4)
"9" + "1"
"10" + 2
degisken = 4
print(degisken*degisken)

sakla = 9 
yeni_sakla = sakla*10

ifade = "selam"
type(ifade)

ifade = "gelecegi yaziyoruz"
ifade[1]

a = "bu uzun bir metindir"
a[2:5]

"_Python_".strip("_")

ifade = "Merhaba! "
ifade.strip("")

ifade = "1012340"
ifade = ifade + "1"
ifade.strip("1")

#VERİ YAPILARI [], list()

notlar=[90,80,34,87]
type(notlar)

liste_genis=["a",19.3,90,notlar]
len(liste_genis)

liste_genis[2]
type(liste_genis[0])

#tum_liste=[liste,liste_genis] liste birleştirme
#del tum_liste

#liste elemana erişme

liste =[90,80,34,87,[1,2,3,4]]
liste[4][1]

#LİSTELERE ELEMAN EKLEME SİLME
liste1=["ali","veli","ceren","ahmet","pol"]




liste12 = [1,2,3,4,5,6]

x = liste12.pop()
liste21 = []
liste21.append(x)

print(liste12)
print(liste21)


a = 4
string = "1,2,3,4,5"

liste = list(string)

uzunluk = len(liste)

print(uzunluk)

liste1 = [1,2,3,5,6,7,8,9]
liste2 = [2,4,6,8,10]

for i in liste2:
    if i not in liste1:
        liste1.append(i)
print(liste1)

liste = [1,2,3,4]
liste = liste + ["MertMekatronik"]
print(liste)

liste1 = [1,2,3,4,5,6]
liste2 = [7,8,9,10,11]

for i in range(len(liste1)):
    liste1.append(liste2[i])

print(liste2)

liste = [10,20,30]
print(liste * 2)

liste = [12,3,4,9,5]
liste.insert(2,6)

print(liste)

liste = [350,400,100,123,260,370]
liste = sorted(liste)

print(liste)

liste = [350,400,100,123,260,370]
liste.reverse()

print(liste)

#count fonksiyonu
liste1=["ali","veli","ceren","ahmet","ali"]
liste1.count("ali")

#copy metodu
liste_yedek=liste1.copy() #listeyi kopyalar

#extend metodu

liste1.extend(["a","10"]) #['ali', 'veli', 'ceren', 'ahmet', 'ali', 'a', '10']
liste1 #listeye kalıcı değişiklik yaparak ekleme yaptı

#index meteodu
liste1.index("ali") #ali kelimesinin indexsini verir

#reverse metodu
liste1.reverse() #['10', 'a', 'ali', 'ahmet', 'ceren', 'veli', 'ali']
liste1 #tersine listeye yazar


#sort metodu
liste=[10,20,30,33,4,44,]
liste.sort()
liste #[4, 10, 20, 30, 33, 44] küçükten büyüye doğru sıralar 

#clear metodu listeyi sıfırlar 
liste.clear()
liste #[] boş listeyi bize verir 

#Tuple veri yapıları 

t=("ali","mehmet",1,2,3.2,[1,2,3])
z="ali","mehmet",1,2,3.2,[1,2,3]


t=("ali","mehmet",1,2,3.2,[1,2,3])

t[1:3]

#Veri yapısı-sözluk dictoneriy
sozluk={"REG":"Regirasyon modeli",
        "LOJ":"Loojistik Regirasyon ",
        "CART":"Classification and Reg"}
sozluk

len(sozluk) #3 çıktısını verecek

type(sozluk) #type(sozluk) Out[12]: dict

sozluk[0] #KeyError: 0 hata alırız sebebp sozluk sırasızdır listedeki gibi indis numarasına göre alamayız

#Key word anahtar  kelime ile çalışır
sozluk["REG"] #anahtar kelime Out[14]: 'Regirasyon modeli'


#içiçe geçmiş sozluk eleman arama
sozluk={"REG":{"rss":10,
               "mm":90,
               "ww":11},
        "LOJ":{"rss":10,
               "mm":90,
               "ww":11},
        "CART":{"rss":10,
               "mm":90,
               "ww":11},}

sozluk["REG"]["ww"] #Out[16]: 11 REG in ww sini degereni getit gibi 


#eleman ekleme degiştirme sözcuge 

sozluk["REG"]["ww"]="12"
sozluk #'REG': {'rss': 10, 'mm': 90, 'ww': '12'}, 11 i 12 yaptı
sozluk["ere"]="ara bacaguy"
sozluk #key word ile dictionary ekler 

#KUMELER Setler veri yapılaraı 

#set olusturmak
s=set()
s
#listeler yardımı ile set oluşturma
l=[1,2,"ali"] 
s=set(l)
s
#tuple ler uzerinden set olusturmma
t=("ali",)
s=set(t)
s
#stringi sete attıgın zaman  ali degisşkenin tuttugu set 
ali="her-sey sana_guzel" 
type(ali)
s=set(ali) #{' ', '-', '_', 'a', 'e', 'g', 'h', 'l', 'n', 'r', 's', 'u', 'y', 'z'}
s

l=["wer","der"]

s=set(l)
#eklem
s.add("ile")
s

s.add("zerre")
s
#silme
s.remove("zerre")
s
s.discard("der")
s


# difference
set1=set([1,2,3,4])
set2=set([6,3,1])
set1.difference(set2) #cıktı {4} set1 de olub set2 de olmayan

set1.symmetric_difference(set2) #birinde olub diğerinde olmayan aynı zamanda 



#kumeleri birleştirme kesiştirme

set1=set([1,2,3,4])
set2=set([6,3,1])


set1.intersection(set2) #kesişim  Out[36]: {1, 3}
kesişim=set1.intersection(set2)
set1.union(set2)        #birleşim  Out[37]: {1, 2, 3, 4, 6}
birleşim=set1.union(set2)


#SETlerde  sorgulama işlemleri
set1=set([1,2,3,4])
set2=set([6,3,1])

#iki küme bosşmu  sorgusu

set1.isdisjoint(set2)
# set1.isdisjoint(set2)
# Out[40]: False

#bir kümenin butun elemanları başka kumede yer alıyormu 

set1.issubset(set2)
# set1.issubset(set2)
# Out[41]: False





liste = [1,1,2,3,4,5,1,2,1]
liste.count(2) #ikiden kactane var



liste = [10,20,30,40]
liste.pop(1)
liste       #20 listenin indisi 1 olan eleman oldugundan onu cıkartır



liste = ["a","b","c"]
liste.reverse()
liste

t = ("a",10,"b")
t[0] = 1 #hata üretir tuple degiştirilemez

liste = ["a","b","c"]
liste.index("b")

liste = [50,10,30,40]
liste.clear()
liste

#fonksiyonlar 

def kare_al(x):
    print(x**2)
kare_al(3)

def kare_al(x):
    
    print("girilen sayın:" + str(x))
    print("girilen sayının karesi:" + str(x**2))
    
kare_al(3)

#iki argumanlı fonksıyon tanımlama 

def kare_al(x):
    print(x**2)

def carpma_yap(x,y):
    print(x*y)

carpma_yap(3,5)



# =============================================================================
# #on tanımlıargumanlar 
# =============================================================================


def carpma_yap(x,y=1):
    
    print(x*y)
carpma_yap(y=3,x=9)

# =============================================================================
# #ne zaman fonksiyonlar yazılır tekrar edenleri 
# =============================================================================

def direk_hesap(ısı,nem,sarj):
    print((ısı+nem)/sarj)
direk_hesap(30,40,20)



# =============================================================================
#return ifadesi  kullanılır 
#fonksiyonların çıktısını girdi olarak kullanma  
# =============================================================================

def direk_hesap(ısı,nem,sarj):
    return((ısı+nem)/sarj)
cikti=direk_hesap(30,40,20)*9
cikti

# =============================================================================
# locals() ve globals() ddeğişkenler
# =============================================================================

x=10 
y=12

def carpma_yap(x,y):
    return x*y
print(carpma_yap(x,y)) #global değişkenler ile işem yapma 

def carpma_yap(x,y):
    return x*y

carpma_yap(2,3)  #local işlem yapar ne zamankı global işlem yapmak isteriz ozamn
                    # x y degerlerini vere bilir

x=[] #global
def elema_ek(y):
    x.append(y) #local etki alanı
elema_ek()
x
  
# =============================================================================
# true false bullen yapma   
# =============================================================================
  #karar kontrol yapıları 
  
sinir=500
gelir=4000

if gelir<sinir:
    print("gelir mashallahıı var ")
    
else:
    print("gelir yok")

#elif- birden fazla kosulu yapmak ıcın


sinir=5000
gelir=5000
gelir2=6000
gelir3=3500

if gelir>sinir:
    print("tebrikllergeliriniz sınırı aşmışdır ")
    
elif gelir<sinir:
    print("cezalı durum")
else:
    print("bir se yapmay agerk yok  yok"  )

# =============================================================================
# #mini bir gelir kaynagı sorgulama uygulaması 
# 
# =============================================================================
magaza_adi=input("magaza adı nedir?")
gelir=int(input("geliriniz giriniz!"))
if gelir>sinir:
    print("tebrikler  " +  str(magaza_adi) + "  pramosyon kazandınız")
elif gelir< sinir:
    print("uyarı"+ str(gelir))
else :
    print("takibe devam azim li olll")


# gor dongusu
ogrenciler_l=["alii","veli","ahmet","can","darek"]
for i in ogrenciler_l:
    print(i)

list=[1,2,3,5,6,7,8,9,24]
for  a in list[2:4]:
    if a%2==0:
        print("a"+ str({a})+ "is even")
    else:
        print("a "+ str( {a}) +" is odd")

my_str="ahmet"
x=0
for i in my_str:
    if x==0:
        print("*")
        x+=1
    else:
       print(my_str[0:x]) 
    
def kare_al(x):
    print(x**2)
kare_al(2)


# maaslara yuzde 20 zam  

# fonksiyon 
def zam_mas(x):
    print(x*20/100+x)
    
maslar=[1000,200,30000,2342]
for i in maslar:
    zam_mas(i)
    
def yıldız_koy(x):
    
    print("*")   

d="ahmet"
x=0
for i in d:
    x+=1
    for i in d:
        print(x)
        x+=1
        
        yıldız_koy(i)
        print(d[0:x])













