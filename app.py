def luas_segitiga():
    a = int(input("Masukkan Alas Segitiga :  "))
    t = int(input("Masukkan Tinggi Segitiga :  "))
    luas = a * t / 2
    print("Luas Segitiga : ", luas)

luas_segitiga()

def luas_persegi_panjang():
    p = int(input("Masukkan Panjang : "))
    l = int(input("Masukkan Lebar :  "))
    luasp = p * l
    print("Luas Persegi Panjang : ", luasp)

luas_persegi_panjang()

def luas_lingkaran():
    r = int(input("Masukkan Jari-jari : "))
    phi = 22/7
    luasl = phi * r * r
    print("Luas lingkaran : " , luasl)

luas_lingkaran()