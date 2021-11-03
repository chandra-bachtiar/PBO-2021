## Chandra Bachtiar
## 200511151
## Tugas 4 - Fungsi
import math

LANJUT = True

def lanjut():
    ket = ''
    nomor = 0;
    while(nomor == 0):
        ket = input("Ingin Melakukan Perhitungan Lagi (y/n) : ")
        if(ket == 'y' or ket == 'n'):
            nomor = 1
        else:
            print("Input Tidak Dikenal!")
            nomor = 0

    if ket == 'y':
        LANJUT = True
    elif ket == 'n':
        LANJUT = False
        exit()

def persegi():
    print("\n\n====== Program Keliling & Luas Persegi ======")
    #Variabel yang di perlukan 
    sisi = int(input("Masukan Panjang sisi (cm) : "))

    #Proses Hitung
    keliling = 4 * sisi
    luas = sisi * sisi

    print("Keliling Persegi : ",keliling,"Cm")
    print("Luas Persegi : ",luas,"Cm2")
    print("====== Program Selesai ======\n\n")
    lanjut()

def segitiga():
    print("\n\n====== Program Keliling & Luas Segitiga Sama Sisi ======")
    #Variabel yang di perlukan 
    sisi = int(input("Masukan Panjang sisi (cm) : "))
    tinggi = int(input("Masukan Panjang tinggi (cm) : "))

    #Proses Hitung
    keliling = sisi*3
    luas = 0.5 * sisi * tinggi

    print("Keliling Segitiga Sama Sisi : ",keliling,"Cm")
    print("Luas Segitiga Sama sisi : ",luas,"Cm2")
    print("====== Program Selesai ======\n\n")
    lanjut()

def lingkaran():
    print("\n\n====== Program Keliling & Luas Lingkaran ======")

    #Variabel yang di perlukan 
    diameter = int(input("Masukan diameter lingkaran (cm) : "))

    #Proses Hitung
    jari = diameter/2
    keliling = (22/7) * jari 
    luas = (22/7) * 2 * jari

    print("Keliling Lingkaran : ",round(keliling,1),"Cm")
    print("Luas Lingkaran : ",round(luas,1),"Cm2")
    print("====== Program Selesai ======\n\n")
    lanjut()

def balok():
    print("\n\n====== Program Keliling & Luas Balok ======")

    #Variabel yang di perlukan 
    diameter = int(input("Masukan diameter Balok (cm) : "))

    #Proses Hitung
    jari = diameter/2
    keliling = (22/7) * jari 
    luas = (22/7) * 2 * jari

    print("Volume Balok : ",round(keliling,1),"Cm")
    print("Luas Balok : ",round(luas,1),"Cm2")
    print("====== Program Selesai ======\n\n")
    lanjut()

def kerucut():
    print("\n\n====== Program Volume & Luas Kerucut ======")

    # #Variabel yang di perlukan 
    jari = int(input("Masukan Jari Jari alas (cm) : "))
    pelukis = int(input("Masukan Panjang Garis Pelukis (cm) : "))

    # #Proses Hitung
    rs = jari + pelukis
    luas = (22/7) * jari * rs

    #cari tinggi kerucut rumus t2 = s2 - r2
    tmpTinggi = pelukis**2 - jari**2
    tinggi = math.sqrt(tmpTinggi)

    #Hitung Volume
    volume = (1/3) * ((22/7) * (jari**2) * tinggi)

    print("Volume Kerucut : ",round(volume,1),"Cm3")
    print("Luas Kerucut : ",round(luas,1),"Cm2")
    print("====== Program Selesai ======\n\n")
    lanjut()

def bola():
    print("\n\n====== Program Volume & Luas Bola ======")

    # #Variabel yang di perlukan 
    jari = int(input("Masukan Jari Jari (cm) : "))

    #Proses Hitung Luas || rumus Luas = 4 x π x r2
    luas = 4 * (22/7) * (jari**2)

    #Proses Hitung Volume || rumus Volume = 4/3 x π x r3
    volume = 4/3 * ((22/7) * (jari**3))

    print("Volume Bola : ",round(volume,1),"Cm3")
    print("Luas Bola : ",round(luas,1),"Cm2")
    print("====== Program Selesai ======\n\n")
    lanjut()

def tabung():
    print("\n\n====== Program Volume & Luas Tabung ======")

    # #Variabel yang di perlukan 
    jari = int(input("Masukan Jari Jari Tabung (cm) : "))
    tinggi = int(input("Masukan Tinggi Tabung (cm) : "))

    #Proses Hitung Luas || rumus Luas = 2 x π x r x (r + t)
    luas = 2 * (22/7) * jari * (jari + tinggi)

    #Proses Hitung Volume || rumus Volume = π x r2 x t
    volume = (22/7) * jari * jari * tinggi

    print("Volume Tabung : ",round(volume,1),"Cm3")
    print("Luas Tabung : ",round(luas,1),"Cm2")
    print("====== Program Selesai ======\n\n")
    lanjut()

def bmi():
    print("\n\n====== Program Hitung Body Mass Index ======")

    berat = int(input("Masukan Berat Badan (Kg) : "))
    tinggi = int(input("Masukan Tinggi Badan (cm) : "))

    #Hitung Body Mass Index dengan rumus Berat Badan / tinggi * tinggi
    ideal = berat / ((tinggi/100) * (tinggi/100))

    if ideal < 18.5 :
        print("Anda kekurangan berat badan.")
    elif ideal >= 18.5 and ideal <= 24.9:
        print("Anda Normal (Ideal).")
    elif ideal >= 25.0 and ideal <= 29.9:
        print("Anda Kelebihan berat badan.")
    elif ideal >= 30:
        print("Kegemukan (Obesitas)")

    print("====== Program Selesai ======\n\n")
    lanjut()


def menu():
    print("\n")
    print("----- PILIH PERHITUNGAN -----")
    print("[1] Luas & Keliling Persegi")
    print("[2] Luas & Keliling Segitiga Sama Sisi")
    print("[3] Luas & Keliling Lingkaran")
    print("[4] Volume & Luas Permukaan Balok")
    print("[5] Volume & Luas Permukaan Kerucut")
    print("[6] Volume & Luas Permukaan Bola")
    print("[7] Volume & Luas Permukaan Tabung")
    print("[8] Body Mass Index (BMI)")
    print("[0] Exit!")

    pilih = input("Pilih Nomor Perhitungan > ")

    if pilih == '1':
        persegi()
    elif pilih == '2':
        segitiga()
    elif pilih == '3':
        lingkaran()
    elif pilih == '4':
        balok()
    elif pilih == '5':
        kerucut()
    elif pilih == '6':
        bola()
    elif pilih == '7':
        tabung()
    elif pilih == '8':
        bmi()
    elif pilih == '0':
        exit()
    else:
        print("Unknow Input!.")

if __name__ == "__main__":
    while(LANJUT == True):
        menu()