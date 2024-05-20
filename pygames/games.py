import random

def main():
    print("Pilih Salah Satu!")
    print("1. Kertas")
    print("2. Batu")
    print("3. Gunting")
    print("4. Keluar")
    
    pilih = int(input("Masukkan Pilihan Anda: "))
    comp = random.randint(1, 3)

    if pilih == 1:
        print("Kamu Memilih Kertas")
        if comp == 1:
            print("Komputer Memilih Kertas")
            print("Seri!")
        elif comp == 2:
            print("Komputer Memilih Batu")
            print("Kamu Menang!")
        else:
            print("Komputer Memilih Gunting")
            print("Komputer Menang!")
    elif pilih == 2:
        print("Kamu Memilih Batu")
        if comp == 1:
            print("Komputer Memilih Kertas")
            print("Komputer Menang!")
        elif comp == 2:
            print("Komputer Memilih Batu")
            print("Seri!")
        else:
            print("Komputer Memilih Gunting")
            print("Kamu Menang!")
    elif pilih == 3:
        print("Kamu Memilih Gunting")
        if comp == 1:
            print("Komputer Memilih Kertas")
            print("Kamu Menang!")
        elif comp == 2:
            print("Komputer Memilih Batu")
            print("Komputer Menang!")
        else:
            print("Komputer Memilih Gunting")
            print("Seri!")
    elif pilih == 4:
        print("Terima Kasih")
        exit()
    else:
        print("Pilihan Tidak Tersedia")

main()
