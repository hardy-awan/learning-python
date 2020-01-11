## Rumus Tabung
def hitung(a, b):
    hasil = a * a * b
    print(hasil)

nilai1= 10
nilai2 = 28
hitung(nilai1, nilai2)

##Rumus segitiga sama kaki
hitung2 = lambda nilai: nilai * 3
print(hitung2(50))



class myCalculator:
    def __init__(obj, nilai3, nilai4):
        obj.nilai3 = nilai3
        obj.nilai4 = nilai4

    def tambah(tambah):
        hasil1= tambah.nilai3 + tambah.nilai4
        print(hasil1)

    def kurang(kurang):
        hasil2 = kurang.nilai3 - kurang.nilai4
        print(hasil2)

    def bagi(bagi):
        hasil3 = bagi.nilai3 / bagi.nilai4
        print(hasil3)

    def kali(kali):
        hasil4 = kali.nilai3 * kali.nilai4
        print(hasil4)



p1 = myCalculator(100, 100)

p1.tambah()
p1.kurang()
p1.bagi()
p1.kali()