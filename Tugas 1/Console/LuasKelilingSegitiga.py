## Menampilkan luas dan keliling Segitiga
## Nama : Chandra Bachtiar
## NIM : 200511151
## Kelas : K1 Teknik Informatika

print("====== Program Keliling & Luas Segitiga ======")
print("Pilih Opsi : \n1. Keliling Segitiga. \n2. Luas Segitiga")
print("Pilih Bentuk Segitiga : \n1. Segitiga Sama Kaki\n")
opsi = int(input("Masukan Pilihan (1/2) : "))
if opsi == 1:
    sisi1 = int(input("Masukan Sisi 1 (cm): "))
    sisi2 = int(input("Masukan Sisi 2 (cm): "))
    sisi3 = int(input("Masukan Sisi 3 (cm): "))
    #Proses Hitung
    keliling = sisi1 + sisi2 + sisi3
    print("Keliling Segitiga : ",keliling,"Cm")
    print("====== Program Selesai ======")
elif opsi == 2:
    alas = int(input("Masukan Alas Segitiga (cm) : "))
    tinggi = int(input("Masukan Tinggi Segitiga (cm) : "))
    #Proses Hitung
    luas = 0.5 * alas * tinggi
    print("Luas Segitiga : ",luas,"Cm2")
    print("====== Program Selesai ======")
else:
    print("Pilihan tidak diketahui")
    print("====== Program Selesai ======")