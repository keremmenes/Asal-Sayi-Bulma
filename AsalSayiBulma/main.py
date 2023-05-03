for x in range(2,100): # x ikiden 100 e kadar
    control=True # control değişkeni
    for y in range(2,x-1):  #kendisine bölünmemesi gerektiği için x-1 alıyoruz
        if x%y==0:
            control=False
            break
    if control:
        print (x)
print("\n")
        #  *******İLK 100 FİBONACCİ SAYISI YAZDIRMA******
a=1
b=1
for i in range(100):
    c=a+b
    a,b=b,c  #   Çoklu atama
    print(c)