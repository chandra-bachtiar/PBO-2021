## Menampilkan luas dan Volume Balok
## Nama : Chandra Bachtiar
## NIM : 200511151
## Kelas : K1 Teknik Informatika

print("====== Program Keliling & Luas Balok ======")

#Variabel yang di perlukan 
diameter = int(input("Masukan diameter Balok (cm) : "))

#Proses Hitung
jari = diameter/2
keliling = (22/7) * jari 
luas = (22/7) * 2 * jari

print("Keliling Balok : ",round(keliling,1),"Cm")
print("Luas Balok : ",round(luas,1),"Cm2")
print("====== Program Selesai ======")
