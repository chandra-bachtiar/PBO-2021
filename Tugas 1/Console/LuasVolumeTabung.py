## Menampilkan luas dan Volume Tabung
## Nama : Chandra Bachtiar
## NIM : 200511151
## Kelas : K1 Teknik Informatika

print("====== Program Volume & Luas Tabung ======")

# #Variabel yang di perlukan 
jari = int(input("Masukan Jari Jari Tabung (cm) : "))
tinggi = int(input("Masukan Tinggi Tabung (cm) : "))

#Proses Hitung Luas || rumus Luas = 2 x π x r x (r + t)
luas = 2 * (22/7) * jari * (jari + tinggi)

#Proses Hitung Volume || rumus Volume = π x r2 x t
volume = (22/7) * jari * jari * tinggi

print("Volume Tabung : ",round(volume,1),"Cm3")
print("Luas Tabung : ",round(luas,1),"Cm2")
print("====== Program Selesai ======")
