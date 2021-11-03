## Menampilkan luas dan keliling Lingkaran
## Nama : Chandra Bachtiar
## NIM : 200511151
## Kelas : K1 Teknik Informatika

print("====== Program Keliling & Luas Lingkaran ======")

#Variabel yang di perlukan 
diameter = int(input("Masukan diameter lingkaran (cm) : "))

#Proses Hitung
jari = diameter/2
keliling = (22/7) * jari 
luas = (22/7) * 2 * jari

print("Keliling Lingkaran : ",round(keliling,1),"Cm")
print("Luas Lingkaran : ",round(luas,1),"Cm2")
print("====== Program Selesai ======")
